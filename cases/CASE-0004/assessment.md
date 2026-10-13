# CASE-0004: Provisional Assessment

Evaluator-only material.

## Case kind

reported_failure

## Source validity

ambiguous

## Validity basis

The appendix's stated input, with x real and 3^x = 5 but target 3^(x+2) = 51, is reported invalid (the algebraic value is 45). The related released regex row instead says 3*(x+2) = 51. Its dependencies omit an explicit real-domain declaration. The collector preserves the two provenance variants and has not established which exact input produced the published output; therefore this case's source packet remains ambiguous, rather than silently treating the variants as identical.

## Content fidelity

uncertain

## Argument fidelity

not_assessable

## Evidence status

disputed

## Readiness

needs_context

## Reported model

Kimina (7B), as attributed in Figure 1 and Appendix H.1 Example 7. Appendix F reports specialized-model temperature 0 and up to 16,384 generated tokens (except Herald). Exact checkpoint and original request record unknown.

## Reported environment

Published protocol (Appendix F): Lean 4 theorem extraction and type-checking with by sorry, followed by DeepSeek-Prover-V2-7B direct/negated proof attempts at pass@2. Original run-specific Lean version, mathlib commit, request settings and compiler logs were not recovered. The subsequently released repository pins leanprover/lean4:v4.9.0-rc1 in src/veriform/proving/lean_server/lean/lean-toolchain; this is repository metadata, not a verified original-run environment.

## Reported outcome

Figure 1 and Appendix H.1 report that narrowing x from real to natural makes 3^x = 5 unsatisfiable and permits ex falso. Figure 1 also reports a real-typed output for the unperturbed 45 case; that comparison artifact was not independently recovered. No new proof result is claimed.

## Original prompt status

unavailable

## Original prompt

unknown

## Licensing

Paper: Cornish, Ghinassi, Yeh, Liu, Xu, Yin, Wagner, Li, Teh and Ong (2026), CC BY 4.0 (arXiv license link https://creativecommons.org/licenses/by/4.0/). Dataset/repository: MIT; copyright (c) 2024 The Authors, retained in LICENSE.source.txt. Minimal source excerpts only; no full paper retained. Exact excerpts are unmodified; collector descriptions and judgments are separately labeled.

## Notes

The text below is the exact lstlisting excerpt in sections/appendix/qualitative_examples.tex, verified against the primary arXiv v1 TeX source. It is a published theorem/proof excerpt, not a recovered raw autoformalizer response. Appendix F separates statement autoformalization from subsequent proving; do not attribute all proof-body tactics to the named autoformalizer. Ellipses, if present, are the paper's own omissions. This case records the paper's reported mechanism, with a related released row retained separately. The discrepancy may reflect provenance/versioning or a transcription issue; its cause is unknown, and it is not a demonstrated paper error. The fine-tuned result lookup timed out. Resolve the exact appendix-run input/output pairing before selecting an original-protocol reproduction.

## Primary Artifacts

- https://arxiv.org/pdf/2608.10916v1
- https://arxiv.org/src/2608.10916v1
- https://github.com/Ighina/FaithformBench/blob/fd90fe330bf423f6046af24435d44cf03a227584/FaithformBench-Regex.csv
- https://huggingface.co/datasets/ighina/Faithform-AF/tree/86b7061b73580c6694f593ded9f7fbbc1d07083e
