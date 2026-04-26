# SPDC Coincidence Analysis
<div class="home-hero">
  <div class="home-hero__content">
    <p class="home-hero__eyebrow">Introduction</p>
    <p class="home-hero__subtitle">
      Photon-pair sources based on type-II spontaneous parametric down-conversion (SPDC) are a standard platform for studying nonclassical light and polarization interference. In the degenerate regime, and under appropriate phase-matching and mode-overlap conditions, the emitted state is well described as a two-mode squeezed vacuum (TMSV) in the horizontal and vertical polarization modes. When this state is sent through polarization optics and measured with non-photon-number-resolving detectors, the experimentally relevant quantities are typically coincidence probabilities rather than resolved photon-number statistics.
      In many practical analyses, coincidence probabilities for such setups are estimated by truncating the TMSV expansion to the lowest few photon-number terms. While this can be sufficient in the weak-pumping regime, it does not provide an exact description of the full state. This limitation becomes especially relevant when higher-order pair contributions are non-negligible or when one wishes to retain a fully analytical treatment in the presence of loss.
      Here I present the derivation of an exact analytical expression for the coincidence probability of a type-II SPDC-generated TMSV state after a half-wave plate (HWP) and subsequent polarization-resolved detection with bucket detectors. 
      My approach adds the Positive Operator-Valued Measure (POVM) description of lossy bucket detectors to the TMSV state transformed by the HWP. This way, all photon-number contributions are included exactly, and detector loss can be incorporated through mode-dependent efficiencies. The resulting formalism yields compact expressions for the vacuum probabilities entering the coincidence signal and therefore for the coincidence probability itself.
    </p>
    <!-- 
    <div class="home-hero__actions">
      <a class="md-button md-button--primary" href="theory/experimental_setup/">Read the theory</a>
      <a class="md-button" href="https://github.com/nicosieber/spdc-coincidence-analysis">GitHub</a>
    </div>
    -->
  </div>
</div>

## Sections

<div class="tile-grid">
  <a class="tile" href="theory/experimental_setup/">
    <div class="tile__icon">📘</div>
    <h3>Main derivation</h3>
    <p>Introduction, notation, physical setup, and the structure of the derivation.</p>
  </a>

  <a class="tile" href="concepts_and_foundations/overview/">
    <div class="tile__icon">🧮</div>
    <h3>Additional concepts, identities and derivations</h3>
    <p>Detailed derivation of identities used for the main derivation.</p>
  </a>

  <a class="tile tile--disabled" href="javascript:void(0);" aria-disabled="true">
    <div class="tile__icon">📓</div>
    <h3>Notebooks</h3>
    <p>Numerical checks, examples, and interactive computational support. Coming soon.</p>
  </a>
</div>