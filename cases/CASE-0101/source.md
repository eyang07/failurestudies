# CASE-0101: Source Packet

Paper: [ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization](https://arxiv.org/pdf/2510.15981)

Version: arXiv:2510.15981v1, submitted 2025-10-13 10:20:11 UTC

Locator: arXiv:2510.15981v1, Figure 2(b), p. 4; Appendix A.5.1 and Figure 7, pp. 15-17. Repository data/benchmark_0409.json record origin=dummy,id=6; benchmark_results/output_pickle/benckmark6%20-%20think%20noDAG/dummy_6.json.pickle.html and benchmark_results/output_pickle/benckmark5%20-%20no%20think%20noDAG/dummy_6.json.pickle.html, nodeInfo.l3.solved_lemma.

Input kind: original

Transcription status: exact_transcription

## Supplied Mathematical Material

Theorem (exact nl_theorem field):
If $n$ is an odd integer, then $n^2 \equiv 1 \pmod{8}$.

Proof (exact nl_proof field):
Since $n$ is odd, we can write $n = 2k + 1$ for some integer $k$. Then $n^2 = (2k + 1)^2 = 4k^2 + 4k + 1$. We can factor this as $n^2 = 4k(k + 1) + 1$. Now, either $k$ is even or $k$ is odd. If $k$ is even, then $k + 1$ is odd, and if $k$ is odd, then $k + 1$ is even. In either case, $k(k + 1)$ is even, so $k(k + 1) = 2m$ for some integer $m$. Therefore $n^2 = 4(2m) + 1 = 8m + 1$, which means $n^2 \equiv 1 \pmod{8}$.
