# CASE-0102: Published Output

Status: excerpt

This is archival evidence, not code generated or verified by this study.

Exact released non-thinking noDAG tc_1.formalization.lean_code:
import Mathlib
import Aesop

set_option maxHeartbeats 0

open BigOperators Real Nat Topology Rat Filter

variable (a : ℕ → ℝ)
(tc_1 : ∀ n m, (n < m) → ∃ d, a m - a n = (m - n) * d)

Exact l5.solved_lemma.lean_code:
import Mathlib
import Aesop

set_option maxHeartbeats 0

open BigOperators Real Nat Topology Rat Filter

lemma l5
  (a : ℕ → ℝ)
  (tc_1 : ∀ n m, (n < m) → ∃ d, a m - a n = (m - n) * d)
  (tc_2 : a 1 = 5 ∧ a 3 = 11)
  (l1 : ∃ d, a 3 = a 1 + 2 * d)
  (l2 : 11 = 5 + 2 * (Classical.choose l1))
  (l3 : 2 * (Classical.choose l1) = 6)
  (l4 : Classical.choose l1 = 3) :
  a 5 = a 1 + 4 * (Classical.choose l1) := by
  have hd : Classical.choose l1 = 3 := l4
  rw [hd]
  have ⟨d, h⟩ := tc_1 1 5 (by linarith)
  have h₁ : d = 3 := by
    have ⟨d', hd'⟩ := tc_1 1 3 (by linarith)
    rw [tc_2.1, tc_2.2] at hd'
    simp at hd'
    rw [← hd'] at l4
    exact l4.symm
  rw [h₁] at h
  simp at h
  rw [h]
  rw [tc_2.1]
  ring
