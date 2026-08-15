"""
sos_data.py
Static list of important Indian emergency helpline numbers.
Kept as plain Python data (no external API) for reliability in a demo.
"""

EMERGENCY_NUMBERS = [
    {"name_en": "National Emergency", "name_hi": "राष्ट्रीय आपातकालीन", "name_mr": "राष्ट्रीय आणीबाणी", "number": "112"},
    {"name_en": "Police", "name_hi": "पुलिस", "name_mr": "पोलीस", "number": "100"},
    {"name_en": "Fire", "name_hi": "अग्निशमन", "name_mr": "अग्निशमन दल", "number": "101"},
    {"name_en": "Ambulance", "name_hi": "एम्बुलेंस", "name_mr": "रुग्णवाहिका", "number": "102 / 108"},
    {"name_en": "Women Helpline", "name_hi": "महिला हेल्पलाइन", "name_mr": "महिला हेल्पलाइन", "number": "1091"},
    {"name_en": "Child Helpline", "name_hi": "चाइल्ड हेल्पलाइन", "name_mr": "चाइल्ड हेल्पलाइन", "number": "1098"},
    {"name_en": "Cyber Crime Helpline", "name_hi": "साइबर क्राइम हेल्पलाइन", "name_mr": "सायबर क्राइम हेल्पलाइन", "number": "1930"},
    {"name_en": "Road Accident Emergency", "name_hi": "सड़क दुर्घटना आपातकाल", "name_mr": "रस्ता अपघात आणीबाणी", "number": "1073"},
    {"name_en": "Senior Citizen Helpline", "name_hi": "वरिष्ठ नागरिक हेल्पलाइन", "name_mr": "ज्येष्ठ नागरिक हेल्पलाइन", "number": "1291 / 14567"},
    {"name_en": "Disaster Management (NDMA)", "name_hi": "आपदा प्रबंधन (एनडीएमए)", "name_mr": "आपत्ती व्यवस्थापन (एनडीएमए)", "number": "1078"},
]


def get_localized_numbers(lang: str):
    """Return list of dicts with a single 'name' field localized to the given language."""
    key_map = {"English": "name_en", "हिंदी": "name_hi", "मराठी": "name_mr"}
    key = key_map.get(lang, "name_en")
    return [{"name": item[key], "number": item["number"]} for item in EMERGENCY_NUMBERS]
