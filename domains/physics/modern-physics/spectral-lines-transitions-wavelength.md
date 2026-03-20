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

## Explainer

From your study of the hydrogen atom, you know that electrons occupy discrete energy levels labeled by the principal quantum number n, with energies E_n = −13.6 eV / n². An electron sitting in an excited state cannot stay there indefinitely — it eventually releases the exact energy difference as a single photon. This is the origin of spectral lines: each line corresponds to one specific transition between two specific levels. Because the energy levels are discrete, the photon energies are discrete, and so the emitted or absorbed wavelengths form a precise, characteristic pattern rather than a continuous smear.

The **Rydberg formula** 1/λ = R∞(1/n₁² − 1/n₂²) is simply a reorganization of the energy difference ΔE = E_n₁ − E_n₂ combined with the photon energy relation E = hc/λ. Here R∞ = 1.097 × 10⁷ m⁻¹ is the Rydberg constant. The formula groups transitions by their final level n₁, producing distinct **spectral series**. The **Lyman series** (n₁ = 1) involves transitions to the ground state and lies in the ultraviolet — these photons are energetic because the ground state is so far below higher levels. The **Balmer series** (n₁ = 2) falls in the visible range; its first few lines give hydrogen its characteristic red, cyan, and violet emission. The **Paschen series** (n₁ = 3) and higher series fall in the infrared, where transitions carry less energy.

The physical picture is straightforward: absorption and emission are mirror images. When white light passes through cool hydrogen gas, electrons in the ground state absorb photons that exactly match Lyman-series energies, producing dark absorption lines at precisely those wavelengths. When hydrogen gas is energized (electrically or thermally), electrons are excited upward and then cascade back down, emitting bright emission lines at the same wavelengths. This duality — the same pattern appears in absorption and emission — is one of the most powerful tools in astrophysics, allowing us to identify elements in distant stars simply by matching line patterns.

What makes spectral analysis so revealing is that the pattern is a fingerprint of the atomic energy-level structure. If you observe a set of spectral lines and can identify the series they belong to, you can read off the energy differences between levels directly. Every element has a unique set of energy levels, and therefore a unique spectral signature. Hydrogen's simplicity — only one electron, allowing exact analytic solutions — made it the testing ground for quantum mechanics, and the perfect match between the Rydberg formula and the Schrödinger equation predictions was one of the key validations of the new theory.
