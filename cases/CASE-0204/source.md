# CASE-0204: Source Packet

Paper: [Navier-Stokes lost in translation: Why Lean verification of AI autoformalisation does not guarantee correct natural language proofs](https://arxiv.org/pdf/2610.08144v1)

Version: arXiv:2610.08144v1, submitted 2026-10-06 10:58:01 UTC; 25 pages

Locator: arXiv:2610.08144v1, Example 3.3 and Section 3.2.1, printed pp. 8-12; Figure 4 on p. 9. Original NL source: Lemma 10.5, equation (10.19), pp. 122-123. Code commit f9e8bc5b38b6e212696e8a30e3e91517af887bbd.

Input kind: original

Transcription status: partial_transcription

## Supplied Mathematical Material

Equation excerpt (10.19), notation linearized: |integral pi*w dot grad(chi_R)| <= (C_T/R)*[(B_R+1)*B_R^(1/2)+R^(-3/4)*B_R^(3/4)]. Context paraphrase: R>=1; the pressure identity preceding the estimate is stated for almost every t in (0,T). The NL derivation pairs pressure terms with a cutoff-weighted velocity and uses interpolation. The complete Lemma 10.5, norm definitions and hypotheses are omitted.
