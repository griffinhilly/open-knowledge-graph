---
id: coulomb-gauge
title: Coulomb Gauge
domain: physics
course: electrodynamics
prerequisites:
- id: gauge-transformations
  type: hard
- id: scalar-vector-potentials
  type: hard
builds-toward:
- quantum-electrodynamics-intro
tags:
- coulomb-gauge
- instantaneous-interaction
stage: advanced
status: draft
---

# Coulomb Gauge

## Core Idea
The Coulomb gauge (∇·A = 0) simplifies calculations in the non-relativistic limit and atomic physics. In this gauge, the scalar potential φ satisfies Poisson's equation ∇²φ = -ρ/ε₀ (instantaneous Coulomb interaction), while the vector potential A satisfies a wave equation with a source term. This gauge naturally separates Coulomb (instantaneous) interactions from radiation effects.

## Questions

```yaml
- question: "In the Coulomb gauge, the scalar potential φ(r,t) responds instantaneously to changes in the charge distribution. Does this mean that information can travel faster than the speed of light?"
  type: multiple-choice
  options:
    - "Yes — the instantaneous scalar potential directly transmits information between distant charges"
    - "No — the instantaneous φ is a gauge artifact; the physical fields E and B still propagate causally at c"
    - "Only in the non-relativistic limit, where special relativity is not applicable"
    - "No — because the Coulomb gauge is only valid for static charge distributions"
  answer: 1
  explanation: "The apparent instantaneity of φ is a gauge artifact, not a physical effect. Gauge potentials are not directly observable — only E and B are measurable, and these always propagate causally at the speed of light. The instantaneous φ and the wave-equation terms in A conspire together to give the correct causal E and B fields. No physical measurement at any location can detect a change at a distant source any faster than c. This is a subtle but crucial point: the division of the electromagnetic field into potentials depends on the gauge choice; only the total physical fields are gauge-invariant and observable."

- question: "Why is the Coulomb gauge particularly convenient for calculating atomic and molecular physics problems?"
  type: multiple-choice
  options:
    - "It makes Maxwell's equations manifestly Lorentz covariant, simplifying relativistic corrections"
    - "It eliminates the vector potential entirely, reducing the problem to a scalar equation"
    - "It separates the dominant Coulomb interaction (captured by φ) from the radiation field (captured by the transverse A), allowing perturbation theory to be structured cleanly"
    - "It ensures that the scalar potential is always zero outside the charge distribution"
  answer: 2
  explanation: "In the Coulomb gauge, ∇²φ = −ρ/ε₀, so φ is precisely the familiar Coulomb potential — the dominant electron-nucleus interaction in atomic systems. The radiation field (photon emission and absorption) lives in the transverse vector potential A (which satisfies ∇·A = 0). This clean separation lets you first compute atomic states from the Coulomb potential alone, then treat A as a perturbation responsible for transitions. Option A describes the Lorenz gauge, not Coulomb. Option B is false — A is still present and carries the radiation physics. Option D is false; the Coulomb potential extends throughout space."

- question: "The choice of gauge (Coulomb vs. Lorenz) changes the values of the physically measurable electric and magnetic fields at a given point."
  type: true-false
  answer: false
  explanation: "False. This is the fundamental point of gauge invariance. The electric field E = −∇φ − ∂A/∂t and magnetic field B = ∇×A are unchanged by a gauge transformation (adding ∇λ to A and subtracting ∂λ/∂t from φ). Different gauges assign different values to the potentials φ and A, but these are mathematical conveniences — only E and B have direct physical meaning. Any gauge gives the same predictions for observable quantities; the choice of gauge is purely a matter of computational convenience."

- question: "The Lorenz gauge is preferred over the Coulomb gauge for non-relativistic atomic physics because it produces simpler equations for atomic energy levels."
  type: true-false
  answer: false
  explanation: "False — the preference is reversed. The Coulomb gauge is preferred for non-relativistic atomic physics precisely because it separates Coulomb interactions from radiation effects in a way that matches the dominant physics: the electron-nucleus Coulomb interaction is much larger than the radiation corrections, making Coulomb gauge a natural starting point for perturbation theory. The Lorenz gauge is preferred for relativistic calculations because it treats space and time symmetrically and keeps Lorentz covariance manifest — a priority in quantum field theory and high-energy physics, not in atomic spectroscopy."

- question: "Explain why the apparently instantaneous scalar potential in the Coulomb gauge does not violate the principle of causality."
  type: short-answer
  answer: "The scalar potential φ is not directly observable. Physical measurements detect only the electric and magnetic fields E and B, which are gauge-invariant combinations of φ and A. In the Coulomb gauge, φ is instantaneous but A satisfies a wave equation with a retarded source term; together they produce E and B that propagate causally at c. The instantaneity of φ is a mathematical artifact of the gauge choice — it cancels exactly with terms in A to give the correct causal fields. No experiment can detect the 'instantaneous' change in φ directly."
  explanation: "This subtlety is important for understanding what gauge choice represents. A gauge transformation changes φ and A but leaves E and B unchanged. Since only E and B are observable, you can always rewrite the problem in a different gauge without changing any physical prediction. The Coulomb gauge happens to assign an instantaneous character to φ, but this is a feature of how the math is organized, not a feature of the physics."
```

## Explainer

From gauge transformations you know that the scalar potential φ and vector potential A⃗ are not uniquely determined by the physical fields E⃗ and B⃗. You can add ∇λ to A⃗ and subtract ∂λ/∂t from φ for any scalar function λ, leaving E⃗ and B⃗ unchanged. A **gauge choice** is a condition that fixes λ and thereby picks a unique representative pair (φ, A⃗) from each equivalence class of physically identical potentials. The Coulomb gauge imposes ∇·A⃗ = 0 — the vector potential is divergence-free.

The payoff for this choice is that Poisson's equation ∇²φ = −ρ/ε₀ drops out immediately for the scalar potential. You already solved Poisson's equation in electrostatics: its solution is the familiar Coulomb integral φ(r⃗, t) = (1/4πε₀) ∫ ρ(r⃗', t)/|r⃗ − r⃗'| d³r'. Notice that t appears only as a parameter — the scalar potential in the Coulomb gauge responds to the charge distribution *instantaneously*, as if electrostatics applied at every moment. This apparent violation of relativity is a gauge artifact, not physics: the physically measurable fields E⃗ and B⃗ still propagate at c, and no signal actually travels faster than light. The instantaneous φ and the wave-equation terms in A⃗ conspire to give causal fields.

The **separation of Coulomb and radiation physics** is the Coulomb gauge's great practical advantage. In atomic and molecular physics, the dominant interaction between an electron and a nucleus is the Coulomb attraction, which is captured entirely by φ. The radiation field — light absorbed or emitted during transitions — lives in the transverse part of A⃗ (the part satisfying ∇·A⃗ = 0). Perturbation theory for atomic transitions can therefore be structured cleanly: compute the unperturbed atomic states from the Coulomb potential, then treat the transverse vector potential as a perturbation responsible for photon emission and absorption. This is the standard approach in non-relativistic quantum electrodynamics and quantum optics.

The Coulomb gauge trades manifest Lorentz covariance for simplicity in the non-relativistic domain. The Lorenz gauge (∂_μ A^μ = 0) is the preferred choice in relativistic calculations because it treats space and time symmetrically and makes the covariance of Maxwell's equations explicit. But for atoms, molecules, and condensed matter systems — where velocities are far below c and the primary interaction is electrostatic — the Coulomb gauge is the natural language. Recognizing which gauge is most convenient for a given problem, and knowing what can and cannot depend on the gauge choice, is a core skill in advanced electrodynamics.
