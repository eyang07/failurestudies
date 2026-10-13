# CASE-0201: Provisional Assessment

Evaluator-only material.

## Case kind

reported_failure

## Source validity

invalid

## Validity basis

The target statement is valid, but the supplied argument is invalid. Collector's elementary inspection: the claimed product (x-1)(x+1)^2 has value -1 at x=0, while p(0)=1. Thus the claimed factorization cannot equal p; x-1 also need not be nonnegative on x>=-1. The paper likewise classifies the argument as incorrect. This is an input-proof defect, not by itself a translation failure.

## Content fidelity

violated

## Argument fidelity

violated

## Evidence status

candidate

## Readiness

needs_artifacts

## Reported model

Paper caption: ChatGPT-6 (Astra Ultra); visible figure selector: GPT-6 Astra Ultra. Exact model snapshot/settings unknown.

## Reported environment

Figure 1 shows import Mathlib and a displayed work duration of 24 seconds. Lean/mathlib versions, tool access and compiler transcript unknown.

## Reported outcome

Authors report a compiling correct Lean proof despite the defective supplied argument. Compilation and axiom closure were not checked by this collector.

## Original prompt status

partial

## Original prompt

Exact instruction excerpt from Figure 1: "Write this up as a Lean proof which compiles". The remaining prompt is not transcribed: it supplies the polynomial, domain and erroneous multiplicities summarized in source_text, then requests code alone for a library. Complete visible prompt is accessible in cubic_squish.jpg. Prior conversation/system context unknown.

## Licensing

Paper and figure: arXiv non-exclusive distribution license; code-block-specific license unknown. Only limited excerpts and independently written descriptions retained; no image/PDF copied.

## Notes

This is a curated erroneous argument. No valid parent input or mutation history was retrieved, so original versus perturbed is unknown. The target formula/domain are preserved at the visible endpoint, whereas the source proof's mathematical assertions are repaired. A future protocol must freeze the actual screenshot prompt, not reconstruct it from the typeset example. Reviewer: collector /root/collect_lost_translation; no second review.

## Primary Artifacts

- https://arxiv.org/pdf/2610.08144v1#page=2
- https://arxiv.org/html/2610.08144v1
- https://arxiv.org/html/2610.08144v1/cubic_squish.jpg
- https://arxiv.org/abs/2610.08144v1
