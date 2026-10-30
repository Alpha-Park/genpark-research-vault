# -*- coding: utf-8 -*-
"""
GenPark Research Vault Client
Pure Python Standard Library (Zero External Dependencies)
Implements academic paper citation impact (h-index, i10-index, g-index),
bibliographic coupling cosine similarity, and scientific keyphrase lexical importance scoring.
"""

import math
from typing import Dict, Any, List, Optional

class GenParkResearchVault:
    """
    Automated academic citation analysis, literature synthesis, and knowledge graph engine.
    """

    def __init__(self):
        pass

    def calculate_h_index_and_citation_metrics(
        self,
        citation_counts: List[int]
    ) -> Dict[str, Any]:
        """
        Calculates Hirsch h-index, i10-index, and Egghe g-index:
          h-index: max h such that at least h papers have >= h citations.
          g-index: max g such that the top g papers have >= g^2 cumulative citations.
        """
        if not citation_counts:
            return {"h_index": 0, "i10_index": 0, "g_index": 0, "total_citations": 0}

        sorted_cites = sorted(citation_counts, reverse=True)
        total_cites = sum(sorted_cites)
        n = len(sorted_cites)

        # 1. h-index
        h = 0
        for i, c in enumerate(sorted_cites):
            if c >= i + 1:
                h = i + 1
            else:
                break

        # 2. i10-index
        i10 = sum(1 for c in sorted_cites if c >= 10)

        # 3. g-index
        cum_sum = 0
        g = 0
        for i, c in enumerate(sorted_cites):
            cum_sum += c
            rank = i + 1
            if cum_sum >= rank * rank:
                g = rank

        mean_citations = round(total_cites / n, 2)

        return {
            "total_papers_analyzed": n,
            "total_citations": total_cites,
            "h_index": h,
            "i10_index": i10,
            "g_index": g,
            "mean_citations_per_paper": mean_citations,
            "impact_classification": "WORLD_CLASS_SCHOLAR" if h >= 20 else ("PROLIFIC_RESEARCHER" if h >= 10 else "EMERGING_ACADEMIC")
        }

    def compute_bibliographic_coupling_cosine(
        self,
        citations_paper_a: List[str],
        citations_paper_b: List[str]
    ) -> Dict[str, Any]:
        """
        Computes bibliographic coupling similarity between two research papers based on shared cited literature:
          Cosine = |A n B| / sqrt(|A| * |B|)
          Jaccard = |A n B| / |A u B|
        """
        set_a = set(citations_paper_a)
        set_b = set(citations_paper_b)

        if not set_a or not set_b:
            return {"cosine_similarity": 0.0, "jaccard_similarity": 0.0, "shared_references_count": 0}

        intersection = set_a.intersection(set_b)
        union = set_a.union(set_b)

        cosine = len(intersection) / math.sqrt(len(set_a) * len(set_b))
        jaccard = len(intersection) / len(union)

        return {
            "references_count_paper_a": len(set_a),
            "references_count_paper_b": len(set_b),
            "shared_references_count": len(intersection),
            "shared_references": sorted(list(intersection)),
            "cosine_similarity": round(cosine, 4),
            "jaccard_similarity": round(jaccard, 4),
            "affinity_strength": "HIGHLY_COUPLED_RELATED_WORK" if cosine >= 0.4 else "LOOSELY_CONNECTED"
        }

    def extract_latent_keyphrase_importance(
        self,
        abstract_text: str,
        top_k: int = 5
    ) -> Dict[str, Any]:
        """
        Extracts salient scientific keywords using frequency-adjusted lexical weighting.
        """
        stop_words = {"the", "and", "of", "to", "in", "a", "is", "that", "for", "with", "as", "by", "on", "are", "this", "we", "our"}
        words = [w.strip(" .,!?:;()[]{}").lower() for w in abstract_text.split() if w.strip(" .,!?:;()[]{}")]
        
        freqs = {}
        for w in words:
            if len(w) > 3 and w not in stop_words:
                freqs[w] = freqs.get(w, 0) + 1

        sorted_phrases = sorted(freqs.items(), key=lambda kv: kv[1], reverse=True)[:top_k]

        return {
            "total_abstract_words": len(words),
            "top_keyphrases": [{"phrase": k, "frequency": v} for k, v in sorted_phrases]
        }
