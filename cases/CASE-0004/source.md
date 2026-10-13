# CASE-0004: Source Packet

Paper: [FaithformBench: Benchmarking Faithfulness of Mathematical Chain-of-Thought Autoformalisation](https://arxiv.org/pdf/2608.10916v1)

Version: arXiv:2608.10916v1, submitted 2026-08-11; relevant TeX member sections/appendix/qualitative_examples.tex. Released repository inspected at fd90fe330bf423f6046af24435d44cf03a227584 (2026-09-25).

Locator: arXiv:2608.10916v1, Figure 1 and Appendix H.1 Example 7, PDF pages 1 and 24 (1-based); sections/appendix/qualitative_examples.tex. Related released record: FaithformBench-Regex.csv at commit fd90fe330bf423f6046af24435d44cf03a227584, problem_id=omnimath-629, node_id=step_8, type_of_perturbation=regex_perturbed, saved CSV index column 4647. Exact input-to-output linkage is unresolved because the expressions differ.

Input kind: perturbed

Transcription status: partial_transcription

## Supplied Mathematical Material

Published appendix mathematical input (exact formula transcription only; surrounding prose not represented as a verbatim prompt):
x ∈ ℝ; 3^x = 5; 3^(x+2) = 51.
The complete original request is unavailable.

Related released regex target step_content (verbatim, a distinct provenance variant):
Therefore, 3*(x+2) = 51.

Related released dependencies_content (verbatim CSV field):
['3^(x+2) = 3^x · 3^2.', 'Since 3^x = 5, substitute into 3^x · 3^2 to get 3^x · 3^2 = 5 · 3^2.', 'Compute 3^2 = 9.', '5 · 3^2 = 5 · 9.', 'Compute 5 · 9 = 45.']

Related released depencies (verbatim CSV field):
['step_3', 'step_4', 'step_5', 'step_6', 'step_7']

Do not replace '*' by '^' in the released row or claim this row is the exact input underlying the appendix output.
