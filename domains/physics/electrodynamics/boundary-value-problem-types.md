---
id: boundary-value-problem-types
title: Classification of Boundary Value Problems
domain: physics
course: electrodynamics
prerequisites:
- id: laplace-poisson-equations-electrostatics
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- green-function-method-electrostatics
- spherical-harmonics-electrostatics
tags:
- boundary-conditions
- dirichlet
- neumann
- mixed-boundary-conditions
stage: advanced
status: draft
---

# Classification of Boundary Value Problems

## Core Idea
Boundary value problems are classified by the type of boundary condition: Dirichlet (potential specified), Neumann (normal field specified), or mixed. The uniqueness theorem establishes that each type has a unique solution under appropriate regularity conditions.

## Explainer

From Laplace's and Poisson's equations you know that the electrostatic potential V satisfies ∇²V = 0 in free space (or ∇²V = −ρ/ε₀ with sources). These are partial differential equations with infinitely many solutions taken alone. A **boundary value problem** (BVP) pins down the unique physical solution by specifying conditions on V at the boundaries of the region. The classification of BVPs by boundary condition type tells you what physical information you need to specify and whether a unique solution is guaranteed.

A **Dirichlet boundary condition** specifies the value of the potential V itself on the boundary. This corresponds physically to grounded or held-at-fixed-voltage conductors: you know V = 0 on a grounded surface or V = V₀ on a conductor held at potential V₀. This is the most common type in electrostatics. The Dirichlet problem always has a unique solution when V is specified on a closed surface enclosing the region of interest — a consequence of the maximum principle for harmonic functions.

A **Neumann boundary condition** specifies the normal derivative ∂V/∂n on the boundary, which equals −E_n, the normal component of the electric field. This arises when you know the surface charge density (since σ = ε₀E_n from the boundary condition on E) but not the potential itself. For example, if charge is deposited on an insulating surface where you know the charge density but not the resulting potential, you have a Neumann problem. Neumann problems have a unique solution up to an additive constant — you can always add a constant to V without changing E.

**Mixed boundary conditions** specify V on part of the boundary and ∂V/∂n on the rest. Real problems often combine grounded conductors (Dirichlet) with insulating surfaces carrying known charge (Neumann) in the same geometry. The **uniqueness theorem** — proved by supposing two solutions exist, subtracting them, and showing the difference must be zero — is the key theoretical result: it tells you that finding any solution satisfying the boundary conditions is sufficient, because that solution is the only one. This justifies powerful shortcut methods like the method of images, where you replace a complex physical setup with a simpler equivalent that happens to satisfy the same boundary conditions.
