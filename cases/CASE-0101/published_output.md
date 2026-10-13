# CASE-0101: Published Output

Status: excerpt

This is archival evidence, not code generated or verified by this study.

Exact released thinking noDAG l3.solved_lemma.lean_code:
import Mathlib
import Aesop
set_option maxHeartbeats 0
open BigOperators Real Nat Topology Rat Filter

theorem l3
  (n : ℤ) (k : ℤ)
  (tc_1 : Odd n)
  (l1 : n = 2 * k + 1)
  (l2 : n^2 = 4 * k^2 + 4 * k + 1) :
  n^2 = 4 * k * (k + 1) + 1 := by
  have h_main : 4 * k^2 + 4 * k + 1 = 4 * k * (k + 1) + 1 := by
    have h₀ : 4 * k * (k + 1) = 4 * k ^ 2 + 4 * k := by
      ring
    linarith
  
  have h_final : n^2 = 4 * k * (k + 1) + 1 := by
    have h₁ : n ^ 2 = 4 * k ^ 2 + 4 * k + 1 := l2
    have h₂ : 4 * k ^ 2 + 4 * k + 1 = 4 * k * (k + 1) + 1 := h_main
    linarith
  
  exact h_final

Exact released non-thinking noDAG l3.solved_lemma.lean_code:
import Mathlib
import Aesop

set_option maxHeartbeats 0

open BigOperators Real Nat Topology Rat Filter

lemma l3
  (n : ℤ)
  (tc_1 : n % 2 = 1)
  (l1 : ∃ k : ℤ, n = 2 * k + 1)
  (l2 : ∃ k : ℤ, n^2 = 4 * k^2 + 4 * k + 1) :
  ∃ k : ℤ, n^2 = 4 * k * (k + 1) + 1 := by
  obtain ⟨k, hk⟩ := l2
  use k
  rw [hk]
  ring
