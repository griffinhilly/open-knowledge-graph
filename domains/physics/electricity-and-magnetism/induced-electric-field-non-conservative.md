---
id: induced-electric-field-non-conservative
title: 'Induced Electric Field: Non-Conservative Behavior'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: faraday-law-of-induction
  type: hard
- id: electric-field
  type: hard
builds-toward:
- maxwells-equations-overview
tags:
- induction
- non-conservative
- Maxwell's equations
stage: formal-systems
status: draft
---

# Induced Electric Field: Non-Conservative Behavior

## Core Idea
Changing magnetic fields induce electric fields even without charges. This induced electric field is non-conservative: line integrals around closed loops are non-zero, equal to negative rate of change of magnetic flux. Faraday's law in differential form is ∇ × E = -∂B/∂t. Non-conservative electric fields are fundamental to transformers and induction motors.

## How It's Best Learned
Derive Faraday's law in differential form from the integral form using Stokes' theorem. Analyze induced field patterns around changing flux regions.

## Common Misconceptions
- All electric fields are conservative (only electrostatic fields from static charges are).
- Induced electric fields can be described by a scalar potential (only vector potentials work).
- Induced fields are the same as fields from charge distributions (they arise from time-varying B fields).

## Explainer

From your study of Faraday's law, you know that a changing magnetic flux through a loop induces an EMF: ε = −dΦ_B/dt. But EMF around a loop is just the line integral of the electric field: ε = ∮ E⃗ · dL⃗. Put these together and you arrive at a remarkable conclusion: even with no wire present, no charges, no conductor at all — a changing magnetic field creates an electric field in the surrounding space. This is the **induced electric field**, and it is fundamentally different from the Coulomb electric field you first studied.

The core distinction is **conservative vs. non-conservative**. The electrostatic field from charges has zero curl everywhere: ∮ E⃗ · dL⃗ = 0 around any closed path. This is what allows us to define a unique scalar potential V at every point. The induced electric field violates this: ∮ E⃗ · dL⃗ = −dΦ_B/dt ≠ 0 when flux is changing. A line integral that depends on the path (and is non-zero around a closed loop) cannot be the gradient of any scalar function. This is what "non-conservative" means precisely: there is no potential energy landscape from which this field derives. Consequently, you cannot describe induced electric fields with a scalar potential V — only a **vector potential** A⃗ works, via E⃗ = −∂A⃗/∂t.

To see the field pattern concretely, imagine a solenoid with increasing current. The magnetic field inside grows; by symmetry, the induced electric field outside must circulate in closed rings centered on the solenoid axis. Using the integral form of Faraday's law on a circular path of radius r, you get E · 2πr = −dΦ/dt, which gives E = (r/2) · |dB/dt| inside (where Φ grows with r²) and E ∝ 1/r outside (where flux is fixed). These circulating E-field rings have no beginning and no end — they don't start or terminate on charges. This looping topology is the physical signature of a non-conservative field.

This physics is what makes **transformers** work. The primary coil creates a time-varying B field through a core; the induced electric field drives current around the secondary coil even though the two coils are electrically isolated. It also sets up the structure of Faraday's law in differential form: ∇ × E⃗ = −∂B⃗/∂t. This equation — one of Maxwell's equations — pairs with Ampère-Maxwell: ∇ × B⃗ = μ₀J⃗ + μ₀ε₀ ∂E⃗/∂t. Together they reveal that changing E creates B and changing B creates E, which is how electromagnetic waves sustain themselves in empty space.
