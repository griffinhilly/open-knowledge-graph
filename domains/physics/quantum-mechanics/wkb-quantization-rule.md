---
id: wkb-quantization-rule
title: WKB Quantization and Bohr-Sommerfeld Rule
domain: physics
course: quantum-mechanics
prerequisites:
- id: wkb-approximation
  type: hard
tags:
- wkb
- quantization
stage: formal-systems
status: draft
---

# WKB Quantization and Bohr-Sommerfeld Rule

## Core Idea
WKB quantization: ∮ p(x) dx = (n + ½)πℏ (Bohr-Sommerfeld rule) for bound states between classical turning points. Reproduces harmonic oscillator and hydrogen spectra to leading order.

## Explainer

The WKB approximation gives the semiclassical wavefunction in a region where the potential varies slowly: ψ(x) ≈ A/√p(x) · exp(±i/ℏ ∫p(x) dx), where p(x) = √(2m(E−V(x))) is the local classical momentum. This solution oscillates with a phase that accumulates as the particle traverses the classically allowed region. The **quantization rule** emerges from demanding that this phase be consistent around a complete classical orbit — a condition that picks out discrete allowed energies.

Think of a classical particle bouncing back and forth between two **turning points** x₁ and x₂, where E = V(x) so p = 0. In one complete oscillation, the particle travels from x₁ to x₂ and back. For the wavefunction to be single-valued and well-behaved, the total accumulated phase must match up correctly after the round trip. Each turning point contributes an additional phase shift of π/2 (a quarter wavelength) due to the connection formulas that stitch the WKB solution across the classically forbidden region. Two turning points contribute a total of π/2 + π/2 = π, so the **Bohr-Sommerfeld rule** is: ∮ p dx = 2∫[x₁ to x₂] p(x) dx = (n + ½) · 2πℏ, or equivalently ∮ p dx = (n + ½)h.

The **½ correction** — the Maslov index contribution — is what distinguishes the modern Bohr-Sommerfeld rule from Bohr's original semiclassical quantization, which used ∮ p dx = nh. The original rule gives the wrong zero-point energy for the harmonic oscillator (it predicts E₀ = 0 instead of ℏω/2) and incorrect spectra near the ground state. Adding the ½ accounts for the phase shifts at the turning points and correctly reproduces the harmonic oscillator energies Eₙ = (n + ½)ℏω for all n ≥ 0. For hydrogen, the WKB rule reproduces the Bohr formula Eₙ = −13.6 eV/n² to leading order, which is already exact because the Coulomb potential happens to have special symmetry.

The power of the rule is practical: to find the allowed energies of a complicated potential, you do not need to solve the Schrödinger equation exactly. Instead, sketch p(x) = √(2m(E−V(x))) as a function of x for a trial energy E, and compute the integral ∫p dx numerically between the turning points. Sweep E until the integral equals (n + ½)πℏ. This technique works whenever the de Broglie wavelength varies slowly compared to the scale over which p itself changes — the **semiclassical condition** λ · |dp/dx| ≪ p² — and breaks down near turning points and at very low quantum numbers where the quantum corrections are large.
