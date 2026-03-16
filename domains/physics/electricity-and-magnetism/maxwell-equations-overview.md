---
id: maxwell-equations-overview
title: Maxwell's Equations and Electromagnetic Waves
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: rlc-resonance
  type: soft
- id: ampere-law-field
  type: hard
- id: curl-and-divergence
  type: hard
- id: divergence-theorem
  type: soft
tags:
- maxwell
- equations
- em-waves
stage: formal-systems
status: draft
---

# Maxwell's Equations and Electromagnetic Waves

## Core Idea
Maxwell's four equations (Gauss, no monopoles, Faraday, Ampere-Maxwell) describe how charges and currents produce fields and how changing fields induce each other. In vacuum with no charges or currents, combining these equations yields the wave equation: ∇²E⃗ = μ₀ε₀ ∂²E⃗/∂t², giving plane EM waves propagating at c = 1/√(μ₀ε₀). This unifies electricity, magnetism, and light.

## Explainer

Before Maxwell, physicists had four separate empirical laws about electricity and magnetism. Gauss's law described how electric charges produce diverging electric fields. A second law asserted that there are no magnetic monopoles — magnetic field lines always form closed loops. Faraday's law (which you know from Ampere's law and curl) said that a changing magnetic field curls around an induced electric field. Ampere's law said that currents produce circulating magnetic fields. These four laws were verified experimentally, but they were treated as independent facts. Maxwell's contribution was noticing that this collection was mathematically inconsistent and physically incomplete.

The problem Maxwell identified was in Ampere's law. The original form, ∇ × B⃗ = μ₀J⃗, implies that ∇ · J⃗ = 0 always — current is always steady. But if a capacitor is charging, current flows into the plates, charge builds up, and the current is not steady. Applying the original Ampere's law to a surface that passes between the capacitor plates gives a different answer than applying it to a surface that passes through the wire — a contradiction. Maxwell fixed this by adding the **displacement current** term: ∂E⃗/∂t also produces a curling magnetic field, just as real current does. This one addition made the equations self-consistent and, more importantly, created a feedback loop: a changing E⃗ produces a curling B⃗, and a changing B⃗ produces a curling E⃗.

That mutual induction between changing fields is the heart of electromagnetic waves. To see it, take Maxwell's equations in vacuum with no sources. Apply the curl operator to Faraday's law, substitute the Ampere-Maxwell equation, and use the vector identity ∇ × (∇ × E⃗) = ∇(∇·E⃗) − ∇²E⃗. Since ∇·E⃗ = 0 in empty space (Gauss's law with no charge), you arrive at ∇²E⃗ = μ₀ε₀ ∂²E⃗/∂t². This is the wave equation — the same form as the equation for sound waves in a medium. The wave speed is 1/√(μ₀ε₀). When Maxwell plugged in the known values of μ₀ and ε₀, he got 3 × 10⁸ m/s — identical to the independently measured speed of light. The conclusion was inescapable: light is an electromagnetic wave.

This was one of the most profound unifications in physics. Two seemingly unrelated phenomena — electromagnetism and optics — turned out to be different aspects of the same underlying field theory. The framework predicted the existence of radio waves, X-rays, and gamma rays before any of them were discovered experimentally. Maxwell's equations in their differential form, as you now know them, also set the stage for special relativity: Einstein noticed that these equations are not consistent with Newtonian mechanics under Galilean transformations but are naturally covariant under Lorentz transformations — ultimately forcing a revision of space and time itself.
