# CASE-0002: Published Output

Status: excerpt

This is archival evidence, not code generated or verified by this study.

theorem my_favorite_theorem (rate_A rate_B : ℝ) (h_rate_A : rate_A = 5)
    (h_rate_B : rate_B = 2 * rate_A)
    (h_total : 1000 * rate_A + 1000 * rate_B = 686 * rate_A + 686 * rate_B) :
    1000 - 2 = 686 := by
  have h_false : False := by
    have h₁ : rate_B = 10 := by
      rw [h_rate_B]
      rw [h_rate_A]
      ...
    have h₂ : 1000 * rate_A + 1000 * rate_B = 686 * rate_A + 686 * rate_B := h_total
    rw [h_rate_A, h₁] at h₂
    norm_num at h₂ ⊢
    <;> linarith
  have h_main : 1000 - 2 = 686 := by
    exfalso
    exact h_false
  exact h_main
