# CASE-0003: Provisional Assessment

Evaluator-only material.

## Case kind

reported_failure

## Source validity

invalid

## Validity basis

The authors report replacing subtraction by addition in the definition of change. The source row is classified general_knowledge/axiom, with no parent assumptions. Under the ordinary monetary meaning identified by that row and the unperturbed counterpart, the altered universal rule is invalid. The collector inspected the changed operator and declared role, not a Lean proof. Without that monetary interpretation an isolated equation could instead be read as an assignment; this interpretation issue is retained in uncertainties.

## Content fidelity

violated

## Argument fidelity

not_assessable

## Evidence status

reported

## Readiness

needs_artifacts

## Reported model

Claude Opus 4.7, as attributed in Appendix H.1 Example 6; exact snapshot and request parameters unknown.

## Reported environment

Published protocol (Appendix F): Lean 4 theorem extraction and type-checking with by sorry, followed by DeepSeek-Prover-V2-7B direct/negated proof attempts at pass@2. Original run-specific Lean version, mathlib commit, request settings and compiler logs were not recovered. The subsequently released repository pins leanprover/lean4:v4.9.0-rc1 in src/veriform/proving/lean_server/lean/lean-toolchain; this is repository metadata, not a verified original-run environment.

## Reported outcome

Appendix H.1 reports a valid theorem that assumes precisely the target equation and returns that assumption. Not independently checked.

## Original prompt status

partial

## Original prompt

PARTIAL DOCUMENTARY RECORD, not a captured original request. The published repository's FORMALIZE_USER template is:
User Input:
CONTEXT: {context}
STATEMENT: {informal_problem}
Lean 4 Output:
The complete generic few-shot instructions are in Appendix G and src/veriform/llm/prompts.py at the pinned commit. The original instantiated messages, whitespace/context serialization and per-request settings were not recovered. Do not treat a reconstruction from the template and CSV as the original request.

## Licensing

Paper: Cornish, Ghinassi, Yeh, Liu, Xu, Yin, Wagner, Li, Teh and Ong (2026), CC BY 4.0 (arXiv license link https://creativecommons.org/licenses/by/4.0/). Dataset/repository: MIT; copyright (c) 2024 The Authors, retained in LICENSE.source.txt. Minimal source excerpts only; no full paper retained. Exact excerpts are unmodified; collector descriptions and judgments are separately labeled.

## Notes

The text below is the exact lstlisting excerpt in sections/appendix/qualitative_examples.tex, verified against the primary arXiv v1 TeX source. It is a published theorem/proof excerpt, not a recovered raw autoformalizer response. Appendix F separates statement autoformalization from subsequent proving; do not attribute all proof-body tactics to the named autoformalizer. Ellipses, if present, are the paper's own omissions. The exact released target and empty dependency list are available. The selected public result lookup returned 'the dataset index is loading'; the raw original autoformalizer response was not recovered.

## Primary Artifacts

- https://arxiv.org/pdf/2608.10916v1
- https://arxiv.org/src/2608.10916v1
- https://github.com/Ighina/FaithformBench/blob/fd90fe330bf423f6046af24435d44cf03a227584/FaithformBench.csv
- https://github.com/Ighina/FaithformBench/blob/fd90fe330bf423f6046af24435d44cf03a227584/src/veriform/llm/prompts.py
- https://huggingface.co/datasets/ighina/Faithform-LLMs/tree/6eea0500fc04bb9c94603ed61a73526959569ef9
