---
id: surface-integrals-scalar
title: Surface Integrals of Scalar Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: parametric-surfaces
  type: hard
- id: cross-product-3d
  type: hard
builds-toward:
- surface-integrals-vector
- stokes-theorem
tags:
- surface-integral
- area
stage: formal-systems
status: draft
---

# Surface Integrals of Scalar Functions

## Core Idea
The surface integral ∬_S f dS integrates f over surface S. If S is parametrized as r(u,v), then dS = ||r_u × r_v|| du dv, and ∬_S f dS = ∬_D f(r(u,v)) ||r_u × r_v|| du dv.
