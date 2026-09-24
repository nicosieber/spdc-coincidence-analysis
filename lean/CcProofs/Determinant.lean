import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

/-!
# Algebraic spine of `docs/theory/cc_derivation.md`

This file formalizes the parts of the coincidence-probability derivation that are
pure (linear) algebra and real analysis. The Fock-space / coherent-state steps are
taken as a hypothesis (see `P00_of_det`), because Mathlib has no bosonic Fock space.
-/

open Matrix Real

noncomputable section

/-- The TMSV coupling matrix `M` from `tmsv.md`, with `c = cos 2ϑ`, `s = sin 2ϑ`. -/
def Mmat (c s : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![2 * c * s, s ^ 2 - c ^ 2; s ^ 2 - c ^ 2, -(2 * c * s)]

/-- The loss matrix `D = diag(t_H, t_V)`. -/
def Dmat (tH tV : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![tH, 0; 0, tV]

/-- Section "Evaluation of the determinant", in terms of `c, s` with `c² + s² = 1`. -/
theorem det_Q_cs (c s l tH tV : ℝ) (h : c ^ 2 + s ^ 2 = 1) :
    (1 - l ^ 2 • (Mmat c s * Dmat tH tV * Mmat c s * Dmat tH tV)).det
      = (1 - l ^ 2 * tH * tV) ^ 2 - l ^ 2 * (tH - tV) ^ 2 * (2 * c * s) ^ 2 := by
  simp only [Mmat, Dmat, det_fin_two, Matrix.mul_apply, Fin.sum_univ_two,
    Matrix.sub_apply, Matrix.one_apply, Matrix.smul_apply, smul_eq_mul,
    Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.empty_val', Matrix.cons_val_fin_one]
  simp
  linear_combination
    (-2 * l ^ 2 * tH * tV * (c ^ 2 + s ^ 2 + 1)
      + l ^ 4 * tH ^ 2 * tV ^ 2 * (c ^ 2 + s ^ 2 + 1) * ((c ^ 2 + s ^ 2) ^ 2 + 1)) * h

/-- Same statement with the half-wave-plate angle `ϑ` and efficiencies `η_H, η_V`
(the boxed `det Q` formula of the derivation). -/
theorem det_Q (ϑ l ηH ηV : ℝ) :
    (1 - l ^ 2 • (Mmat (cos (2 * ϑ)) (sin (2 * ϑ)) * Dmat (1 - ηH) (1 - ηV)
        * Mmat (cos (2 * ϑ)) (sin (2 * ϑ)) * Dmat (1 - ηH) (1 - ηV))).det
      = (1 - l ^ 2 * (1 - ηH) * (1 - ηV)) ^ 2 - l ^ 2 * (ηH - ηV) ^ 2 * sin (4 * ϑ) ^ 2 := by
  rw [det_Q_cs _ _ _ _ _ (cos_sq_add_sin_sq _)]
  have : sin (4 * ϑ) = 2 * cos (2 * ϑ) * sin (2 * ϑ) := by
    rw [show 4 * ϑ = 2 * (2 * ϑ) by ring, sin_two_mul]; ring
  rw [this]; ring

/-- The 1-D complex Gaussian integral used for each `z_j` (already in Mathlib). -/
example (a : ℂ) (ha : 0 < a.re) :
    ∫ x : ℝ, Complex.exp (-a * (x : ℂ) ^ 2) = (↑π / a) ^ (1 / 2 : ℂ) :=
  integral_gaussian_complex ha

/-- Final formula for `P^{(η_H,η_V)}(0,0)`, *assuming* the operator/Gaussian-integral
part of the derivation, i.e. `P00 = Λ² / √(det Q)`. -/
theorem P00_of_det (ϑ l ηH ηV P00 : ℝ)
    (hquantum : P00 = (1 - l ^ 2) / Real.sqrt
      (1 - l ^ 2 • (Mmat (cos (2 * ϑ)) (sin (2 * ϑ)) * Dmat (1 - ηH) (1 - ηV)
        * Mmat (cos (2 * ϑ)) (sin (2 * ϑ)) * Dmat (1 - ηH) (1 - ηV))).det) :
    P00 = (1 - l ^ 2) / Real.sqrt
      ((1 - l ^ 2 * (1 - ηH) * (1 - ηV)) ^ 2 - l ^ 2 * (ηH - ηV) ^ 2 * sin (4 * ϑ) ^ 2) := by
  rw [hquantum, det_Q]

/-- Section "Inclusion of dark counts": inclusion–exclusion with dark counts, and
`d_H = d_V = 0` recovers the dark-count-free formula. -/
theorem Pcoinc_dark_zero (PH PV P00 : ℝ) :
    let Pc := fun dH dV : ℝ => 1 - (1 - dH) * PH - (1 - dV) * PV + (1 - dH) * (1 - dV) * P00
    Pc 0 0 = 1 - PH - PV + P00 := by
  intro Pc; simp [Pc]

/-- "Physical interpretation": with both dark-count probabilities equal to 1, the
coincidence probability is 1 regardless of the state. -/
theorem Pcoinc_dark_one (PH PV P00 : ℝ) :
    1 - (1 - 1) * PH - (1 - 1) * PV + (1 - 1) * (1 - 1) * P00 = (1 : ℝ) := by
  ring

end
