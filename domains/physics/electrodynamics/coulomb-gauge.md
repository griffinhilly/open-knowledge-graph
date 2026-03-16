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

## Explainer

From gauge transformations you know that the scalar potential φ and vector potential A⃗ are not uniquely determined by the physical fields E⃗ and B⃗. You can add ∇λ to A⃗ and subtract ∂λ/∂t from φ for any scalar function λ, leaving E⃗ and B⃗ unchanged. A **gauge choice** is a condition that fixes λ and thereby picks a unique representative pair (φ, A⃗) from each equivalence class of physically identical potentials. The Coulomb gauge imposes ∇·A⃗ = 0 — the vector potential is divergence-free.

The payoff for this choice is that Poisson's equation ∇²φ = −ρ/ε₀ drops out immediately for the scalar potential. You already solved Poisson's equation in electrostatics: its solution is the familiar Coulomb integral φ(r⃗, t) = (1/4πε₀) ∫ ρ(r⃗', t)/|r⃗ − r⃗'| d³r'. Notice that t appears only as a parameter — the scalar potential in the Coulomb gauge responds to the charge distribution *instantaneously*, as if electrostatics applied at every moment. This apparent violation of relativity is a gauge artifact, not physics: the physically measurable fields E⃗ and B⃗ still propagate at c, and no signal actually travels faster than light. The instantaneous φ and the wave-equation terms in A⃗ conspire to give causal fields.

The **separation of Coulomb and radiation physics** is the Coulomb gauge's great practical advantage. In atomic and molecular physics, the dominant interaction between an electron and a nucleus is the Coulomb attraction, which is captured entirely by φ. The radiation field — light absorbed or emitted during transitions — lives in the transverse part of A⃗ (the part satisfying ∇·A⃗ = 0). Perturbation theory for atomic transitions can therefore be structured cleanly: compute the unperturbed atomic states from the Coulomb potential, then treat the transverse vector potential as a perturbation responsible for photon emission and absorption. This is the standard approach in non-relativistic quantum electrodynamics and quantum optics.

The Coulomb gauge trades manifest Lorentz covariance for simplicity in the non-relativistic domain. The Lorenz gauge (∂_μ A^μ = 0) is the preferred choice in relativistic calculations because it treats space and time symmetrically and makes the covariance of Maxwell's equations explicit. But for atoms, molecules, and condensed matter systems — where velocities are far below c and the primary interaction is electrostatic — the Coulomb gauge is the natural language. Recognizing which gauge is most convenient for a given problem, and knowing what can and cannot depend on the gauge choice, is a core skill in advanced electrodynamics.
