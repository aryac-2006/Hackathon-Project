"""
app.py
LegalEase India — Multilingual Legal Information Assistant
A hackathon MVP. NOT legal advice. India-only. TF-IDF based retrieval,
no LLM, no paid APIs.

Run locally:   streamlit run app.py
"""

import os
import io
import streamlit as st

from src.constants import (
    NAVY, SAFFRON, WHITE, LIGHT_BG, GREY_TEXT, FONT_FAMILY,
    SUPPORTED_LANGS, APP_TITLE,
)
from src.ui_text import T
from src.pdf_utils import extract_pages_from_pdf
from src.chunking import build_chunks_for_document, build_chunks_from_plain_text
from src.retrieval import DocumentIndex, extractive_summary
from src.sos_data import get_localized_numbers
from src.lawyer_directory import (
    load_lawyers, get_unique_cities, get_unique_specializations,
    get_unique_languages, filter_lawyers,
)

# ----------------------------------------------------------------------
# PAGE CONFIG (must be first Streamlit call)
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="LegalEase India",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------
# CUSTOM CSS — simple Indian-themed palette, clean student-project look
# ----------------------------------------------------------------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {{
    font-family: {FONT_FAMILY};
    font-size: 15px;
    color: {GREY_TEXT};
}}

h1, h2, h3 {{
    color: {NAVY};
    font-weight: 600;
}}
h1 {{ font-size: 26px; }}
h2 {{ font-size: 20px; }}
h3 {{ font-size: 17px; }}

.stApp {{
    background-color: {LIGHT_BG};
}}

section[data-testid="stSidebar"] {{
    background-color: {NAVY};
}}
section[data-testid="stSidebar"] * {{
    color: {WHITE} !important;
}}

.disclaimer-box {{
    background-color: #FFF4E5;
    border-left: 5px solid {SAFFRON};
    padding: 12px 16px;
    border-radius: 6px;
    font-size: 13.5px;
    margin-bottom: 14px;
    color: {NAVY};
}}

.citation-box {{
    background-color: #F0F2F6;
    border-left: 4px solid {NAVY};
    padding: 10px 14px;
    border-radius: 6px;
    font-size: 13.5px;
    margin-top: 8px;
}}

.lawyer-card {{
    background-color: {WHITE};
    border: 1px solid #E0E0E0;
    border-radius: 10px;
    padding: 14px;
    margin-bottom: 12px;
}}

.sos-badge {{
    background-color: #D32F2F;
    color: {WHITE} !important;
    padding: 4px 10px;
    border-radius: 14px;
    font-weight: 600;
    font-size: 13px;
}}

div.stButton > button {{
    background-color: {SAFFRON};
    color: {NAVY};
    font-weight: 600;
    border-radius: 8px;
    border: none;
}}
div.stButton > button:hover {{
    background-color: #e6822e;
    color: {WHITE};
}}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# SESSION STATE INITIALIZATION
# ----------------------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "English"
if "doc_index" not in st.session_state:
    st.session_state.doc_index = DocumentIndex()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # list of dicts: role, content, meta(optional)
if "index_dirty" not in st.session_state:
    st.session_state.index_dirty = False  # True when new chunks added but index not rebuilt
if "pending_query" not in st.session_state:
    st.session_state.pending_query = None  # used to inject voice-recognized text

lang = st.session_state.lang

# ----------------------------------------------------------------------
# SIDEBAR — language selector + SOS button + disclaimer
# ----------------------------------------------------------------------
with st.sidebar:
    st.markdown(f"### ⚖️ {APP_TITLE}")
    chosen_lang = st.selectbox(
        T(lang, "sidebar_language_label"),
        SUPPORTED_LANGS,
        index=SUPPORTED_LANGS.index(st.session_state.lang),
    )
    if chosen_lang != st.session_state.lang:
        st.session_state.lang = chosen_lang
        st.rerun()

    st.markdown("---")
    if st.button(T(lang, "sos_button_label"), use_container_width=True):
        st.session_state["_show_sos_popover"] = True

    st.markdown("---")
    st.markdown(f"**{T(lang, 'disclaimer_title')}**")
    st.caption(T(lang, "disclaimer_text"))

# ----------------------------------------------------------------------
# HEADER
# ----------------------------------------------------------------------
st.markdown(f"# ⚖️ {T(lang, 'app_title')}")
st.caption(T(lang, "tagline"))

st.markdown(
    f"<div class='disclaimer-box'><b>{T(lang, 'disclaimer_title')}</b><br>{T(lang, 'disclaimer_text')}</div>",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# TABS
# ----------------------------------------------------------------------
tab_chat, tab_docs, tab_lawyer, tab_sos, tab_about = st.tabs([
    T(lang, "nav_chat"),
    T(lang, "nav_documents"),
    T(lang, "nav_lawyer"),
    T(lang, "nav_sos"),
    T(lang, "nav_about"),
])

# ========================================================================
# TAB 1: CHAT
# ========================================================================
with tab_chat:
    col_main, col_side = st.columns([2, 1])

    # ---------------- Upload / build index (right column) ----------------
    with col_side:
        st.markdown(f"### {T(lang, 'upload_header')}")

        uploaded_pdfs = st.file_uploader(
            T(lang, "upload_pdf_label"),
            type=["pdf"],
            accept_multiple_files=True,
            key="pdf_uploader",
        )

        pasted_name = st.text_input(T(lang, "paste_text_name_label"), value="", key="pasted_name")
        pasted_text = st.text_area(T(lang, "paste_text_label"), value="", height=120, key="pasted_text")
        if st.button(T(lang, "add_pasted_doc_btn"), key="add_pasted_btn"):
            if not pasted_text.strip():
                st.warning(T(lang, "empty_text_warning"))
            else:
                doc_name = pasted_name.strip() or f"Pasted Document {len(st.session_state.doc_index.chunks) + 1}"
                new_chunks = build_chunks_from_plain_text(doc_name, pasted_text)
                st.session_state.doc_index.add_chunks(new_chunks)
                st.session_state.index_dirty = True
                st.success(f"Added '{doc_name}' ({len(new_chunks)} chunk(s)).")

        if st.button(T(lang, "build_index_btn"), key="build_index_btn"):
            # Process any newly uploaded PDFs that aren't already in the index
            already_indexed_docs = {c["doc_name"] for c in st.session_state.doc_index.chunks}
            newly_added_docs = 0
            newly_added_chunks = 0

            if uploaded_pdfs:
                for pdf_file in uploaded_pdfs:
                    if pdf_file.name in already_indexed_docs:
                        continue
                    pages = extract_pages_from_pdf(pdf_file)
                    if not pages:
                        st.warning(f"{pdf_file.name}: {T(lang, 'empty_text_warning')}")
                        continue
                    new_chunks = build_chunks_for_document(pdf_file.name, pages)
                    st.session_state.doc_index.add_chunks(new_chunks)
                    newly_added_docs += 1
                    newly_added_chunks += len(new_chunks)

            if st.session_state.doc_index.has_chunks():
                st.session_state.doc_index.build_index()
                st.session_state.index_dirty = False
                st.success(T(
                    lang, "index_built_success",
                    n=st.session_state.doc_index.num_chunks(),
                    d=st.session_state.doc_index.num_docs(),
                ))
            else:
                st.warning(T(lang, "no_docs_warning"))

        st.markdown("---")
        st.markdown(f"### {T(lang, 'image_header')}")
        img_upload = st.file_uploader(T(lang, "image_upload_label"), type=["jpg", "jpeg", "png"], key="img_uploader")
        img_camera = st.camera_input(T(lang, "image_camera_label"), key="img_camera")

        shown_image = img_camera if img_camera is not None else img_upload
        if shown_image is not None:
            st.image(shown_image, use_container_width=True)
            st.info(T(lang, "ocr_note"))

        st.markdown("---")
        st.markdown(f"### {T(lang, 'voice_header')}")
        st.caption("Record a short question. If recognition fails, just type instead.")
        try:
            from st_audiorec import st_audiorec
            audio_bytes = st_audiorec()
            AUDIOREC_AVAILABLE = True
        except Exception:
            audio_bytes = None
            AUDIOREC_AVAILABLE = False
            st.caption("🎙️ Voice recorder component not installed — type your question below instead.")

        if AUDIOREC_AVAILABLE and audio_bytes is not None:
            if st.button("🔎 " + T(lang, "voice_processing"), key="process_voice_btn"):
                with st.spinner(T(lang, "voice_processing")):
                    recognized_text = None
                    try:
                        import speech_recognition as sr
                        recognizer = sr.Recognizer()
                        audio_file = io.BytesIO(audio_bytes)
                        with sr.AudioFile(audio_file) as source:
                            audio_data = recognizer.record(source)
                        recognized_text = recognizer.recognize_google(audio_data)
                    except ImportError:
                        st.error(T(lang, "voice_lib_missing"))
                    except Exception:
                        st.error(T(lang, "voice_fail"))

                    if recognized_text:
                        st.success(f"{T(lang, 'voice_recognized')}: {recognized_text}")
                        st.session_state.pending_query = recognized_text

    # ---------------- Chat interface (left/main column) ----------------
    with col_main:
        st.markdown(f"### {T(lang, 'nav_chat')}")

        # Render existing chat history
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                if msg.get("meta"):
                    meta = msg["meta"]
                    st.markdown(
                        f"<div class='citation-box'>"
                        f"<b>{T(lang, 'match_score')}:</b> {meta['score']:.3f}<br>"
                        f"<b>{T(lang, 'source_doc')}:</b> {meta['doc_name']}<br>"
                        f"<b>{T(lang, 'page_no')}:</b> {meta['page_num']}<br>"
                        f"<b>{T(lang, 'chunk_id')}:</b> {meta['chunk_id']}<br>"
                        f"<b>{T(lang, 'excerpt')}:</b> {meta['excerpt']}"
                        f"</div>",
                        unsafe_allow_html=True,
                    )

        # Determine the query: either from voice or from chat_input
        typed_query = st.chat_input(T(lang, "chat_input_placeholder"))
        query = None
        if st.session_state.pending_query:
            query = st.session_state.pending_query
            st.session_state.pending_query = None
        elif typed_query:
            query = typed_query

        if query is not None:
            if not query.strip():
                st.warning(T(lang, "empty_question_warning"))
            elif not st.session_state.doc_index.has_chunks() or st.session_state.doc_index.vectorizer is None:
                st.warning(T(lang, "no_docs_warning"))
            else:
                st.session_state.chat_history.append({"role": "user", "content": query})

                best_chunk, best_score, _ = st.session_state.doc_index.best_match(query)

                if best_chunk is None:
                    answer_text = T(lang, "not_found_answer")
                    st.session_state.chat_history.append({"role": "assistant", "content": answer_text})
                else:
                    summary = extractive_summary(best_chunk["raw_text"], max_sentences=3)
                    answer_text = summary
                    meta = {
                        "score": best_score,
                        "doc_name": best_chunk["doc_name"],
                        "page_num": best_chunk["page_num"],
                        "chunk_id": best_chunk["chunk_id"],
                        "excerpt": best_chunk["raw_text"][:400] + ("..." if len(best_chunk["raw_text"]) > 400 else ""),
                    }
                    st.session_state.chat_history.append({"role": "assistant", "content": answer_text, "meta": meta})

                st.rerun()

# ========================================================================
# TAB 2: DOCUMENTS
# ========================================================================
with tab_docs:
    st.markdown(f"## {T(lang, 'doc_tab_header')}")

    idx = st.session_state.doc_index
    if not idx.has_chunks():
        st.info(T(lang, "no_docs_yet"))
    else:
        c1, c2 = st.columns(2)
        c1.metric(T(lang, "total_docs"), idx.num_docs())
        c2.metric(T(lang, "total_chunks"), idx.num_chunks())

        # Per-document breakdown
        doc_summary = {}
        for c in idx.chunks:
            doc_summary.setdefault(c["doc_name"], 0)
            doc_summary[c["doc_name"]] += 1

        st.markdown("#### " + T(lang, "doc_tab_header"))
        for doc_name, count in doc_summary.items():
            st.write(f"📄 **{doc_name}** — {count} chunk(s)")

        st.markdown("---")
        if st.button(T(lang, "clear_index_btn")):
            st.session_state.doc_index.clear()
            st.session_state.chat_history = []
            st.success(T(lang, "index_cleared"))
            st.rerun()

# ========================================================================
# TAB 3: FIND A LAWYER
# ========================================================================
with tab_lawyer:
    st.markdown(f"## {T(lang, 'lawyer_header')}")
    st.caption(T(lang, "lawyer_disclaimer"))

    lawyers_path = os.path.join(os.path.dirname(__file__), "data", "lawyers.json")
    lawyers = load_lawyers(lawyers_path)

    if not lawyers:
        st.warning("Lawyer directory data could not be loaded.")
    else:
        cities = ["All"] + get_unique_cities(lawyers)
        specializations = ["All"] + get_unique_specializations(lawyers)
        languages = ["All"] + get_unique_languages(lawyers)
        max_possible_fee = max(l.get("fees", 0) for l in lawyers)

        f1, f2, f3, f4 = st.columns(4)
        sel_city = f1.selectbox(T(lang, "filter_city"), cities)
        sel_spec = f2.selectbox(T(lang, "filter_specialization"), specializations)
        sel_lang = f3.selectbox(T(lang, "filter_language"), languages)
        sel_fee = f4.slider(T(lang, "filter_fees"), min_value=0, max_value=int(max_possible_fee), value=int(max_possible_fee))

        filtered = filter_lawyers(lawyers, city=sel_city, specialization=sel_spec, language=sel_lang, max_fee=sel_fee)

        if not filtered:
            st.info(T(lang, "no_lawyers_found"))
        else:
            cols = st.columns(2)
            for i, lw in enumerate(filtered):
                with cols[i % 2]:
                    st.markdown("<div class='lawyer-card'>", unsafe_allow_html=True)
                    ic1, ic2 = st.columns([1, 2])
                    with ic1:
                        st.image(lw.get("photo", ""), width=80)
                    with ic2:
                        st.markdown(f"**{lw['name']}**")
                        st.caption(f"{lw['city']}, {lw['state']}")
                    st.write(f"🗣️ {', '.join(lw.get('languages', []))}")
                    st.write(f"🏷️ {', '.join(lw.get('specialization', []))}")
                    st.write(f"💰 ₹{lw.get('fees', 'N/A')} / consultation")
                    st.write(f"🕒 {lw.get('availability', 'N/A')}")
                    st.write(f"📧 {lw.get('email', 'N/A')}")
                    st.write(f"📞 {lw.get('phone', 'N/A')}")
                    st.markdown("</div>", unsafe_allow_html=True)

# ========================================================================
# TAB 4: SOS
# ========================================================================
with tab_sos:
    st.markdown(f"## {T(lang, 'sos_header')}")
    st.error(T(lang, "sos_note"))

    numbers = get_localized_numbers(lang)
    for item in numbers:
        c1, c2 = st.columns([3, 1])
        c1.write(f"**{item['name']}**")
        c2.markdown(f"<span class='sos-badge'>{item['number']}</span>", unsafe_allow_html=True)

# ========================================================================
# TAB 5: ABOUT & SOURCES
# ========================================================================
with tab_about:
    st.markdown(f"## {T(lang, 'about_header')}")
    st.write(T(lang, "about_text"))

    st.markdown(f"### {T(lang, 'about_sources_header')}")
    st.markdown("""
- **India Code** — https://www.indiacode.nic.in (official repository of Indian legislation)
- **eGazette (Government of India)** — https://egazette.gov.in
- **National Consumer Helpline / Ministry of Consumer Affairs** — https://consumerhelpline.gov.in
- **Legal Services Authorities (NALSA)** — https://nalsa.gov.in (free legal aid information)
- **National Judicial Data Grid** — https://njdg.ecourts.gov.in
""")

    st.markdown("---")
    st.caption("Built as a hackathon MVP. Not affiliated with the Government of India. "
               "No legal advice is provided by this application.")
