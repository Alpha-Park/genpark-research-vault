# -*- coding: utf-8 -*-
from client import GenParkResearchVault

vault = GenParkResearchVault()

# 1. h-index & Citation Impact
citations = [84, 52, 41, 33, 19, 12, 11, 9, 6, 4, 2, 1]
metrics = vault.calculate_h_index_and_citation_metrics(citations)
print(f"Citation Metrics: h-index={metrics['h_index']}, i10={metrics['i10_index']}, g-index={metrics['g_index']} ({metrics['impact_classification']})")
print(f"  Total Citations: {metrics['total_citations']} (Mean: {metrics['mean_citations_per_paper']} per paper)")

# 2. Bibliographic Coupling Cosine
paper_a_refs = ["vaswani2017attention", "devlin2018bert", "brown2020gpt3", "radford2019gpt2"]
paper_b_refs = ["vaswani2017attention", "brown2020gpt3", "touvron2023llama", "openai2023gpt4"]
coupling = vault.compute_bibliographic_coupling_cosine(paper_a_refs, paper_b_refs)
print()
print(f"Bibliographic Coupling: Cosine={coupling['cosine_similarity']}, Jaccard={coupling['jaccard_similarity']}")
print(f"  Shared Literature: {coupling['shared_references']} ({coupling['affinity_strength']})")

# 3. Scientific Keyphrase Extraction
abstract = """
Autonomous multi-agent swarms coordinate through decentralized consensus protocols.
We present an empirical evaluation of latency budgets, communication topology, and cryptographic proof verification.
"""
keys = vault.extract_latent_keyphrase_importance(abstract, top_k=4)
print()
print(f"Extracted Keyphrases: {[k['phrase'] for k in keys['top_keyphrases']]}")
