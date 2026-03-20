---
id: displacement-current-and-maxwell
title: Displacement Current and Maxwell's Equations
domain: physics
course: electrodynamics
prerequisites:
- id: faraday-law-of-induction
  type: hard
- id: multivariable-calculus
  type: hard
builds-toward:
- maxwells-equations-differential-form
- electromagnetic-wave-equation
tags:
- maxwell-equations
- displacement-current
- symmetry
stage: formal-systems
status: draft
---

# Displacement Current and Maxwell's Equations

## Core Idea
Maxwell added the displacement current term ε₀∂E/∂t to Ampère's law, creating beautiful symmetry where changing E produces B just as changing B produces E. This correction was essential for predicting electromagnetic waves and ensuring current continuity.

## Explainer

By the 1860s, three of Maxwell's four equations were established: Gauss's laws for electric and magnetic fields, and Faraday's law linking a changing B⃗ to a circulating E⃗. Ampère's law linked a circulating B⃗ to steady currents. The problem: when you apply Ampère's law to the gap between the plates of a charging capacitor, no conventional current crosses that gap — yet a magnetic field clearly exists there by continuity arguments. The law was inconsistent.

Maxwell's solution was to notice that while no charge crosses the gap, the electric field in the gap is changing as the capacitor charges. He postulated that a **displacement current** ε₀∂E/∂t should generate a magnetic field just as a real current does. Adding this term to Ampère's law — ∇ × B⃗ = μ₀J⃗ + μ₀ε₀∂E⃗/∂t — fixed the inconsistency. The modification created a profound symmetry: Faraday had shown that ∂B/∂t drives circulating E⃗; now Maxwell showed that ∂E/∂t drives circulating B⃗. The two laws became mirrors of each other.

The consequences were revolutionary. Taking the curl of the modified Faraday and Ampère laws and substituting one into the other produces the **electromagnetic wave equation**: ∇²E⃗ = μ₀ε₀∂²E⃗/∂t². This is a wave equation with speed v = 1/√(μ₀ε₀). Plugging in the known constants gives v ≈ 3×10⁸ m/s — exactly the measured speed of light. Maxwell concluded that light itself is an electromagnetic wave. This was arguably the greatest unification in 19th-century physics: optics, electricity, and magnetism were revealed as one.

The displacement current also resolves the capacitor paradox completely. In the gap between capacitor plates, ε₀∂E/∂t acts as an effective current density equal to the conduction current density in the wires feeding the plates. Ampère's law, applied to any surface bounded by the same loop around the wire, gives the same B⃗ regardless of whether you choose a surface that intersects the wire (where J⃗ is nonzero) or one that passes through the gap (where ∂E/∂t is nonzero). The physics is consistent, and a crucial lesson about mathematical self-consistency in physics is illustrated: when a law breaks down at a boundary case, the violation points toward a deeper truth.
