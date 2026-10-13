# CASE-0203: Provisional Assessment

Evaluator-only material.

## Case kind

reported_failure

## Source validity

unknown

## Validity basis

No independent PDE validity judgment. The original NL statement/proof and the cited declaration were read only for archival comparison; their full surrounding hypotheses and mathematical implications were not verified.

## Content fidelity

violated

## Argument fidelity

uncertain

## Evidence status

reported

## Readiness

archival_only

## Reported model

Original formalization model unknown in the inspected artifacts. ChatGPT-6 (Astra Ultra) in Figure 3 is a later critique participant, not established as the generator of the cited Lean code.

## Reported environment

Pinned repository metadata read directly: leanprover/lean4:v4.34.0-rc2; mathlib revision 85e3a25e006c35636f0e53b0e9296caca2685bc0. These are snapshot configuration values, not verified original-run settings. Figure 3 critique displays 3 minutes 24 seconds; it is not an autoformalization runtime.

## Reported outcome

The authors allege an extra required input derivative. They explicitly qualify the comparison by distinguishing torus derivatives from mixed derivatives and by taking a maximum over derivative words. No source-theorem or compilation verification is claimed here.

## Original prompt status

unavailable

## Original prompt

unknown

## Licensing

Critique paper: arXiv non-exclusive distribution license. Referenced repository: Apache-2.0 at pinned commit. Original NL PDF reuse license not established. No full source artifact redistributed.

## Notes

Figure 3 was visually inspected: its prompt asks for criticism of a suspected mismatch, not generation of a formalization. It is not original-run evidence. Keep this case out of the first elementary reproduction set. Reviewer: collector /root/collect_lost_translation; substantive PDE review pending.

## Primary Artifacts

- https://arxiv.org/pdf/2610.08144v1#page=4
- https://arxiv.org/html/2610.08144v1/Figure3Fixed.jpg
- https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf#page=95
- https://github.com/openai/NavierStokesAndEuler/blob/f9e8bc5b38b6e212696e8a30e3e91517af887bbd/NavierStokes/SmoothFamilyTorusInverse.lean#L1059-L1080
- https://raw.githubusercontent.com/openai/NavierStokesAndEuler/f9e8bc5b38b6e212696e8a30e3e91517af887bbd/NavierStokes/SmoothFamilyTorusInverse.lean
- https://raw.githubusercontent.com/openai/NavierStokesAndEuler/f9e8bc5b38b6e212696e8a30e3e91517af887bbd/lean-toolchain
- https://raw.githubusercontent.com/openai/NavierStokesAndEuler/f9e8bc5b38b6e212696e8a30e3e91517af887bbd/lake-manifest.json
- https://raw.githubusercontent.com/openai/NavierStokesAndEuler/f9e8bc5b38b6e212696e8a30e3e91517af887bbd/LICENSE
