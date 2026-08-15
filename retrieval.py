"""
retrieval.py
Core "AI" of the app: TF-IDF vectorization + cosine similarity search
over document chunks. Uses character n-grams (analyzer="char_wb") so
that it works reasonably across English, Hindi and Marathi scripts
without needing language-specific tokenizers or any external model.
"""

from typing import List, Dict, Tuple, Optional
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .constants import TOP_K, SIMILARITY_THRESHOLD


class DocumentIndex:
    """Holds all chunks + the fitted TF-IDF index for the current session."""

    def __init__(self):
        self.chunks: List[Dict] = []          # list of chunk dicts
        self.vectorizer: Optional[TfidfVectorizer] = None
        self.matrix = None                    # TF-IDF matrix for all chunks

    def add_chunks(self, new_chunks: List[Dict]):
        self.chunks.extend(new_chunks)

    def has_chunks(self) -> bool:
        return len(self.chunks) > 0

    def num_docs(self) -> int:
        return len({c["doc_name"] for c in self.chunks})

    def num_chunks(self) -> int:
        return len(self.chunks)

    def clear(self):
        self.chunks = []
        self.vectorizer = None
        self.matrix = None

    def build_index(self):
        """(Re)fit the TF-IDF vectorizer over all current chunks."""
        if not self.chunks:
            self.vectorizer = None
            self.matrix = None
            return

        texts = [c["raw_text"] for c in self.chunks]
        # char_wb n-grams (3-5) work across scripts (Devanagari + Latin)
        # without needing language-specific tokenization.
        self.vectorizer = TfidfVectorizer(
            analyzer="char_wb",
            ngram_range=(3, 5),
            min_df=1,
            max_features=50000,
        )
        self.matrix = self.vectorizer.fit_transform(texts)

    def search(self, query: str, top_k: int = TOP_K) -> List[Tuple[Dict, float]]:
        """
        Search the index for the query.

        Returns:
            List of (chunk_dict, score) tuples, sorted by score descending,
            length <= top_k. Empty list if index is not built or query is empty.
        """
        query = (query or "").strip()
        if not query or self.vectorizer is None or self.matrix is None:
            return []

        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.matrix)[0]

        # Get indices of top_k highest scores
        ranked_indices = scores.argsort()[::-1][:top_k]
        results = [(self.chunks[i], float(scores[i])) for i in ranked_indices]
        return results

    def best_match(self, query: str) -> Tuple[Optional[Dict], float, List[Tuple[Dict, float]]]:
        """
        Convenience method: returns (best_chunk_or_None, best_score, all_top_matches).
        best_chunk is None if score is below SIMILARITY_THRESHOLD.
        """
        results = self.search(query)
        if not results:
            return None, 0.0, []

        best_chunk, best_score = results[0]
        if best_score < SIMILARITY_THRESHOLD:
            return None, best_score, results

        return best_chunk, best_score, results


def extractive_summary(text: str, max_sentences: int = 3) -> str:
    """
    Very simple extractive 'summary': just returns the first N sentences
    of the given text. No generation, no invention — purely extractive,
    so it works the same for English/Hindi/Marathi punctuation (., ।, ॥).
    """
    if not text:
        return ""

    # Split on common sentence terminators used in English, Hindi, Marathi
    import re
    sentences = re.split(r'(?<=[.!?।॥])\s+', text.strip())
    sentences = [s for s in sentences if s.strip()]

    if not sentences:
        return text[:300]

    return " ".join(sentences[:max_sentences])
