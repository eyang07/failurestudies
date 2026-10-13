# CASE-0202: Published Output

Status: description_only

This is archival evidence, not code generated or verified by this study.

Description of visually inspected Figure 2: theorem trace_sq_nonneg_of_isSymm takes A : Matrix (Fin n) (Fin n) R with hA : A.IsSymm. It unfolds the square, changes the trace goal into a double entrywise sum, applies Finset.sum_nonneg twice, rewrites using hA.apply i j, and finishes with mul_self_nonneg. No diagonalization or eigenbasis construction is visible.
