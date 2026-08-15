"""
ui_text.py
A simple internal dictionary-based translation system.
No external translation API is used — everything is a static lookup.
Keys are consistent across all three languages so the rest of the
app can just call: T(lang, "some_key")
"""

TEXT = {
    "app_title": {
        "English": "LegalEase India — Multilingual Legal Information Assistant",
        "हिंदी": "लीगलईज़ इंडिया — बहुभाषी कानूनी जानकारी सहायक",
        "मराठी": "लीगलईज इंडिया — बहुभाषिक कायदेशीर माहिती सहाय्यक",
    },
    "tagline": {
        "English": "Understand government & legal documents in simple language.",
        "हिंदी": "सरकारी और कानूनी दस्तावेज़ों को सरल भाषा में समझें।",
        "मराठी": "सरकारी आणि कायदेशीर कागदपत्रे सोप्या भाषेत समजून घ्या.",
    },
    "disclaimer_title": {
        "English": "⚠️ Important Disclaimer",
        "हिंदी": "⚠️ महत्वपूर्ण अस्वीकरण",
        "मराठी": "⚠️ महत्त्वाची सूचना",
    },
    "disclaimer_text": {
        "English": (
            "This tool provides general legal INFORMATION only, extracted from "
            "documents you upload. It is NOT legal advice and does NOT replace "
            "a qualified lawyer. For your specific situation, please consult a "
            "licensed advocate."
        ),
        "हिंदी": (
            "यह उपकरण केवल आपके द्वारा अपलोड किए गए दस्तावेज़ों से सामान्य कानूनी "
            "जानकारी प्रदान करता है। यह कानूनी सलाह नहीं है और किसी योग्य वकील का "
            "विकल्प नहीं है। अपनी विशेष स्थिति के लिए कृपया लाइसेंस प्राप्त वकील से "
            "संपर्क करें।"
        ),
        "मराठी": (
            "हे साधन तुम्ही अपलोड केलेल्या कागदपत्रांमधून केवळ सर्वसाधारण कायदेशीर "
            "माहिती देते. ही कायदेशीर सल्ला नाही आणि पात्र वकिलाची जागा घेत नाही. "
            "तुमच्या विशिष्ट परिस्थितीसाठी कृपया परवानाधारक वकिलाचा सल्ला घ्या."
        ),
    },
    "nav_chat": {"English": "💬 Chat", "हिंदी": "💬 चैट", "मराठी": "💬 चॅट"},
    "nav_documents": {"English": "📄 Documents", "हिंदी": "📄 दस्तावेज़", "मराठी": "📄 कागदपत्रे"},
    "nav_lawyer": {"English": "⚖️ Find a Lawyer", "हिंदी": "⚖️ वकील खोजें", "मराठी": "⚖️ वकील शोधा"},
    "nav_sos": {"English": "🆘 SOS", "हिंदी": "🆘 एसओएस", "मराठी": "🆘 एसओएस"},
    "nav_about": {"English": "ℹ️ About & Sources", "हिंदी": "ℹ️ बारे में और स्रोत", "मराठी": "ℹ️ माहिती आणि स्रोत"},

    "upload_header": {
        "English": "📤 Upload documents",
        "हिंदी": "📤 दस्तावेज़ अपलोड करें",
        "मराठी": "📤 कागदपत्रे अपलोड करा",
    },
    "upload_pdf_label": {
        "English": "Upload one or more PDF documents",
        "हिंदी": "एक या अधिक PDF दस्तावेज़ अपलोड करें",
        "मराठी": "एक किंवा अधिक PDF कागदपत्रे अपलोड करा",
    },
    "paste_text_label": {
        "English": "Or paste text as a document",
        "हिंदी": "या पाठ को दस्तावेज़ के रूप में पेस्ट करें",
        "मराठी": "किंवा मजकूर कागदपत्र म्हणून पेस्ट करा",
    },
    "paste_text_name_label": {
        "English": "Name for this pasted document",
        "हिंदी": "इस पेस्ट किए गए दस्तावेज़ का नाम",
        "मराठी": "या पेस्ट केलेल्या कागदपत्राचे नाव",
    },
    "add_pasted_doc_btn": {
        "English": "Add pasted text to index",
        "हिंदी": "पेस्ट किए गए टेक्स्ट को इंडेक्स में जोड़ें",
        "मराठी": "पेस्ट केलेला मजकूर इंडेक्समध्ये जोडा",
    },
    "build_index_btn": {
        "English": "Build / Refresh Index",
        "हिंदी": "इंडेक्स बनाएं / ताज़ा करें",
        "मराठी": "इंडेक्स तयार करा / ताजे करा",
    },
    "index_built_success": {
        "English": "Index built successfully with {n} chunk(s) from {d} document(s).",
        "हिंदी": "{d} दस्तावेज़ों से {n} खंड(खंडों) के साथ इंडेक्स सफलतापूर्वक बनाया गया।",
        "मराठी": "{d} कागदपत्रांमधून {n} भागांसह इंडेक्स यशस्वीरित्या तयार झाला.",
    },
    "no_docs_warning": {
        "English": "⚠️ Please upload at least one PDF or paste some text before asking a question.",
        "हिंदी": "⚠️ कृपया प्रश्न पूछने से पहले कम से कम एक PDF अपलोड करें या कुछ टेक्स्ट पेस्ट करें।",
        "मराठी": "⚠️ कृपया प्रश्न विचारण्यापूर्वी किमान एक PDF अपलोड करा किंवा काही मजकूर पेस्ट करा.",
    },
    "empty_text_warning": {
        "English": "⚠️ No readable text could be extracted from this document.",
        "हिंदी": "⚠️ इस दस्तावेज़ से कोई पठनीय टेक्स्ट नहीं निकाला जा सका।",
        "मराठी": "⚠️ या कागदपत्रातून कोणताही वाचनीय मजकूर काढता आला नाही.",
    },
    "empty_question_warning": {
        "English": "⚠️ Please type a question before sending.",
        "हिंदी": "⚠️ भेजने से पहले कृपया एक प्रश्न लिखें।",
        "मराठी": "⚠️ पाठवण्यापूर्वी कृपया प्रश्न टाइप करा.",
    },
    "not_found_answer": {
        "English": "🤔 Not enough information found in uploaded document(s). Try rephrasing, or upload a more relevant document.",
        "हिंदी": "🤔 अपलोड किए गए दस्तावेज़(दस्तावेज़ों) में पर्याप्त जानकारी नहीं मिली। कृपया प्रश्न को अलग तरीके से लिखें या अधिक प्रासंगिक दस्तावेज़ अपलोड करें।",
        "मराठी": "🤔 अपलोड केलेल्या कागदपत्रांमध्ये पुरेशी माहिती सापडली नाही. कृपया प्रश्न वेगळ्या पद्धतीने विचारा किंवा अधिक संबंधित कागदपत्र अपलोड करा.",
    },
    "chat_input_placeholder": {
        "English": "Ask a question about your uploaded document(s)...",
        "हिंदी": "अपने अपलोड किए गए दस्तावेज़(दस्तावेज़ों) के बारे में प्रश्न पूछें...",
        "मराठी": "तुमच्या अपलोड केलेल्या कागदपत्रांबद्दल प्रश्न विचारा...",
    },
    "match_score": {"English": "Top match score", "हिंदी": "शीर्ष मिलान स्कोर", "मराठी": "सर्वोत्तम जुळणी गुण"},
    "source_doc": {"English": "Source document", "हिंदी": "स्रोत दस्तावेज़", "मराठी": "स्रोत कागदपत्र"},
    "page_no": {"English": "Page number", "हिंदी": "पृष्ठ संख्या", "मराठी": "पृष्ठ क्रमांक"},
    "chunk_id": {"English": "Chunk ID", "हिंदी": "खंड आईडी", "मराठी": "भाग आयडी"},
    "excerpt": {"English": "Excerpt used", "हिंदी": "प्रयुक्त अंश", "मराठी": "वापरलेला उतारा"},

    "voice_header": {
        "English": "🎙️ Voice input (beta)",
        "हिंदी": "🎙️ आवाज़ इनपुट (बीटा)",
        "मराठी": "🎙️ आवाज इनपुट (बीटा)",
    },
    "voice_record_label": {
        "English": "Record your question",
        "हिंदी": "अपना प्रश्न रिकॉर्ड करें",
        "मराठी": "तुमचा प्रश्न रेकॉर्ड करा",
    },
    "voice_processing": {
        "English": "Processing audio...",
        "हिंदी": "ऑडियो प्रोसेस हो रहा है...",
        "मराठी": "ऑडिओ प्रक्रिया होत आहे...",
    },
    "voice_recognized": {
        "English": "Recognized text",
        "हिंदी": "पहचाना गया टेक्स्ट",
        "मराठी": "ओळखलेला मजकूर",
    },
    "voice_fail": {
        "English": "😕 Could not recognize speech. Please try again or type your question instead.",
        "हिंदी": "😕 आवाज़ पहचानी नहीं जा सकी। कृपया पुनः प्रयास करें या इसके बजाय टाइप करें।",
        "मराठी": "😕 आवाज ओळखता आली नाही. कृपया पुन्हा प्रयत्न करा किंवा त्याऐवजी टाइप करा.",
    },
    "voice_lib_missing": {
        "English": "Voice recognition library not available in this environment. Please type your question.",
        "हिंदी": "इस वातावरण में आवाज़ पहचान लाइब्रेरी उपलब्ध नहीं है। कृपया अपना प्रश्न टाइप करें।",
        "मराठी": "या वातावरणात आवाज ओळख लायब्ररी उपलब्ध नाही. कृपया तुमचा प्रश्न टाइप करा.",
    },

    "image_header": {
        "English": "🖼️ Upload or capture an image",
        "हिंदी": "🖼️ छवि अपलोड करें या कैप्चर करें",
        "मराठी": "🖼️ प्रतिमा अपलोड करा किंवा टिपा",
    },
    "image_upload_label": {
        "English": "Upload an image (JPG/PNG)",
        "हिंदी": "एक छवि अपलोड करें (JPG/PNG)",
        "मराठी": "प्रतिमा अपलोड करा (JPG/PNG)",
    },
    "image_camera_label": {
        "English": "Or capture using camera",
        "हिंदी": "या कैमरे का उपयोग करके कैप्चर करें",
        "मराठी": "किंवा कॅमेरा वापरून टिपा",
    },
    "ocr_note": {
        "English": "ℹ️ OCR not enabled in MVP — image is shown for reference only, text is not extracted from it.",
        "हिंदी": "ℹ️ MVP में OCR सक्षम नहीं है — छवि केवल संदर्भ के लिए दिखाई गई है, इससे टेक्स्ट नहीं निकाला जाता।",
        "मराठी": "ℹ️ MVP मध्ये OCR सक्षम नाही — प्रतिमा केवळ संदर्भासाठी दाखवली आहे, त्यातून मजकूर काढला जात नाही.",
    },

    "doc_tab_header": {
        "English": "📄 Uploaded Documents & Index",
        "हिंदी": "📄 अपलोड किए गए दस्तावेज़ और इंडेक्स",
        "मराठी": "📄 अपलोड केलेली कागदपत्रे आणि इंडेक्स",
    },
    "total_docs": {"English": "Total documents", "हिंदी": "कुल दस्तावेज़", "मराठी": "एकूण कागदपत्रे"},
    "total_chunks": {"English": "Total chunks", "हिंदी": "कुल खंड", "मराठी": "एकूण भाग"},
    "clear_index_btn": {
        "English": "🗑️ Clear / Reset Index",
        "हिंदी": "🗑️ इंडेक्स साफ़ करें / रीसेट करें",
        "मराठी": "🗑️ इंडेक्स साफ करा / रीसेट करा",
    },
    "index_cleared": {
        "English": "Index cleared.",
        "हिंदी": "इंडेक्स साफ़ कर दिया गया।",
        "मराठी": "इंडेक्स साफ केला.",
    },
    "no_docs_yet": {
        "English": "No documents uploaded yet. Go to the Chat tab to upload PDFs or paste text.",
        "हिंदी": "अभी तक कोई दस्तावेज़ अपलोड नहीं किया गया है। PDF अपलोड करने या टेक्स्ट पेस्ट करने के लिए चैट टैब पर जाएं।",
        "मराठी": "अद्याप कोणतीही कागदपत्रे अपलोड केलेली नाहीत. PDF अपलोड करण्यासाठी किंवा मजकूर पेस्ट करण्यासाठी चॅट टॅबवर जा.",
    },

    "lawyer_header": {
        "English": "⚖️ Find a Lawyer (Directory)",
        "हिंदी": "⚖️ वकील खोजें (निर्देशिका)",
        "मराठी": "⚖️ वकील शोधा (निर्देशिका)",
    },
    "lawyer_disclaimer": {
        "English": "Directory is informational; verify credentials independently.",
        "हिंदी": "यह निर्देशिका केवल जानकारी के लिए है; कृपया स्वतंत्र रूप से योग्यताओं की पुष्टि करें।",
        "मराठी": "ही निर्देशिका केवळ माहितीसाठी आहे; कृपया स्वतंत्रपणे पात्रता तपासा.",
    },
    "filter_city": {"English": "City", "हिंदी": "शहर", "मराठी": "शहर"},
    "filter_specialization": {"English": "Specialization", "हिंदी": "विशेषज्ञता", "मराठी": "विशेषज्ञता"},
    "filter_language": {"English": "Language", "हिंदी": "भाषा", "मराठी": "भाषा"},
    "filter_fees": {"English": "Max consultation fee (₹)", "हिंदी": "अधिकतम परामर्श शुल्क (₹)", "मराठी": "कमाल सल्ला शुल्क (₹)"},
    "no_lawyers_found": {
        "English": "No lawyers match the selected filters.",
        "हिंदी": "चयनित फ़िल्टर से मेल खाने वाला कोई वकील नहीं मिला।",
        "मराठी": "निवडलेल्या फिल्टरशी जुळणारा कोणताही वकील सापडला नाही.",
    },

    "sos_header": {
        "English": "🆘 Emergency Numbers (India)",
        "हिंदी": "🆘 आपातकालीन नंबर (भारत)",
        "मराठी": "🆘 आणीबाणी क्रमांक (भारत)",
    },
    "sos_note": {
        "English": "If you are in immediate danger, call 112.",
        "हिंदी": "यदि आप तत्काल खतरे में हैं, तो 112 पर कॉल करें।",
        "मराठी": "जर तुम्ही तात्काळ धोक्यात असाल, तर 112 वर कॉल करा.",
    },

    "about_header": {
        "English": "ℹ️ About This Project",
        "हिंदी": "ℹ️ इस प्रोजेक्ट के बारे में",
        "मराठी": "ℹ️ या प्रकल्पाबद्दल",
    },
    "about_text": {
        "English": (
            "LegalEase India is a hackathon MVP that helps citizens understand "
            "government and legal documents in simple language using classic NLP "
            "(TF-IDF + cosine similarity). It does not use any large language model "
            "and does not connect to paid APIs. All answers are extracted directly "
            "from documents you provide — nothing is invented."
        ),
        "हिंदी": (
            "लीगलईज़ इंडिया एक हैकाथॉन एमवीपी है जो क्लासिक एनएलपी (TF-IDF + कोसाइन "
            "समानता) का उपयोग करके नागरिकों को सरकारी और कानूनी दस्तावेज़ों को सरल भाषा "
            "में समझने में मदद करता है। यह किसी बड़े भाषा मॉडल का उपयोग नहीं करता और "
            "किसी सशुल्क एपीआई से नहीं जुड़ता। सभी उत्तर सीधे आपके द्वारा प्रदान किए गए "
            "दस्तावेज़ों से निकाले जाते हैं — कुछ भी गढ़ा नहीं जाता।"
        ),
        "मराठी": (
            "लीगलईज इंडिया हा एक हॅकेथॉन एमव्हीपी आहे जो क्लासिक एनएलपी (TF-IDF + "
            "कोसाइन समानता) वापरून नागरिकांना सरकारी आणि कायदेशीर कागदपत्रे सोप्या "
            "भाषेत समजून घेण्यास मदत करतो. हे कोणतेही मोठे भाषा मॉडेल वापरत नाही आणि "
            "कोणत्याही सशुल्क एपीआयशी जोडलेले नाही. सर्व उत्तरे थेट तुम्ही दिलेल्या "
            "कागदपत्रांमधून काढली जातात — काहीही रचलेले नाही."
        ),
    },
    "about_sources_header": {
        "English": "Suggested India-specific sources for real documents",
        "हिंदी": "वास्तविक दस्तावेज़ों के लिए सुझाए गए भारत-विशिष्ट स्रोत",
        "मराठी": "खऱ्या कागदपत्रांसाठी सुचवलेले भारत-विशिष्ट स्रोत",
    },
    "sidebar_language_label": {
        "English": "🌐 Language / भाषा",
        "हिंदी": "🌐 भाषा / Language",
        "मराठी": "🌐 भाषा / Language",
    },
    "sos_button_label": {"English": "🆘 SOS", "हिंदी": "🆘 एसओएस", "मराठी": "🆘 एसओएस"},
}


def T(lang: str, key: str, **kwargs) -> str:
    """
    Translation helper.
    lang: one of "English", "हिंदी", "मराठी"
    key: key in TEXT dict
    kwargs: optional .format() args, e.g. T(lang, "index_built_success", n=5, d=2)
    Falls back to English, then to the raw key if nothing is found.
    """
    entry = TEXT.get(key)
    if entry is None:
        return key
    value = entry.get(lang, entry.get("English", key))
    if kwargs:
        try:
            value = value.format(**kwargs)
        except Exception:
            pass
    return value
