import Mathlib.Analysis.Matrix.PosDef
import Mathlib.Analysis.SpecialFunctions.Gaussian.FourierTransform
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.Tactic

open Matrix Complex MeasureTheory
open scoped Real

noncomputable section

variable {n : Type*} [Fintype n] [DecidableEq n]

set_option linter.unusedSectionVars false

/-! ## Linear algebra: simultaneous diagonalization -/

/-- Real spectral theorem in the form `Uᵀ U = 1`, `Uᵀ H U = diag`. -/
lemma real_spectral {H : Matrix n n ℝ} (hH : H.IsHermitian) :
    ∃ U : Matrix n n ℝ, Uᵀ * U = 1 ∧ Uᵀ * H * U = diagonal hH.eigenvalues := by
  refine ⟨hH.eigenvectorUnitary, ?_, ?_⟩
  · have := Unitary.coe_star_mul_self hH.eigenvectorUnitary
    simpa [star_eq_conjTranspose, conjTranspose_eq_transpose_of_trivial] using this
  · have := hH.conjStarAlgAut_star_eigenvectorUnitary
    simp only [Unitary.conjStarAlgAut_star_apply] at this
    simpa [star_eq_conjTranspose, conjTranspose_eq_transpose_of_trivial] using this

/-- If `B` is positive definite and `C` symmetric, there is a real `P` with
`Pᵀ B P = 1` and `Pᵀ C P = diag κ`. (In `cc_derivation.md`: `P = B^{-1/2} Oᵀ`.) -/
lemma simultaneous_diag {B C : Matrix n n ℝ} (hB : B.PosDef) (hC : C.IsHermitian) :
    ∃ (P : Matrix n n ℝ) (κ : n → ℝ), Pᵀ * B * P = 1 ∧ Pᵀ * C * P = diagonal κ := by
  obtain ⟨U, hUU, hUB⟩ := real_spectral hB.1
  set b := hB.1.eigenvalues
  have hb : ∀ i, 0 < b i := hB.eigenvalues_pos
  let S : Matrix n n ℝ := diagonal fun i => (Real.sqrt (b i))⁻¹
  let P₁ := U * S
  have hP₁ : P₁ᵀ * B * P₁ = 1 := by
    have : P₁ᵀ * B * P₁ = S * (Uᵀ * B * U) * S := by
      simp only [P₁, S, transpose_mul, diagonal_transpose, Matrix.mul_assoc]
    rw [this, hUB, diagonal_mul_diagonal, diagonal_mul_diagonal, ← diagonal_one]
    congr 1; funext i
    have h := Real.sq_sqrt (hb i).le
    have h0 : Real.sqrt (b i) ≠ 0 := (Real.sqrt_pos.2 (hb i)).ne'
    field_simp
    linarith
  set K := P₁ᵀ * C * P₁
  have hK : K.IsHermitian := by
    rw [IsHermitian, conjTranspose_eq_transpose_of_trivial]
    have hC' : Cᵀ = C := by simpa [conjTranspose_eq_transpose_of_trivial] using hC.eq
    simp only [K, transpose_mul, transpose_transpose, hC', Matrix.mul_assoc]
  obtain ⟨V, hVV, hVK⟩ := real_spectral hK
  refine ⟨P₁ * V, hK.eigenvalues, ?_, ?_⟩
  · calc (P₁ * V)ᵀ * B * (P₁ * V) = Vᵀ * (P₁ᵀ * B * P₁) * V := by
          simp only [transpose_mul, Matrix.mul_assoc]
      _ = 1 := by rw [hP₁, Matrix.mul_one, hVV]
  · calc (P₁ * V)ᵀ * C * (P₁ * V) = Vᵀ * K * V := by
          simp only [K, transpose_mul, Matrix.mul_assoc]
      _ = _ := hVK

/-- The complex matrix `A = B + iC`. -/
def cplx (B C : Matrix n n ℝ) : Matrix n n ℂ :=
  B.map (↑) + Complex.I • C.map (↑)

/-- `det P ^ 2 * det B = 1`. -/
lemma det_sq_mul_det {B P : Matrix n n ℝ} (h : Pᵀ * B * P = 1) : P.det ^ 2 * B.det = 1 := by
  have := congrArg det h
  rw [det_mul, det_mul, det_transpose, det_one] at this
  linear_combination this

/-- `det A · (det P)² = ∏ (1 + iκⱼ)`. -/
lemma det_cplx_mul {B C P : Matrix n n ℝ} {κ : n → ℝ}
    (hB : Pᵀ * B * P = 1) (hC : Pᵀ * C * P = diagonal κ) :
    (cplx B C).det * (P.det : ℂ) ^ 2 = ∏ i, (1 + I * κ i) := by
  let f := (algebraMap ℝ ℂ).mapMatrix (m := n)
  have hPc : (P.map (↑) : Matrix n n ℂ)ᵀ * cplx B C * P.map (↑)
      = diagonal fun i => 1 + I * κ i := by
    have e1 : (P.map (↑) : Matrix n n ℂ)ᵀ * B.map (↑) * P.map (↑) = (Pᵀ * B * P).map (↑) := by
      have h := (Matrix.map_mul : ((Pᵀ * B) * P).map Complex.ofRealHom = _)
      rw [(Matrix.map_mul : (Pᵀ * B).map Complex.ofRealHom = _)] at h
      rw [← transpose_map]
      exact h.symm
    have e2 : (P.map (↑) : Matrix n n ℂ)ᵀ * C.map (↑) * P.map (↑) = (Pᵀ * C * P).map (↑) := by
      have h := (Matrix.map_mul : ((Pᵀ * C) * P).map Complex.ofRealHom = _)
      rw [(Matrix.map_mul : (Pᵀ * C).map Complex.ofRealHom = _)] at h
      rw [← transpose_map]
      exact h.symm
    rw [cplx, Matrix.mul_add, Matrix.add_mul, Matrix.mul_smul, Matrix.smul_mul, e1, e2, hB, hC]
    ext i j
    by_cases hij : i = j <;> simp [hij, diagonal, one_apply]
  have := congrArg det hPc
  rw [det_mul, det_mul, det_transpose, det_diagonal] at this
  have hd : (P.map ((↑) : ℝ → ℂ)).det = (P.det : ℂ) := by
    simpa using (RingHom.map_det (algebraMap ℝ ℂ) P).symm
  rw [hd] at this
  linear_combination this

/-- `det A = det B · ∏ (1 + iκⱼ)`. -/
lemma det_cplx {B C P : Matrix n n ℝ} {κ : n → ℝ}
    (hB : Pᵀ * B * P = 1) (hC : Pᵀ * C * P = diagonal κ) :
    (cplx B C).det = B.det * ∏ i, (1 + I * κ i) := by
  have h1 := det_cplx_mul hB hC
  have h2 : ((P.det ^ 2 * B.det : ℝ) : ℂ) = 1 := by rw [det_sq_mul_det hB]; simp
  push_cast at h2
  linear_combination (B.det : ℂ) * h1 - (cplx B C).det * h2

/-! ## Quadratic forms -/

/-- The real quadratic form `ξᵀ M ξ`. -/
def qf (M : Matrix n n ℝ) (x : n → ℝ) : ℝ := x ⬝ᵥ (M *ᵥ x)

lemma qf_comp (M P : Matrix n n ℝ) (z : n → ℝ) : qf M (P *ᵥ z) = qf (Pᵀ * M * P) z := by
  simp only [qf, ← mulVec_mulVec, dotProduct_mulVec, vecMul_transpose]

lemma qf_one (z : n → ℝ) : qf 1 z = ∑ i, z i ^ 2 := by
  simp [qf, dotProduct, sq]

lemma qf_diagonal (κ : n → ℝ) (z : n → ℝ) : qf (diagonal κ) z = ∑ i, κ i * z i ^ 2 := by
  simp only [qf, dotProduct, mulVec_diagonal]
  exact Finset.sum_congr rfl fun i _ => by ring

lemma continuous_qf (M : Matrix n n ℝ) : Continuous (qf M) := by
  unfold qf dotProduct mulVec dotProduct
  fun_prop

/-! ## Linear change of variables -/

lemma integral_eq_abs_det_mul_integral_comp (P : Matrix n n ℝ) (hP : P.det ≠ 0)
    (f : (n → ℝ) → ℂ) (hf : Continuous f) :
    ∫ x, f x = ((|P.det| : ℝ) : ℂ) * ∫ z, f (P *ᵥ z) := by
  have hmap := Real.map_matrix_volume_pi_eq_smul_volume_pi hP
  have h : ∫ z, f (P *ᵥ z) = ∫ x, f x ∂(Measure.map (toLin' P) volume) := by
    rw [integral_map (toLin' P).continuous_of_finiteDimensional.aemeasurable
      hf.aestronglyMeasurable]
    simp [toLin'_apply]
  rw [h, hmap, integral_smul_measure, ENNReal.toReal_ofReal (abs_nonneg _), abs_inv,
    Complex.real_smul]
  have : ((|P.det| : ℝ) : ℂ) ≠ 0 := by exact_mod_cast abs_ne_zero.2 hP
  push_cast
  field_simp

/-! ## The multivariate complex Gaussian integral -/

/-- **Complex Gaussian integral, diagonalized form.**
For `A = B + iC` with `B` positive definite and `C` symmetric (both real), there are real
`κⱼ` (the eigenvalues of `B^{-1/2} C B^{-1/2}`) with
`∫ exp(-½ ξᵀAξ) dξ = (det B)^{-1/2} ∏ⱼ (2π / (1 + iκⱼ))^{1/2}` and
`det A = det B ∏ⱼ (1 + iκⱼ)`. -/
theorem integral_gaussian_complex_matrix {B C : Matrix n n ℝ} (hB : B.PosDef)
    (hC : C.IsHermitian) :
    ∃ κ : n → ℝ,
      ∫ ξ : n → ℝ, cexp (-(1 / 2 : ℂ) * ((qf B ξ : ℂ) + I * qf C ξ))
        = ((Real.sqrt B.det)⁻¹ : ℂ) * ∏ i, (2 * π / (1 + I * κ i)) ^ (1 / 2 : ℂ)
      ∧ (cplx B C).det = B.det * ∏ i, (1 + I * κ i) := by
  obtain ⟨P, κ, h1, h2⟩ := simultaneous_diag hB hC
  refine ⟨κ, ?_, det_cplx h1 h2⟩
  have hdet := det_sq_mul_det h1
  have hP : P.det ≠ 0 := by rintro h; simp [h] at hdet
  rw [integral_eq_abs_det_mul_integral_comp P hP _ (by
    have := continuous_qf B; have := continuous_qf C; fun_prop)]
  simp_rw [qf_comp, h1, h2, qf_one, qf_diagonal]
  have hint : ∀ z : n → ℝ,
      cexp (-(1 / 2 : ℂ) * (((∑ i, z i ^ 2 : ℝ) : ℂ) + I * ((∑ i, κ i * z i ^ 2 : ℝ) : ℂ)))
        = cexp (-∑ i, (1 + I * κ i) / 2 * (z i : ℂ) ^ 2 + ∑ i, (0 : n → ℂ) i * z i) := by
    intro z
    congr 1
    push_cast
    simp only [Pi.zero_apply, zero_mul, Finset.sum_const_zero, add_zero, Finset.mul_sum, ← Finset.sum_add_distrib,
      ← Finset.sum_neg_distrib]
    exact Finset.sum_congr rfl fun i _ => by ring
  simp_rw [hint]
  rw [GaussianFourier.integral_cexp_neg_sum_mul_add (fun i => by simp) 0]
  congr 1
  · -- the Jacobian: `|det P| = (det B)^{-1/2}`
    have hBpos := hB.det_pos
    have : |P.det| = (Real.sqrt B.det)⁻¹ := by
      rw [← Real.sqrt_sq_eq_abs, ← Real.sqrt_inv]
      congr 1
      field_simp
      linarith
    rw [this]; push_cast; rfl
  · refine Finset.prod_congr rfl fun i _ => ?_
    have h0 : (1 + I * κ i) ≠ 0 := by
      intro h; have := congrArg Complex.re h; simp at this
    simp only [Pi.zero_apply, zero_pow two_ne_zero, zero_div, Complex.exp_zero, mul_one]
    congr 1
    field_simp

/-- **Complex Gaussian integral, branch-free form.** With `I := (2π)^{-n/2} ∫ exp(-½ ξᵀAξ) dξ`,
this says `I² · det A = 1`, i.e. `I = 1/√(det A)` up to the choice of square-root branch. -/
theorem integral_gaussian_complex_matrix_sq {B C : Matrix n n ℝ} (hB : B.PosDef)
    (hC : C.IsHermitian) :
    (∫ ξ : n → ℝ, cexp (-(1 / 2 : ℂ) * ((qf B ξ : ℂ) + I * qf C ξ))) ^ 2 * (cplx B C).det
      = (2 * (π : ℂ)) ^ Fintype.card n := by
  obtain ⟨κ, hI, hA⟩ := integral_gaussian_complex_matrix hB hC
  have hBpos := hB.det_pos
  have h0 : ∀ i, (1 + I * κ i) ≠ 0 := by
    intro i h; have := congrArg Complex.re h; simp at this
  rw [hI, hA, mul_pow, ← Finset.prod_pow]
  simp_rw [one_div, cpow_ofNat_inv_pow]
  have hs : ((Real.sqrt B.det : ℂ)⁻¹) ^ 2 * (B.det : ℂ) = 1 := by
    rw [inv_pow, ← Complex.ofReal_pow, Real.sq_sqrt hBpos.le]
    have : (B.det : ℂ) ≠ 0 := by exact_mod_cast hBpos.ne'
    field_simp
  calc ((Real.sqrt B.det : ℂ)⁻¹) ^ 2 * (∏ i, 2 * π / (1 + I * κ i))
        * ((B.det : ℂ) * ∏ i, (1 + I * κ i))
      = (((Real.sqrt B.det : ℂ)⁻¹) ^ 2 * (B.det : ℂ))
        * ∏ i, (2 * π / (1 + I * κ i) * (1 + I * κ i)) := by
        rw [Finset.prod_mul_distrib]; ring
    _ = (2 * (π : ℂ)) ^ Fintype.card n := by
        rw [hs, one_mul]
        simp_rw [div_mul_cancel₀ _ (h0 _)]
        simp

/-! ## Statement in the notation of `cc_derivation.md` -/

lemma cplx_re_im (A : Matrix n n ℂ) : cplx (A.map re) (A.map im) = A := by
  ext i j
  simp only [cplx, Matrix.add_apply, Matrix.smul_apply, Matrix.map_apply, smul_eq_mul]
  rw [mul_comm]; exact re_add_im _

lemma quadratic_form_cplx (B C : Matrix n n ℝ) (ξ : n → ℝ) :
    (fun i => (ξ i : ℂ)) ⬝ᵥ (cplx B C *ᵥ fun i => (ξ i : ℂ)) = (qf B ξ : ℂ) + I * qf C ξ := by
  simp only [qf, cplx, dotProduct, mulVec, Matrix.add_apply, Matrix.smul_apply, Matrix.map_apply,
    smul_eq_mul]
  push_cast
  simp only [Finset.mul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => by ring

/-- **The Gaussian integral of `cc_derivation.md`** (section "Evaluation of the complex Gaussian
integral"), for any dimension `n` (the derivation uses `n = 4`):
if `A` is complex symmetric with positive definite real part `B = Re A`, then
`I := ∫ dⁿξ/(2π)^{n/2} exp(-½ ξᵀAξ)` satisfies `I² · det A = 1`, stated here without
dividing by `(2π)^{n/2}`. -/
theorem integral_gaussian_complex_symmetric (A : Matrix n n ℂ) (hA : Aᵀ = A)
    (hB : (A.map re).PosDef) :
    (∫ ξ : n → ℝ, cexp (-(1 / 2 : ℂ) *
        ((fun i => (ξ i : ℂ)) ⬝ᵥ (A *ᵥ fun i => (ξ i : ℂ))))) ^ 2 * A.det
      = (2 * (π : ℂ)) ^ Fintype.card n := by
  have hC : (A.map im).IsHermitian := by
    rw [IsHermitian, conjTranspose_eq_transpose_of_trivial, ← transpose_map, hA]
  have := integral_gaussian_complex_matrix_sq hB hC
  rw [cplx_re_im] at this
  simp_rw [← this, ← quadratic_form_cplx, cplx_re_im]

end
