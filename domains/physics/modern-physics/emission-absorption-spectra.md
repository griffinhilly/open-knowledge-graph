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
stage: formal-systems
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

## Explainer

You know from the electromagnetic spectrum that light is a wave with energy related to frequency. But classical physics had a deep problem: it predicted that a hot gas of atoms should radiate at every frequency, smoothly and continuously. Instead, experiments showed that each element emits and absorbs light only at a specific, discrete set of wavelengths. For hydrogen, Balmer noticed in 1885 that the visible emission lines fit a suspiciously regular pattern, and Rydberg showed the formula 1/λ = R_H(1/n₁² − 1/n₂²) with integers n₁ and n₂. Classical physics had no explanation for why integers would appear in an optical formula.

The discreteness is the crucial clue: atoms must have discrete internal energy states. When an atom has excess energy (for example, in a hot gas or after electron collision), it can release that energy by emitting a photon. You know from the electromagnetic spectrum that light comes in photon packets with energy E = hf = hc/λ. The photon's energy must exactly match the difference between two allowed energy levels of the atom: ΔE = hc/λ. Only those photon wavelengths exist for which the energy difference matches a real pair of levels. The **emission spectrum** is a bright-line spectrum: sharp bright lines against a dark background, each line corresponding to one possible energy-level transition.

**Absorption spectra** are the same physics running backward. Send a continuous spectrum of white light through a cool gas. Photons of exactly the right energy to bump the atom from a lower to a higher energy level get absorbed; all other photons pass through unaffected. The transmitted light shows a continuous spectrum with dark gaps — **Fraunhofer lines** — at precisely the wavelengths that were emitted by hot atoms of the same element. The gap wavelengths are identical to the emission line wavelengths, which is why you can identify the composition of the sun and distant stars by matching the dark absorption lines in sunlight to laboratory emission spectra. This spectroscopic fingerprinting is the foundation of all remote composition analysis in astronomy.

The Rydberg formula's integers n₁ and n₂ are the quantum numbers labeling the energy levels. The Balmer series (visible, n₁ = 2) corresponds to transitions falling into the second energy level from higher ones. The Lyman series (ultraviolet, n₁ = 1) falls into the ground state; the Paschen series (infrared, n₁ = 3) falls into the third level. The same integer pattern that Rydberg observed empirically will be derived from first principles when you study the Bohr model — and the fact that the formula works so precisely is strong evidence that the energy levels are genuinely quantized. The failure of classical physics to explain discrete spectra was one of the central motivations for developing quantum theory.
