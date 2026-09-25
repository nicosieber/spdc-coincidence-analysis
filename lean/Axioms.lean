import CcProofs

/-! Axiom audit, run by CI (`lake env lean Axioms.lean`). Any `sorryAx` in the output means a
theorem has a gap; only `propext`, `Classical.choice` and `Quot.sound` are expected. -/

#print axioms integral_gaussian_complex_symmetric
#print axioms integral_gaussian_complex_matrix
#print axioms integral_gaussian_complex_matrix_sq
#print axioms Amat_eq
#print axioms det_Amat
#print axioms Bmat_posDef
#print axioms Iphys_sq_mul_detQ
#print axioms P00_closed_form
