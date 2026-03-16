---
id: curl-divergence
title: Curl and Divergence
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: curl-and-divergence
  type: hard
- id: partial-derivatives-basics
  type: hard
builds-toward:
- greens-theorem
- stokes-theorem
- divergence-theorem
tags:
- curl
- divergence
stage: formal-systems
status: draft
---

# Curl and Divergence

## Core Idea
For F = (P, Q, R), curl is ∇×F = (R_y - Q_z, P_z - R_x, Q_x - P_y) (rotation), and divergence is ∇·F = P_x + Q_y + R_z (outflow). Conservative fields have curl = 0.

## Explainer

From your work with partial derivatives, you know that ∂f/∂x measures how a scalar function changes in the x-direction while other variables are held fixed. Curl and divergence extend this idea to **vector fields** — functions F that assign a vector to each point in space. Where a scalar function has one rate of change per direction, a vector field has many partial derivatives interacting with each other, and curl and divergence are specific combinations that extract physically meaningful information.

**Divergence** measures whether a vector field is spreading out or compressing at each point. For F = (P, Q, R), the divergence is ∇·F = ∂P/∂x + ∂Q/∂y + ∂R/∂z — the sum of the "self-derivatives" of each component. Think of F as the velocity field of a fluid. At each point, divergence measures the net rate at which fluid is expanding away from that point. If ∇·F > 0 at a point, fluid is being created there (a **source**). If ∇·F < 0, fluid is draining away (a **sink**). If ∇·F = 0 everywhere, the fluid is incompressible — as much flows in as flows out. Divergence is a scalar: one number at each point.

**Curl** measures the local rotation in a vector field. For F = (P, Q, R), the curl is ∇×F = (∂R/∂y − ∂Q/∂z, ∂P/∂z − ∂R/∂x, ∂Q/∂x − ∂P/∂y) — the "cross-derivatives" between different components. In the fluid analogy: if you placed a tiny paddle wheel at a point in the fluid, would it spin? Curl measures this local rotation. Its direction gives the axis of rotation (by the right-hand rule), and its magnitude gives the angular speed. A field with ∇×F = **0** everywhere is called **irrotational** or **conservative** — it has no local spin. Conservative fields are exactly the gradient fields (F = ∇φ for some scalar potential φ), and line integrals around closed loops in such fields are always zero.

Both operations are organized through the **del operator** ∇ = (∂/∂x, ∂/∂y, ∂/∂z) treated as a formal vector. Divergence is the dot product ∇·F (scalar output), and curl is the cross product ∇×F (vector output). This notation is more than a mnemonic — the antisymmetry of the cross product correctly captures why curl reverses when you flip orientation, and why the identity ∇·(∇×F) = 0 holds identically (the divergence of any curl is zero). These two operations are the key ingredients in the major theorems ahead — Green's theorem in the plane, Stokes' theorem on surfaces, and the Divergence Theorem in space — which relate curl and divergence to the boundary behavior of vector fields.
