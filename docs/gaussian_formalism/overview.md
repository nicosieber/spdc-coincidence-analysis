# Gaussian formalism

The [main derivation](../theory/cc_derivation.md) evaluates

<span id="eq1"></span>

$$
P^{(\eta_H,\eta_V)}(0,0)=\langle \Psi \rvert\left(1-\eta_H\right)^{\hat{n}_H}\otimes \left(1-\eta_V\right)^{\hat{n}_V}\lvert \Psi \rangle
\tag{1}
$$

by moving $t^{\hat n}$ through the exponential, inserting coherent states and doing a complex Gaussian integral. This section gets the same result with the method N. Quesada and co-workers use for Gaussian boson sampling with threshold ("click") detectors <a href="#ref-hamilton2017">[1]</a>, <a href="#ref-quesada2018">[2]</a>, <a href="#ref-kruse2019">[3]</a>. The same method is implemented in the Python library `thewalrus` <a href="#ref-gupt2019">[4]</a>.

Everything is written with the same objects as the main derivation: the vector $\mathbf{\hat a}=(\hat a_H,\hat a_V)^T$, the matrix $M$, the matrix $D$ and coherent states $\lvert\alpha_H,\alpha_V\rangle$. No quadratures ($\hat x,\hat p$) and no Wigner functions are needed.

## Outline of Quesada's approach

### The core idea

The main derivation works with the **state vector** $\lvert\Psi\rangle$: it carries the whole exponential $e^{\frac{\lambda}{2}(\mathbf{\hat a^{\dagger}})^TM\mathbf{\hat a^{\dagger}}}$ through every step. Quesada's approach rests on two observations that make this unnecessary.

1. **The state is completely determined by its covariance matrix.** For states like the TMSV (Gaussian states), all information is contained in the expectation values of products of *two* ladder operators: $\langle\Psi\rvert\hat a_H^{\dagger}\hat a_H\lvert\Psi\rangle$, $\langle\Psi\rvert\hat a_H\hat a_V\lvert\Psi\rangle$, $\langle\Psi\rvert\hat a_H\hat a_H\lvert\Psi\rangle$, … These numbers are collected in a single $4\times4$ matrix $\sigma_Q$, the (Husimi) **covariance matrix**. Every later step works with this matrix instead of the state vector.
2. **"No click" is a determinant.** The probability that none of the detectors clicks is given by one universal formula, $P(0,0)=1/\sqrt{\det\sigma_Q}$. Click probabilities (coincidences) follow from such no-click probabilities by inclusion-exclusion.

The physics of the setup (source, HWP, detector efficiency) thus only enters through which numbers stand in $\sigma_Q$.

### The steps

| Step | What is done | Input | Output | Page |
|---|---|---|---|---|
| 0 | Fix the notation | $\lvert\Psi\rangle$, $M$, $D$ | eqs. (2)–(5) | [Notation](notation.md) |
| 1 | Justify the vacuum formula $P(0,0)=1/\sqrt{\det\sigma_Q}$ | coherent states, the $Q$ function | eq. (12) | [Covariance matrix and vacuum probability](covariance_matrix.md) |
| 2 | Compute the second-order expectation values (covariance matrix) of the state behind the HWP | $\lvert\Psi\rangle$, i.e. $\lambda$ and $M$ | $4\times4$ matrix $\sigma_Q$, eq. (26) | [Covariance matrix and vacuum probability](covariance_matrix.md#psi-cov) |
| 3 | Include the detector efficiency as a beam splitter in front of a perfect detector | $\sigma_Q$, $\eta_H$, $\eta_V$ | lossy matrix $\sigma_Q'$, eq. (35a) | [Detector efficiency](detector_efficiency.md) |
| 4 | Evaluate $\det\sigma_Q'$ | $\sigma_Q'$ | $P^{(\eta_H,\eta_V)}(0,0)$, eq. (46) | [Determinant](determinant.md) |
| 5 | Write coincidences through no-click probabilities and evaluate them | $\sigma_Q'$ and its one-mode parts | $P_{\mathrm{cc}}$, eq. (50) | [Coincidence probability](coincidence.md) |

In more detail:

1. **Vacuum formula.** $\sigma_Q$ is exactly the covariance matrix of the probability distribution $Q(\boldsymbol\alpha)=\langle\boldsymbol\alpha\rvert\rho\lvert\boldsymbol\alpha\rangle/\pi^2$ built from coherent states. For a bell-shaped $Q$, the height at $\boldsymbol\alpha=0$ follows directly from its covariance matrix, $\pi^2Q(0)=1/\sqrt{\det\sigma_Q}$, and $\pi^2Q(0)$ is the vacuum probability. This is the one general result the method imports.
2. **Covariance matrix.** One relation, $\mathbf{\hat a}\lvert\Psi\rangle=\lambda M\mathbf{\hat a^{\dagger}}\lvert\Psi\rangle$, lets every second-order expectation value be computed without expanding $\lvert\Psi\rangle$ in Fock states. The result is remarkably simple: the photon-number matrix is $\nu\mathbb{1}$ and the pair-correlation matrix is $\mu M$, with $\nu$ and $\mu$ depending only on $\lambda$.
3. **Detector efficiency.** The no-click element $(1-\eta)^{\hat n}$ of the lossy POVM equals the vacuum probability behind a beam splitter of transmissivity $\eta$. On the covariance matrix, this beam splitter acts very simply: every $\hat a_H$ or $\hat a_H^{\dagger}$ in an expectation value brings a factor $\sqrt{\eta_H}$, and likewise for $V$. No operator ordering or conjugation through exponentials is needed.
4. **Determinant.** $\sigma_Q'$ has the block form $\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)$, so its determinant splits into two $2\times2$ determinants, $\det(A+B)\det(A-B)$. The result is $\det\sigma_Q'=\det(\mathbb{1}-\lambda^2MDMD)/(1-\lambda^2)^2$, i.e. the determinant of the main derivation.
5. **Coincidences.** "Both click" is rewritten through "no click" probabilities (inclusion–exclusion). Each of them is the height of a bell curve at the origin: of the full $Q$ function, or of its one-mode marginals, whose covariance matrices are $2\times2$ parts of $\sigma_Q'$. The resulting formula is what Quesada et al. call the **Torontonian**.

A side-by-side comparison with the main derivation, two interactive dashboards and numerical checks against `thewalrus` are on the page [Comparison and numerical checks](../dashboard/comparison.md).

### Supporting concepts

The general mathematical tools used along the way are derived separately under [Additional concepts](../concepts_and_foundations/overview.md):

- [Peak height of a Gaussian distribution](../concepts_and_foundations/gaussian_peak_height.md): why the height of a bell curve at its centre is $1/\sqrt{\det}$ of its covariance matrix.
- [Commutator with an operator exponential](../concepts_and_foundations/commutator_exponential.md): $[\hat A,e^{\hat X}]=[\hat A,\hat X]\,e^{\hat X}$.
- [Detector loss as a beam splitter](../concepts_and_foundations/loss_beam_splitter.md): why $(1-\eta)^{\hat n}$ is the vacuum probability behind a beam splitter.
- [Block-matrix identities](../concepts_and_foundations/block_matrices.md): determinants of $\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)$ and Jacobi's complementary-minor identity.

## References

The numbering is shared by all pages of this section. Each page lists the references it cites.

<p id="ref-hamilton2017">
[1] C. S. Hamilton, R. Kruse, L. Sansoni, S. Barkhofen, C. Silberhorn, I. Jex,
<em>Gaussian Boson Sampling</em>, Phys. Rev. Lett. <strong>119</strong>, 170501 (2017). Available: https://arxiv.org/abs/1612.01199
</p>

<p id="ref-quesada2018">
[2] N. Quesada, J. M. Arrazola, N. Killoran,
<em>Gaussian boson sampling using threshold detectors</em>, Phys. Rev. A <strong>98</strong>, 062322 (2018). Available: https://arxiv.org/abs/1807.01639
</p>

<p id="ref-kruse2019">
[3] R. Kruse, C. S. Hamilton, L. Sansoni, S. Barkhofen, C. Silberhorn, I. Jex,
<em>Detailed study of Gaussian boson sampling</em>, Phys. Rev. A <strong>100</strong>, 032326 (2019). Available: https://arxiv.org/abs/1801.07488
</p>

<p id="ref-gupt2019">
[4] B. Gupt, J. Izaac, N. Quesada,
<em>The Walrus: a library for the calculation of hafnians, Hermite polynomials and Gaussian boson sampling</em>, J. Open Source Softw. <strong>4</strong>(44), 1705 (2019). Documentation: https://the-walrus.readthedocs.io
</p>

<p id="ref-husimi1940">
[5] K. Husimi,
<em>Some Formal Properties of the Density Matrix</em>, Proc. Phys.-Math. Soc. Jpn. <strong>22</strong>, 264 (1940). Available: https://doi.org/10.11429/ppmsj1919.22.4_264
</p>

<p id="ref-cahill1969">
[6] K. E. Cahill, R. J. Glauber,
<em>Density Operators and Quasiprobability Distributions</em>, Phys. Rev. <strong>177</strong>, 1882 (1969). Available: https://doi.org/10.1103/PhysRev.177.1882
</p>

<p id="ref-leonhardt1997">
[7] U. Leonhardt,
<em>Measuring the Quantum State of Light</em>, Cambridge University Press, Cambridge (1997).
</p>

<p id="ref-weedbrook2012">
[8] C. Weedbrook, S. Pirandola, R. García-Patrón, N. J. Cerf, T. C. Ralph, J. H. Shapiro, S. Lloyd,
<em>Gaussian quantum information</em>, Rev. Mod. Phys. <strong>84</strong>, 621 (2012). Available: https://arxiv.org/abs/1110.3234
</p>

<p id="ref-ferraro2005">
[9] A. Ferraro, S. Olivares, M. G. A. Paris,
<em>Gaussian states in continuous variable quantum information</em>, 2005. Available: https://arxiv.org/abs/quant-ph/0503237
</p>

<p id="ref-powell2011">
[10] P. D. Powell,
<em>Calculating Determinants of Block Matrices</em>, 2011. Available: https://arxiv.org/abs/1112.4379
</p>

<p id="ref-meurer2017">
[11] A. Meurer et al.,
<em>SymPy: symbolic computing in Python</em>, PeerJ Comput. Sci. <strong>3</strong>, e103 (2017). Available: https://doi.org/10.7717/peerj-cs.103
</p>

<p id="ref-lvovsky2014">
[12] A. I. Lvovsky,
<em>Squeezed Light</em>, 2014. Available: https://arxiv.org/abs/1401.4118
</p>
