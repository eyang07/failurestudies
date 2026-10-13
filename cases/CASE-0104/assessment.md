# CASE-0104: Provisional Assessment

Evaluator-only material.

## Case kind

comparison_nonfailure

## Source validity

valid

## Validity basis

Same valid mathematical source as CASE-0102. This is a related output comparison in PF-dummy_9, not an independent mathematical problem or frequency sample.

## Content fidelity

uncertain

## Argument fidelity

uncertain

## Evidence status

disputed

## Readiness

needs_context

## Reported model

Paper Section 6.1: thinking ProofFlow uses Goedel-Formalizer-2 32B and Goedel-Prover-V2 32B. Released benchmark_think_noDAG.py names google/gemini-2.5-pro for graph construction, but current script settings do not establish exact metadata of this saved export.

## Reported environment

Paper Section 6.1 reports Lean v4.15.0 via LeanServer. Mathlib commit and environment identity for these HTML exports are unknown. Repository commit is 97f1b7be82380733fb0380973c164e40645ae9da. No local compilation or proof-completeness audit was performed.

## Reported outcome

Paper Figure 9 reports a final step using TC1, TC2 and L5 while bypassing L1-L4. The inspected thinking noDAG endpoint explicitly uses l3 to recover d=3, followed by l5 and tc_2. The released endpoint reports lean_pass=true, lean_verify=true; its automated score is 0 with a wrong-dependencies remark. No independent verification was performed.

## Original prompt status

unavailable

## Original prompt

unknown

## Licensing

Repository excerpts: MIT License, Copyright (c) 2024 ProofFlow Team; notice retained in MIT-LICENSE.txt. Paper: Rafael Cabral, Tuan Manh Do, Xuejun Yu, Wai Ming Tai, Zijin Feng, Xin Shen, arXiv:2510.15981v1, CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Paper summaries are collector paraphrases. Exact source fields and Lean snippets are copied from the pinned repository without corrections.

## Notes

Comparison is scoped to the claimed wholesale bypass of L1-L4. The visible code uses l3 and recomputes the short division step represented by l4. Unused l4 alone does not establish an argument violation under this study's allowance for justified local elaboration. Whole-proof content/completeness remains unaudited; tc_1 and def_1 use different forms of the sequence assumption. Do not count this comparison as a fully validated successful proof or as disproving the paper.

## Primary Artifacts

- https://arxiv.org/pdf/2510.15981v1
- https://github.com/Huawei-AI4Math/ProofFlow/blob/97f1b7be82380733fb0380973c164e40645ae9da/data/benchmark_0409.json
- https://raw.githubusercontent.com/Huawei-AI4Math/ProofFlow/97f1b7be82380733fb0380973c164e40645ae9da/benchmark_results/output_pickle/benckmark6%20-%20think%20noDAG/dummy_9.json.pickle.html
- https://github.com/Huawei-AI4Math/ProofFlow/blob/97f1b7be82380733fb0380973c164e40645ae9da/LICENSE
