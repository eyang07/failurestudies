# CASE-0001: Provisional Assessment

Evaluator-only material.

## Case kind

reported_failure

## Source validity

invalid

## Validity basis

The authors classify this perturbed step as invalid. The recovered dependency says d = 13 while the target says the same segment has length 12. The collector inspected this numerical disagreement, without checking the whole original problem or executing Lean. This concerns the target statement relative to its supplied dependency, not a complete informal proof.

## Content fidelity

violated

## Argument fidelity

not_assessable

## Evidence status

reported

## Readiness

needs_artifacts

## Reported model

GPT-5.2, as attributed in Appendix H.1 Example 2; exact model snapshot and request parameters unknown.

## Reported environment

Published protocol (Appendix F): Lean 4 theorem extraction and type-checking with by sorry, followed by DeepSeek-Prover-V2-7B direct/negated proof attempts at pass@2. Original run-specific Lean version, mathlib commit, request settings and compiler logs were not recovered. The subsequently released repository pins leanprover/lean4:v4.9.0-rc1 in src/veriform/proving/lean_server/lean/lean-toolchain; this is repository metadata, not a verified original-run environment.

## Reported outcome

Appendix H.1 reports a valid Lean theorem that abandons the input's distance content and proves numeral reflexivity. This is an author-reported successful proof of an unfaithful translation, not an independently checked result.

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

The text below is the exact lstlisting excerpt in sections/appendix/qualitative_examples.tex, verified against the primary arXiv v1 TeX source. It is a published theorem/proof excerpt, not a recovered raw autoformalizer response. Appendix F separates statement autoformalization from subsequent proving; do not attribute all proof-body tactics to the named autoformalizer. Ellipses, if present, are the paper's own omissions. The exact input/dependency fields are available. The selected result lookup on the public Faithform-LLMs viewer returned 'the dataset index is loading'; no matching raw output was obtained. A future protocol can use the exact input packet, but original-protocol reproduction needs the original messages, model settings and complete artifacts.

## Primary Artifacts

- https://arxiv.org/pdf/2608.10916v1
- https://arxiv.org/src/2608.10916v1
- https://github.com/Ighina/FaithformBench/blob/fd90fe330bf423f6046af24435d44cf03a227584/FaithformBench.csv
- https://github.com/Ighina/FaithformBench/blob/fd90fe330bf423f6046af24435d44cf03a227584/src/veriform/llm/prompts.py
- https://huggingface.co/datasets/ighina/Faithform-LLMs/tree/6eea0500fc04bb9c94603ed61a73526959569ef9
