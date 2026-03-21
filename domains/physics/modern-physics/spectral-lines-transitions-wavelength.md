---
id: spectral-lines-transitions-wavelength
title: Spectral Lines and Energy Transitions
domain: physics
course: modern-physics
prerequisites:
- id: hydrogen-quantum-mechanics
  type: hard
- id: hydrogen-atom-spectrum
  type: soft
builds-toward:
- atomic-selection-rules
tags:
- quantum
- spectroscopy
- atoms
stage: advanced
status: draft
---

# Spectral Lines and Energy Transitions

## Core Idea
Transitions between energy levels emit or absorb photons with frequency f = ΔE/h. For hydrogen, wavelengths are given by 1/λ = R(1/n₁² − 1/n₂²) (Rydberg formula). Each series (Lyman, Balmer, Paschen) corresponds to transitions ending on a specific level. Spectral analysis reveals atomic energy level structure directly.

## Questions

```yaml
- question: "Why do atoms emit light at discrete wavelengths rather than a continuous spectrum?"
  type: multiple-choice
  options:
    - "Electrons move in discrete circular orbits, so their orbital speeds take only discrete values"
    - "Atomic energy levels are discrete, so transitions between levels release photons with exactly quantized energies ΔE = hf, corresponding to specific wavelengths"
    - "The Rydberg formula restricts wavelengths by an empirical rule that happens to give discrete values"
    - "Electrons only emit photons when they collide with other atoms, and collision energies are quantized"
  answer: 1
  explanation: "The discreteness of spectral lines follows directly from the discreteness of energy levels. An electron transitioning from level n₂ to level n₁ releases exactly ΔE = E_{n₂} − E_{n₁} as a photon. Since ΔE = hf = hc/λ, each specific pair of levels produces a specific wavelength — no other wavelength is possible. Option A describes an older (Bohr) picture that is not the full quantum explanation. Option C reverses the logic: the Rydberg formula is a consequence of quantized energy levels, not an independent empirical constraint."

- question: "A cool hydrogen gas cloud sits between an observer and a hot, bright star emitting a continuous spectrum. What does the observer see?"
  type: multiple-choice
  options:
    - "Bright emission lines at Lyman-series wavelengths superimposed on the continuous spectrum"
    - "A continuous spectrum with no features — cold gas is transparent to all wavelengths"
    - "A continuous spectrum with dark absorption lines at Lyman-series wavelengths, because ground-state electrons absorb photons matching those transitions"
    - "A continuous spectrum with dark lines at Balmer-series wavelengths, because the visible photons are selectively absorbed"
  answer: 2
  explanation: "At normal temperatures, nearly all hydrogen atoms are in the ground state (n = 1). Photons that match Lyman-series energies (transitions from n = 1 to higher levels) are absorbed, producing dark absorption lines in the continuous stellar spectrum. The Balmer series (n = 1 → n = 2 transitions) would only be absorbed by atoms already in n = 2, which is negligible at room temperature — so Balmer absorption requires hot gas. The key principle: absorption lines appear at exactly the same wavelengths as emission lines for the same transitions."

- question: "The Balmer series of hydrogen spectral lines falls in the ultraviolet, because transitions to n = 2 involve large energy differences that produce high-frequency photons."
  type: true-false
  answer: false
  explanation: "The Balmer series (transitions ending on n₁ = 2) falls in the VISIBLE range — this is why hydrogen appears reddish in emission nebulae (the Hα line at 656 nm) and why Balmer lines were the first hydrogen series discovered (visible to the naked eye). The LYMAN series (transitions to n₁ = 1, the ground state) falls in the ultraviolet, because the ground state sits so far below higher levels that those transitions carry more energy. The Paschen series (n₁ = 3) and higher fall in the infrared."

- question: "The same set of wavelengths that appear as dark absorption lines in a cool hydrogen gas also appear as bright emission lines in hot hydrogen gas, because the relevant energy differences are the same regardless of transition direction."
  type: true-false
  answer: true
  explanation: "Absorption and emission are mirror processes: the same pair of energy levels (say n = 1 and n = 3) is involved whether a photon is absorbed (electron jumps up) or emitted (electron falls down). The photon energy — and therefore wavelength — is determined by the energy difference ΔE = |E_3 − E_1|, which is the same in both cases. This equivalence is the basis for stellar spectroscopy: astronomers identify elements in stellar atmospheres by matching dark absorption line patterns to known emission spectra of the same elements."

- question: "Explain why the Lyman, Balmer, and Paschen series each falls in a different part of the electromagnetic spectrum. What property of the transitions determines which series lands in the UV, visible, or IR?"
  type: short-answer
  answer: "Each series corresponds to transitions ending on a specific lower level n₁ (Lyman: n₁ = 1, Balmer: n₁ = 2, Paschen: n₁ = 3). The energy of the emitted photon is ΔE = 13.6 eV × (1/n₁² − 1/n₂²). The crucial factor is n₁: transitions ending on n₁ = 1 (the ground state) release the most energy, because the ground state energy (−13.6 eV) is far below the higher levels. These large energy differences correspond to high-frequency, short-wavelength photons in the UV. Transitions ending on n₁ = 2 release less energy (the reference level is higher), landing in the visible. Transitions ending on n₁ = 3 release even less energy, landing in the infrared. Within each series, lines get closer together as n₂ increases, converging at the series limit where n₂ → ∞."
  explanation: "The series structure is the most elegant feature of hydrogen spectroscopy: instead of a random collection of lines, all lines fall into families with a shared lower level. The Rydberg formula makes this explicit — grouping by n₁ groups by final energy level, and the energy of that final level sets the photon energy scale for the whole series."
```

## Explainer

From your study of the hydrogen atom, you know that electrons occupy discrete energy levels labeled by the principal quantum number n, with energies E_n = −13.6 eV / n². An electron sitting in an excited state cannot stay there indefinitely — it eventually releases the exact energy difference as a single photon. This is the origin of spectral lines: each line corresponds to one specific transition between two specific levels. Because the energy levels are discrete, the photon energies are discrete, and so the emitted or absorbed wavelengths form a precise, characteristic pattern rather than a continuous smear.

The **Rydberg formula** 1/λ = R∞(1/n₁² − 1/n₂²) is simply a reorganization of the energy difference ΔE = E_n₁ − E_n₂ combined with the photon energy relation E = hc/λ. Here R∞ = 1.097 × 10⁷ m⁻¹ is the Rydberg constant. The formula groups transitions by their final level n₁, producing distinct **spectral series**. The **Lyman series** (n₁ = 1) involves transitions to the ground state and lies in the ultraviolet — these photons are energetic because the ground state is so far below higher levels. The **Balmer series** (n₁ = 2) falls in the visible range; its first few lines give hydrogen its characteristic red, cyan, and violet emission. The **Paschen series** (n₁ = 3) and higher series fall in the infrared, where transitions carry less energy.

The physical picture is straightforward: absorption and emission are mirror images. When white light passes through cool hydrogen gas, electrons in the ground state absorb photons that exactly match Lyman-series energies, producing dark absorption lines at precisely those wavelengths. When hydrogen gas is energized (electrically or thermally), electrons are excited upward and then cascade back down, emitting bright emission lines at the same wavelengths. This duality — the same pattern appears in absorption and emission — is one of the most powerful tools in astrophysics, allowing us to identify elements in distant stars simply by matching line patterns.

What makes spectral analysis so revealing is that the pattern is a fingerprint of the atomic energy-level structure. If you observe a set of spectral lines and can identify the series they belong to, you can read off the energy differences between levels directly. Every element has a unique set of energy levels, and therefore a unique spectral signature. Hydrogen's simplicity — only one electron, allowing exact analytic solutions — made it the testing ground for quantum mechanics, and the perfect match between the Rydberg formula and the Schrödinger equation predictions was one of the key validations of the new theory.
