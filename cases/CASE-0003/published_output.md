# CASE-0003: Published Output

Status: excerpt

This is archival evidence, not code generated or verified by this study.

theorem my_favorite_theorem (change amount_paid total_cost : ℝ)
    (h : change = amount_paid + total_cost) : change = amount_paid + total_cost := by
  have h_main : change = amount_paid + total_cost := by
    -- The proof is straightforward because the goal is exactly the hypothesis `h`.
    exact h
  exact h_main
