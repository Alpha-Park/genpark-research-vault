# -*- coding: utf-8 -*-
"""
GenPark Research Vault MCP Server
FastMCP standard interface for h-index computation, bibliographic coupling, and keyphrase extraction.
"""

import json
from typing import Dict, Any, List
from client import GenParkResearchVault

try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("genpark-research-vault")
except ImportError:
    class MockFastMCP:
        def __init__(self, name):
            self.name = name
        def tool(self):
            def decorator(f):
                return f
            return decorator
    mcp = MockFastMCP("genpark-research-vault")

vault = GenParkResearchVault()

@mcp.tool()
def calculate_h_index_and_citation_metrics(
    citation_counts: List[int]
) -> str:
    """
    Calculates Hirsch h-index, i10-index, and Egghe g-index from citation counts.
    """
    res = vault.calculate_h_index_and_citation_metrics(citation_counts)
    return json.dumps(res, indent=2)

@mcp.tool()
def compute_bibliographic_coupling_cosine(
    citations_paper_a: List[str],
    citations_paper_b: List[str]
) -> str:
    """
    Computes bibliographic coupling similarity between two research papers.
    """
    res = vault.compute_bibliographic_coupling_cosine(citations_paper_a, citations_paper_b)
    return json.dumps(res, indent=2)

@mcp.tool()
def extract_latent_keyphrase_importance(
    abstract_text: str,
    top_k: int = 5
) -> str:
    """
    Extracts salient scientific keywords using frequency-adjusted lexical weighting.
    """
    res = vault.extract_latent_keyphrase_importance(abstract_text, top_k)
    return json.dumps(res, indent=2)

def main():
    print("Testing Research Vault:")
    print(calculate_h_index_and_citation_metrics([55, 32, 28, 14, 10, 8, 3, 1]))

if __name__ == "__main__":
    main()
