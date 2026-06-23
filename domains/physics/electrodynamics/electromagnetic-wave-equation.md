---
id: electromagnetic-wave-equation
title: Derivation of the Electromagnetic Wave Equation
domain: physics
course: electrodynamics
prerequisites:
- id: maxwells-equations-differential-form
  type: hard
- id: differential-equations-intro
  type: hard
- id: wave-equation-one-dimensional
  type: hard
- id: wave-equation-pde
  type: soft
- id: ampere-maxwell-law
  type: hard
- id: maxwell-equations-differential-form
  type: hard
builds-toward:
- plane-waves-in-vacuum
- poynting-vector-and-energy-flux
tags:
- waves
- wave-equation
- propagation
stage: expert
status: validated
---

# Derivation of the Electromagnetic Wave Equation

## Core Idea
In source-free regions, Maxwell's equations combine to yield wave equations: ∇²E = μ₀ε₀∂²E/∂t² and ∇²B = μ₀ε₀∂²B/∂t². These show electromagnetic disturbances propagate at c = 1/√(μ₀ε₀), revealing light as an electromagnetic phenomenon and unifying optics with electromagnetism.

## Questions

```yaml
- question: "In the derivation of the electromagnetic wave equation in source-free space, what role does the Ampère-Maxwell term (μ₀ε₀ ∂E⃗/∂t) play?"
  type: multiple-choice
  options:
    - "It introduces a damping term that limits the wave speed to values below c"
    - "It provides the coupling between changing E and changing B that closes the feedback loop allowing self-propagating waves to exist"
    - "It ensures the equations apply only to static charge distributions"
    - "It is mathematically required for dimensional consistency but has no physical content"
  answer: 1
  explanation: "The displacement current term is the crucial addition Maxwell made to Ampère's law. Without it, Faraday's law says a changing B produces E, but there is no reciprocal law saying a changing E produces B. Taking the curl of Faraday's law and substituting Ampère-Maxwell creates a second-order equation in E alone, with the μ₀ε₀ term providing the 'restoring' temporal derivative that gives it wave character. Removing this term breaks the symmetry and eliminates self-propagating solutions."

- question: "If Maxwell's displacement current term did not exist — so Ampère's law read ∇ × B⃗ = 0 in source-free space — what would happen to electromagnetic wave propagation?"
  type: multiple-choice
  options:
    - "Waves would propagate but at a different speed"
    - "Waves would still propagate because Faraday's law alone couples E and B sufficiently"
    - "No self-sustaining electromagnetic waves could exist — a changing E field would not generate B, breaking the feedback loop required for propagation"
    - "Waves would propagate but only longitudinally, not transversely"
  answer: 2
  explanation: "Self-propagating waves require mutual induction: changing E creates B, and changing B creates E, with each sustaining the other in a traveling disturbance. Faraday's law covers only one direction of this coupling (changing B → E). Without the displacement current, the reverse coupling (changing E → B) is absent. Taking the curl of Faraday's law would give ∇²E⃗ = 0, a Laplace equation with no wave solutions. The displacement current term is what transforms a static-field theory into a wave theory."

- question: "The propagation speed predicted by Maxwell's wave equation, c = 1/√(μ₀ε₀), matched the known speed of light before Maxwell derived it — this match was already measured from astronomical observations."
  type: true-false
  answer: true
  explanation: "By the time Maxwell assembled his equations in the 1860s, Rømer and others had measured the speed of light from observations of Jupiter's moons to good accuracy. Maxwell computed 1/√(μ₀ε₀) from electrically measured constants and recognized immediately that the agreement was not coincidental — it meant light was electromagnetic in nature. The theoretical prediction and the experimental measurement converged, making this one of the most compelling unifications in physics history."

- question: "The electromagnetic wave equation is derived by assuming that light is a wave and then verifying that Maxwell's equations are consistent with this assumption."
  type: true-false
  answer: false
  explanation: "The derivation runs in the opposite direction: starting only from Maxwell's equations for E and B fields (with no assumption about light), applying vector calculus identities, and discovering that the resulting equations have wave-equation form. Light's wave nature is an output of the derivation, not an input. This is what makes the result so significant — a theory built from Coulomb's law and Ampère's observations of steady currents, extended by one additional term, predicts transverse wave propagation at the speed of light without any wave assumption."

- question: "Why does the identity c = 1/√(μ₀ε₀) matter for physics beyond simply predicting the speed of electromagnetic waves?"
  type: short-answer
  answer: "It reveals that light is an electromagnetic phenomenon — the same equations governing static charges and steady currents also govern optics. This unifies electromagnetism and optics under a single theoretical framework, meaning every optical phenomenon (reflection, refraction, polarization, interference) is ultimately governed by Maxwell's equations."
  explanation: "Before Maxwell, optics and electromagnetism were separate disciplines. The identity c = 1/√(μ₀ε₀) collapsed that separation: light is just a high-frequency electromagnetic wave. This unification had enormous consequences — it predicted radio waves (verified by Hertz), motivated the search for an ether (which failed, leading to special relativity), and established the template for the great unifications of 20th-century physics. The numerical coincidence is a signal of deep structural identity, not a curiosity."
```

## Explainer

You know Maxwell's equations in differential form, and you know the one-dimensional and partial-differential-equation forms of the wave equation. The electromagnetic wave equation is where these two threads converge — the derivation is a direct algebraic manipulation, and the result is one of the most consequential predictions in the history of physics.

Start in source-free space: no charges (ρ = 0) and no currents (J⃗ = 0). Maxwell's equations reduce to ∇ · E⃗ = 0, ∇ · B⃗ = 0, ∇ × E⃗ = −∂B⃗/∂t, and ∇ × B⃗ = μ₀ε₀ ∂E⃗/∂t. Take the curl of Faraday's law: ∇ × (∇ × E⃗) = −∂(∇ × B⃗)/∂t. The left side, by the vector identity ∇ × (∇ × F⃗) = ∇(∇ · F⃗) − ∇²F⃗, becomes ∇(∇ · E⃗) − ∇²E⃗. Since ∇ · E⃗ = 0 in source-free space, this is just −∇²E⃗. Substituting Ampère-Maxwell on the right gives −∂(μ₀ε₀ ∂E⃗/∂t)/∂t = −μ₀ε₀ ∂²E⃗/∂t². Assembling both sides: **∇²E⃗ = μ₀ε₀ ∂²E⃗/∂t²**. An identical derivation (taking the curl of Ampère-Maxwell instead) yields ∇²B⃗ = μ₀ε₀ ∂²B⃗/∂t².

You recognize this immediately from your wave equation prerequisites: it has exactly the form ∇²f = (1/v²) ∂²f/∂t², where v is the wave propagation speed. Comparing, **v = 1/√(μ₀ε₀)**. Plugging in the measured values μ₀ = 4π × 10⁻⁷ T·m/A and ε₀ ≈ 8.85 × 10⁻¹² C²/(N·m²) gives v ≈ 3 × 10⁸ m/s — the measured speed of light. This agreement was not a tuned coincidence; Maxwell recognized it immediately as revealing that **light is an electromagnetic wave**. The unification of optics with electromagnetism follows automatically: every optical phenomenon is, at bottom, governed by Maxwell's equations.

The wave equation also constrains the structure of the solutions. Plane-wave solutions of the form E⃗ = E₀ cos(k⃗ · r⃗ − ωt) satisfy the equation provided ω/k = c. Substituting back into Maxwell's equations reveals that E⃗ and B⃗ are mutually perpendicular and both perpendicular to the direction of propagation — electromagnetic waves are **transverse**. Furthermore, the ratio of electric to magnetic field amplitudes is always E₀/B₀ = c. These relationships are not assumed — they are forced by the equations. The fact that a 19th-century theory of static charges and steady currents, extended by one displacement-current term, should automatically produce self-propagating transverse waves at the speed of light remains one of the most stunning deductive achievements in physics.
