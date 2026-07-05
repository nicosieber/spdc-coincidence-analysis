# Coincidence probability

The coincidence dashboard visualizes the normalized coincidence probability of the
half-wave-plate-rotated TMSV, measured by two lossy bucket detectors, as a function of the
plate angle \(\vartheta\). It is built on the closed form derived in
[Derivation of the coincidence probability](../../theory/cc_derivation.md):

\begin{equation}
P_{\mathrm{coinc}}
=
1
-
P_H^{(\eta_H)}(0)
-
P_V^{(\eta_V)}(0)
+
P^{(\eta_H,\eta_V)}(0,0).
\end{equation}

A closed form is only as trustworthy as the independent check behind it. This coincidence
metric therefore comes with **two independent numerical validations** of the same number:
one built from scratch in NumPy, one built with the purpose-built quantum-optics toolkit
QuTiP. Both carry the identical live dashboard at the top and then walk through their own
engine. Pick a route.

<div class="tile-grid">
  <a class="tile" href="../../dashboard/coincidence/numpy">
    <div class="tile__icon">🔢</div>
    <h3>NumPy dashboard</h3>
    <p>The Fock-space simulation from scratch — creation operators as array shifts, the state as a power series, no specialised library.</p>
  </a>

  <a class="tile" href="../../dashboard/coincidence/qutip">
    <div class="tile__icon">⚛️</div>
    <h3>QuTiP dashboard</h3>
    <p>The same physics with QuTiP operators — a second, independent implementation and the natural starting point for dark counts, number-resolving detectors and mixed states.</p>
  </a>
</div>
