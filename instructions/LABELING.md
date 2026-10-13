# Labeling Rules

## Independent Dimensions

Content fidelity concerns objects, definitions, assumptions, bindings, and conclusions. Argument fidelity concerns the supplied reasoning and required dependencies. Judge each as `preserved`, `violated`, `uncertain`, or `not_assessable`, conditional on the actual evidence available. A valid conclusion does not establish argument fidelity.

## Mechanisms

| Label | Positive evidence | Avoid this false positive |
| --- | --- | --- |
| ASSUMPTION | Unsupported premise, lost condition, or invalid scope transfer | Legitimate case assumption, derived premise, or equivalent bundled hypothesis |
| CONCLUSION | Altered, omitted, weakened, or trivialized target | Equivalent reformulation with a justified correspondence |
| BINDING | Changed witness dependence, quantifier order, variable identity, or scope | Alpha-renaming or justified reordering of independent binders |
| INTERPRETATION | Wrong type, domain, definition, operation, or object | Standard equivalent representation with a documented bridge |
| DEPENDENCY | Essential source intermediate bypassed or an unjustified dependency used | Inlining the same reasoning or merely renaming a lemma |
| STRATEGY | Substantive argument replacement | Local elaboration filling genuinely implicit details |
| SILENT_REPAIR | Source error changed into a different valid claim/argument without disclosure | Explicitly identifying the error or recording a separate corrected variant |

Use all supported labels; leave labels empty for nonfailures and source defects. Record the exact changed component and its consequence. Different tactics alone are not evidence. A stronger premise can weaken the overall theorem: explain the logical change, not just token differences.

## Evidence and Causality

- `reported`: attributed claim in the source paper/artifact, not independently established here.
- `candidate`: our additional diagnosis with evidence but incomplete adjudication.
- `disputed`: disagreement or material ambiguity remains.
- `confirmed`: reserved for separately documented independent validation; not assigned by archival collectors.

No numerical confidence score is required. Express uncertainty through status, limitations, and supporting evidence. A statement can be valid while its supplied proof is invalid; explain both in the validity basis. Failure to find a proof is not a counterexample. In a final-artifact-only case, keep the first divergence and cause `unknown`.

Published examples are curated. Count distinct source families separately from their variants and do not use this collection to estimate prevalence. A source defect found by Pistis is not automatically a model-induced mistranslation.
