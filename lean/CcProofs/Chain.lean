import CcProofs.Determinant
import CcProofs.Gaussian

/-!
# Connecting the Gaussian integral to the closed form

`Gaussian.lean` evaluates `∫ exp(-½ ξᵀAξ)` for an abstract `A`, and `Determinant.lean` evaluates
`det(1 - λ²MDMD)`. This file builds the concrete matrices `Q`, `W`, `A = WᵀQW` of
`cc_derivation.md` and closes the gap between them:

1. `det_Amat`: `det A = det Q = det(1 - λ²MDMD)`.
2. `Bmat_posDef`: `B = Re A` is positive definite for `0 ≤ λ < 1`, `0 ≤ t_H, t_V ≤ 1`, so the
   Gaussian theorem applies (`matrix_properties.md`).
3. `Iphys_sq_mul_detQ`: `I² · det Q = 1` with the explicit `det Q`, and `P00_closed_form`: the
   final `P^{(η_H,η_V)}(0,0)` formula, assuming only the Fock-space part of the derivation.

`l` stands for `λ`, and `tH`, `tV` for `t_{H,V} = 1 - η_{H,V}`.
-/

open Matrix Complex
open scoped Real

noncomputable section

/-- The index set of `ℝ⁴ = ℝ² ⊕ ℝ²`, e.g. `ξ = (x, y)` or `χ = (α, α*)`. -/
abbrev Idx := Fin 2 ⊕ Fin 2

variable (l c s tH tV : ℝ)

/-- `L = DMD`. -/
def Lmat : Matrix (Fin 2) (Fin 2) ℝ := Dmat tH tV * Mmat c s * Dmat tH tV

/-- `Q = [[-λM, 1], [1, -λL]]` (equation `eq:Q`). -/
def Qmat : Matrix Idx Idx ℝ :=
  fromBlocks (-l • Mmat c s) 1 1 (-l • Lmat c s tH tV)

/-- `W = (1/√2) [[1, i], [1, -i]]`, so that `χ = (α, α*) = W ξ`. -/
def Wmat : Matrix Idx Idx ℂ :=
  ((Real.sqrt 2)⁻¹ : ℂ) • fromBlocks 1 (I • 1) 1 (-I • 1)

/-- `A = Wᵀ Q W`. -/
def Amat : Matrix Idx Idx ℂ :=
  Wmatᵀ * (Qmat l c s tH tV).map (↑) * Wmat

/-- `B = Re A = diag(1 - λ/2 (L+M), 1 + λ/2 (L+M))`. -/
def Bmat : Matrix Idx Idx ℝ :=
  fromBlocks (1 - (l / 2) • (Lmat c s tH tV + Mmat c s)) 0
    0 (1 + (l / 2) • (Lmat c s tH tV + Mmat c s))

/-- `C = Im A = [[0, λ/2 (L-M)], [λ/2 (L-M), 0]]`. -/
def Cmat : Matrix Idx Idx ℝ :=
  fromBlocks 0 ((l / 2) • (Lmat c s tH tV - Mmat c s))
    ((l / 2) • (Lmat c s tH tV - Mmat c s)) 0

/-! ## The explicit form of `A` (equation `ABiC`) -/

theorem Amat_eq : Amat l c s tH tV = cplx (Bmat l c s tH tV) (Cmat l c s tH tV) := by
  have h2 : ((Real.sqrt 2 : ℂ))⁻¹ ^ 2 = 1 / 2 := by
    rw [inv_pow, ← Complex.ofReal_pow, Real.sq_sqrt (by norm_num)]; push_cast; ring
  ext i j
  rcases i with i | i <;> rcases j with j | j <;> fin_cases i <;> fin_cases j <;>
    simp [Amat, Wmat, Qmat, Bmat, Cmat, Lmat, Mmat, Dmat, cplx, Matrix.mul_apply,
      fromBlocks, Matrix.one_apply] <;>
    ring_nf <;> simp only [h2, I_sq] <;> ring

lemma cplx_map_re (B C : Matrix Idx Idx ℝ) : (cplx B C).map re = B := by
  ext i j; simp [cplx]

lemma cplx_map_im (B C : Matrix Idx Idx ℝ) : (cplx B C).map im = C := by
  ext i j; simp [cplx]

/-- `A` is complex symmetric. -/
theorem Amat_transpose : (Amat l c s tH tV)ᵀ = Amat l c s tH tV := by
  rw [Amat_eq]
  ext i j
  rcases i with i | i <;> rcases j with j | j <;> fin_cases i <;> fin_cases j <;>
    simp [Bmat, Cmat, Lmat, Mmat, Dmat, cplx, fromBlocks] <;>
    (try ring_nf) <;> simp

/-! ## Step 1: `det A = det Q = det(1 - λ²MDMD)` -/

lemma sign_sumComm : Equiv.Perm.sign (Equiv.sumComm (Fin 2) (Fin 2)) = 1 := by
  decide

/-- `det W = -1`, hence `(det W)² = 1`. -/
theorem det_Wmat : Wmat.det = -1 := by
  have h4 : ((Real.sqrt 2 : ℂ))⁻¹ ^ 4 = 1 / 4 := by
    rw [inv_pow, show (4 : ℕ) = 2 * 2 from rfl, pow_mul, ← Complex.ofReal_pow,
      Real.sq_sqrt (by norm_num)]; push_cast; ring
  rw [Wmat, det_smul, det_fromBlocks_one₁₁, Matrix.one_mul, ← sub_smul, det_smul, det_one]
  simp only [Fintype.card_sum, Fintype.card_fin]
  rw [show (2 + 2 : ℕ) = 4 from rfl, h4]
  ring_nf; rw [I_sq]

/-- `det Q = det(1 - λ²MDMD)`, using the block structure of `Q`. -/
theorem det_Qmat :
    (Qmat l c s tH tV).det = (1 - l ^ 2 • (Mmat c s * Dmat tH tV * Mmat c s * Dmat tH tV)).det := by
  have hswap : (Qmat l c s tH tV).submatrix id (Equiv.sumComm (Fin 2) (Fin 2))
      = fromBlocks 1 (-l • Mmat c s) (-l • Lmat c s tH tV) 1 := by
    ext i j; rcases i with i | i <;> rcases j with j | j <;> rfl
  have h := det_permute' (Equiv.sumComm (Fin 2) (Fin 2)) (Qmat l c s tH tV)
  rw [hswap, sign_sumComm, det_fromBlocks_one₁₁] at h
  simp only [Units.val_one, Int.cast_one, one_mul] at h
  rw [← h, neg_smul, neg_smul, Matrix.neg_mul, Matrix.mul_neg, neg_neg, Matrix.smul_mul,
    Matrix.mul_smul, smul_smul, ← sq, ← Matrix.smul_mul, det_one_sub_mul_comm, Matrix.mul_smul]
  simp only [Lmat, Matrix.mul_assoc]

/-- `det A = det(1 - λ²MDMD)` (the step from `Gaussian.lean` to `Determinant.lean`). -/
theorem det_Amat :
    (Amat l c s tH tV).det
      = ((1 - l ^ 2 • (Mmat c s * Dmat tH tV * Mmat c s * Dmat tH tV)).det : ℂ) := by
  rw [Amat, det_mul, det_mul, det_transpose, det_Wmat, ← det_Qmat]
  rw [show ((Qmat l c s tH tV).map ((↑) : ℝ → ℂ)).det = ((Qmat l c s tH tV).det : ℂ) by
    simpa using (RingHom.map_det (algebraMap ℝ ℂ) (Qmat l c s tH tV)).symm]
  ring

/-! ## Step 2: `B = Re A` is positive definite (`matrix_properties.md`) -/

/-- The quadratic form `uᵀMu` for `u = (u₁, u₂)`. -/
def qM (u₁ u₂ : ℝ) : ℝ := 2 * c * s * (u₁ ^ 2 - u₂ ^ 2) + 2 * (s ^ 2 - c ^ 2) * u₁ * u₂

/-- `|uᵀMu| ≤ |u|²`, i.e. `‖M‖ ≤ 1` (`M` is orthogonal since `c² + s² = 1`). -/
lemma abs_qM (h : c ^ 2 + s ^ 2 = 1) (u₁ u₂ : ℝ) : |qM c s u₁ u₂| ≤ u₁ ^ 2 + u₂ ^ 2 := by
  have key : (u₁ ^ 2 + u₂ ^ 2) ^ 2 - qM c s u₁ u₂ ^ 2
      = (2 * c * s * (2 * u₁ * u₂) - (s ^ 2 - c ^ 2) * (u₁ ^ 2 - u₂ ^ 2)) ^ 2 := by
    unfold qM; linear_combination (-(c ^ 2 + s ^ 2 + 1) * (u₁ ^ 2 + u₂ ^ 2) ^ 2) * h
  have hR : 0 ≤ u₁ ^ 2 + u₂ ^ 2 := by positivity
  rw [abs_le]
  constructor <;> nlinarith [sq_nonneg (2 * c * s * (2 * u₁ * u₂) - (s ^ 2 - c ^ 2) * (u₁ ^ 2 - u₂ ^ 2))]

/-- `|uᵀ(L + M)u| ≤ 2|u|²`, i.e. `‖L + M‖ ≤ 2`, for `0 ≤ t_H, t_V ≤ 1`. -/
lemma abs_qLM (h : c ^ 2 + s ^ 2 = 1) (htH : tH ^ 2 ≤ 1) (htV : tV ^ 2 ≤ 1) (u₁ u₂ : ℝ) :
    |qM c s (tH * u₁) (tV * u₂) + qM c s u₁ u₂| ≤ 2 * (u₁ ^ 2 + u₂ ^ 2) := by
  have h1 := abs_qM c s h (tH * u₁) (tV * u₂)
  have h2 := abs_qM c s h u₁ u₂
  have h3 : (tH * u₁) ^ 2 + (tV * u₂) ^ 2 ≤ u₁ ^ 2 + u₂ ^ 2 := by
    nlinarith [sq_nonneg u₁, sq_nonneg u₂]
  calc _ ≤ |qM c s (tH * u₁) (tV * u₂)| + |qM c s u₁ u₂| := abs_add_le _ _
    _ ≤ 2 * (u₁ ^ 2 + u₂ ^ 2) := by linarith

/-- The quadratic form of `B`. -/
lemma Bmat_quadratic_form (x : Idx → ℝ) :
    x ⬝ᵥ (Bmat l c s tH tV *ᵥ x)
      = (x (.inl 0) ^ 2 + x (.inl 1) ^ 2)
        - l / 2 * (qM c s (tH * x (.inl 0)) (tV * x (.inl 1)) + qM c s (x (.inl 0)) (x (.inl 1)))
        + (x (.inr 0) ^ 2 + x (.inr 1) ^ 2)
        + l / 2 * (qM c s (tH * x (.inr 0)) (tV * x (.inr 1)) + qM c s (x (.inr 0)) (x (.inr 1))) := by
  simp [dotProduct, mulVec, Fintype.sum_sum_type, Fin.sum_univ_two, Bmat, fromBlocks, Lmat, Mmat,
    Dmat, qM, Matrix.one_apply]
  ring

lemma Bmat_isHermitian : (Bmat l c s tH tV).IsHermitian := by
  rw [IsHermitian, conjTranspose_eq_transpose_of_trivial]
  ext i j
  rcases i with i | i <;> rcases j with j | j <;> fin_cases i <;> fin_cases j <;>
    simp [Bmat, Lmat, Mmat, Dmat, fromBlocks] <;> (try ring_nf) <;> simp

/-- **`B = Re A` is positive definite** for `0 ≤ λ < 1` and `0 ≤ t_H, t_V ≤ 1`
(`matrix_properties.md`): `ξᵀBξ ≥ (1 - λ)|ξ|² > 0`. -/
theorem Bmat_posDef (h : c ^ 2 + s ^ 2 = 1) (hl0 : 0 ≤ l) (hl1 : l < 1)
    (htH0 : 0 ≤ tH) (htH1 : tH ≤ 1) (htV0 : 0 ≤ tV) (htV1 : tV ≤ 1) :
    (Bmat l c s tH tV).PosDef := by
  refine PosDef.of_dotProduct_mulVec_pos (Bmat_isHermitian l c s tH tV) fun x hx => ?_
  rw [star_trivial, Bmat_quadratic_form]
  have htH : tH ^ 2 ≤ 1 := by nlinarith
  have htV : tV ^ 2 ≤ 1 := by nlinarith
  have hu := abs_le.1 (abs_qLM c s tH tV h htH htV (x (.inl 0)) (x (.inl 1)))
  have hv := abs_le.1 (abs_qLM c s tH tV h htH htV (x (.inr 0)) (x (.inr 1)))
  -- `ξ ≠ 0`, so `|ξ|² > 0`
  have hR : 0 < x (.inl 0) ^ 2 + x (.inl 1) ^ 2 + x (.inr 0) ^ 2 + x (.inr 1) ^ 2 := by
    obtain ⟨i, hi⟩ : ∃ i, x i ≠ 0 := by
      by_contra h0; push Not at h0; exact hx (funext h0)
    have hi2 : 0 < x i ^ 2 := lt_of_le_of_ne (sq_nonneg _) (Ne.symm (pow_ne_zero 2 hi))
    have := sq_nonneg (x (.inl 0)); have := sq_nonneg (x (.inl 1))
    have := sq_nonneg (x (.inr 0)); have := sq_nonneg (x (.inr 1))
    rcases i with i | i <;> fin_cases i <;> simp at hi2 <;> linarith
  have h1 := mul_le_mul_of_nonneg_left hu.2 hl0
  have h2 := mul_le_mul_of_nonneg_left hv.1 hl0
  nlinarith [mul_pos (sub_pos.2 hl1) hR]

/-! ## Step 3: from the Gaussian integral to the closed form -/

/-- `det Q` in terms of `ϑ`, `λ`, `η_H`, `η_V` (the boxed formula of `cc_derivation.md`). -/
abbrev detQ (ϑ l ηH ηV : ℝ) : ℝ :=
  (1 - l ^ 2 * (1 - ηH) * (1 - ηV)) ^ 2 - l ^ 2 * (ηH - ηV) ^ 2 * Real.sin (4 * ϑ) ^ 2

/-- The matrix `A` of the derivation, with `c = cos 2ϑ`, `s = sin 2ϑ`, `t = 1 - η`. -/
abbrev Aphys (ϑ l ηH ηV : ℝ) : Matrix Idx Idx ℂ :=
  Amat l (Real.cos (2 * ϑ)) (Real.sin (2 * ϑ)) (1 - ηH) (1 - ηV)

/-- The normalized Gaussian integral `I = ∫ d⁴ξ/(2π)² exp(-½ ξᵀAξ)`. -/
def Iphys (ϑ l ηH ηV : ℝ) : ℂ :=
  (∫ ξ : Idx → ℝ, cexp (-(1 / 2 : ℂ) *
    ((fun i => (ξ i : ℂ)) ⬝ᵥ (Aphys ϑ l ηH ηV *ᵥ fun i => (ξ i : ℂ))))) / (2 * π) ^ 2

/-- **End-to-end: `I² · det Q = 1`** for all physical parameters `0 ≤ λ < 1`,
`0 ≤ η_H, η_V ≤ 1`, with `det Q = (1 - λ²(1-η_H)(1-η_V))² - λ²(η_H-η_V)² sin²(4ϑ)`.
Combines the Gaussian integral (`Gaussian.lean`), `det A = det(1 - λ²MDMD)` (step 1),
positivity of `B` (step 2) and the evaluation of the determinant (`Determinant.lean`). -/
theorem Iphys_sq_mul_detQ (ϑ l ηH ηV : ℝ) (hl0 : 0 ≤ l) (hl1 : l < 1)
    (hH0 : 0 ≤ ηH) (hH1 : ηH ≤ 1) (hV0 : 0 ≤ ηV) (hV1 : ηV ≤ 1) :
    Iphys ϑ l ηH ηV ^ 2 * (detQ ϑ l ηH ηV : ℂ) = 1 := by
  have hB : ((Aphys ϑ l ηH ηV).map re).PosDef := by
    rw [Aphys, Amat_eq, cplx_map_re]
    exact Bmat_posDef _ _ _ _ _ (Real.cos_sq_add_sin_sq _) hl0 hl1
      (by linarith) (by linarith) (by linarith) (by linarith)
  have hG := integral_gaussian_complex_symmetric (Aphys ϑ l ηH ηV) (Amat_transpose ..) hB
  have hdet : (Aphys ϑ l ηH ηV).det = (detQ ϑ l ηH ηV : ℂ) := by
    rw [Aphys, det_Amat, det_Q]
  rw [hdet] at hG
  simp only [Fintype.card_sum, Fintype.card_fin, show (2 + 2 : ℕ) = 2 * 2 from rfl] at hG
  have hπ : (2 * (π : ℂ)) ≠ 0 := by
    have := Real.pi_pos; exact mul_ne_zero two_ne_zero (by exact_mod_cast this.ne')
  rw [Iphys, div_pow, ← pow_mul, div_mul_eq_mul_div, hG, div_self (pow_ne_zero _ hπ)]

/-- **The no-click probability `P^{(η_H,η_V)}(0,0)`.** The only physics input is the
Fock-space/coherent-state part of the derivation, which turns `P(0,0)` into `Λ² · I`
(`hquantum`, with `Λ² = 1 - λ²`), plus the fact that a probability is nonnegative (`hprob`).
The latter also fixes the square-root branch: `I = +1/√(det Q)`. -/
theorem P00_closed_form (ϑ l ηH ηV P00 : ℝ) (hl0 : 0 ≤ l) (hl1 : l < 1)
    (hH0 : 0 ≤ ηH) (hH1 : ηH ≤ 1) (hV0 : 0 ≤ ηV) (hV1 : ηV ≤ 1)
    (hquantum : (P00 : ℂ) = (1 - l ^ 2) * Iphys ϑ l ηH ηV) (hprob : 0 ≤ P00) :
    P00 = (1 - l ^ 2) / Real.sqrt (detQ ϑ l ηH ηV) := by
  have hI := Iphys_sq_mul_detQ ϑ l ηH ηV hl0 hl1 hH0 hH1 hV0 hV1
  have hΛ : 0 < 1 - l ^ 2 := by nlinarith
  -- `I` is real: `I = P00 / Λ²`
  set j := P00 / (1 - l ^ 2) with hj
  have hIj : Iphys ϑ l ηH ηV = (j : ℂ) := by
    have : (1 - (l : ℂ) ^ 2) ≠ 0 := by exact_mod_cast hΛ.ne'
    rw [hj]; push_cast; rw [hquantum]; field_simp
  rw [hIj] at hI
  have hreal : j ^ 2 * detQ ϑ l ηH ηV = 1 := by exact_mod_cast hI
  have hj0 : 0 ≤ j := div_nonneg hprob hΛ.le
  have hF : 0 < detQ ϑ l ηH ηV := by
    by_contra hF; push Not at hF; nlinarith [sq_nonneg j]
  -- `j ≥ 0` and `j² = 1/det Q`, so `j = 1/√(det Q)`
  have hjF : j = 1 / Real.sqrt (detQ ϑ l ηH ηV) := by
    rw [← Real.sqrt_sq hj0, one_div, ← Real.sqrt_inv]
    congr 1
    field_simp
    linarith
  rw [div_eq_mul_one_div, ← hjF, hj]
  field_simp

end
