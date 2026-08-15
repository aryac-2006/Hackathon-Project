"""
lawyer_directory.py
Loads the local sample lawyers.json file and provides simple
filtering helpers used by the "Find a Lawyer" tab.
"""

import json
import os
from typing import List, Dict


def load_lawyers(json_path: str) -> List[Dict]:
    """Load lawyer records from a local JSON file. Returns [] on any error."""
    try:
        if not os.path.exists(json_path):
            return []
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception:
        return []


def get_unique_cities(lawyers: List[Dict]) -> List[str]:
    return sorted({l.get("city", "").strip() for l in lawyers if l.get("city")})


def get_unique_specializations(lawyers: List[Dict]) -> List[str]:
    specs = set()
    for l in lawyers:
        for s in l.get("specialization", []):
            specs.add(s)
    return sorted(specs)


def get_unique_languages(lawyers: List[Dict]) -> List[str]:
    langs = set()
    for l in lawyers:
        for lg in l.get("languages", []):
            langs.add(lg)
    return sorted(langs)


def filter_lawyers(
    lawyers: List[Dict],
    city: str = "All",
    specialization: str = "All",
    language: str = "All",
    max_fee: int = None,
) -> List[Dict]:
    """Apply the selected filters and return the matching subset."""
    result = lawyers

    if city and city != "All":
        result = [l for l in result if l.get("city") == city]

    if specialization and specialization != "All":
        result = [l for l in result if specialization in l.get("specialization", [])]

    if language and language != "All":
        result = [l for l in result if language in l.get("languages", [])]

    if max_fee is not None:
        result = [l for l in result if l.get("fees", 0) <= max_fee]

    return result
