---
id: lorentz-force-complete-em
title: Complete Lorentz Force Law and Maxwell's Framework
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: ampere-law-applications
  type: hard
- id: faraday-law-electromagnetic-induction
  type: hard
- id: cross-product
  type: hard
- id: dot-product
  type: hard
- id: maxwells-equations-overview
  type: soft
tags:
- lorentz-force
- maxwell
- unification
stage: advanced
status: validated
---
# Complete Lorentz Force Law and Maxwell's Framework

## Core Idea
The Lorentz force law F = q(E + v × B) unifies electric and magnetic phenomena. Combined with Maxwell's equations (Gauss's law, no magnetic monopoles, Faraday's law, Ampere-Maxwell law), it forms the complete framework of classical electromagnetism.

## How It's Best Learned
Revisit Gauss's law, Faraday's law, and Ampere's law as four equations governing E and B. Solve a problem involving both electric and magnetic forces to see how they combine.

## Explainer

You already know Faraday's law (a changing B field induces an electric field) and Ampere's law (currents and changing E fields produce magnetic fields). The **Lorentz force law** F⃗ = q(E⃗ + v⃗ × B⃗) is the complementary statement about how those fields act on matter: a charge q moving at velocity v⃗ through both an electric field E⃗ and a magnetic field B⃗ experiences forces from both simultaneously. The electric piece qE⃗ acts in the direction of the field regardless of how the charge is moving. The magnetic piece q(v⃗ × B⃗) requires motion — a stationary charge feels no magnetic force — and from the cross-product you already know, it acts perpendicular to both the velocity and the magnetic field. This perpendicularity means the magnetic force does no work on the charge; it can bend the trajectory but never speed up or slow down the particle.

Together, Lorentz force plus **Maxwell's four equations** form the complete framework of classical electromagnetism. The four equations are: Gauss's law for E (∇·E⃗ = ρ/ε₀, charges source field lines), Gauss's law for B (∇·B⃗ = 0, no magnetic monopoles), Faraday's law (∇ × E⃗ = −∂B⃗/∂t, changing B induces E), and the Ampere-Maxwell law (∇ × B⃗ = μ₀J⃗ + μ₀ε₀ ∂E⃗/∂t, currents and changing E produce B). The last term — the **displacement current** μ₀ε₀ ∂E⃗/∂t — was Maxwell's key addition. Without it, the Ampere-Maxwell law would be inconsistent with charge conservation, and the framework would not support electromagnetic waves.

The real power of Maxwell's equations is what you can derive from them together. Taking the curl of Faraday's law and substituting the Ampere-Maxwell law yields a wave equation for E⃗ with speed c = 1/√(μ₀ε₀). When you plug in the values of those constants, out comes the speed of light — a prediction that electricity and magnetism were not separate phenomena but two aspects of a single electromagnetic field. This is one of the great unifications in physics history: optics, electricity, and magnetism are the same thing viewed from different contexts.

The unification also has a deeper significance that your prerequisites set up. Faraday's law and Ampere's law, which you learned as separate experimental facts, turn out to be intimately linked: a changing E field creates B, and a changing B field creates E. These mutual inductions sustain each other as a self-propagating wave traveling through empty space. The Lorentz force law then closes the loop by describing how that wave, once created, exerts forces on the charged matter it encounters — from radio antennas to the retina of your eye.

## Questions

```yaml
- question: "A proton moves in the +x direction with speed v in a magnetic field pointing in the +z direction. What is the direction of the magnetic force on the proton?"
  type: short-answer
  answer: "The force is in the −y direction. F⃗ = qv⃗ × B⃗ = q(v x̂) × (B ẑ) = qvB (x̂ × ẑ) = qvB(−ŷ). Since q > 0 for a proton, the force points in −y."
  explanation: "Use the right-hand rule for the cross product x̂ × ẑ = −ŷ (or equivalently, ẑ × x̂ = ŷ, so x̂ × ẑ = −ŷ). The result is perpendicular to both the velocity and the field, confirming that the magnetic force does no work — it curves the proton into circular motion in the x-y plane."

- question: "Which of Maxwell's equations was modified by Maxwell himself (relative to its pre-Maxwell form), and what physical consequence did this modification enable?"
  type: short-answer
  answer: "Ampere's law was modified by adding the displacement current term μ₀ε₀ ∂E⃗/∂t. This made the equations self-consistent with charge conservation and, crucially, allowed the derivation of electromagnetic waves propagating through vacuum at the speed of light."
  explanation: "Without the displacement current, a contradiction arose in circuits with capacitors: the original Ampere's law predicted a magnetic field around a wire carrying current, but gave inconsistent results when the surface bounding the Amperian loop was chosen to pass through a capacitor gap (where no current flows). The displacement current term resolved this inconsistency and had the momentous side effect of predicting that light is an electromagnetic wave."
```
