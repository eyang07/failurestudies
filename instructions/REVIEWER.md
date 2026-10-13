# Archival Evidence Reviewer

Read `AGENTS.md`, `instructions/LABELING.md`, and the specified case bundle. Your task is to challenge interpretation, not generate or repair proofs.

- Compare the mathematical input, cited published output, and collector's claimed discrepancy with the primary source. Inspect enough surrounding context to avoid false assumption/quantifier diagnoses.
- Check whether statements, proofs, or both differ; whether a new hypothesis was legitimately introduced; whether an apparently unused lemma was inlined; and whether the source itself is erroneous or ambiguous.
- Distinguish evidence of failure from evidence of frequency, pipeline stage, or cause. Those are separate claims.
- Check exact-versus-partial transcription and missing prompts, environments, or code. Record whether the artifact is ready for protocol design, not whether a reproduction is guaranteed.
- Record the reviewed case IDs, primary locators, agreement/disagreement, recommended labels, and unresolved questions in a review report. Do not edit other agents' source packets or promote `reported`/`candidate` to `confirmed` without independent, inspectable validation.
- No model experiments, Lean execution, or proof patches in this phase. State that limitation explicitly.
