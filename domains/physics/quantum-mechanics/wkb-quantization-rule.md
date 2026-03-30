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
stage: expert
status: validated
---

# WKB Quantization and Bohr-Sommerfeld Rule

## Core Idea
WKB quantization: ∮ p(x) dx = (n + ½)πℏ (Bohr-Sommerfeld rule) for bound states between classical turning points. Reproduces harmonic oscillator and hydrogen spectra to leading order.

## Questions

```yaml
- question: "Using the Bohr-Sommerfeld rule ∮ p dx = (n + ½)πℏ, what is the ground-state energy (n=0) of a harmonic oscillator with angular frequency ω?"
  type: multiple-choice
  options:
    - "0 — no energy at the lowest quantum state"
    - "ℏω/2 — a non-zero zero-point energy"
    - "ℏω — one full quantum of energy"
    - "The rule cannot be applied to a harmonic oscillator"
  answer: 1
  explanation: "With n=0, the rule gives ∮ p dx = ½πℏ = ½h, yielding E₀ = ℏω/2. This non-zero zero-point energy is a direct consequence of the ½ in the quantization condition. The original Bohr rule (∮ p dx = nh) with n=0 gives zero, which is wrong — it predicts the oscillator can be completely at rest, violating the uncertainty principle."

- question: "The ½ in the Bohr-Sommerfeld rule ∮ p dx = (n + ½)πℏ originates from which physical effect?"
  type: multiple-choice
  options:
    - "The kinetic energy averaging over a half-cycle of the classical orbit"
    - "Phase shifts of π/2 at each of the two classical turning points"
    - "A relativistic correction to the non-relativistic momentum"
    - "Spin degeneracy of the electron states"
  answer: 1
  explanation: "At each turning point, the WKB wavefunction must be matched across the classically forbidden region using connection formulas. Each turning point contributes a phase shift of π/2 (a quarter-wavelength). With two turning points per orbit, the total extra phase is π, which translates into the ½ in the quantization rule. This is called the Maslov index contribution."

- question: "Bohr's original semiclassical quantization rule ∮ p dx = nh correctly predicts the harmonic oscillator energy spectrum."
  type: true-false
  answer: false
  explanation: "Bohr's original rule predicts energies Eₙ = nℏω (with n = 1, 2, 3, ...) and incorrectly predicts zero ground-state energy for n = 0. The modern Bohr-Sommerfeld rule ∮ p dx = (n + ½)πℏ gives Eₙ = (n + ½)ℏω, which matches the exact quantum mechanical result. The ½ correction comes from phase shifts at the turning points — a quantum effect that the original Bohr model neglected."

- question: "The WKB approximation breaks down near classical turning points because the semiclassical condition λ|dp/dx| ≪ p² is violated there."
  type: true-false
  answer: true
  explanation: "At a turning point, the classical momentum p(x) → 0 while dp/dx remains finite. This makes the ratio λ|dp/dx|/p² diverge, violating the condition that the de Broglie wavelength changes slowly compared to p itself. This is why special 'connection formulas' (Airy functions) are needed to stitch the WKB solutions across turning points — the WKB form alone is not valid there."

- question: "Explain in physical terms why the Bohr-Sommerfeld quantization rule contains the term (n + ½) rather than simply n."
  type: short-answer
  answer: "The ½ accounts for the quantum-mechanical phase shifts that occur at the two classical turning points. Each turning point contributes a phase advance of π/2 to the wavefunction as it penetrates into the classically forbidden region and is reflected. Two turning points give a total extra phase of π, equivalent to half a quantum of action, which adds the ½ to the quantization condition."
  explanation: "This Maslov index correction distinguishes the semiclassical WKB theory from Bohr's cruder model. Its practical consequence is the zero-point energy ℏω/2 of the harmonic oscillator — the quantum system cannot sit at the bottom of the potential well because the wavefunction must have minimum curvature consistent with the boundary conditions. The ½ is not a correction to the orbit — it is a statement that the quantum wavefunction 'feels' the turning points as reflecting walls with phase delay."
```

## Explainer

The WKB approximation gives the semiclassical wavefunction in a region where the potential varies slowly: ψ(x) ≈ A/√p(x) · exp(±i/ℏ ∫p(x) dx), where p(x) = √(2m(E−V(x))) is the local classical momentum. This solution oscillates with a phase that accumulates as the particle traverses the classically allowed region. The **quantization rule** emerges from demanding that this phase be consistent around a complete classical orbit — a condition that picks out discrete allowed energies.

Think of a classical particle bouncing back and forth between two **turning points** x₁ and x₂, where E = V(x) so p = 0. In one complete oscillation, the particle travels from x₁ to x₂ and back. For the wavefunction to be single-valued and well-behaved, the total accumulated phase must match up correctly after the round trip. Each turning point contributes an additional phase shift of π/2 (a quarter wavelength) due to the connection formulas that stitch the WKB solution across the classically forbidden region. Two turning points contribute a total of π/2 + π/2 = π, so the **Bohr-Sommerfeld rule** is: ∮ p dx = 2∫[x₁ to x₂] p(x) dx = (n + ½) · 2πℏ, or equivalently ∮ p dx = (n + ½)h.

The **½ correction** — the Maslov index contribution — is what distinguishes the modern Bohr-Sommerfeld rule from Bohr's original semiclassical quantization, which used ∮ p dx = nh. The original rule gives the wrong zero-point energy for the harmonic oscillator (it predicts E₀ = 0 instead of ℏω/2) and incorrect spectra near the ground state. Adding the ½ accounts for the phase shifts at the turning points and correctly reproduces the harmonic oscillator energies Eₙ = (n + ½)ℏω for all n ≥ 0. For hydrogen, the WKB rule reproduces the Bohr formula Eₙ = −13.6 eV/n² to leading order, which is already exact because the Coulomb potential happens to have special symmetry.

The power of the rule is practical: to find the allowed energies of a complicated potential, you do not need to solve the Schrödinger equation exactly. Instead, sketch p(x) = √(2m(E−V(x))) as a function of x for a trial energy E, and compute the integral ∫p dx numerically between the turning points. Sweep E until the integral equals (n + ½)πℏ. This technique works whenever the de Broglie wavelength varies slowly compared to the scale over which p itself changes — the **semiclassical condition** λ · |dp/dx| ≪ p² — and breaks down near turning points and at very low quantum numbers where the quantum corrections are large.
