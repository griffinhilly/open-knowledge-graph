---
id: maxwell-equations-differential-form
title: Maxwell's Equations in Differential Form
domain: physics
course: electrodynamics
prerequisites:
- id: maxwell-equations-integral-form
  type: hard
- id: partial-derivatives
  type: hard
- id: curl-and-divergence
  type: hard
- id: curl-divergence
  type: hard
- id: curl-and-divergence-operators
  type: hard
builds-toward:
- electromagnetic-wave-equation
- boundary-value-problems-electrostatics
tags:
- maxwell-equations
- pdes
- differential-forms
stage: advanced
status: draft
---

# Maxwell's Equations in Differential Form

## Core Idea
The differential (local) forms of Maxwell's equations describe how electric and magnetic fields change at each point in space and time. Using divergence and curl operators, these four equations express the same physics as the integral forms but as partial differential equations. The differential forms are essential for deriving wave equations and solving problems computationally.

## How It's Best Learned
Derive the differential forms from the integral versions using the divergence and Stokes theorems. Practice interpreting each equation physically: ∇·E relates to local charge density, ∇·B = 0 reflects no monopoles, ∇×E = -∂B/∂t couples electric and magnetic fields, and ∇×B involves current and displacement current.

## Common Misconceptions
- Thinking divergence and curl are abstract; remember they describe how fields spread out and circulate.
- Applying these equations outside their domain of validity (classical limit, non-relativistic speeds).
- Neglecting boundary conditions, which are essential for solving the resulting differential equations.

## Explainer

You know the integral forms of Maxwell's equations: Gauss's law relates total electric flux through a closed surface to enclosed charge; Ampere-Maxwell relates B's circulation around a loop to enclosed current plus displacement current; Faraday's law relates E's circulation to the rate of change of magnetic flux; and the magnetic Gauss's law says no net magnetic flux ever exits a closed surface. The differential forms say the same things, but at every individual point in space rather than averaged over finite regions — a far more powerful perspective for deriving new results and solving problems computationally.

The translation uses two theorems from vector calculus you've studied: the divergence theorem (converts a surface flux integral into a volume integral of ∇·F) and Stokes's theorem (converts a circulation integral into a surface integral of ∇×F). Applying these to the integral forms yields the four differential equations. **∇·E = ρ/ε₀** (Gauss): the divergence of E at a point equals the charge density there. Where there is positive charge, E field lines diverge outward; where negative charge, they converge inward. No charge means no net divergence — E lines pass straight through. **∇·B = 0** (magnetic Gauss): B always has zero divergence everywhere — B field lines form closed loops, never beginning or ending.

**∇×E = −∂B/∂t** (Faraday): the curl of E at a point equals the negative rate of change of B at that point. Where B is increasing in time, E circulates around it — this is what drives current in a transformer secondary coil. **∇×B = μ₀J + μ₀ε₀∂E/∂t** (Ampere-Maxwell): B circulates around regions of current density J, and also around regions where E is changing in time. That last term — the **displacement current** μ₀ε₀∂E/∂t that Maxwell added — is what makes the four equations consistent and predicts electromagnetic waves even in vacuum.

The differential forms become essential when deriving the electromagnetic wave equation. Take the curl of Faraday's law: ∇×(∇×E) = −∂(∇×B)/∂t. Substitute Ampere-Maxwell (with J = 0 in vacuum): ∇×(∇×E) = −μ₀ε₀∂²E/∂t². Apply the vector identity ∇×(∇×E) = ∇(∇·E) − ∇²E, and use ∇·E = 0 in free space: the result is ∇²E = μ₀ε₀∂²E/∂t², the wave equation, with propagation speed c = 1/√(μ₀ε₀). This derivation — entirely impossible without the differential forms — is one of the great results in physics. It showed that light is an electromagnetic wave, unifying optics and electromagnetism.
