"""
chunking.py
Splits page text into overlapping character-based chunks and attaches
metadata (doc_name, page_num, chunk_id, raw_text). Character-based
chunking (rather than word/token based) keeps things simple and works
reasonably across English, Hindi and Marathi scripts.
"""

from typing import List, Dict
from .constants import CHUNK_SIZE_CHARS, CHUNK_OVERLAP_CHARS


def chunk_text(text: str, size: int = CHUNK_SIZE_CHARS, overlap: int = CHUNK_OVERLAP_CHARS) -> List[str]:
    """Split a block of text into overlapping chunks."""
    text = text.strip()
    if not text:
        return []

    if len(text) <= size:
        return [text]

    chunks = []
    start = 0
    step = max(size - overlap, 1)  # avoid infinite loop if overlap >= size
    while start < len(text):
        end = start + size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start += step

    return chunks


def build_chunks_for_document(doc_name: str, pages: List[tuple]) -> List[Dict]:
    """
    Build a list of chunk dicts for a single document.

    Args:
        doc_name: display name of the document
        pages: list of (page_num, page_text) tuples

    Returns:
        List of dicts: {doc_name, page_num, chunk_id, raw_text}
    """
    all_chunks = []
    running_id = 0
    for page_num, page_text in pages:
        pieces = chunk_text(page_text)
        for piece in pieces:
            running_id += 1
            all_chunks.append({
                "doc_name": doc_name,
                "page_num": page_num,
                "chunk_id": f"{doc_name}-p{page_num}-c{running_id}",
                "raw_text": piece,
            })
    return all_chunks


def build_chunks_from_plain_text(doc_name: str, text: str) -> List[Dict]:
    """Same as above but for a single pasted block of text (no real pages -> page 1)."""
    return build_chunks_for_document(doc_name, [(1, text)])
