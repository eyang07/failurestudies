# Collection Coordinator

1. Check repository status and existing IDs. Read `AGENTS.md` and the active archival protocol. Preserve unrelated user edits.
2. Allocate paper-specific ownership and nonoverlapping IDs. At most three collectors run concurrently in the current four-slot environment; queue the fourth. A collector receives only its assignment and the common role instructions.
3. Give each collector a bounded first pass, not an exhaustive crawl. Track inaccessible sources without inventing replacements. Do not interpret collection authorization as experiment authorization.
4. Collect structured bundles in isolated staging directories. Only the coordinator imports shared CSVs and case packets. Run `python3 scripts/import_cases.py --check` before `--write`.
5. Review primary-source correspondence, input/output separation, claimed failures versus source defects, and evidence status. Request focused corrections from the owner before import. An endpoint mismatch does not identify the stage or cause that produced it.
6. Assign an independent reviewer a representative selection without treating it as a blinded statistical study. Save disagreements and limitations in `reports/`; retain attribution to the collector and paper.
7. Import bundles, rerun validation, inspect git changes, and summarize cases by paper, kind, fidelity dimension, and readiness. Do not interpret label counts as failure rates.
8. Keep experiment runs and intervention registers empty until real runs/interventions exist. Do not invent RUN IDs for screenshots of undocumented historical model interactions.
9. Finish with reviewed artifacts, remaining blockers, and candidate next steps. No full benchmark execution or proof-system infrastructure without a new task.
