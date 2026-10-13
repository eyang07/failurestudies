# CASE-0002: Provisional Assessment

Evaluator-only material.

## Case kind

reported_failure

## Source validity

invalid

## Validity basis

The authors identify the regex perturbation as false. The collector's documentary arithmetic inspection notes that 1000 - 2 is 998, not 686; splitting 1000 equally across two publishers gives 500. This concerns the altered step, not the validity of every source-chain statement. No Lean execution occurred.

## Content fidelity

violated

## Argument fidelity

not_assessable

## Evidence status

reported

## Readiness

needs_artifacts

## Reported model

Kimina (7B), as attributed in Appendix H.1 Example 5 and Section 6. Appendix F reports greedy decoding (temperature 0) and a 16,384 generated-token limit for the specialized models other than Herald. Exact checkpoint and this request's record unknown.

## Reported environment

Published protocol (Appendix F): Lean 4 theorem extraction and type-checking with by sorry, followed by DeepSeek-Prover-V2-7B direct/negated proof attempts at pass@2. Original run-specific Lean version, mathlib commit, request settings and compiler logs were not recovered. The subsequently released repository pins leanprover/lean4:v4.9.0-rc1 in src/veriform/proving/lean_server/lean/lean-toolchain; this is repository metadata, not a verified original-run environment.

## Reported outcome

Appendix H.1 reports a provable theorem obtained from an inconsistent bundle of premises, using False to close the false arithmetic goal. Not independently checked.

## Original prompt status

unavailable

## Original prompt

unknown

## Licensing

Paper: Cornish, Ghinassi, Yeh, Liu, Xu, Yin, Wagner, Li, Teh and Ong (2026), CC BY 4.0 (arXiv license link https://creativecommons.org/licenses/by/4.0/). Dataset/repository: MIT; copyright (c) 2024 The Authors, retained in LICENSE.source.txt. Minimal source excerpts only; no full paper retained. Exact excerpts are unmodified; collector descriptions and judgments are separately labeled.

## Notes

The text below is the exact lstlisting excerpt in sections/appendix/qualitative_examples.tex, verified against the primary arXiv v1 TeX source. It is a published theorem/proof excerpt, not a recovered raw autoformalizer response. Appendix F separates statement autoformalization from subsequent proving; do not attribute all proof-body tactics to the named autoformalizer. Ellipses, if present, are the paper's own omissions. The regex input agrees with the arithmetic summarized in the appendix. No full fine-tuned-model prompt or matching raw result was recovered. The bounded public Faithform-AF row lookup timed out. Other family facts may justify the rate values, but do not justify the inconsistent h_total equation.

## Primary Artifacts

- https://arxiv.org/pdf/2608.10916v1
- https://arxiv.org/src/2608.10916v1
- https://github.com/Ighina/FaithformBench/blob/fd90fe330bf423f6046af24435d44cf03a227584/FaithformBench-Regex.csv
- https://huggingface.co/datasets/ighina/Faithform-AF/tree/86b7061b73580c6694f593ded9f7fbbc1d07083e
