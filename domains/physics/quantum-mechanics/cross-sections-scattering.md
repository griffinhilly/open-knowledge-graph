---
id: cross-sections-scattering
title: Cross Sections in Quantum Scattering
domain: physics
course: quantum-mechanics
prerequisites:
- id: scattering-theory-intro
  type: hard
- id: born-approximation
  type: soft
tags:
- cross-sections
- scattering
stage: expert
status: validated
---
# Cross Sections in Quantum Scattering

## Core Idea
Differential cross section dσ/dΩ = |f(θ,φ)|² gives scattering rate into solid angle. Total σ_tot = ∫ dσ/dΩ dΩ measures overall probability.

## Questions

```yaml
- question: "A slow neutron has a cross section of 10,000 barns for a certain nuclear reaction, despite the nucleus having a geometric cross-sectional area of roughly 1 barn. What best explains this?"
  type: multiple-choice
  options:
    - "The cross section formula must be incorrectly normalized — it should be divided by the target's geometric area"
    - "Slow neutrons have very large de Broglie wavelengths, so they physically spread out and overlap the entire nucleus"
    - "The quantum mechanical scattering amplitude is dramatically enhanced by resonance, making the effective interaction area far exceed the geometric target size"
    - "The barn is a poorly defined unit; the geometric and quantum cross sections are always equal when units are consistent"
  answer: 2
  explanation: "The cross section dσ/dΩ = |f(θ,φ)|² is an effective area determined by the scattering amplitude f, not by geometric dimensions. Near a nuclear resonance, f is enhanced dramatically — the quantum-mechanical interaction 'looks' far larger than the nucleus. This is one of the clearest demonstrations that cross section is a measure of interaction strength, not physical size. Slow neutrons have long de Broglie wavelengths, which contributes to resonance enhancement, but the core effect is the magnitude of f at resonance."

- question: "What does the optical theorem state in quantum scattering theory?"
  type: multiple-choice
  options:
    - "The total cross section equals the sum of differential cross sections integrated over all solid angles, which is its definition"
    - "The total cross section is proportional to the imaginary part of the forward scattering amplitude: σ_tot = (4π/k) Im[f(θ=0)]"
    - "The differential cross section at 90° determines the total cross section through a symmetry argument"
    - "Optical and quantum scattering obey the same cross-section formula because light and matter both satisfy wave equations"
  answer: 1
  explanation: "The optical theorem σ_tot = (4π/k) Im[f(θ=0)] is non-trivial: it links the total probability of scattering (involving all angles) to a single complex number — the imaginary part of the forward scattering amplitude. The theorem follows from probability conservation: the incident beam is depleted as particles scatter away, and this depletion appears as destructive interference in the forward direction. It provides a powerful consistency check — any scattering calculation must satisfy this relation — and reveals that quantum amplitudes interfere in ways with no classical analogue."

- question: "The differential cross section dσ/dΩ has units of area per steradian, representing the effective interaction area presented to particles scattered into each infinitesimal solid angle element."
  type: true-false
  answer: true
  explanation: "The squared modulus |f(θ,φ)|² has units of length² per steradian (since f has units of length). Integrating dσ/dΩ over a solid angle element dΩ gives an area — the effective cross section for scattering into that angular region. Integrating over all 4π steradians gives the total cross section σ_tot with pure area units. The 'per steradian' reflects that the differential cross section is a density over direction space."

- question: "A particle that scatters with a very large total cross section is expected to have physically struck a large target."
  type: true-false
  answer: false
  explanation: "The cross section is an effective area, not a geometric one. A small nucleus near a quantum mechanical resonance can present an enormous effective cross section to an incoming particle — far larger than its physical size — because the scattering amplitude f is resonantly enhanced. Conversely, a physically large target might have a small cross section if the interaction potential is weak. The total cross section measures interaction probability, not physical contact area."

- question: "Explain why the cross section is described as an 'effective area' rather than a geometric area, and why this distinction matters in quantum scattering."
  type: short-answer
  answer: "A geometric cross section is the physical profile area of a target — how much space it occupies transverse to the beam. A quantum mechanical cross section is the effective area that determines scattering probability, derived from the scattering amplitude as dσ/dΩ = |f(θ,φ)|². These can differ dramatically because the interaction is governed by the quantum mechanical potential — its range, depth, and resonant structure — rather than by the target's physical size. A nucleus near a resonance has an enormously enhanced scattering amplitude, yielding a cross section thousands of times its geometric area. Conversely, a neutral atom might have a small cross section for certain interactions despite its comparatively large physical size. The distinction matters because it means cross sections encode information about the interaction potential, not just the target geometry, making them the central measurable quantity in particle and nuclear physics for inferring fundamental forces."
  explanation: "In classical mechanics, the cross section for hard-sphere scattering equals the geometric cross-sectional area πR². Quantum mechanics replaces R with the scattering amplitude f, which can be large or small relative to any geometric length scale depending on the resonance structure of the potential."
```

## Explainer

From your introduction to scattering theory, you know that when a quantum particle collides with a target, the wavefunction far from the target takes the form of an incident plane wave plus an outgoing spherical wave: ψ ~ e^(ikz) + f(θ,φ) e^(ikr)/r. The **scattering amplitude** f(θ,φ) encodes everything about the physics of the collision — it depends on the interaction potential, the incident energy, and the angles of observation. Cross sections translate this complex-valued amplitude into experimentally measurable quantities.

Think of the cross section as an effective area. Classically, if you throw a marble at a billiard ball, the probability of a hit depends on the billiard ball's geometric cross-sectional area. In quantum mechanics, the "effective area" a target presents to an incoming particle depends on the scattering amplitude in a given direction. The **differential cross section** dσ/dΩ = |f(θ,φ)|² tells you how many particles scatter per unit time into the tiny solid angle dΩ around direction (θ,φ), per unit incident flux. Taking the squared modulus converts the probability amplitude f into a real-valued, measurable probability density.

Integrating over all solid angles gives the **total cross section** σ_tot = ∫ |f(θ,φ)|² dΩ. This is the single number summarizing the overall likelihood of scattering — it has units of area (often quoted in barns, where 1 barn = 10⁻²⁴ cm²). A large σ_tot means the target looks "big" to the incoming particle, even if geometrically it is tiny. For example, slow neutrons have enormous cross sections for certain nuclear reactions because the quantum mechanical resonance amplifies f dramatically.

There is also a deep connection between σ_tot and the forward scattering amplitude through the **optical theorem**: σ_tot = (4π/k) Im[f(θ=0)]. This remarkable result links a total probability (which involves interference from all directions) to a single complex number evaluated at zero angle. It follows from probability conservation — the incident beam is depleted by scattering, and this depletion shows up as destructive interference in the forward direction. The optical theorem is a consistency check on any scattering calculation and a reminder that in quantum mechanics, probability amplitudes interfere in ways that have no classical analogue.
