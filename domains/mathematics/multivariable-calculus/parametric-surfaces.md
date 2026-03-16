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

## Explainer

You already know how a **vector-valued function** r(t) traces a curve by mapping a one-dimensional parameter t to points in ℝ³. A **parametric surface** extends this idea to two parameters: r(u, v) = ⟨x(u,v), y(u,v), z(u,v)⟩ maps a region in the (u, v) parameter plane to a surface in ℝ³. As u and v range over their domain, r sweeps out a two-dimensional sheet in space. This lets you describe surfaces — spheres, cylinders, tori, graphs — in a uniform framework, even when no single formula z = f(x, y) can describe them.

The derivatives from your prerequisite on **partial derivatives** now describe the surface's local geometry. The partial derivative r_u = ∂r/∂u is the tangent vector you get by moving along the surface in the u-direction (holding v fixed). Similarly, r_v is the tangent vector in the v-direction. At any smooth point of the surface, these two vectors span the **tangent plane** — the plane that best approximates the surface at that point. From your knowledge of the **cross product**, you know that r_u × r_v is perpendicular to both tangent vectors. This cross product is therefore a **normal vector** to the surface.

The magnitude |r_u × r_v| is the most important quantity for integration. Imagine a small rectangle in the parameter domain with dimensions du × dv. Its image on the surface is a small parallelogram with sides r_u du and r_v dv. The area of a parallelogram spanned by two vectors equals the magnitude of their cross product, so the area element on the surface is dS = |r_u × r_v| du dv. This is the surface analogue of the Jacobian factor r that appeared in polar coordinates: it converts parameter-space area into actual surface area. Every surface integral you will compute — for scalar quantities and for flux — uses this formula.

To use parametric surfaces in practice, you need to parametrize familiar shapes. A sphere of radius R uses spherical angles: r(φ, θ) = ⟨R sin φ cos θ, R sin φ sin θ, R cos φ⟩ for φ ∈ [0, π], θ ∈ [0, 2π). A cylinder of radius R and height h uses r(θ, z) = ⟨R cos θ, R sin θ, z⟩. A graph z = f(x, y) parametrizes trivially: r(x, y) = ⟨x, y, f(x, y)⟩, which gives r_x × r_y = ⟨−f_x, −f_y, 1⟩ and |r_x × r_y| = √(f_x² + f_y² + 1), recovering the surface area formula you may have seen earlier. The power of the parametric framework is that all three cases use the same r_u × r_v calculation, regardless of how different the surfaces look.
