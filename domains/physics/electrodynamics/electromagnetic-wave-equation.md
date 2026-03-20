---
id: electromagnetic-wave-equation
title: Derivation of the Electromagnetic Wave Equation
domain: physics
course: electrodynamics
prerequisites:
- id: maxwells-equations-differential-form
  type: hard
- id: differential-equations
  type: hard
- id: wave-equation-one-dimensional
  type: hard
- id: wave-equation-pde
  type: hard
builds-toward:
- plane-waves-in-vacuum
- poynting-vector-and-energy-flux
tags:
- waves
- wave-equation
- propagation
stage: advanced
status: draft
---

# Derivation of the Electromagnetic Wave Equation

## Core Idea
In source-free regions, Maxwell's equations combine to yield wave equations: ∇²E = μ₀ε₀∂²E/∂t² and ∇²B = μ₀ε₀∂²B/∂t². These show electromagnetic disturbances propagate at c = 1/√(μ₀ε₀), revealing light as an electromagnetic phenomenon and unifying optics with electromagnetism.

## Explainer

You know Maxwell's equations in differential form, and you know the one-dimensional and partial-differential-equation forms of the wave equation. The electromagnetic wave equation is where these two threads converge — the derivation is a direct algebraic manipulation, and the result is one of the most consequential predictions in the history of physics.

Start in source-free space: no charges (ρ = 0) and no currents (J⃗ = 0). Maxwell's equations reduce to ∇ · E⃗ = 0, ∇ · B⃗ = 0, ∇ × E⃗ = −∂B⃗/∂t, and ∇ × B⃗ = μ₀ε₀ ∂E⃗/∂t. Take the curl of Faraday's law: ∇ × (∇ × E⃗) = −∂(∇ × B⃗)/∂t. The left side, by the vector identity ∇ × (∇ × F⃗) = ∇(∇ · F⃗) − ∇²F⃗, becomes ∇(∇ · E⃗) − ∇²E⃗. Since ∇ · E⃗ = 0 in source-free space, this is just −∇²E⃗. Substituting Ampère-Maxwell on the right gives −∂(μ₀ε₀ ∂E⃗/∂t)/∂t = −μ₀ε₀ ∂²E⃗/∂t². Assembling both sides: **∇²E⃗ = μ₀ε₀ ∂²E⃗/∂t²**. An identical derivation (taking the curl of Ampère-Maxwell instead) yields ∇²B⃗ = μ₀ε₀ ∂²B⃗/∂t².

You recognize this immediately from your wave equation prerequisites: it has exactly the form ∇²f = (1/v²) ∂²f/∂t², where v is the wave propagation speed. Comparing, **v = 1/√(μ₀ε₀)**. Plugging in the measured values μ₀ = 4π × 10⁻⁷ T·m/A and ε₀ ≈ 8.85 × 10⁻¹² C²/(N·m²) gives v ≈ 3 × 10⁸ m/s — the measured speed of light. This agreement was not a tuned coincidence; Maxwell recognized it immediately as revealing that **light is an electromagnetic wave**. The unification of optics with electromagnetism follows automatically: every optical phenomenon is, at bottom, governed by Maxwell's equations.

The wave equation also constrains the structure of the solutions. Plane-wave solutions of the form E⃗ = E₀ cos(k⃗ · r⃗ − ωt) satisfy the equation provided ω/k = c. Substituting back into Maxwell's equations reveals that E⃗ and B⃗ are mutually perpendicular and both perpendicular to the direction of propagation — electromagnetic waves are **transverse**. Furthermore, the ratio of electric to magnetic field amplitudes is always E₀/B₀ = c. These relationships are not assumed — they are forced by the equations. The fact that a 19th-century theory of static charges and steady currents, extended by one displacement-current term, should automatically produce self-propagating transverse waves at the speed of light remains one of the most stunning deductive achievements in physics.
