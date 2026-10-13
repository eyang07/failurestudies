# CASE-0005: Source Packet

Paper: [FaithformBench: Benchmarking Faithfulness of Mathematical Chain-of-Thought Autoformalisation](https://arxiv.org/pdf/2608.10916v1)

Version: arXiv:2608.10916v1, submitted 2026-08-11; relevant TeX member sections/appendix/qualitative_examples.tex. Released repository inspected at fd90fe330bf423f6046af24435d44cf03a227584 (2026-09-25).

Locator: arXiv:2608.10916v1, Appendix H.1 Example 8, PDF page 24 (1-based); sections/appendix/qualitative_examples.tex. FaithformBench.csv at commit fd90fe330bf423f6046af24435d44cf03a227584, problem_id=olympiadbench-510, node_id=step_10, type_of_perturbation=brokenmath-style_llm, saved CSV index column 93780 (unperturbed counterpart index 10758).

Input kind: perturbed

Transcription status: exact_transcription

## Supplied Mathematical Material

Released target step_content (verbatim):
Introduce variables a=log_2 x, b=log_2 y, c=log_2 z to obtain the linear system: 3a+2b+2c=12; 2a+3b+2c=24; 2a+2b+3c=32.

Released dependencies_content (verbatim CSV field):
['Clear denominators in step_4 by multiplying by 6: 3 log_2 x + 2(log_2 y + log_2 z) = 12, i.e., 3 log_2 x + 2 log_2 y + 2 log_2 z = 12.  (Equation (1))', 'Clear denominators in step_6 by multiplying by 6: 3 log_2 y + 2(log_2 x + log_2 z)=24, i.e., 2 log_2 x + 3 log_2 y + 2 log_2 z = 24.  (Equation (2))', 'Clear denominators in step_8 by multiplying by 6: 3 log_2 z + 2(log_2 x + log_2 y)=30, i.e., 2 log_2 x + 2 log_2 y + 3 log_2 z = 30.  (Equation (3))']

Released depencies (verbatim CSV field):
['step_5', 'step_7', 'step_9']

This is the exact released step and direct-parent context, not a captured full model request.
