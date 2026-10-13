# CASE-0104: Source Packet

Paper: [ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization](https://arxiv.org/pdf/2510.15981)

Version: arXiv:2510.15981v1, submitted 2025-10-13 10:20:11 UTC

Locator: arXiv:2510.15981v1 Appendix A.5.3 and Figure 9, pp. 17-19; benchmark_results/output_pickle/benckmark6%20-%20think%20noDAG/dummy_9.json.pickle.html, nodeInfo.ts_1.solved_lemma and nodeInfo.ts_1.score.

Input kind: original

Transcription status: exact_transcription

## Supplied Mathematical Material

Theorem (exact nl_theorem field):
If $(a_n)$ is an arithmetic sequence with $a_1 = 5$ and $a_3 = 11$, then $a_5 = 17$.

Proof (exact nl_proof field):
Since $(a_n)$ is arithmetic, there exists a common difference $d$ such that $a_n = a_1 + (n-1)d$ for all $n$. From the given information, $a_3 = a_1 + 2d$. Substituting the values: $11 = 5 + 2d$, which gives us $2d = 6$, so $d = 3$. Now we can find $a_5 = a_1 + 4d = 5 + 4(3) = 5 + 12 = 17$
