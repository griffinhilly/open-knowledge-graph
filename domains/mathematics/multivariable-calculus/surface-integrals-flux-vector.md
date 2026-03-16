---
id: surface-integrals-flux-vector
title: Surface Integrals and Flux of Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: surface-integrals-scalar-function
  type: hard
- id: surface-integrals-flux
  type: hard
builds-toward:
- stokes-theorem-applications
- divergence-theorem-applications
tags:
- flux
- vector-fields
- surface-integrals
stage: formal-systems
status: draft
---

# Surface Integrals and Flux of Vector Fields

## Core Idea
The flux of F through oriented surface S is ∬_S F · n dS = ∬_S F · (r_u × r_v) du dv, measuring flow through the surface. When F is the curl of another vector field, Stokes' theorem relates this to a line integral around the boundary.

## Explainer

From your work with scalar surface integrals, you know how to integrate a function f over a surface S: parameterize the surface as r(u, v), compute the cross product r_u × r_v to get the area element dS = |r_u × r_v| du dv, and integrate ∬_D f(r(u,v)) |r_u × r_v| du dv. This measures "how much of f accumulates on S." The **flux of a vector field** through a surface asks a different question entirely: not how much of a scalar quantity sits on S, but how much of a vector field F passes through S. This requires the surface to be **oriented** — equipped with a consistent choice of "which side is the outside," specified by a unit normal vector **n** at each point.

The central idea is that only the component of F perpendicular to the surface contributes to flow through it. If F points directly along the normal, it passes through the surface at full strength. If F is tangent to the surface (perpendicular to n), it slides along without crossing. The contribution at each point is F · **n** — the dot product projects F onto the normal direction. The total **flux** is the surface integral ∬_S F · **n** dS. Since **n** = (r_u × r_v)/|r_u × r_v| and dS = |r_u × r_v| du dv, the magnitude |r_u × r_v| cancels, leaving the clean formula: ∬_S F · **n** dS = ∬_D F(r(u,v)) · (r_u × r_v) du dv. The cross product encodes both the surface area element and the normal direction in one object.

Orientation is not a formality — it changes the sign of the flux. The cross product r_u × r_v points in one of two possible normal directions depending on the parameterization; reversing the parameterization's order (swapping u and v) reverses the cross product and negates the integral. For a closed surface (like a sphere), the convention is that the outward normal points away from the enclosed region. For a surface with boundary (like a hemisphere or a disk), the orientation of the boundary curve and the surface normal are linked by the right-hand rule. Getting orientation right means checking, after computing r_u × r_v, that the result points in the intended direction — and if not, negating the entire integral.

The physical interpretation is the reason all of this machinery matters. For a fluid with velocity field F, the flux of F through a surface S measures the volume of fluid crossing S per unit time — positive if the flow is in the direction of **n**, negative if it opposes **n**. For an electric field, it is electric flux. This quantity is the foundation of the Divergence Theorem: the total flux of F outward through a closed surface equals the integral of ∇·F over the enclosed volume. If ∇·F = 0 (an incompressible fluid or a divergence-free field), exactly as much flows in as flows out through any closed surface, and the net flux is zero. The flux integral is therefore not just a computation — it is the precise formalization of "how much of a vector field crosses a boundary," which is the central object in all three fundamental theorems of vector calculus you are about to encounter.
