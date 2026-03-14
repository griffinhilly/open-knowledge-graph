---
id: surface-integrals-flux
title: Surface Integrals and Flux of Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: greens-theorem
  type: hard
- id: parametric-surfaces
  type: hard
builds-toward:
- stokes-and-divergence-theorems
tags:
- surface-integrals
- flux
- normal-vectors
stage: formal-systems
status: draft
---

# Surface Integrals and Flux of Vector Fields

## Core Idea
The surface integral ∬_S F · dS computes flux (net flow of F through S). Using parametrization r(u, v), dS = (r_u × r_v) du dv, and the integral becomes ∬_D F(r(u,v)) · (r_u × r_v) du dv. Orientation (choice of normal direction) affects the sign.
