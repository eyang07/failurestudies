# Archival Case Collector

Read the repository's `AGENTS.md`, `STUDY_PLAN.md`, this file, and your assignment. This phase retrieves and interprets existing evidence only. Do not generate new formalizations, run Lean, patch proofs, call paid model APIs, or start experimental trials.

## Ownership

Write only your assigned `imports/<paper_id>/bundle.json` and optional supporting files below that directory. Do not edit shared registers, other collectors' files, or git history. The coordinator allocates IDs, validates submissions, and imports them. Use `apply_patch` for manual file edits. In restricted workspaces use the coordinator's staging directory.

## Retrieval

1. Read the primary paper's relevant examples and methods. Inspect linked primary repositories/datasets when useful. Pin actual versions, dataset IDs, sections, pages, and code commits when known.
2. Collect 2-5 distinct, informative examples initially. Do not invent failures to meet a quota. Include comparison nonfailures or source defects only when clearly classified as such.
3. Prefer the three target mechanisms: changed assumptions, weakened/trivialized conclusions, and bypassed reasoning. Other mechanisms remain eligible and multi-labeling is allowed.
4. Keep exact input, published output, and your interpretation separate. Never silently repair source typos, reconstruct missing prompts, or present a paraphrase as an exact input.
5. Source excerpts must be limited to what is necessary. Do not commit full copyrighted PDFs. Preserve code/data licensing and attribution; mark unknown licenses. Raw sources may be kept locally in ignored directories.
6. Inspect images when essential mathematical signs or prompts are only visible there. If you cannot verify the transcription, mark it partial and record the ambiguity.

## Required Bundle

Create valid UTF-8 JSON with these top-level keys:

```json
{
  "paper_id": "assigned-slug",
  "paper_title": "Exact paper title",
  "paper_url": "Primary source URL",
  "paper_version": "actual version or unknown",
  "collector": "agent identifier",
  "retrieved_at": "YYYY-MM-DD",
  "coverage_notes": "Sections inspected and selection rationale",
  "limitations": ["Missing artifacts, licensing, or other limitations"],
  "cases": []
}
```

Every case must contain these fields (use strings unless shown otherwise):

- `case_id`, `proof_family_id`, `source_locator`, `topic`.
- `case_kind`: `reported_failure`, `candidate_failure`, `source_defect`, `comparison_nonfailure`, or `theoretical_example`. Use `candidate_failure` when our inspection of released artifacts suggests a failure not specifically reported by the paper.
- `task_type`: `statement_translation`, `proof_translation`, or `source_proof_checking`.
- `input_kind`: `original`, `perturbed`, or `unknown`.
- `source_validity`: `valid`, `invalid`, `ambiguous`, or `unknown`; explain in `source_validity_basis` whether this concerns the statement, proof, or both and who checked it.
- `source_text_status`: `exact_transcription`, `partial_transcription`, `paraphrase`, or `unavailable`; `source_text`: minimal mathematical input, with any transcribed context clearly identified.
- `published_output_status`: `full`, `excerpt`, `description_only`, or `unavailable`; `published_output`: exact excerpt or explicitly labeled description, never your replacement proof.
- `artifact_urls`: array of primary artifact URLs; `license_notes`.
- `original_prompt_status`: `exact`, `partial`, or `unavailable`; `original_prompt`: text or `unknown`.
- `reported_model`, `reported_environment`, `reported_outcome`: attributed published information or `unknown`; these are NOT results of our experiments.
- `reproduction_readiness`: `ready_for_protocol`, `needs_artifacts`, `needs_context`, or `archival_only`; `notes`.
- `finding`: an object with `finding_id`, `labels` (array), `content_fidelity`, `argument_fidelity`, `evidence_status`, `observed_mismatch`, `consequence`, `source_span`, `lean_location`, `first_observed_divergence`, `evidence`, `uncertainties` (array), and `causal_hypothesis`.

Allowed labels: ASSUMPTION, CONCLUSION, BINDING, INTERPRETATION, DEPENDENCY, STRATEGY, SILENT_REPAIR. Labels may be empty for source defects/nonfailures; do not label a source error as a translation error.

Both fidelity judgments use `preserved`, `violated`, `uncertain`, or `not_assessable`. They are provisional judgments interpreted together with evidence status, not new compiled results. Collectors use only `reported`, `candidate`, or `disputed`, NEVER `confirmed`. No lifecycle logs means `first_observed_divergence` is `unknown`; identify visible endpoint mismatches in the evidence instead. Causal attribution is `unknown` unless a controlled comparison supports it.

## Handoff

Validate JSON, count cases by kind, list exact versus incomplete inputs, and summarize missing artifacts. Cite sources in each case. Stop after the first bounded collection; do not exhaustively crawl or download whole repositories. Explicitly state that no reproduction or independent Lean verification was performed.
