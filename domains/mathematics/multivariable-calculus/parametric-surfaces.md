---
id: parametric-surfaces
title: Parametric Surfaces
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-valued-functions
  type: hard
- id: partial-derivatives
  type: hard
- id: cross-product
  type: hard
builds-toward:
- surface-integrals-scalar
- flux-integrals
tags:
- parametric-surface
- normal-vector
- surface
- tangent-plane
stage: formal-systems
status: validated
---

# Parametric Surfaces

## Core Idea
A parametric surface is described by a vector function r(u, v) = ⟨x(u,v), y(u,v), z(u,v)⟩ mapping a 2D parameter domain to a surface in ℝ³. The partial derivatives r_u and r_v are tangent vectors to the surface, and their cross product r_u × r_v gives a normal vector to the surface. The magnitude |r_u × r_v| is the surface area element dS for surface integrals. Parametric surfaces generalize from explicit surfaces z = f(x,y) to surfaces that may loop back or cannot be expressed as functions.

## How It's Best Learned
Practice parametrizing familiar surfaces: sphere (using spherical angles), cylinder (using angle and height), and the graph z = f(x,y) (using x and y directly). For each, compute r_u × r_v and verify that it points outward (or inward). Emphasize that the parametrization is not unique — the same surface has infinitely many valid parametrizations.

## Common Misconceptions
- The normal vector r_u × r_v is not generally a unit vector; its magnitude |r_u × r_v| is the area scaling factor.
- If r_u × r_v = 0 at a point, the surface has a singularity at that parameter value (e.g., the north pole of a sphere in standard parametrization).
- The orientation of the normal (inward vs outward) depends on the order of r_u × r_v vs r_v × r_u.
