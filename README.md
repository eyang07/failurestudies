# failurestudies

Diagnostic research on mathematical-content and argument faithfulness in Lean autoformalization.

## Start Here

1. Read [STUDY_PLAN.md](STUDY_PLAN.md) for the research plan.
2. Read [AGENTS.md](AGENTS.md) for experiment and data-integrity requirements.
3. For archival collection, use [the reusable launch prompt](prompts/COLLECT_CASE_STUDIES.md) and [archival-v1](protocols/archival-v1/PROTOCOL.md).
4. Browse [the case index](reports/CASE_INDEX.md) and [collection report](reports/COLLECTION_REPORT.md) after import. No new model experiments or independent Lean verification are part of archival collection.

## Records

The four CSV files in `registry/` can be imported as spreadsheet tabs. Archival cases and provisional findings are not new experimental results. Run and intervention registers remain empty until real experiments occur. Keep version-controlled CSVs and artifact links authoritative; do not maintain conflicting spreadsheet copies.

- `cases.csv`: one row per source case or explicitly identified source variant.
- `runs.csv`: one row per archived or newly generated run; record its provenance.
- `findings.csv`: one row per observed mismatch, linked to the case and run when available.
- `interventions.csv`: one row per proposed/tested intervention version.

Use a CSV parser/writer, quote commas/newlines correctly, and use semicolons for multiple labels or IDs. Leave inapplicable identifiers empty; use `unknown` for applicable but unavailable information. Fidelity values are `preserved`, `violated`, `uncertain`, and `not_assessable`. Evidence status is `reported`, `candidate`, `confirmed`, or `disputed`; explain the review basis rather than inventing a confidence score.

## Artifact Layout

Create directories as work requires them:

```text
protocols/<protocol-id>/          Frozen settings, prompts, sampling, and budgets
cases/<case-id>/source.md         Exact source transcription and provenance
cases/<case-id>/source_files/     Local raw attachments (not committed)
cases/<case-id>/assessment.md     Evaluator-only rubric, validity, and notes
runs/<run-id>/                   Inputs, metadata, transcript, candidates, logs
findings/<finding-id>.md          Evidence and adjudication
interventions/<intervention-id>/  Hypothesis, change, comparisons, results
reports/                         Aggregate analyses and decision memos
```

Preserve attempt 0 and every repair as distinct files. Hash each frozen source packet and prompt. Link findings to precise source spans, declaration names, and artifact versions. Evaluation material and other runs must not be exposed to generation agents merely because they share this repository.

There is deliberately no Lean project or model API integration yet. Pin those environments in individual protocols when actual cases and authorized budgets are selected.

## Parallel Collection

- [Collector](instructions/COLLECTOR.md): retrieves primary evidence into a paper-owned JSON bundle.
- [Coordinator](instructions/COORDINATOR.md): assigns IDs, validates, reviews, and imports submissions.
- [Reviewer](instructions/REVIEWER.md): challenges labels and evidence without altering source material.
- [Labeling rules](instructions/LABELING.md): shared mechanism definitions and uncertainty handling.

Bundles live at `imports/<paper-id>/bundle.json`. From the repository root:

```sh
python3 scripts/import_cases.py --check
python3 scripts/import_cases.py --write
python3 -m unittest discover -s tests -v
```

The importer validates required fields, labels, ID ownership, and immutable packet consistency before writing. It generates case packets, findings, the case index, and CSV rows; it does not call models or Lean. Existing different rows/packets are rejected rather than silently overwritten. Before changing an imported source, allocate a new variant; conduct later adjudication in separate review records.

Published output excerpts retain their original whitespace and are exempt from code-style whitespace checks. CSV `reviewer=pending` means case-level adjudication remains open; the bounded documentary batch review is recorded separately in `reports/ARCHIVAL_REVIEW.md` and is not formal confirmation.
