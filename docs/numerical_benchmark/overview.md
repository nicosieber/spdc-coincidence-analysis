# Numerical benchmarks

The [derivation](../theory/cc_derivation.md) gives a closed-form expression for the
coincidence-click probability of the HWP-rotated TMSV measured by two lossy bucket
detectors. This section checks that closed form against **independent simulations that
build the quantum state explicitly** in a truncated Fock space and apply the detector
model directly — no analytic shortcut.

Two implementations, same physics, same answer:

- **[NumPy from scratch](numerical_benchmark_numpy.md)** — the state as an $N\times N$
  array, creation operators as array shifts, the exponential as a power series. Depends on
  nothing but `numpy`.
- **[QuTiP](numerical_benchmark_qutip.md)** — the same construction in a purpose-built
  quantum-optics toolkit, and the natural launch point for extensions the closed form
  cannot express (dark counts, number-resolving detectors, mixed states).

Both reproduce the closed form to the Fock-truncation floor ($\sim10^{-10}$) at a
deliberately demanding operating point ($\lambda=0.7$, $\bar n\approx0.96$ pairs per mode),
which is what validates the analytic result the [dashboards](../dashboard/dashboard.md)
are built on.
