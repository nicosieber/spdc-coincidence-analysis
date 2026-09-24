# Lean proofs for `docs/theory/cc_derivation.md`

Machine-checked proofs (Lean 4 + Mathlib) of parts of the coincidence-probability derivation.

| File | Contents |
|---|---|
| `CcProofs/Determinant.lean` | `det(1 − λ²MDMD) = (1 − λ²t_H t_V)² − λ²(t_H − t_V)² sin²(4ϑ)`, the final `P(0,0)` formula (assuming the operator part as a hypothesis), dark-count limits |
| `CcProofs/Gaussian.lean` | Multivariate complex Gaussian integral: for complex symmetric `A` with `Re A` positive definite, `(∫ dⁿξ exp(−½ ξᵀAξ))² · det A = (2π)ⁿ`, plus the explicit form `(det B)^{-1/2} ∏ⱼ (2π/(1+iκⱼ))^{1/2}` |

Not formalized: the Fock-space / coherent-state steps, and the choice of square-root branch
(`I = +1/√det A`) for the physical case.

## Build

Requires [elan](https://github.com/leanprover/elan).

```sh
cd lean
lake exe cache get   # download prebuilt Mathlib (first time only)
lake build
```

To check that a theorem has no gaps (`sorry`), add e.g.
`#print axioms integral_gaussian_complex_symmetric` to a file and run `lake env lean <file>`;
only `propext`, `Classical.choice` and `Quot.sound` should be listed.
