# SPDC Coincidence Analysis

This repository contains tools and code (coming soon) for analyzing coincidence measurements in **Spontaneous Parametric Down-Conversion (SPDC)** experiments.

👉 **Live demo / website:**  
https://nicosieber.github.io/spdc-coincidence-analysis/

---

## Overview

Photon-pair sources based on type-II spontaneous parametric down-conversion (SPDC) are a standard platform for studying nonclassical light and polarization interference. In the degenerate regime, and under appropriate phase-matching and mode-overlap conditions, the emitted state is well described as a two-mode squeezed vacuum (TMSV) in the horizontal and vertical polarization modes.

When this state is processed through polarization optics (e.g., a half-wave plate) and measured using non-photon-number-resolving (bucket) detectors, the experimentally accessible quantities are typically coincidence probabilities rather than full photon-number statistics. In many practical approaches, these probabilities are approximated by truncating the TMSV expansion to low photon numbers. While valid in the weak-pumping regime, such approximations break down when higher-order pair contributions become relevant.

This project presents an exact analytical framework for computing coincidence probabilities in such setups. The approach combines:

- The transformation of the TMSV state under polarization optics  
- A Positive Operator-Valued Measure (POVM) description of lossy bucket detectors  

This allows all photon-number contributions to be included exactly, while detector inefficiencies are incorporated through mode-dependent efficiencies. The resulting formalism yields compact analytical expressions for vacuum probabilities and, consequently, for the coincidence probability itself.

---

## Features

- 📊 Exact analytical treatment of SPDC coincidence probabilities  
- 🔬 Includes full TMSV photon-number contributions (no truncation)  
- ⚙️ Incorporates detector efficiency via POVM formalism  
- ⚡ Automatic deployment via GitHub Actions  

---

## Use Cases

- Quantum optics experiments  
- SPDC photon coincidence measurements  
- Educational demonstrations of nonclassical light  

---

## Contributing

Contributions are welcome! If you’d like to improve the project:

- Fork the repository  
- Create a feature branch  
- Submit a pull request  

---

## Feedback & Improvements

I’m always open to feedback, suggestions, and bug reports.

If you notice:
- errors  
- unclear documentation  
- potential improvements  

please feel free to open an issue or reach out.

---

## Author

**Nico Sieber**  
🔗 LinkedIn: https://www.linkedin.com/in/nico-sieber-0a7204156/