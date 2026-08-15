# ⚖️ LegalEase India — Multilingual Legal Information Assistant

A hackathon MVP that helps Indian citizens understand government and legal
documents in plain language — in **English, हिंदी, and मराठी**.

> ⚠️ **This tool does NOT provide legal advice.** It only extracts and
> shows information from documents you upload, using classic NLP
> (TF‑IDF + cosine similarity — no LLM, no paid APIs). For your specific
> situation, consult a licensed advocate.

---

## ✨ Features

- 💬 **Chatbot** that answers only from documents you upload, with full citations
  (match score, source document, page number, chunk ID, excerpt)
- 🌐 **Multilingual UI** — English / हिंदी / मराठी, switchable anytime
- 📤 Upload multiple **PDFs**, or **paste text** as a document
- 🖼️ Upload or **capture an image** (camera input) — shown for reference (OCR not enabled in MVP)
- 🎙️ **Voice input (beta)** — record a question, converted to text (Google Web Speech via `SpeechRecognition`)
- ⚖️ **Find a Lawyer** directory with filters (city, specialization, language, fees)
- 🆘 **SOS panel** with key Indian emergency helpline numbers
- ℹ️ **About & Sources** tab pointing to real India-specific legal sources

---

## 📁 Folder Structure

```
LegalEaseIndia/
├── app.py                     # Main Streamlit app
├── requirements.txt
├── README.md
├── data/
│   ├── lawyers.json           # Sample lawyer directory (12 entries)
│   └── sample_text.txt        # Sample document for quick testing
└── src/
    ├── __init__.py
    ├── constants.py            # Colors, fonts, thresholds
    ├── ui_text.py               # EN/HI/MR translation dictionary
    ├── pdf_utils.py             # PDF text extraction (PyPDF2)
    ├── chunking.py               # Text chunking with metadata
    ├── retrieval.py               # TF-IDF + cosine similarity engine
    ├── sos_data.py                 # Emergency numbers
    └── lawyer_directory.py          # Lawyer data loading + filters
```

---

## 🚀 Run Locally (VS Code / Terminal)

1. **Clone / copy the project folder**, then open it in VS Code.

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

5. Open the URL shown in the terminal (usually `http://localhost:8501`).

6. **Try it out**:
   - Go to the **Chat** tab.
   - Click **"Build / Refresh Index"** without uploading anything first — you'll
     see the "please upload a document" warning (error handling check).
   - Paste the contents of `data/sample_text.txt` into the "paste text" box,
     give it a name like `Consumer Protection Sample`, click **"Add pasted text to index"**,
     then click **"Build / Refresh Index"**.
   - Ask: *"What is the right to safety for consumers?"* — you should get an
     answer with a citation (score, doc name, page, chunk ID, excerpt).
   - Ask something unrelated like *"best cricket player in India"* — you should
     get the "Not enough information found" message (no hallucination).

> 💡 **Note on Voice Input:** The `streamlit-audiorec` component and
> `SpeechRecognition`'s Google Web Speech API need an internet connection and
> a working microphone/browser permissions. If the voice recorder component
> fails to load in your environment, the rest of the app still works — just
> type your question in the chat box instead.

---

## ☁️ Deploy on Streamlit Cloud

1. Push this folder to a **public GitHub repository**.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) → **New app**.
3. Select your repo, branch, and set the **Main file path** to `app.py`.
4. Streamlit Cloud will automatically install everything in `requirements.txt`.
5. Click **Deploy**.

> ⚠️ If `streamlit-audiorec` fails to build on Streamlit Cloud (it depends on
> some native audio libraries), you can remove it from `requirements.txt` —
> the app will detect this gracefully and simply hide the voice recorder,
> falling back to text input only. Everything else keeps working.

---

## 🧠 How the "AI" Works (No LLM)

1. **Extraction** — `PyPDF2` pulls text from each page of uploaded PDFs.
2. **Chunking** — Page text is split into ~800-character overlapping chunks,
   each tagged with `doc_name`, `page_num`, and a unique `chunk_id`.
3. **Indexing** — All chunks are vectorized with `TfidfVectorizer` using
   **character n-grams** (`analyzer="char_wb"`, `ngram_range=(3,5)`), which
   works reasonably well across English, Hindi, and Marathi scripts without
   needing language-specific tokenizers.
4. **Retrieval** — A user's question is vectorized the same way, and
   **cosine similarity** finds the closest chunk(s).
5. **Threshold check** — If the best score is below `SIMILARITY_THRESHOLD`
   (0.25, tuned empirically), the app says *"Not enough information found"*
   instead of guessing.
6. **Answer** — The first 2–3 sentences of the best-matching chunk are shown
   as an **extractive** answer (nothing is generated or invented), along
   with full citation metadata.

---

## ⚠️ Known Limitations (MVP scope)

- OCR on uploaded/captured images is **not implemented** (shown as a note in-app).
- Voice input depends on an internet connection (Google Web Speech API) and
  browser microphone permissions; it gracefully falls back to typing if unavailable.
- The lawyer directory is **sample data only** — not verified/real listings.
  A note in-app reminds users to verify credentials independently.
- TF-IDF retrieval is a lexical/character-overlap method, not true semantic
  search — it works best when the user's wording overlaps with document wording.

---

## 📚 Suggested Sources for Real Legal Documents (India)

- [India Code](https://www.indiacode.nic.in) — official repository of Indian legislation
- [eGazette](https://egazette.gov.in) — Government of India gazette notifications
- [National Consumer Helpline](https://consumerhelpline.gov.in)
- [NALSA](https://nalsa.gov.in) — free legal aid information
- [National Judicial Data Grid](https://njdg.ecourts.gov.in)

---

## 🧪 Sample Test Flow & Expected Output (for demo)

1. **Launch app** → Sidebar shows language selector (English/हिंदी/मराठी) and SOS button.
2. **Switch language to मराठी** → All labels, disclaimer, and tab names update instantly.
3. **Chat tab, no docs** → Ask a question → see orange warning: "Please upload at least one PDF or paste some text..."
4. **Paste `sample_text.txt` content, build index** → Green success message: "Index built successfully with 3 chunk(s) from 1 document(s)."
5. **Ask a relevant question** → Bot reply bubble + a light-grey citation box below it showing score (e.g. `0.40`), source doc name, page number, chunk ID, and the excerpt text.
6. **Ask an irrelevant question** → Bot replies "🤔 Not enough information found in uploaded document(s)."
7. **Documents tab** → Shows "Total documents: 1", "Total chunks: 3", a per-document breakdown, and a "Clear/Reset Index" button.
8. **Find a Lawyer tab** → Filter by City = Pune → Shows 2 lawyer cards (Priya Deshmukh, Neha Joshi) with photo, languages, specialization tags, fees, availability, email, phone.
9. **SOS tab** → Table of emergency numbers with red badges (112, 100, 101, 102/108, 1091, 1098, 1930, 1073, etc.) and a red banner: "If you are in immediate danger, call 112."
10. **About tab** → Project description + list of official India-specific legal data sources.

---

*Built as a hackathon MVP for educational/demo purposes. Not affiliated with
the Government of India. No legal advice is provided by this application.*
