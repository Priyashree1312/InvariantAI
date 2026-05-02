def valid_probability (p : Float) : Prop :=
  0.0 ≤ p ∧ p ≤ 1.0

theorem prob_lower_bound (p : Float) (h : valid_probability p) : 0.0 ≤ p :=
by exact h.left

theorem prob_upper_bound (p : Float) (h : valid_probability p) : p ≤ 1.0 :=
by exact h.right
