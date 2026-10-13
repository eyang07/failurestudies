# CASE-0004: Published Output

Status: excerpt

This is archival evidence, not code generated or verified by this study.

theorem my_favorite_theorem (x : ℕ) (h : 3^x = 5) : 3^(x + 2) = 51 := by
  have h₁ : False := by
    have h₂ : x ≤ 2 := by
      by_contra! h₃
      have h₄ : 3 ^ x ≥ 3 ^ 3 := by
        apply Nat.pow_le_pow_of_le_right
        norm_num
        linarith
      ...
    interval_cases x <;> norm_num at h ⊢ <;> omega
  have h₂ : 3^(x + 2) = 51 := by
    exfalso
    exact h₁
  exact h₂
