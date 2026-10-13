# Archival evidence review

Reviewer: `/root/review_archival_cases`

Date: 2026-10-12

Phase: archival-v1; documentary and elementary mathematical inspection only.

## Disposition

Accept the four bundles for a provisional archival register after the two content-scope corrections below. The coordinator applied both before first import, and this reviewer read back the changed fields. No remaining blocking factual correction was identified in the bounded audit. This is not independent Lean verification and does not promote any finding to `confirmed`.

All 15 packets were read. Focused review covered CASE-0101--0104, CASE-0201--0202, CASE-0003--0004, and CASE-0301--0302. CASE-0001, CASE-0002, CASE-0005, CASE-0203, and CASE-0204 received a metadata/overclaim check, not a full mathematical audit. No experiments, Lean execution, proof patches, new formalizations, or additional literature search were performed.

## Blocking issues resolved before import

1. **CASE-0201 / FIND-0201:** the original `content_fidelity=preserved` used only the theorem endpoint as its scope. The supplied proof also asserts root multiplicities and a factorization, which the displayed answer changes. Set `content_fidelity` to `violated`; retain `argument_fidelity=violated`, `labels=[SILENT_REPAIR]`, and `evidence_status=candidate`. Record separately that the polynomial, real domain, and final nonnegativity target are preserved. The coordinator made this change. An elementary check supports the mismatch: at zero the erroneous product is -1, whereas the polynomial is 1. This mathematical inspection does not check the Lean artifact.
2. **CASE-0202 / FIND-0202:** the original `content_fidelity=preserved` again meant only the final theorem. Set it to `uncertain` at supplied-input scope; retain the endpoint-preserved observation and the candidate `STRATEGY;DEPENDENCY` diagnosis. The coordinator made this change. The screenshot prompt and typeset source are not identical, and the packet is only partially transcribed. Do not infer a full-input preservation result from the shared final theorem. A change of argument need not by itself establish a content violation, so `uncertain` is appropriate here.

Primary locators for these corrections: [Example 2.1 and Figure 1](https://arxiv.org/html/2610.08144v1#S2), [Figure 1 asset](https://arxiv.org/html/2610.08144v1/cubic_squish.jpg), and [Figure 2 asset](https://arxiv.org/html/2610.08144v1/matrix_example_slim.jpg). This reviewer read the primary article's mathematical text. The assets resolved as image URLs, but their pixels were not independently inspected in this review; detailed screenshot transcription remains the collector's evidence.

## ProofFlow

Primary article locator: [Appendix A.5.1--A.5.3](https://arxiv.org/html/2510.15981v1#A5). Released-record locators are pinned in the bundle at commit `97f1b7be82380733fb0380973c164e40645ae9da`, under `benchmark_results/output_pickle/`.

| Case | Agreement and labels | Scope and required treatment |
| --- | --- | --- |
| CASE-0101 | Agree with empty labels and `disputed`. | The supplied thinking and non-thinking `dummy_6` l3 excerpts explicitly consume l2. This challenges only identification of those endpoints with the paper's illustrated bypass. Keep `comparison_nonfailure`; the local preservation flags must never be counted as whole-proof success. |
| CASE-0102 | Agree with candidate `ASSUMPTION;BINDING;INTERPRETATION` and content violation. | The displayed pairwise existential slope permits a different slope for every index pair. It loses the shared difference. Retain `candidate_failure`, not a paper-attributed diagnosis. |
| CASE-0103 | Agree with candidate `ASSUMPTION;CONCLUSION;DEPENDENCY` and both violations. | The displayed l3 declaration omits the needed probability relation and changes the intermediate target. Its countermodel concerns that complete declaration, not an unspecified assembled proof. Retain `candidate_failure`. |
| CASE-0104 | Agree with empty labels, `disputed`, and uncertain fidelity flags. | The excerpt explicitly uses l3 and rederives d=3, consistent with local inlining of l4. An unused lemma name does not establish a substantive argument replacement. Keep `comparison_nonfailure`. |

The CASE-0102 diagnosis has an inspectable mathematical basis independent of the recorded solver failure: for each n<m choose the real slope `(a(m)-a(n))/(m-n)`. Every real sequence satisfies the displayed condition. Set a(1)=5, a(3)=11, and a(5)=100. The first two values hold but the requested fifth value does not. This also explains why separately obtained slopes cannot simply be identified. The compiler error excerpt in the packet resolves the intended real subtraction/coercion in that condition.

The CASE-0103 countermodel is also sound: on a two-element space, assign the empty set value 0, the two singleton values 0.6 and 0.7, and the universe value 1. All four range/normalization conditions in the displayed declaration hold. The disjoint singletons have intersection value 0. Additivity is absent, so the requested lower bound does not follow. A measurable-space instance alone supplies no probability axioms.

No label change is needed for either candidate. Retain `first_observed_divergence=unknown` and `causal_hypothesis=unknown`: final node exports do not identify the first generation or repair stage that introduced a mismatch. The quoted paper claims and the selected exports have not been linked to identical runs. The review checked the packet's exact code text and primary paper prose, but independent raw-URL retrieval of the two candidate exports failed; it did not independently verify the export bytes or their stored blob hashes.

## FaithformBench

Primary locator: [Appendix H.1, Examples 6--7, PDF page 24](https://arxiv.org/pdf/2608.10916v1#page=24). Primary PDF extraction supports the published hypothesis/target comparison and the real-to-natural domain comparison. The released-row provenance was inspected through the collected bundle, not independently downloaded again.

- **CASE-0003:** retain `reported`, `ASSUMPTION;CONCLUSION`, and argument `not_assessable`. The displayed theorem proves an equation from the same equation. The diagnosis depends on treating the source as a claim about monetary change. The row's `general_knowledge`/`axiom` tags and missing original request leave an assignment/definition reading unresolved. The existing uncertainty note correctly records that limitation; do not upgrade this to an independently established model failure or treat the proof-body tactics as necessarily produced by the autoformalizer.
- **CASE-0004:** retain `disputed`, content `uncertain`, and `INTERPRETATION;ASSUMPTION`. Relative to the paper-described real input, the natural-number premise is impossible; that is a valid mathematical explanation. The related released multiplication row is not the same as the paper's exponentiation input. Keep both strings distinct and in one proof family, without claiming an exact input/output match. Before reproduction, identify the actual request or create explicit separately identified source variants; do not silently replace `*` with `^`.
- **CASE-0001, CASE-0002, CASE-0005:** no blocking overclaim found in the limited packet review. Their descriptions point to concrete target, premise, or witness-binding changes. Keep reported status, partial-output qualifications, and missing-run limitations. The CASE-0005 account appropriately narrows the issue to detached logarithmic bindings.

The five cases are intentionally perturbed, author-selected examples. They are not five independent prevalence observations, and the printed ellipses are not complete executable proof bodies.

## Pistis And Advanced Cases

Primary locator: [Pistis Figures 7--8 and Section 4.5, PDF page 7](https://arxiv.org/pdf/2608.15432v1#page=7). Primary text extraction supports the citation-gap and refutation descriptions.

Keep CASE-0301 and CASE-0302 as `source_defect`, empty mechanism labels, both fidelity fields `not_assessable`, and evidence `reported`. The first concerns a source citation; the second concerns a supplied AI-written intermediate assertion. Neither is an observed Pistis mistranslation. The published refutation sketch contains a challenged assertion with `sorry` and omits premises/proofs; it is not evidence of a completed independently checked theorem. No metadata change is required.

CASE-0203 and CASE-0204 remain archival-only reported allegations. Their packets distinguish visible declarations from unverified norm, hypothesis, time-quantifier, and dependency correspondences. Preserve those qualifications. In particular, CASE-0204 must not be summarized as a uniform weakening, and neither case establishes an error in the overarching PDE result. This reviewer did not adjudicate the advanced analysis.

## Register And Next-Step Constraints

The review leaves 15 provisional packets: two new candidate diagnoses, two provenance comparisons, two source-defect contrasts, and nine paper-selected failure records whose evidence remains reported, candidate, or disputed. These categories are descriptive collection counts, not a verified failure rate. CASE-0102 and CASE-0104 share a proof family.

Exact metadata changes recommended and already applied: CASE-0201 content `preserved -> violated`; CASE-0202 content `preserved -> uncertain`, with explicit theorem-endpoint scope notes. Preserve all other evidence-status distinctions. Add this review's path to the collection index/report rather than overwriting collector attribution.

The elementary ProofFlow candidate packets contain enough mathematical detail to motivate a later frozen protocol; the available metadata does not support exact original-run reproduction. LIT screenshot cases need exact visible input/output capture and an explicit preservation scope. CASE-0004 needs provenance resolution. Pistis and the advanced PDE cases need complete artifacts and specialist review. No further retrieval or experimental phase is authorized by this report.
