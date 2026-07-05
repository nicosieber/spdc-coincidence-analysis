# Visibility

<iframe
  src="../assets/plots/visibility_vs_etaH_plot.html"
  width="100%"
  height="600"
  style="border:0;"
  loading="lazy">
</iframe>

The visibility quantifies the relative depth of the coincidence modulation. It is computed
from the unnormalized coincidence curve
\(C(\vartheta)=P_{\mathrm{coinc}}(\vartheta)\) as

\begin{equation}
\label{eq:visibility_def}
V
=
\frac{C_{\max}-C_{\min}}{C_{\max}+C_{\min}},
\end{equation}

with

\begin{equation}
C_{\max}=\max_{\vartheta \in [0,\pi/4]} C(\vartheta),
\qquad
C_{\min}=\min_{\vartheta \in [0,\pi/4]} C(\vartheta).
\end{equation}

For the half-wave-plate-rotated TMSV the extremes sit at fixed angles: the coincidence
curve peaks at \(\vartheta=0\) and dips at \(\vartheta=\pi/8\). A larger visibility therefore
corresponds to a deeper coincidence dip, while \(V=0\) would correspond to a flat
coincidence curve.

## The ideal ceiling

In the loss-free limit \(\eta_H=\eta_V\to 1\) the visibility reduces to a function of the
squeezing parameter alone,

\begin{equation}
\label{eq:visibility_ideal}
V_{\mathrm{ideal}}(\lambda)=\sqrt{1-\lambda^2},
\end{equation}

which is the ceiling any real measurement approaches from below. It is set by the same
multi-pair statistics that limit the coincidence contrast: the mean pair number per mode is

\begin{equation}
\bar n(\lambda)=\frac{\lambda^2}{1-\lambda^2},
\end{equation}

so as \(\lambda\) grows the source emits more multi-pair events, which fill in the
coincidence dip and pull the visibility down. Weak squeezing gives near-unit visibility at
the cost of count rate; strong squeezing gives high count rate at the cost of contrast. For
orientation, at \(\lambda=0.5\) (\(\bar n\approx0.33\) pairs/mode) the best achievable
visibility is already \(0.87\).

!!! note "Loss costs statistics, asymmetry costs neither"
    At fixed *mean* efficiency, making the two arms unequal leaves the visibility almost
    untouched. Scanning the loss imbalance \(\delta=(\eta_H-\eta_V)/2\) from \(0\) to
    \(0.29\) at fixed \(\bar\eta\) scales the *entire* coincidence curve down — fewer
    counts — but holds the visibility essentially constant at \(V\approx0.809\). Detector
    imbalance costs statistics, not contrast; it is the squeezing \(\lambda\), through the
    ceiling \(\sqrt{1-\lambda^2}\), that sets how deep the dip can be.
