---
id: emission-absorption-spectra
title: Emission and Absorption Spectra
domain: physics
course: modern-physics
prerequisites:
- id: electromagnetic-spectrum
  type: hard
- id: electric-potential
  type: soft
builds-toward:
- bohr-model
tags:
- spectroscopy
- atomic
- energy-levels
- balmer-series
stage: advanced
status: validated
---

# Emission and Absorption Spectra

## Core Idea
Heated gases emit light at discrete, element-specific wavelengths (emission spectrum), while cool gases absorb the same wavelengths from a continuous background (absorption spectrum). Balmer discovered the visible hydrogen series in 1885; Rydberg generalized it with the formula 1/λ = R(1/n₁² − 1/n₂²). These discrete spectra are a fingerprint of atomic structure, but classical physics provided no explanation for why atoms emit at only certain frequencies rather than continuously.

## How It's Best Learned
Use a diffraction grating to observe actual hydrogen emission lines in lab; identify the series. Then note that the pattern implies discrete internal energy levels before introducing the Bohr model.

## Common Misconceptions
- Emission and absorption spectra for the same element have different lines — they involve the same transitions; absorption lines are dark lines at exactly the same wavelengths as bright emission lines.
- All elements produce the same spectral lines — spectra are unique to each element, which is why spectroscopy can identify composition remotely.

## Questions

```yaml
- question: "An astronomer observes a gas cloud that produces dark absorption lines in an otherwise continuous spectrum. A lab scientist heats a sample of the same element and records its emission spectrum. How do the two sets of spectral lines compare?"
  type: multiple-choice
  options:
    - "The emission lines are at longer wavelengths than the absorption lines — emission releases less energy than absorption requires"
    - "The emission lines are at shorter wavelengths — the cold gas absorbs high-energy photons that the hot gas cannot produce"
    - "The emission lines are at identical wavelengths to the absorption lines — both involve the same atomic energy-level transitions"
    - "The lines are at completely different wavelengths — emission and absorption involve different types of electron transitions"
  answer: 2
  explanation: "Emission and absorption are the same atomic transition running in opposite directions. An atom emits a photon when an electron falls from a higher to a lower energy level; it absorbs a photon of identical energy when the electron is excited from that lower level back up to the higher one. The photon energy — and therefore the wavelength — is determined by ΔE = hc/λ, which is the same for both processes. This is why dark Fraunhofer absorption lines in sunlight are at exactly the same wavelengths as the bright emission lines of the same elements in a laboratory flame."

- question: "Classical physics predicted that heated atoms should radiate light continuously across all wavelengths. Why was the discovery of discrete spectral lines such a problem for this prediction?"
  type: multiple-choice
  options:
    - "Classical physics predicted absorption but not emission, so the existence of emission lines was entirely unexpected"
    - "The Rydberg formula expressed spectral wavelengths using integer quantum numbers — discrete integers cannot emerge naturally from any continuous classical model"
    - "Classical physics predicted only metals could emit visible light when heated, so gas emission lines violated this prediction"
    - "Classical physics predicted spectral lines at the same wavelengths for all elements, so element-specific lines were anomalous"
  answer: 1
  explanation: "Classical electromagnetic theory predicted that an accelerating charge (an electron in an atom) should radiate continuously across all frequencies. Instead, each element emitted only a discrete set of wavelengths, and Rydberg's formula showed these wavelengths were governed by integer pairs (n₁, n₂). There is no way to derive integers from a continuous classical model. The discreteness was the crucial clue pointing toward quantized energy levels inside atoms — a concept entirely foreign to classical physics."

- question: "The dark Fraunhofer lines in sunlight are at exactly the same wavelengths as the bright emission lines seen when the same elements are heated in a laboratory."
  type: true-false
  answer: true
  explanation: "This identity is the foundation of spectroscopic composition analysis. A cool gas absorbs exactly the photon energies it would emit when hot, because both processes involve the same atomic energy-level transitions. The sun's outer atmosphere absorbs specific wavelengths from the continuous radiation produced by the hot interior, leaving dark gaps. Matching those gaps to laboratory emission lines identifies the elements present — allowing us to determine the chemical composition of the sun and distant stars without physically sampling them."

- question: "The Balmer series, Lyman series, and Paschen series in hydrogen involve three different types of hydrogen atoms undergoing distinct internal transitions."
  type: true-false
  answer: false
  explanation: "All three series come from the same hydrogen atom. The difference is which lower energy level the electron transitions into, not the type of atom or transition. Lyman series (UV): transitions fall to n = 1 (ground state). Balmer series (visible): transitions fall to n = 2. Paschen series (IR): transitions fall to n = 3. A single hydrogen atom can produce lines from all three series depending on which higher level it was excited to and which lower level it falls back to."

- question: "Why do discrete emission spectra — rather than continuous emission — imply that atoms have discrete internal energy levels?"
  type: short-answer
  answer: "A photon's energy is fixed by its wavelength: E = hc/λ. For an atom to emit a photon of a specific wavelength, it must release exactly that amount of energy. If atoms could exist at any energy, they could release photons of any wavelength, producing a continuous spectrum. The fact that only certain discrete wavelengths are emitted means the atom can only release certain fixed amounts of energy — which means it can only occupy certain discrete internal energy states. Each spectral line is a readout of one specific allowed energy-level transition."
  explanation: "This logic runs in both directions: discrete spectra imply discrete energy levels, and discrete energy levels predict discrete spectra. The Bohr model you will study next derives these energy levels from first principles and reproduces the Rydberg formula, confirming that the observed spectral integers n₁ and n₂ are quantum numbers labeling those levels."
```

## Explainer

You know from the electromagnetic spectrum that light is a wave with energy related to frequency. But classical physics had a deep problem: it predicted that a hot gas of atoms should radiate at every frequency, smoothly and continuously. Instead, experiments showed that each element emits and absorbs light only at a specific, discrete set of wavelengths. For hydrogen, Balmer noticed in 1885 that the visible emission lines fit a suspiciously regular pattern, and Rydberg showed the formula 1/λ = R_H(1/n₁² − 1/n₂²) with integers n₁ and n₂. Classical physics had no explanation for why integers would appear in an optical formula.

The discreteness is the crucial clue: atoms must have discrete internal energy states. When an atom has excess energy (for example, in a hot gas or after electron collision), it can release that energy by emitting a photon. You know from the electromagnetic spectrum that light comes in photon packets with energy E = hf = hc/λ. The photon's energy must exactly match the difference between two allowed energy levels of the atom: ΔE = hc/λ. Only those photon wavelengths exist for which the energy difference matches a real pair of levels. The **emission spectrum** is a bright-line spectrum: sharp bright lines against a dark background, each line corresponding to one possible energy-level transition.

**Absorption spectra** are the same physics running backward. Send a continuous spectrum of white light through a cool gas. Photons of exactly the right energy to bump the atom from a lower to a higher energy level get absorbed; all other photons pass through unaffected. The transmitted light shows a continuous spectrum with dark gaps — **Fraunhofer lines** — at precisely the wavelengths that were emitted by hot atoms of the same element. The gap wavelengths are identical to the emission line wavelengths, which is why you can identify the composition of the sun and distant stars by matching the dark absorption lines in sunlight to laboratory emission spectra. This spectroscopic fingerprinting is the foundation of all remote composition analysis in astronomy.

The Rydberg formula's integers n₁ and n₂ are the quantum numbers labeling the energy levels. The Balmer series (visible, n₁ = 2) corresponds to transitions falling into the second energy level from higher ones. The Lyman series (ultraviolet, n₁ = 1) falls into the ground state; the Paschen series (infrared, n₁ = 3) falls into the third level. The same integer pattern that Rydberg observed empirically will be derived from first principles when you study the Bohr model — and the fact that the formula works so precisely is strong evidence that the energy levels are genuinely quantized. The failure of classical physics to explain discrete spectra was one of the central motivations for developing quantum theory.
