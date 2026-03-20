---
id: cross-sections-scattering
title: Cross Sections in Quantum Scattering
domain: physics
course: quantum-mechanics
prerequisites:
- id: scattering-theory-intro
  type: hard
tags:
- cross-sections
- scattering
stage: advanced
status: draft
---

# Cross Sections in Quantum Scattering

## Core Idea
Differential cross section dσ/dΩ = |f(θ,φ)|² gives scattering rate into solid angle. Total σ_tot = ∫ dσ/dΩ dΩ measures overall probability.

## Explainer

From your introduction to scattering theory, you know that when a quantum particle collides with a target, the wavefunction far from the target takes the form of an incident plane wave plus an outgoing spherical wave: ψ ~ e^(ikz) + f(θ,φ) e^(ikr)/r. The **scattering amplitude** f(θ,φ) encodes everything about the physics of the collision — it depends on the interaction potential, the incident energy, and the angles of observation. Cross sections translate this complex-valued amplitude into experimentally measurable quantities.

Think of the cross section as an effective area. Classically, if you throw a marble at a billiard ball, the probability of a hit depends on the billiard ball's geometric cross-sectional area. In quantum mechanics, the "effective area" a target presents to an incoming particle depends on the scattering amplitude in a given direction. The **differential cross section** dσ/dΩ = |f(θ,φ)|² tells you how many particles scatter per unit time into the tiny solid angle dΩ around direction (θ,φ), per unit incident flux. Taking the squared modulus converts the probability amplitude f into a real-valued, measurable probability density.

Integrating over all solid angles gives the **total cross section** σ_tot = ∫ |f(θ,φ)|² dΩ. This is the single number summarizing the overall likelihood of scattering — it has units of area (often quoted in barns, where 1 barn = 10⁻²⁴ cm²). A large σ_tot means the target looks "big" to the incoming particle, even if geometrically it is tiny. For example, slow neutrons have enormous cross sections for certain nuclear reactions because the quantum mechanical resonance amplifies f dramatically.

There is also a deep connection between σ_tot and the forward scattering amplitude through the **optical theorem**: σ_tot = (4π/k) Im[f(θ=0)]. This remarkable result links a total probability (which involves interference from all directions) to a single complex number evaluated at zero angle. It follows from probability conservation — the incident beam is depleted by scattering, and this depletion shows up as destructive interference in the forward direction. The optical theorem is a consistency check on any scattering calculation and a reminder that in quantum mechanics, probability amplitudes interfere in ways that have no classical analogue.
