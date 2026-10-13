# Archival Collection v1

Date: 2026-10-12. Phase: literature retrieval and provisional labeling only.

## Authorization and Boundary

The user requested parallel agents to retrieve, analyze, and label existing case studies. This protocol authorizes a bounded archival pass and evidence review. It does not authorize new proof-generation experiments, training, proof repairs, paid model calls, or claims of independent Lean verification.

## Assignments

| Paper ID | Primary paper | Collector ID allocation | Initial target |
| --- | --- | --- | --- |
| faithformbench | https://arxiv.org/pdf/2608.10916 | CASE/FIND 0001-0099 | 4-5 distinct Appendix H cases |
| proofflow | https://arxiv.org/pdf/2510.15981 | CASE/FIND 0101-0199 | 2-4 dependency/statement cases and clearly marked comparisons |
| lost-in-translation | https://arxiv.org/pdf/2610.08144 | CASE/FIND 0201-0299 | Examples 2.1, 2.2, 3.1, 3.3 |
| pistis | https://arxiv.org/pdf/2608.15432 | CASE/FIND 0301-0399 | 2-3 concrete source-gap/refutation or translation cases |

IDs use four digits, e.g. CASE-0101. Reuse of a source problem across variants requires the same proof-family ID. All cases are development-only and selected after outcomes are inspected: use `curated_reported` for paper examples and `curated_artifact` for our candidate diagnoses in released outputs. None is a held-out or output-blind sample. Targets are limits, not quotas.

## Procedure

Collectors follow `instructions/COLLECTOR.md` and write one bundle per paper. The coordinator validates schemas and provenance and imports approved packets with `scripts/import_cases.py`. A reviewer audits selected cases and possible overclaims. Freeze each source packet at import using a SHA-256 digest. Changes to an imported packet require a new variant and documented difference.

## Evaluation Boundary

The exact input, the published output, and the collector's interpretation are separate artifacts. Record the original prompt, model, and environment only when available; otherwise record unknown. Exact reproduction readiness is not assumed from a paper screenshot. Published claims remain reported unless independently validated in a later authorized phase.

Source defects, comparisons, and theoretical examples must not enter the model-failure count. No report may equate Lean compilation with fidelity or an LLM review with formal certification. Record content and argument fidelity separately.

## Deliverables and Stop

Produce import bundles, case packets, CSV registers, a browsable Markdown index, review notes, and a collection summary. Stop after this first bounded pass; do not automatically launch the study plan's proposed 18 experiments. Random sampling, reproduction protocols, and intervention tests remain future phases.
