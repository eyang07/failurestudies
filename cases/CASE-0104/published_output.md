# CASE-0104: Published Output

Status: excerpt

This is archival evidence, not code generated or verified by this study.

Exact released thinking noDAG ts_1.solved_lemma.lean_code:
import Mathlib
import Aesop
set_option maxHeartbeats 0
open BigOperators Real Nat Topology Rat Filter

theorem ts_1 
  (a : ℕ → ℝ) 
  (d : ℝ)
  (tc_1 : ∀ n : ℕ, a (n + 1) = a n + d) 
  (tc_2 : a 1 = 5 ∧ a 3 = 11) 
  (def_1 : ∀ n : ℕ, a n = a 1 + (n - 1) * d) 
  (l1 : a 3 = a 1 + 2 * d) 
  (l2 : 11 = 5 + 2 * d) 
  (l3 : 2 * d = 6) 
  (l4 : d = 3) 
  (l5 : a 5 = a 1 + 4 * d) 
  : a 5 = 17 := by
  have h_d_eq_3 : d = 3 := by
    have h₁ : (2 : ℝ) * d = 6 := by
      exact_mod_cast l3
    have h₂ : d = 3 := by
      linarith
    exact h₂
  
  have h_a5_eq_17 : a 5 = 17 := by
    have h₁ : a 5 = a 1 + 4 * d := l5
    have h₂ : a 1 = 5 := tc_2.1
    have h₃ : d = 3 := h_d_eq_3
    rw [h₁, h₂, h₃]
    norm_num
    <;>
    (try ring_nf at *)
    <;>
    (try norm_num at *)
    <;>
    (try linarith)
  
  exact h_a5_eq_17
