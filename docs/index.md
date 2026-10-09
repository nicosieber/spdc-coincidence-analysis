# SPDC Coincidence Analysis

Photon pairs from type-II spontaneous parametric down-conversion (SPDC) are well described, in the degenerate regime and under suitable phase-matching and mode-overlap conditions, by a two-mode squeezed vacuum (TMSV) in the horizontal and vertical polarization modes. When this state is sent through a half-wave plate (HWP) and a polarizing beam splitter onto two non-photon-number-resolving ("bucket") detectors, the measured quantity is the coincidence probability, the probability that both detectors click.

Such coincidence probabilities are often estimated by truncating the TMSV expansion after the lowest photon-number terms. This works for weak pumping but is not exact, and it becomes inaccurate when multi-pair contributions are no longer negligible. This site derives the coincidence probability **exactly**, with all photon-number contributions included and with independent detector efficiencies \(\eta_H\), \(\eta_V\). The central result is the no-click probability

$$
P^{(\eta_H,\eta_V)}(0,0)
=\frac{1-\lambda^2}{\sqrt{\left(1-\lambda^2(1-\eta_H)(1-\eta_V)\right)^2-\lambda^2(\eta_H-\eta_V)^2\sin^2(4\vartheta)}},
$$

where \(\lambda=\tanh r\) is the squeezing parameter and \(\vartheta\) the HWP angle. The coincidence probability follows directly from it by inclusion–exclusion,
\(P_{\mathrm{cc}}=1-P_H^{(\eta_H)}(0)-P_V^{(\eta_V)}(0)+P^{(\eta_H,\eta_V)}(0,0)\).

## Contents

[Main derivation](theory/experimental_setup.md)
:   The experimental setup, a single-pair warm-up example, the POVM of lossy bucket detectors and the TMSV after the HWP. The no-click probability is then evaluated with coherent states and a complex Gaussian integral, and extended to dark counts and to an arbitrary passive lossless optical element in place of the HWP. The key steps of the derivation are machine-checked in Lean 4.

[Gaussian formalism](gaussian_formalism/overview.md)
:   The same result obtained from the covariance matrix of the state and its \(Q\) function, following Quesada and co-workers. The coincidence probability then appears as a Torontonian, and the two routes are compared side by side and checked numerically.

[Additional concepts, identities and derivations](concepts_and_foundations/overview.md)
:   Self-contained derivations of the identities used along the way: coherent states, operator conjugation, determinant and block-matrix identities, the POVM as a function of the number operator, and detector loss as a beam splitter.

[Interactive dashboards](dashboard/overview.md)
:   Vary \(\lambda\), \(\eta_H\) and \(\eta_V\) and follow the coincidence probability, the visibility and the Fisher information. The closed form is compared against independent truncated-Fock simulations in NumPy and QuTiP.
