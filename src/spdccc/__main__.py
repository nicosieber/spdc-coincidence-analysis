"""Self-test: closed form vs. both Fock engines, to the truncation floor.

    python -m spdccc          # numpy engine only (no qutip needed)
    python -m spdccc --qutip  # also run the QuTiP twin
"""
import sys
import numpy as np

from . import coincidence, visibility, visibility_ideal
from .fock_numpy import brute_Pcoinc as brute_np


def _check(engine, tol, thetas):
    err = 0.0
    for lam in [0.1, 0.3, 0.5, 0.7]:
        for eH, eV in [(0.8, 0.8), (0.6, 0.9), (0.95, 0.4)]:
            for th in thetas:
                err = max(err, abs(coincidence(lam, eH, eV, th)
                                   - engine(lam, eH, eV, th)))
    return err


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv

    err = _check(brute_np, 1e-8, [0.05, np.pi / 8, 0.6, 1.0])
    print(f"max |closed - NumPy Fock|  P_coinc = {err:.2e}")
    assert err < 1e-8, "NumPy engine disagrees with closed form"

    v = max(abs(visibility(l, 1.0, 1.0) - visibility_ideal(l))
            for l in [0.05, 0.2, 0.4, 0.6, 0.75])
    print(f"max |V(eta=1) - sqrt(1-lam^2)|      = {v:.2e}")
    assert v < 1e-10, "visibility ceiling check failed"

    if "--qutip" in argv:
        from .fock_qutip import brute_Pcoinc as brute_q
        errq = _check(brute_q, 1e-9, [0.05, np.pi / 8, 0.6])
        print(f"max |closed - QuTiP Fock|  P_coinc = {errq:.2e}")
        assert errq < 1e-9, "QuTiP engine disagrees with closed form"

    print("validation PASSED")


if __name__ == "__main__":
    main()
