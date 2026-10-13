# Experiment Agent Instructions

## Mission and Scope
- Read `STUDY_PLAN.md` and the assigned protocol before work. Diagnose failures before proposing a general solution. Do not train models or build a new proof language/framework.
- Execute only the assigned phase and cases. Setup or literature inspection does not authorize bulk model runs, paid experiments, interventions, or autonomous subagent spawning.
- For explicitly authorized archival collection, follow `protocols/archival-v1/PROTOCOL.md` and the assigned role in `instructions/`. The reusable launch prompt is `prompts/COLLECT_CASE_STUDIES.md`. Parallel collectors own separate import bundles; only the coordinator updates shared registers.
- Before generation, require a frozen protocol specifying source IDs/hashes, condition prompts, model/settings, environment, sampling, budgets, repair policy, and evaluation rubric. Report missing prerequisites; do not invent the original model or prompt.

## Source and Baseline Integrity
- Preserve source wording and mathematical content. Store the exact input separately from analysis. Never add explanations, fix typos, supply missing lemmas, or expand a baseline proof silently.
- Every source alteration gets a new variant ID, parent case ID, and explicit diff. Record source validity as valid, invalid, ambiguous, or unknown, with evidence.
- Distinguish published reported results, independently checked artifacts, original-protocol reproductions, and current-model baseline runs. Missing original settings make a run an approximation, not an exact replication.
- Define preservation requirements before viewing new outputs. Accept equivalent notation, harmless representation changes, and justified local elaboration; do not demand literal tactic matching.

## Run Discipline
- Use an isolated fresh generation context. Generators receive only the frozen protocol's allowed materials, never evaluator notes, published outputs, reference implementations, prior attempts, or other conditions' results. The supplied informal proof is intended input, not a hidden reference.
- Do not use a full-history agent fork for an independent trial. Prevent generator access to evaluator/other-run folders through actual tool or workspace isolation; if isolation is unavailable, disclose it before running.
- Record exact prompts, attachments, exposed model/version and settings, tool access, Lean version, mathlib commit, budgets, and timestamps. Mark unavailable metadata as unknown.
- A repair round is a feedback batch on the previous candidate followed by a revised candidate. Initial generation is attempt 0. Preserve all candidates, compiler invocations/output, actual usage, and retries; no unlogged searches or resets.
- Follow the frozen repair policy, provisionally at most three feedback rounds. Do not add evaluator hints to compiler feedback. Record any statement changes, rather than silently undoing or overlooking them.
- Stop at the budget. Keep failed, timed-out, interrupted, and nonreproducing runs. Never substitute a new run for an inconvenient outcome.
- A successful compilation is not proof completeness or faithfulness. Check the target's dependency closure for `sorryAx` and unauthorized axioms; record trusted assumptions and distinguish scaffolds from complete proofs.

## Analysis and Labels
- Evaluate content fidelity and argument fidelity independently: preserved, violated, uncertain, or not_assessable. Track compiler status, completeness, and source validity separately.
- Findings may have multiple labels: ASSUMPTION, CONCLUSION, BINDING, INTERPRETATION, DEPENDENCY, STRATEGY, SILENT_REPAIR. Explain labels using exact source spans and Lean declarations/lines.
- Each finding needs the observed mismatch, its mathematical/argument consequence, evidence, evidence status, reviewer, and earliest observable divergence. Use unknown when intermediates were not captured.
- Added hypotheses, unused lemma names, or different tactics alone do not prove unfaithfulness. Check provenance, scope, actual dependency use/inlining, and the predeclared acceptable transformations.
- LLM judgments are candidate diagnoses, not ground truth. Confirm key findings with inspectable reasoning, formal evidence where feasible, and review. Never infer falsity from proof-search failure.
- Keep observations separate from causal hypotheses. Controlled, matched comparisons are needed before attributing failures to a prompt, proof structure, or compiler repair.

## Records and Reporting
- Use stable IDs: CASE-0001, RUN-0001, FIND-0001, INT-0001; coordinators allocate nonoverlapping IDs for concurrent work. Never overwrite another run's artifacts.
- Update the four CSV registers using a CSV parser/writer. Store long text and logs in linked files; use repository-relative artifact paths and semicolon-separated IDs/labels within fields.
- Keep proof families and related variants in the same development/holdout split. Never tune on held-out outputs. Separate curated failure cases from output-blind samples and ordinary inputs from corruptions.
- Report explicit denominators, unknowns, exclusions, and protocol deviations. Do not pool heterogeneous tasks or count repeated attempts as independent problems. Multi-label counts need not sum to 100%.
- A manual output fix is diagnostic only. An intervention must be versioned, compared at matched budgets, and assessed for regressions and noncompletion. Include an explicit natural-language baseline before claiming benefits from structured machinery.
- Finish each assignment with artifacts produced, confirmed versus tentative findings, counts, limitations, and the next justified action. Do not claim a novel mechanism or measured improvement without evidence.
- Do not commit credentials, private unrelated data, full copyrighted source PDFs, or restricted source material. Preserve local raw files as needed; record provenance and hashes in the registry. Review generated logs before committing.
