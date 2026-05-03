# Interactive dashboard
<iframe
  src="../assets/plots/coincidence_plot.html"
  width="100%"
  height="600"
  style="border:0;"
  loading="lazy">
</iframe>
## What is plotted: The coincidence probability of the TMSV

This dashboard visualizes the normalized coincidence probability as a function of the half-wave plate angle \(\vartheta\). The plotted quantity is based on the coincidence probability derived in [Derivation of the coincidence probability](../theory/cc_derivation.md#eq:Pcoinc_inclusion_exclusion):

\begin{equation}
\label{eq:dashboard_pcc}
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

The joint no-click probability entering this expression is given by

\begin{equation}
\label{eq:dashboard_p00}
P^{(\eta_H,\eta_V)}(0,0)
=
\dfrac{1-\lambda^2}{
\sqrt{
\left(1-\lambda^2(1-\eta_H)(1-\eta_V)\right)^2
-
\lambda^2(\eta_H-\eta_V)^2\sin^2(4\vartheta)
}
}.
\end{equation}

The marginal no-click probabilities are obtained from the same expression by setting the efficiency of the opposite detector to zero:

\begin{equation}
\begin{aligned}
P_H^{(\eta_H)}(0)
&=
P^{(\eta_H,\eta_V=0)}(0,0),
\\
P_V^{(\eta_V)}(0)
&=
P^{(\eta_H=0,\eta_V)}(0,0).
\end{aligned}
\end{equation}

## Normalization and visibility

The dashboard plots the coincidence probability normalized by its maximum value over the displayed interval

\begin{equation}
0 \leq \vartheta \leq \frac{\pi}{4}.
\end{equation}

For fixed values of \(\lambda\), \(\eta_H\), and \(\eta_V\), the unnormalized coincidence curve is

\begin{equation}
C(\vartheta)
=
P_{\mathrm{coinc}}(\vartheta).
\end{equation}

The plotted normalized coincidence is

\begin{equation}
\label{eq:dashboard_normalized_coincidence}
C_{\mathrm{norm}}(\vartheta)
=
\frac{C(\vartheta)}{C_{\max}},
\end{equation}

where

\begin{equation}
C_{\max}
=
\max_{\vartheta \in [0,\pi/4]} C(\vartheta).
\end{equation}

Thus, the largest value of the displayed curve is always equal to one. This makes it easier to compare the shape of the coincidence dip for different values of \(\lambda\), \(\eta_H\), and \(\eta_V\).

The visibility shown in the dashboard quantifies the relative depth of the coincidence modulation. It is computed from the unnormalized coincidence curve as

\begin{equation}
\label{eq:dashboard_visibility}
V
=
\frac{C_{\max}-C_{\min}}{C_{\max}+C_{\min}},
\end{equation}

with

\begin{equation}
C_{\min}
=
\min_{\vartheta \in [0,\pi/4]} C(\vartheta).
\end{equation}

A larger visibility therefore corresponds to a deeper coincidence dip, while \(V=0\) would correspond to a flat coincidence curve.