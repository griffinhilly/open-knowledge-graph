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
