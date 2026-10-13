# failurestudies

Diagnostic research on mathematical-content and argument faithfulness in Lean autoformalization.

## Start Here

1. Read [STUDY_PLAN.md](STUDY_PLAN.md) for the research plan.
2. Read [AGENTS.md](AGENTS.md) for experiment and data-integrity requirements.
3. Begin with archival case inspection. No experiments, model selection, or final protocol have been completed by this setup.

## Records

The four CSV files in `registry/` are empty registers, not experimental results. They can be imported as spreadsheet tabs. Keep version-controlled CSVs and artifact links authoritative; do not maintain conflicting spreadsheet copies.

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
