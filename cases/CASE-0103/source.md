# CASE-0103: Source Packet

Paper: [ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization](https://arxiv.org/pdf/2510.15981)

Version: arXiv:2510.15981v1, submitted 2025-10-13 10:20:11 UTC

Locator: arXiv:2510.15981v1 Appendix A.5.2, p. 17; data/benchmark_0409.json origin=dummy,id=7; benchmark_results/output_pickle/benckmark3%20-%20think%20DAG/dummy_7.json.pickle.html, nodeInfo.l3.

Input kind: original

Transcription status: exact_transcription

## Supplied Mathematical Material

Theorem (exact nl_theorem field):
If $P(A) = 0.6$ and $P(B) = 0.7$, then $P(A \cap B) \geq 0.3

Proof (exact nl_proof field):
We know that $P(A \cup B) = P(A) + P(B) - P(A \cap B)$. Since $P(A \cup B) \leq 1$, we have $P(A) + P(B) - P(A \cap B) \leq 1$. Substituting the given values: $0.6 + 0.7 - P(A \cap B) \leq 1$, which gives $1.3 - P(A \cap B) \leq 1$. Therefore $P(A \cap B) \geq 0.3$.
