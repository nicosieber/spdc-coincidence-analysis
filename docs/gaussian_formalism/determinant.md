# The determinant

## Reducing $4\times4$ to two $2\times2$ determinants

The lossy matrix $\sigma_Q'$ of [(35a)](detector_efficiency.md#eq35a) has the block form $\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)$. For any matrix of this form, equation (1) of [Block-matrix identities](../concepts_and_foundations/block_matrices.md#block:det_ABBA) (see also <a href="#ref-powell2011">[10]</a>) gives

<span id="eq36"></span>

$$
\det\sigma_Q'=\det(A+B)\,\det(A-B).
\tag{36}
$$

In our case:

<span id="eq37"></span>

$$
A\pm B=
\begin{pmatrix}
1+\nu\eta_H\pm\mu\eta_H S_4 & \mp\mu\sqrt{\eta_H\eta_V}\,C_4\\
\mp\mu\sqrt{\eta_H\eta_V}\,C_4 & 1+\nu\eta_V\mp\mu\eta_V S_4
\end{pmatrix}.
\tag{37}
$$

## Evaluating the two factors

The $2\times2$ determinant of (37) is "diagonal product minus off-diagonal product":

<span id="eq38"></span>

$$
\det(A\pm B)=\left(1+\nu\eta_H\pm\mu\eta_H S_4\right)\left(1+\nu\eta_V\mp\mu\eta_V S_4\right)-\mu^2\eta_H\eta_V C_4^2 .
\tag{38}
$$

Multiplying out the first product, the terms without $\pm$ and the terms with $\pm$ separate:

<span id="eq39"></span>

$$
\det(A\pm B)
=\underbrace{\Big[(1+\nu\eta_H)(1+\nu\eta_V)-\mu^2\eta_H\eta_V S_4^2-\mu^2\eta_H\eta_V C_4^2\Big]}_{\mathcal{P}}
\;\pm\;\underbrace{\Big[\mu\eta_H S_4\,(1+\nu\eta_V)-\mu\eta_V S_4\,(1+\nu\eta_H)\Big]}_{\Delta},
\tag{39}
$$

so that

<span id="eq40"></span>

$$
\det\sigma_Q'=(\mathcal{P}+\Delta)(\mathcal{P}-\Delta)=\mathcal{P}^2-\Delta^2 .
\tag{40}
$$

**The part $\mathcal{P}$.** The two terms with $S_4^2$ and $C_4^2$ combine, and the HWP angle drops out:

<span id="eq41"></span>

$$
\mu^2\eta_H\eta_V S_4^2+\mu^2\eta_H\eta_V C_4^2=\mu^2\eta_H\eta_V\left(S_4^2+C_4^2\right)=\mu^2\eta_H\eta_V .
\tag{41}
$$

Then, using $\nu^2-\mu^2=-\nu$ from [(18)](covariance_matrix.md#eq18),

<span id="eq42"></span>

$$
\mathcal{P}=(1+\nu\eta_H)(1+\nu\eta_V)-\mu^2\eta_H\eta_V
=1+\nu(\eta_H+\eta_V)+(\nu^2-\mu^2)\eta_H\eta_V
=1+\nu\left(\eta_H+\eta_V-\eta_H\eta_V\right).
\tag{42}
$$

Since $\eta_H+\eta_V-\eta_H\eta_V=1-(1-\eta_H)(1-\eta_V)=1-t_Ht_V$ and $\nu=\lambda^2/(1-\lambda^2)$:

<span id="eq43"></span>

$$
(1-\lambda^2)\,\mathcal{P}=1-\lambda^2+\lambda^2(1-t_Ht_V)=1-\lambda^2t_Ht_V .
\tag{43}
$$

**The part $\Delta$.** The $\nu\eta_H\eta_V$ terms cancel:

<span id="eq44"></span>

$$
\Delta=\mu S_4\big[(1+\nu\eta_V)\eta_H-(1+\nu\eta_H)\eta_V\big]=\mu\,(\eta_H-\eta_V)\,S_4,
\qquad
(1-\lambda^2)\,\Delta=\lambda\,(\eta_H-\eta_V)\sin(4\vartheta).
\tag{44}
$$

## Result

Inserting (43) and (44) into (40):

<span id="eq45"></span>

$$
\det\sigma_Q'
=\frac{\left(1-\lambda^2t_Ht_V\right)^2-\lambda^2(\eta_H-\eta_V)^2\sin^2(4\vartheta)}{(1-\lambda^2)^2}
=\frac{\det Q}{(1-\lambda^2)^2},
\tag{45}
$$

where $\det Q=\det(\mathbb{1}-\lambda^2MDMD)$ is the determinant of the [main derivation](../theory/cc_derivation.md). With [(26)](vacuum_probability.md#eq26) and [(32)](detector_efficiency.md#eq32):

<span id="eq46"></span>

$$
\boxed{\;
P^{(\eta_H,\eta_V)}(0,0)=\frac{1}{\sqrt{\det\sigma_Q'}}
=\frac{1-\lambda^2}
{\sqrt{\big(1-\lambda^2(1-\eta_H)(1-\eta_V)\big)^2-\lambda^2(\eta_H-\eta_V)^2\sin^2(4\vartheta)}}\; .}
\tag{46}
$$

**By-product: $\det Q>0$.** $\sigma_Q'$ is a covariance matrix, hence positive definite. As shown in [Block-matrix identities](../concepts_and_foundations/block_matrices.md#block:rotation), a rotation brings $\sigma_Q'$ to the block-diagonal form $\left(\begin{smallmatrix}A+B&0\\0&A-B\end{smallmatrix}\right)$, so $A+B$ and $A-B$ are positive definite as well. Therefore both factors

<span id="eq47"></span>

$$
(1-\lambda^2)(\mathcal{P}\pm\Delta)=1-\lambda^2t_Ht_V\pm\lambda(\eta_H-\eta_V)\sin(4\vartheta)
\tag{47}
$$

are strictly positive. Their product is $\det Q$, which shows $\det Q>0$ for all $0\le\lambda<1$ and $0\le\eta_{H,V}\le1$.

## Sanity checks

| Limit | $\det\sigma_Q'$ | $P^{(\eta_H,\eta_V)}(0,0)$ | Meaning |
|---|---|---|---|
| $\eta_H=\eta_V=0$ | $1$ | $1$ | blind detectors never click |
| $\eta_H=\eta_V=1$ | $(1-\lambda^2)^{-2}$ | $1-\lambda^2$ | vacuum part $\Lambda^2$ of the TMSV |
| $\eta_H=\eta_V=\eta$ | $\dfrac{(1-\lambda^2(1-\eta)^2)^2}{(1-\lambda^2)^2}$ | $\dfrac{1-\lambda^2}{1-\lambda^2(1-\eta)^2}$ | no $\vartheta$ dependence |
| $\lambda=0$ | $1$ | $1$ | no pump |

The third row explains why $\Delta\propto(\eta_H-\eta_V)$. If both detectors are equally efficient, the "beam splitter in front of the detector" acts identically on both modes, so it can be moved in front of the HWP. The HWP then only rotates the modes before two identical detectors, and that cannot change $P(0,0)$.

## References

<p id="ref-powell2011">
[10] P. D. Powell,
<em>Calculating Determinants of Block Matrices</em>, 2011. Available: https://arxiv.org/abs/1112.4379
</p>
