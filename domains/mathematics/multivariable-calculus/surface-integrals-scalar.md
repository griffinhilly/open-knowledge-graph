---
id: surface-integrals-scalar
title: Surface Integrals of Scalar Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: parametric-surfaces
  type: hard
- id: double-integrals-cartesian
  type: hard
- id: line-integrals-scalar
  type: soft
builds-toward:
- flux-integrals
- stokes-theorem
- divergence-theorem
tags:
- surface-integral
- scalar
- area
- mass
- surface
stage: formal-systems
status: validated
---

# Surface Integrals of Scalar Functions

## Core Idea
The surface integral ∬_S f dS integrates a scalar function f over a surface S, where dS = |r_u × r_v| dA is the surface area element. When f = 1, the integral gives the surface area of S. When f is a mass density, it gives the total mass of a thin shell with that density. The computation converts the surface integral into a double integral over the parameter domain: ∬_S f dS = ∬_D f(r(u,v)) |r_u × r_v| dA.

## How It's Best Learned
Connect to arc length of a curve — surface integrals are the 2D analogue where the 'speed factor' |r′(t)| becomes |r_u × r_v|. Begin with explicit surfaces z = f(x,y), for which |r_x × r_y| = √(f_x² + f_y² + 1), before generalizing to parametric surfaces. Surface area of a sphere is a good benchmark computation.

## Common Misconceptions
- The surface area element dS = |r_u × r_v| dA; forgetting this factor (using dA instead) gives the projected area, not the actual surface area.
- For z = g(x, y) parametrized by (x, y), dS = √(g_x² + g_y² + 1) dx dy — the +1 accounts for the z-component.
- Scalar surface integrals are orientation-independent; only vector surface integrals (flux integrals) depend on which side of the surface is 'outward.'
