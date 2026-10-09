"""
Exact symbolic checks of the Gaussian formalism with ``sympy``.

Confirms
- the determinant identity (45), using the explicit matrix (35a),
- M^2 = 1,
- that calM = mu*M and N = nu*1 solve eq. (12).

Each printed expression must be zero. Run with:

    python scripts/check_gaussian_symbolic.py

Results are shown on the docs page "Comparison and numerical checks".
"""
import sympy as sp
l, eH, eV, th = sp.symbols('lambda eta_H eta_V theta', real=True)
S4, C4 = sp.sin(4*th), sp.cos(4*th)
M  = sp.Matrix([[S4, -C4], [-C4, -S4]])
nu, mu = l**2/(1-l**2), l/(1-l**2)
r = sp.sqrt(eH*eV)
sigQ = sp.Matrix([
    [1+nu*eH, 0,        mu*eH*S4, -mu*r*C4],
    [0,       1+nu*eV, -mu*r*C4,  -mu*eV*S4],
    [mu*eH*S4, -mu*r*C4, 1+nu*eH, 0],
    [-mu*r*C4, -mu*eV*S4, 0,      1+nu*eV]])
detQ = (1 - l**2*(1-eH)*(1-eV))**2 - l**2*(eH-eV)**2*S4**2
print(sp.simplify(sp.trigsimp(sigQ.det() - detQ/(1-l**2)**2)))   # 0
print(sp.simplify(M*M - sp.eye(2)))                                # zero matrix
Mcal, N = mu*M, nu*sp.eye(2)
print(sp.simplify(N - l*Mcal.conjugate()*M),                       # zero matrix
      sp.simplify(Mcal - (l*M + l*N.T*M)))                         # zero matrix
