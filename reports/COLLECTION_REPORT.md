# First Archival Collection

Date: 2026-10-12. Protocol: [archival-v1](../protocols/archival-v1/PROTOCOL.md).

## Scope and Counts

Four collector agents retrieved a bounded, outcome-aware selection of primary-source cases. A separate reviewer audited representative claims, provenance issues, and fidelity-label scope. The coordinator validated all bundles and applied the documented pre-import metadata corrections below.

| Paper | Cases | Scope |
| --- | ---: | --- |
| FaithformBench | 5 | Published perturbed-step failures; all statement-translation tasks |
| ProofFlow | 4 | Two candidate diagnoses in released outputs; two local comparison cases |
| Navier-Stokes lost in translation | 4 | Two elementary proof cases; two advanced archival comparisons |
| Pistis | 2 | Source citation/refutation defects, not formalizer-induced failures |
| Total | 15 | 14 distinct source families |

Case kinds: 9 reported failures, 2 candidate failures, 2 comparison nonfailures, and 2 source defects. Evidence status: 8 reported, 4 candidate, 3 disputed, and **0 confirmed**. These are different classification axes; their counts must not be interchanged.

Eight inputs have exact released transcriptions; seven are partial. Readiness: 8 need artifacts, 5 need context, and 2 are archival-only. No complete original request/response/lifecycle package has been independently verified. Some exact input packets can support a newly specified current-model baseline, but that would not be an exact reproduction of the published run.

**No model-generation experiments, compiler repairs, Lean compilation, independent proof verification, or interventions were executed.** Run and intervention registers intentionally remain empty. This curated first batch is not the study's future output-blind sample and cannot establish failure rates.

## Where to Start

Browse the [case index](CASE_INDEX.md), then each case's `source.md`, `published_output.md`, and `assessment.md`. The JSON bundles in `imports/` preserve the collected metadata; `findings/` contains individual evidence records. Assessment material must remain hidden from any later generation agent.

- [CASE-0102](../cases/CASE-0102/assessment.md): candidate common-difference quantifier drift in a released arithmetic-sequence formalization. A single difference becomes a separately chosen slope for each index pair. The packet includes a mathematical counterexample argument, not a new Lean proof.
- [CASE-0103](../cases/CASE-0103/assessment.md): candidate omission of inclusion-exclusion and replacement of an intermediate probability target. The displayed declaration is insufficient; publisher-recorded proof failure is not the basis of the diagnosis.
- [CASE-0003](../cases/CASE-0003/assessment.md): reported assumed-conclusion example. The released step's axiom/general-knowledge role and missing original messages require interpretive care.
- [CASE-0202](../cases/CASE-0202/assessment.md): candidate spectral-to-entrywise strategy substitution. Preserve the distinction between the actual screenshot prompt and the typeset proof before choosing a future input.

These are priorities for further inspection, not chosen intervention targets or findings of prevalence. Do not conclude that prompts, decomposition, or compiler feedback caused any mismatch from endpoint artifacts alone.

## Provenance Findings

1. ProofFlow's selected released noDAG endpoints do not match the specific dependency-bypass patterns illustrated in the paper. CASE-0101 and CASE-0104 record the actual code and the unresolved figure-to-run linkage. They are not evidence that the paper is false or that a complete proof is faithful.
2. FaithformBench CASE-0004 has an unresolved exponent-versus-multiplication difference between the appendix-described input and a related released regex row. Both are retained; neither is silently substituted for the other.
3. The matrix screenshot prompt in CASE-0202 omits an off-diagonal qualification present in the typeset argument. Its interpretation is therefore explicitly uncertain.
4. The advanced PDE examples pin cited Lean declarations and environment metadata, but those snapshots do not identify the original generator or prove the critique's full mathematical comparison. They remain archival-only and reported.
5. Pistis's two collected examples concern defects in the input argument. Counting them as mistranslations would confound source checking with translation fidelity.

## Review Decisions

See [ARCHIVAL_REVIEW.md](ARCHIVAL_REVIEW.md) for the independent archival review. No source input was corrected or expanded during review.

- CASE-0102 and CASE-0103 were reclassified from `reported_failure` to `candidate_failure`: they are our diagnoses in released artifacts rather than failure claims explicitly made in the paper.
- FIND-0201 content fidelity changed from `preserved` to `violated`: preservation of the final theorem does not preserve the source's altered intermediate polynomial assertions.
- FIND-0202 content fidelity changed from `preserved` to `uncertain`: the target appears preserved, but the full-input comparison is affected by the screenshot/typeset discrepancy.
- No evidence status was promoted to `confirmed`. Review is documentary/mathematical inspection, not independent Lean verification.

## Remaining Work

Recover exact original requests and matching complete outputs where feasible. Select a small reproduction set with an approved rubric and frozen model/tool/budget protocol; explicitly decide whether to reproduce original conditions or test a new current-model baseline. Obtain output-blind cases separately before making any frequency claim. Only then test a mechanism-specific intervention.

The infrastructure is ready for more bounded collectors using the [reusable prompt](../prompts/COLLECT_CASE_STUDIES.md). Allocate fresh IDs, preserve existing sources, and keep later experiment results separate from these archival reports.
