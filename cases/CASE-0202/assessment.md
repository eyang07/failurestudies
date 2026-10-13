# CASE-0202: Provisional Assessment

Evaluator-only material.

## Case kind

reported_failure

## Source validity

ambiguous

## Validity basis

The paper calls its displayed statement and proof correct. The statement is for a real symmetric matrix and the displayed proof restricts zero entries to i!=j. However, Figure 2's actual prompt omits that restriction in the sentence quoted in original_prompt. Read literally, zero entries for every i,j would be false for a general diagonal matrix; read contextually, the intended off-diagonal assertion is recognizable. The collector does not silently resolve this textual difference.

## Content fidelity

uncertain

## Argument fidelity

violated

## Evidence status

candidate

## Readiness

needs_artifacts

## Reported model

Paper caption: ChatGPT-6 (Astra Ultra); visible figure selector: GPT-6 Astra Ultra. Exact snapshot/settings unknown.

## Reported environment

Figure 2 shows import Mathlib, open scoped BigOperators and a displayed work duration of 2 minutes 40 seconds. Lean/mathlib versions, compiler logs and generation tools unknown.

## Reported outcome

Authors report that the output compiles and uses a different argument. No compilation was performed here.

## Original prompt status

partial

## Original prompt

Exact source-defect excerpt visible in Figure 2: "But a_{i,j} = 0 by wlog assumption." The excerpt has no i!=j qualifier. Paraphrase of remaining visible prompt: states the symmetric-matrix theorem; describes an orthonormal diagonalization, trace expansion and eigenvalue-square sum; requests a compiling Lean proof and code alone. The typeset proof on p. 4 does contain i!=j. Their version relationship is unresolved, and the full prompt is not transcribed here.

## Licensing

Paper and figure: arXiv non-exclusive distribution license; code-block-specific license unknown. Minimal excerpts only; complete figure linked rather than copied.

## Notes

Selected for bypassed spectral reasoning. Preserve both the actual Figure 2 prompt and the paper's displayed proof as separately identified inputs if later used; a choice between them requires a protocol decision. The theorem statement appears preserved, but content fidelity is uncertain at full-input scope. Coordinator correction following independent archival review, before first import; see reports/ARCHIVAL_REVIEW.md.

## Primary Artifacts

- https://arxiv.org/pdf/2610.08144v1#page=3
- https://arxiv.org/html/2610.08144v1
- https://arxiv.org/html/2610.08144v1/matrix_example_slim.jpg
