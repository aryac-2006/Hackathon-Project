"""
constants.py
Central place for colors, fonts, thresholds and other fixed values
so we don't hardcode magic numbers/strings all over the app.
"""

# ---------- THEME ----------
NAVY = "#0B1F3B"
SAFFRON = "#FF9933"
WHITE = "#FFFFFF"
LIGHT_BG = "#F7F7F5"
GREY_TEXT = "#4A4A4A"

FONT_FAMILY = "'Poppins', 'Inter', sans-serif"

# ---------- RETRIEVAL ----------
# Below this cosine similarity score we say "not enough information".
# Tuned empirically: with char_wb(3,5) TF-IDF, unrelated short queries
# typically score ~0.13-0.20 against any document (common substrings),
# while genuinely relevant queries score 0.35+. 0.25 gives a safer margin
# against false positives while still catching short relevant queries.
SIMILARITY_THRESHOLD = 0.25

# Number of top matches to consider before picking the best one
TOP_K = 3

# Chunking settings (character based so it works across Hindi/Marathi/English)
CHUNK_SIZE_CHARS = 800
CHUNK_OVERLAP_CHARS = 150

# ---------- MISC ----------
APP_TITLE = "LegalEase India"
SUPPORTED_LANGS = ["English", "हिंदी", "मराठी"]
LANG_CODES = {"English": "en", "हिंदी": "hi", "मराठी": "mr"}

# Emergency numbers reference note (India only)
EMERGENCY_NOTE = "If you are in immediate danger, call 112."
