---
id: energy-level-transitions
title: Quantized Energy Levels and Spectroscopic Transitions
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
builds-toward:
- fluorescence-and-phosphorescence-theory
tags:
- energy-levels
- absorption
- emission
- Boltzmann-population
- line-spectra
- quantization
stage: advanced
status: draft
---

# Quantized Energy Levels and Spectroscopic Transitions

## Core Idea
Quantum mechanics restricts atoms and molecules to discrete energy levels, and transitions between these levels occur by absorption or emission of photons with energy exactly matching the level spacing: Delta-E = h*nu. The Boltzmann distribution governs the population of each level at thermal equilibrium: N_i/N_0 = (g_i/g_0)*exp(-Delta-E_i/k_BT), where g_i is the degeneracy. This population distribution determines which transitions are observable -- absorption requires significant ground-state population, while emission requires population inversion or thermal excitation. Line spectra arise because the allowed energies are discrete; the pattern of lines encodes the energy-level structure and therefore the identity and bonding of the species.

## How It's Best Learned
Calculate energy-level spacings and Boltzmann populations for a simple system (e.g., rotational levels of CO or electronic levels of hydrogen) at different temperatures. Then connect these populations to the relative intensities of spectral lines, seeing how temperature controls which transitions dominate.

## Common Misconceptions
- Assuming all energy levels are equally populated; Boltzmann weighting means higher levels are exponentially less populated unless the spacing is much smaller than k_BT.
- Believing every possible transition is observed; selection rules (Delta-J, Delta-l, spin conservation) restrict which transitions actually occur with appreciable probability.

## Questions

```yaml
- question: "A molecule has two energy levels separated by 0.025 eV (approximately k_BT at room temperature). At room temperature, what can you say about the populations of these two levels?"
  type: multiple-choice
  options:
    - "The upper level is essentially unpopulated — thermal energy is never enough to populate excited states"
    - "The upper level is significantly populated; with ΔE ≈ k_BT, the Boltzmann factor exp(−ΔE/k_BT) ≈ e⁻¹ ≈ 0.37, so the upper level has about 37% of the ground-state population"
    - "Both levels are equally populated — when ΔE equals k_BT, the levels are exactly equal"
    - "The upper level is more populated — thermal energy pushes electrons upward"
  answer: 1
  explanation: "The Boltzmann factor exp(−ΔE/k_BT) gives the ratio of upper to lower state population (ignoring degeneracy). When ΔE = k_BT, this factor is e⁻¹ ≈ 0.37, meaning the upper level has ~37% of the lower level's population — significantly populated. This is typical for rotational levels of small molecules at room temperature. Electronic levels (ΔE ~ eV >> k_BT) have Boltzmann factors of ~10⁻¹⁷ and are essentially unpopulated, which is why electronic absorption spectra show only ground-state transitions."

- question: "A spectroscopist observes that two energy levels exist in a molecule — confirmed by calculations — but she cannot observe any spectral line connecting them. Which explanation is most likely correct?"
  type: multiple-choice
  options:
    - "The levels are too close together for any spectrometer to resolve"
    - "The transition violates a selection rule, making the transition dipole moment zero or near-zero and the transition essentially 'dark'"
    - "The upper level is unpopulated because no photons at that frequency are present in the spectrometer"
    - "The transition can only be observed at very low temperatures when Boltzmann populations shift"
  answer: 1
  explanation: "Selection rules arise from the quantum-mechanical requirement that the transition dipole moment integral ∫ψ*_f μ ψ_i dτ be nonzero. If the wavefunctions have the wrong symmetry or angular momentum properties, this integral evaluates to zero — the transition is 'forbidden' and produces no (or a very weak) spectral line. Common examples: Δl = ±1 for electronic transitions in atoms; ΔJ = ±1 for rotational transitions; the symmetry selection rule for IR vs. Raman activity. The levels exist; the transition just has negligible probability."

- question: "Atomic line spectra appear as sharp, discrete lines rather than continuous bands because transitions between discrete energy levels produce photons of only specific frequencies."
  type: true-false
  answer: true
  explanation: "Each spectral line corresponds to one transition between two specific energy levels: ΔE = hν. Since the energy levels are discrete (quantized), the allowed ΔE values are a specific set — not a continuum. Each ΔE produces photons at one frequency ν = ΔE/h. The pattern of line positions is a unique fingerprint of the atom's energy-level structure. Continuous spectra arise from different sources: blackbody radiation, bremsstrahlung, or transitions to or from a continuum of states (ionization)."

- question: "If you heat a gas to a higher temperature, all rotational spectral lines become equally more intense because more molecules have energy to undergo transitions."
  type: true-false
  answer: false
  explanation: "Heating changes the *distribution* of population across levels, not all lines equally. At higher temperature, the Boltzmann distribution spreads population over more rotational levels (since kT is larger). Lines from low-J states weaken as population migrates to higher J levels; lines from intermediate-J transitions strengthen; and lines from very high J states appear. The envelope of line intensities shifts to higher J. For vibrational or electronic transitions (where ΔE >> kT), higher temperature still primarily populates the ground state and barely affects those line intensities."

- question: "Explain why rotational spectra of molecules have many observable lines while electronic spectra of atoms at room temperature show only absorption from the ground state."
  type: short-answer
  answer: "Rotational energy spacings (microwave region, ~0.001 eV) are much smaller than k_BT at room temperature (~0.025 eV). The Boltzmann factor exp(−ΔE/k_BT) is close to 1 for low J levels, so many rotational levels are significantly populated, and absorption from multiple levels produces many lines. Electronic energy spacings in atoms (UV/visible, ~2–10 eV) are far larger than k_BT. The Boltzmann factor exp(−E/k_BT) is ~10⁻³⁴ to 10⁻¹⁷ for excited electronic states — essentially zero. All population is in the ground state, so only ground-state absorption is observed."
  explanation: "This is why rotational spectroscopy produces rich spectra with hundreds of lines from a single molecule, while atomic emission spectroscopy requires high-temperature sources (flames, electrical discharges) to populate excited electronic states before emission can occur. The Boltzmann distribution is the bridge between the quantum energy ladder and what you actually see in the spectrometer."
```

## Explainer

Quantum mechanics tells you that atoms and molecules cannot have just any amount of energy — they are restricted to specific, discrete **energy levels**, like rungs on a ladder rather than points on a ramp. This is a direct consequence of the wave nature of particles: just as a guitar string can only vibrate at certain frequencies (its harmonics), an electron bound in an atom can only occupy certain energy states. The spacing between these levels depends on the system: electronic levels in atoms are typically separated by electron-volts (visible and UV light), vibrational levels in molecules by tenths of electron-volts (infrared), and rotational levels by thousandths of electron-volts (microwave).

A transition between two levels occurs when the system absorbs or emits a photon whose energy exactly matches the gap: **ΔE = hν**, where h is Planck's constant and ν is the photon frequency. This is why atomic spectra consist of sharp lines rather than continuous bands — each line corresponds to one specific transition between two specific levels. The pattern of lines is a fingerprint of the atom or molecule, encoding its entire energy-level structure. Hydrogen's Balmer series, the sodium doublet, and the rotational spectrum of carbon monoxide are all direct readouts of quantum-mechanical energy ladders.

Not all transitions are equally likely, and some are essentially forbidden. **Selection rules** — derived from the mathematical requirement that the transition dipole moment integral be nonzero — dictate which transitions produce strong spectral lines. For example, in a one-electron atom, the orbital angular momentum quantum number must change by exactly ±1 (Δl = ±1), and spin must be conserved. These rules explain why some gaps in the energy ladder never produce observable lines, even though the energy levels exist. The intensity of an allowed transition depends on two factors: the intrinsic probability of the transition (the transition dipole moment) and how many molecules are in the initial state.

This is where the **Boltzmann distribution** enters. At thermal equilibrium, the population of each energy level follows N_i ∝ g_i·exp(−E_i/k_BT), where g_i is the degeneracy (number of states at that energy) and k_BT sets the thermal energy scale. At room temperature, k_BT ≈ 0.025 eV, which means electronic excited states (gaps of several eV) are essentially unpopulated — you only see absorption from the ground state. Rotational levels, with spacings much smaller than k_BT, are thermally populated across many levels, producing rich spectra with many lines whose intensities rise, peak, and fall as the Boltzmann factor and degeneracy compete. Understanding these population effects lets you predict not just which lines appear, but their relative strengths — connecting quantum mechanics directly to what you observe in the spectrometer.
