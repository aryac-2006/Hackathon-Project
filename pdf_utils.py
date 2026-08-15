"""
pdf_utils.py
Page-wise text extraction from PDF files using PyPDF2.
Kept intentionally simple and dependency-light for Streamlit Cloud.
"""

from typing import List, Tuple
from PyPDF2 import PdfReader


def extract_pages_from_pdf(file_obj) -> List[Tuple[int, str]]:
    """
    Extract text from a PDF file object page by page.

    Args:
        file_obj: a file-like object (e.g. from st.file_uploader)

    Returns:
        List of (page_number, page_text) tuples, 1-indexed page numbers.
        Pages with no extractable text are skipped.
    """
    pages = []
    try:
        reader = PdfReader(file_obj)
    except Exception:
        # Corrupt / unreadable PDF -> return empty list, caller handles the warning
        return pages

    for idx, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        text = text.strip()
        if text:
            pages.append((idx, text))

    return pages
