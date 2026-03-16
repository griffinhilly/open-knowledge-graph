---
id: rydberg-constant-spectroscopic-formula
title: Rydberg Constant and Spectroscopic Line Formula
domain: physics
course: modern-physics
prerequisites:
- id: bohr-model
  type: hard
- id: hydrogen-atom-spectrum
  type: hard
tags:
- atomic-physics
- spectroscopy
- quantum-mechanics
stage: advanced
status: draft
---

# Rydberg Constant and Spectroscopic Line Formula

## Core Idea
The Rydberg formula 1/λ = R(1/n₁² − 1/n₂²) gives the wavelengths of spectral lines emitted by hydrogen as electrons transition between energy levels. The Rydberg constant R ≈ 1.097 × 10⁷ m⁻¹ can be derived from the Bohr model as R = me⁴/(4πε₀²ℏ²). Different series correspond to transitions ending at n₁ = 1 (Lyman), 2 (Balmer), 3 (Paschen), etc.

## How It's Best Learned
Derive the Rydberg formula from Bohr energy levels. Calculate visible spectral lines using the Balmer series (n₁=2). Measure or look up observed wavelengths and compare to predictions.

## Common Misconceptions
The Rydberg constant is the same for all hydrogen isotopes (it varies slightly due to the reduced mass effect). The formula applies to any hydrogen-like ion by replacing R with R×Z².

## Explainer

The Rydberg formula is the crown jewel of early atomic spectroscopy — a compact equation that predicts every spectral line of hydrogen with extraordinary precision. To understand where it comes from, start with what you know from the Bohr model: electrons orbit the nucleus only at specific allowed radii, corresponding to discrete energy levels Eₙ = −13.6/n² eV. When an electron falls from a higher level n₂ to a lower level n₁, it releases a photon whose energy exactly equals the difference ΔE = E_{n₁} − E_{n₂}.

The photon's energy determines its wavelength through E = hc/λ, so you can relate the wavelength directly to the level indices. When you substitute the Bohr energy formula and simplify, the result is the Rydberg formula: 1/λ = R∞(1/n₁² − 1/n₂²), where the **Rydberg constant** R∞ ≈ 1.097 × 10⁷ m⁻¹ bundles together the fundamental constants — electron mass, electron charge, Planck's constant, and the permittivity of free space. The subscript ∞ means we assumed infinite nuclear mass; the small reduced-mass correction gives the isotope-specific value.

The named **spectral series** are just different choices of n₁. The **Lyman series** (n₁ = 1) emits in the ultraviolet — the electron is dropping all the way to the ground state. The **Balmer series** (n₁ = 2) falls in or near visible light, which is why it was discovered first: astronomers could see these lines in starlight. The **Paschen series** (n₁ = 3) and higher are infrared. For each series, n₂ runs from n₁ + 1 to infinity, producing a set of lines that crowd closer together as n₂ increases, converging toward the **series limit** at n₂ → ∞ — the ionization threshold from that shell.

For hydrogen-like ions — atoms stripped of all but one electron, like He⁺ or Li²⁺ — the formula generalizes by replacing R∞ with R∞Z², where Z is the nuclear charge. More nuclear charge pulls the electron tighter, raising all energies by Z², which compresses all wavelengths accordingly. This same scaling predicts X-ray emission lines from heavy elements, extending Rydberg's insight from visible spectroscopy to the entire electromagnetic spectrum of one-electron systems.
