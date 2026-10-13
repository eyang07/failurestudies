# Autoformalization Failure Diagnostic Study

Status: protocol draft; no experiments have been run in this repository.
Recorded: 2026-10-12.

This is the study plan agreed in the discussion. Read `AGENTS.md` for operational instructions. Initial sample sizes and repair limits below are provisional: freeze them in a versioned protocol before executing experiments.

## Study Goal

Identify **which faithfulness failures recur, where they first appear, and what conditions trigger them**, before designing a remedy.

Keep two outcomes separate:
- **Mathematical-content fidelity:** preservation of definitions, assumptions, quantifiers, and conclusions.
- **Argument fidelity:** preservation of the supplied proof's essential reasoning and dependencies.

The workflow should be **inspect -> reproduce -> isolate causes -> test a targeted intervention**. Manually fixing one output helps diagnosis but is not evidence that a method improves autoformalization.

## 1. Assemble Cases

Start with approximately **20 existing examples**, rather than immediately generating many new proofs:

- **10 reported failures**, drawn from FaithformBench, ProofFlow, and the new paper. These reveal mechanisms, not prevalence.
- **10 cases selected without inspecting outputs**, sampled reproducibly from available benchmarks. Include successes and failures; use these only for preliminary frequency estimates.
- Reserve additional, unseen **proof families** for later intervention testing. Variants of the same problem must stay together.

The new paper contributes particularly relevant candidates: Example 2.1 reports correction of an erroneous argument; Example 2.2 reports replacing a spectral proof with an entrywise argument. Its advanced examples can initially remain archival cases rather than reproduction targets. Treat all reported failures as claims to inspect independently. [Navier-Stokes lost in translation, Sections 2-3](https://arxiv.org/pdf/2610.08144).

Keep valid proofs, intentionally corrupted proofs, and ambiguous sources in separate groups. Also distinguish isolated statement translation from whole-proof formalization.

## 2. Create Registry

Use **one spreadsheet with four linked tabs**, plus folders containing the actual artifacts. This is enough infrastructure initially. The repository starts with four corresponding CSV files under `registry/`; keep these as the version-controlled source of truth if a spreadsheet view is used.

| Tab | Required information |
| --- | --- |
| Cases | Case ID; source/version/page or dataset ID; exact statement and proof; mathematical topic; task type; source validity; original/perturbed status; proof-family ID; selection method. |
| Runs | Run ID and Case ID; exact prompts and attachments; model/version/settings; Lean/mathlib versions; available tools; budgets; every generated revision; compiler feedback; final outcome. |
| Findings | Finding ID and Run ID; source passage; corresponding Lean declaration/lines; failure labels; first observed divergence; explanation; evidence; confidence; reviewer. |
| Interventions | Hypothesis; development and held-out cases; exact change; matched baseline; results; regressions; remaining uncertainties. |

Each case gets an immutable source packet. **No explanatory additions, typo corrections, or expanded arguments enter the baseline silently.** Any modification becomes a separately identified variant with a recorded difference.

## 3. Define Labels

Use multiple labels where appropriate, rather than forcing every failure into one category.

| Label | Meaning |
| --- | --- |
| `ASSUMPTION` | Unsupported premise added, required condition omitted, or assumption used outside its legitimate scope. |
| `CONCLUSION` | Target weakened, replaced, partially omitted, or made trivial. |
| `BINDING` | Quantifier order, witness dependence, variable identity, or scope changed. |
| `INTERPRETATION` | Type, definition, operation, domain, or mathematical object changed. |
| `DEPENDENCY` | An essential intermediate result is bypassed or an unjustified dependency introduced. |
| `STRATEGY` | A substantively different argument replaces the supplied argument. |
| `SILENT_REPAIR` | A source error is corrected without faithfully exposing or reporting it. |

Separately record **compilation/proof completion**, **source defects**, and **uncertainty**. They are not interchangeable with translation errors.

Before our own runs, specify the essential preservation requirements and acceptable implementation differences. A new local assumption may be legitimate; an unused named lemma may have been inlined. Neither alone establishes unfaithfulness.

For each fidelity dimension, use `preserved / violated / uncertain / not assessable`, with evidence rather than a numerical impression.

## 4. Reproduce Failures

Select **six informative cases** spanning several mechanisms and proof families, with three independent attempts each: **18 initial runs**.

- Distinguish **original-protocol reproduction** from **testing our current baseline**. If the original prompt or model is unavailable, document the deviation.
- Use fresh contexts. Hide published outputs, evaluator requirements, and reference solutions from generating agents.
- Freeze model settings, tool access, resource limits, and source packets across matched conditions.
- Permit a fixed compiler-repair allowance, provisionally three feedback rounds, while retaining the first attempt and every revision.
- Record timeouts and exhausted budgets; never replace failed runs selectively.

For invalid inputs, faithful behavior may mean exposing an unprovable or false step. **A completed proof is not automatically the desired outcome.**

## 5. Locate Causes

For each reproduced failure, trace the earliest **observable** divergence:

**source -> decomposition/restatement, if present -> Lean statement -> proof body -> compiler repair**

Do not require a decomposition stage in a baseline that does not naturally have one.

Keep **observations** separate from **causal hypotheses**. "The assumption first appeared after compiler feedback" is an observation; "compiler feedback caused assumption invention" requires a controlled comparison.

Test one suspected factor at a time:
- **Prompt sensitivity:** identical source and resources, different instruction wording.
- **Proof sensitivity:** the same theorem with two independently checked arguments, testing whether outputs follow the supplied argument.
- **Repair sensitivity:** compare saved stages, then conduct a matched repair-policy experiment if warranted.
- **Context sensitivity:** vary supplied references or context explicitly, without changing the baseline retrospectively.

## 6. Validate Judgments

Use agents to locate candidate mismatches and draft evidence summaries. Require each confirmed finding to identify **what changed and why it matters**.

Use counterexamples, checked implications, declaration inspection, or proof-dependency inspection where applicable. Audit all findings that drive the project decision and a sample of apparent successes. Disagreements remain uncertain until resolved; an LLM judge is not ground truth.

## 7. Test And Decide

Only after identifying a recurring mechanism should we test a fix.

Develop it on the diagnostic cases, then freeze it and compare against the unchanged baseline on held-out proof families. Include a plain-language instruction baseline before introducing structured contracts or other infrastructure.

Report:
- Confirmed failures by mechanism, task, source validity, and model.
- Recurrence across attempts, without treating repeated runs as independent problems.
- First-divergence locations and supported versus unresolved causes.
- Compilation, content fidelity, and argument fidelity separately, including unknowns.
- Whether interventions prevent failures, merely detect them, or trade them for noncompletion.

**Initial deliverable:** a case registry, an evidence-backed failure taxonomy, and a short decision memo identifying either a reproducible target worth addressing or evidence that we should change direction. That is the immediate research milestone, not a new autoformalization framework.

## Literature Entry Points

- [FaithformBench](https://arxiv.org/pdf/2608.10916): [code](https://github.com/Ighina/FaithformBench).
- [ProofFlow](https://arxiv.org/pdf/2510.15981): [code](https://github.com/Huawei-AI4Math/ProofFlow).
- [Pistis](https://arxiv.org/pdf/2608.15432): methodological context and source-gap analysis; do not confuse source gaps with model translation errors.
- [Navier-Stokes lost in translation](https://arxiv.org/pdf/2610.08144): reported examples to inspect, not population-level frequency evidence.

Pin the actual paper, data, and code versions used for each case. A literature claim is not independently verified merely because it appears in this list.
