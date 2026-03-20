---
id: maxwells-equations-differential-form
title: Maxwell's Equations in Differential Form
domain: physics
course: electrodynamics
prerequisites:
- id: displacement-current-and-maxwell
  type: hard
- id: multivariable-calculus
  type: hard
- id: curl-and-divergence-operators
  type: hard
builds-toward:
- electromagnetic-wave-equation
- conservation-laws-em
- maxwells-equations-integral-form
tags:
- maxwell-equations
- field-theory
- divergence-curl
stage: formal-systems
status: draft
---

# Maxwell's Equations in Differential Form

## Core Idea
Maxwell's four equations in differential form are: ∇·E = ρ/ε₀, ∇·B = 0, ∇×E = -∂B/∂t, and ∇×B = μ₀J + μ₀ε₀∂E/∂t. These are the fundamental equations governing all classical electromagnetic phenomena.

## Explainer

You already know the divergence and curl operators from multivariable calculus, and you've seen **Maxwell's equations** assembled with the displacement current term. The differential form is the most powerful version because it holds at every point in space, not just in integral form over chosen surfaces and loops. Understanding what each equation says locally is the key to reading the physics directly from the mathematics.

**∇·E = ρ/ε₀** is Gauss's law in differential form. The divergence of E at a point equals the local charge density divided by ε₀. Wherever charge density is zero, field lines don't begin or end — they pass through. Wherever ρ ≠ 0, field lines either emanate outward (positive charge) or converge inward (negative charge). **∇·B = 0** says the divergence of B is always zero: magnetic field lines never begin or end anywhere. There are no magnetic monopoles; every field line forms a closed loop. These two divergence equations describe the *sources* of the fields.

The two curl equations describe how changing fields generate each other. **∇×E = −∂B/∂t** is Faraday's law: a time-varying magnetic field creates a circulating electric field. The negative sign (Lenz's law) means the induced E opposes the change in B — if B is increasing into the page, the induced E curls counterclockwise when viewed from the front. **∇×B = μ₀J + μ₀ε₀∂E/∂t** is Ampère's law with Maxwell's displacement current correction: both real current density J and a time-varying electric field ∂E/∂t produce circulating magnetic fields. The displacement current term μ₀ε₀∂E/∂t was Maxwell's crucial insight — without it, Ampère's law is inconsistent for time-varying fields, and electromagnetic waves cannot exist.

Together, the four equations unify electricity and magnetism completely. In vacuum (ρ = 0, J = 0), combining Faraday and Ampère gives ∇×(∇×E) = −μ₀ε₀∂²E/∂t², which simplifies using ∇·E = 0 to ∇²E = μ₀ε₀∂²E/∂t². This is a wave equation with propagation speed c = 1/√(μ₀ε₀) ≈ 3×10⁸ m/s — the speed of light. The fact that this constant equaled the measured speed of light was, to Maxwell, definitive proof that light is an electromagnetic wave. All of classical electrodynamics, optics, and radio propagation follows from these four compact equations.
