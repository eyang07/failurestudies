# CASE-0101: Provisional Assessment

Evaluator-only material.

## Case kind

comparison_nonfailure

## Source validity

valid

## Validity basis

Statement and informal proof are mathematically valid under standard integer arithmetic; collector inspected the odd-number substitution, expansion, parity of consecutive factors, and divisibility conclusion. This is mathematical inspection, not independent Lean verification.

## Content fidelity

preserved

## Argument fidelity

preserved

## Evidence status

disputed

## Readiness

needs_context

## Reported model

Paper Section 6.1: thinking ProofFlow uses Goedel-Formalizer-2 32B and Goedel-Prover-V2 32B; non-thinking uses an anonymized fast-response formalizer and DeepSeek-Prover-V2 671B. Model attribution of the illustrated Figure 7 run is not explicit; the two exports are selected by their released folder names.

## Reported environment

Paper Section 6.1 reports Lean v4.15.0 via LeanServer. Mathlib commit and environment identity for these HTML exports are unknown. Repository commit is 97f1b7be82380733fb0380973c164e40645ae9da. No local compilation or proof-completeness audit was performed.

## Reported outcome

Paper reports noDAG reuses L1 to prove L3 and makes L2 redundant. Both inspected released noDAG l3 records instead explicitly consume l2 and record lean_pass=true and lean_verify=true. These are publisher-recorded statuses; the paper illustration and released files have not been established as the identical run.

## Original prompt status

unavailable

## Original prompt

unknown

## Licensing

Repository excerpts: MIT License, Copyright (c) 2024 ProofFlow Team; notice retained in MIT-LICENSE.txt. Paper: Rafael Cabral, Tuan Manh Do, Xuejun Yu, Wai Ming Tai, Zijin Feng, Xin Shen, arXiv:2510.15981v1, CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Paper summaries are collector paraphrases. Exact source fields and Lean snippets are copied from the pinned repository without corrections.

## Notes

Local comparison only: the expansion-to-factorization transition visibly retains l2 in both inspected exports. Do not count as a whole-proof success, or as disproving the paper. Source graph node numbering differs between dataset, generated graphs, and paper figure; identify the transition by its mathematical text. Output versions and exact original messages are needed to resolve the reported bypass. Source packet: source-records.json; selected complete node records: selected-output-records.json.

## Primary Artifacts

- https://arxiv.org/pdf/2510.15981v1
- https://github.com/Huawei-AI4Math/ProofFlow/blob/97f1b7be82380733fb0380973c164e40645ae9da/data/benchmark_0409.json
- https://raw.githubusercontent.com/Huawei-AI4Math/ProofFlow/97f1b7be82380733fb0380973c164e40645ae9da/benchmark_results/output_pickle/benckmark6%20-%20think%20noDAG/dummy_6.json.pickle.html
- https://raw.githubusercontent.com/Huawei-AI4Math/ProofFlow/97f1b7be82380733fb0380973c164e40645ae9da/benchmark_results/output_pickle/benckmark5%20-%20no%20think%20noDAG/dummy_6.json.pickle.html
- https://github.com/Huawei-AI4Math/ProofFlow/blob/97f1b7be82380733fb0380973c164e40645ae9da/LICENSE
