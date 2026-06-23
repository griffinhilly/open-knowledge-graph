---
id: vibrational-overtones-and-transitions
title: Vibrational Overtones and Hot Bands
domain: chemistry
course: physical-chemistry
prerequisites:
- id: vibrational-spectroscopy-theory
  type: hard
- id: harmonic-oscillator-molecular-vibrations
  type: hard
tags:
- spectroscopy
- vibration
- overtones
- fine-structure
stage: advanced
status: validated
---

# Vibrational Overtones and Hot Bands

## Core Idea
Beyond the fundamental v=0→1 transition, vibrational spectroscopy includes overtones (v=0→2, 0→3, etc.) and hot bands (v=1→2, etc.) with successively lower intensities. These arise from anharmonicity of the potential and non-zero population of excited vibrational states at thermal equilibrium. Combination bands and difference bands add further complexity, requiring detailed analysis for structure determination.

## How It's Best Learned
Measure IR or Raman spectra of polyatomic molecules (CO₂, H₂O) and assign overtones and combination bands; fit spectral data to anharmonic oscillator models with Morse or polynomial potentials; calculate hot-band intensities and verify against temperature-dependent spectra.

## Common Misconceptions
- Assuming only the fundamental transition appears in IR; overtones and hot bands can dominate in strong absorbers like CO or OH. - Treating all overtones as equally probable; selection rules and Franck-Condon factors make higher overtones increasingly weak.

## Questions

```yaml
- question: "A chemist observes a weak IR absorption at approximately 3400 cm⁻¹ — close to, but slightly below, twice the frequency of the fundamental O-H stretch at 3700 cm⁻¹. What is this peak, and what physical phenomenon causes it?"
  type: multiple-choice
  options:
    - "A hot band from the v=1→2 transition, caused by thermal population of the v=1 O-H state at room temperature"
    - "The first overtone of the O-H stretch, appearing at slightly less than 2×3700 cm⁻¹ because anharmonicity causes vibrational energy levels to converge rather than remaining evenly spaced"
    - "A combination band arising from simultaneous excitation of two O-H bending modes near 1700 cm⁻¹ each"
    - "An instrumental artifact from detector nonlinearity at high absorbance values"
  answer: 1
  explanation: "This is the first overtone — the v=0→2 transition. In an anharmonic oscillator, the Δv=±1 selection rule relaxes and Δv=±2 becomes weakly allowed. Crucially, anharmonicity also makes energy levels converge: the gap between v=1 and v=2 is slightly smaller than between v=0 and v=1. So the first overtone appears at slightly less than exactly 2×ν, not exactly 2×ν. The hot band (v=1→2) would also appear below the fundamental, but it requires the v=1 state to be populated, and it would shift with temperature — the overtone is present regardless of temperature."

- question: "A spectroscopist measures an IR spectrum of a diatomic gas at room temperature and then at 100 K. A certain weak absorption slightly below the fundamental frequency disappears at 100 K. What type of transition is this, and why does it disappear?"
  type: multiple-choice
  options:
    - "An overtone transition — at low temperatures, molecules lack the energy needed to jump two vibrational quanta at once"
    - "A hot band (e.g., v=1→2) — at 100 K, very few molecules occupy the v=1 level, so almost none can make this transition"
    - "A combination band — low temperatures prevent two different modes from being simultaneously active"
    - "The fundamental transition itself — it shifts to a lower frequency at low temperature, moving away from its usual position"
  answer: 1
  explanation: "Hot bands arise from thermally populated excited states: molecules already in v=1 absorb to reach v=2. The v=1 population follows the Boltzmann distribution — at room temperature there is a small but measurable population, but at 100 K (much less than the vibrational temperature for most bonds), almost all molecules are in v=0. With no molecules in v=1, the hot band disappears. This temperature dependence is the defining diagnostic for hot bands. Overtones originate from v=0 (which is always the most populated level), so their intensity does not depend on temperature in the same way."

- question: "Vibrational overtones occur because the harmonic oscillator selection rule (Δv = ±1) breaks down in real molecules whose potential energy is anharmonic, allowing Δv = ±2, ±3, and higher transitions."
  type: true-false
  answer: true
  explanation: "This is exactly correct. The Δv = ±1 rule is a consequence of the harmonic oscillator wavefunction mathematics — the transition dipole moment integrals vanish for Δv ≠ ±1 in a perfect harmonic potential. Anharmonicity (the deviation of the real potential from a perfect parabola, well-described by a Morse potential) mixes wavefunctions from adjacent levels, giving non-zero transition dipole moments for Δv = ±2, ±3, etc. The overtones are intrinsically weaker than the fundamental because the mixing is small, and higher overtones are weaker still."

- question: "A hot band and the first overtone for the same vibrational mode appear at the same frequency in the IR spectrum because they both involve the same energy gap between adjacent vibrational levels."
  type: true-false
  answer: false
  explanation: "They appear at different frequencies. The first overtone is the v=0→2 transition, which spans two level spacings — at an anharmonic frequency slightly less than 2ν. The hot band is the v=1→2 transition, which spans one level spacing — but a smaller one than v=0→1, because anharmonic level spacings decrease with increasing v. So the hot band appears at a frequency slightly LOWER than the fundamental (not at the same frequency as the overtone). The fundamental, hot band, and overtone all appear at distinct positions in the spectrum."

- question: "What is the key experimental observation that allows you to distinguish a hot band from an overtone in a vibrational spectrum, and why does that observation work?"
  type: short-answer
  answer: "Temperature dependence. Hot bands strengthen as temperature increases and weaken as temperature decreases (eventually disappearing at very low temperatures). Overtones show no such intensity change with temperature. This works because hot bands require molecules to already be in an excited vibrational state (e.g., v=1) before they can absorb; the population of that excited state follows the Boltzmann distribution and is therefore temperature-sensitive. Overtones originate from v=0, which is always the dominant population regardless of temperature, so their intensity is relatively temperature-insensitive."
  explanation: "This is the diagnostic: if you cool the sample and a weak band disappears (or heat it and the band grows), it is a hot band. If a weak band shows no intensity change with temperature, it is an overtone or combination band. In practice, variable-temperature spectroscopy is a standard technique for assigning ambiguous features in complex molecular spectra."
```

## Explainer

From your study of the harmonic oscillator model of molecular vibrations, you know that energy levels are evenly spaced (Eₙ = (n + ½)hν) and the selection rule Δv = ±1 permits only **fundamental transitions** — the v = 0 → 1 absorption that produces the characteristic IR peak for each vibrational mode. If molecules were truly harmonic, that would be the entire story. But real molecular bonds are not perfect springs: at large displacements, the potential energy curve flattens as the bond approaches dissociation rather than climbing parabolically to infinity. This **anharmonicity** changes both the energy spacing and the selection rules, opening the door to a richer set of transitions.

In an anharmonic oscillator (well-described by a **Morse potential**), energy levels are no longer evenly spaced — they converge as v increases, with the spacing decreasing by roughly 2χₑν per quantum number, where χₑ is the anharmonicity constant. More importantly, the strict Δv = ±1 selection rule relaxes. Transitions with Δv = 2, 3, and higher become weakly allowed. The v = 0 → 2 transition is called the **first overtone**, v = 0 → 3 the **second overtone**, and so on. Each successive overtone is roughly an order of magnitude weaker than the previous one, but they are readily observable in high-sensitivity measurements and appear at frequencies slightly less than 2ν, 3ν, etc. (less than exact multiples because of the converging level spacing).

**Hot bands** arise from a different mechanism: thermal population of excited vibrational states. At room temperature, the Boltzmann distribution places a small but measurable fraction of molecules in v = 1, and these molecules can absorb to reach v = 2. This v = 1 → 2 transition appears at a slightly lower frequency than the fundamental because the anharmonic level spacing decreases with v. Hot bands grow stronger with increasing temperature (as more molecules populate v = 1) and weaker at low temperatures, providing a useful experimental handle for distinguishing them from overtones, which are temperature-independent in their frequency positions.

**Combination bands** and **difference bands** add further complexity in polyatomic molecules. A combination band corresponds to simultaneous excitation of two different vibrational modes (νA + νB), while a difference band involves one mode gaining a quantum while another loses one (νA − νB). These are important in molecules like CO₂, where some modes are IR-inactive as fundamentals but can appear through combination with other modes. Assigning overtones, hot bands, and combination bands in a real spectrum requires fitting the observed frequencies to an anharmonic model, and the pattern of deviations from harmonic predictions directly reveals the shape of the potential energy surface near the bottom of the well. This analysis connects spectroscopic observables back to the fundamental forces holding molecules together.
