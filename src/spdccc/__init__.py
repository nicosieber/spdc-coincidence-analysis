"""
spdc-coincidence-analysis -- physics for the SPDC coincidence-analysis project.



Submodules
----------
spdccc.closedform   analytic closed form (no dependencies beyond numpy; sympy
                  only for the Fisher-information derivatives)
spdccc.fock_numpy   from-scratch NumPy Fock-space simulation (ground truth)
spdccc.fock_qutip   QuTiP twin of the Fock simulation (requires qutip)

The Fock engines are imported lazily -- ``import spdccc`` does not require
qutip; only ``import spdccc.fock_qutip`` does.
"""
from .closedform import (
    p00, marginal_noclick, coincidence, click_probability,
    visibility, visibility_ideal, nbar_per_mode,
    fisher_phi, snl_phi,
    closed_P00, closed_Pcoinc,
)

__all__ = [
    "p00", "marginal_noclick", "coincidence", "click_probability",
    "visibility", "visibility_ideal", "nbar_per_mode",
    "fisher_phi", "snl_phi",
    "closed_P00", "closed_Pcoinc",
]

__version__ = "0.1.0"
