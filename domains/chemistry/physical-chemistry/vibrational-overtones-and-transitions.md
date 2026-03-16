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
builds-toward:
- two-dimensional-nmr-spectroscopy
tags:
- spectroscopy
- vibration
- overtones
- fine-structure
stage: advanced
status: draft
---

# Vibrational Overtones and Hot Bands

## Core Idea
Beyond the fundamental v=0→1 transition, vibrational spectroscopy includes overtones (v=0→2, 0→3, etc.) and hot bands (v=1→2, etc.) with successively lower intensities. These arise from anharmonicity of the potential and non-zero population of excited vibrational states at thermal equilibrium. Combination bands and difference bands add further complexity, requiring detailed analysis for structure determination.

## How It's Best Learned
Measure IR or Raman spectra of polyatomic molecules (CO₂, H₂O) and assign overtones and combination bands; fit spectral data to anharmonic oscillator models with Morse or polynomial potentials; calculate hot-band intensities and verify against temperature-dependent spectra.

## Common Misconceptions
- Assuming only the fundamental transition appears in IR; overtones and hot bands can dominate in strong absorbers like CO or OH. - Treating all overtones as equally probable; selection rules and Franck-Condon factors make higher overtones increasingly weak.

## Explainer

From your study of the harmonic oscillator model of molecular vibrations, you know that energy levels are evenly spaced (Eₙ = (n + ½)hν) and the selection rule Δv = ±1 permits only **fundamental transitions** — the v = 0 → 1 absorption that produces the characteristic IR peak for each vibrational mode. If molecules were truly harmonic, that would be the entire story. But real molecular bonds are not perfect springs: at large displacements, the potential energy curve flattens as the bond approaches dissociation rather than climbing parabolically to infinity. This **anharmonicity** changes both the energy spacing and the selection rules, opening the door to a richer set of transitions.

In an anharmonic oscillator (well-described by a **Morse potential**), energy levels are no longer evenly spaced — they converge as v increases, with the spacing decreasing by roughly 2χₑν per quantum number, where χₑ is the anharmonicity constant. More importantly, the strict Δv = ±1 selection rule relaxes. Transitions with Δv = 2, 3, and higher become weakly allowed. The v = 0 → 2 transition is called the **first overtone**, v = 0 → 3 the **second overtone**, and so on. Each successive overtone is roughly an order of magnitude weaker than the previous one, but they are readily observable in high-sensitivity measurements and appear at frequencies slightly less than 2ν, 3ν, etc. (less than exact multiples because of the converging level spacing).

**Hot bands** arise from a different mechanism: thermal population of excited vibrational states. At room temperature, the Boltzmann distribution places a small but measurable fraction of molecules in v = 1, and these molecules can absorb to reach v = 2. This v = 1 → 2 transition appears at a slightly lower frequency than the fundamental because the anharmonic level spacing decreases with v. Hot bands grow stronger with increasing temperature (as more molecules populate v = 1) and weaker at low temperatures, providing a useful experimental handle for distinguishing them from overtones, which are temperature-independent in their frequency positions.

**Combination bands** and **difference bands** add further complexity in polyatomic molecules. A combination band corresponds to simultaneous excitation of two different vibrational modes (νA + νB), while a difference band involves one mode gaining a quantum while another loses one (νA − νB). These are important in molecules like CO₂, where some modes are IR-inactive as fundamentals but can appear through combination with other modes. Assigning overtones, hot bands, and combination bands in a real spectrum requires fitting the observed frequencies to an anharmonic model, and the pattern of deviations from harmonic predictions directly reveals the shape of the potential energy surface near the bottom of the well. This analysis connects spectroscopic observables back to the fundamental forces holding molecules together.
