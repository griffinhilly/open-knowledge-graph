---
id: surface-parametrization-tangent
title: Parametric Surfaces and Tangent Vectors
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: change-of-variables-jacobian
  type: hard
builds-toward:
- surface-area-integrals
- surface-integrals-flux
tags:
- parametric-surfaces
- tangent-vectors
- normal-vectors
stage: formal-systems
status: draft
---

# Parametric Surfaces and Tangent Vectors

## Core Idea
A surface can be parametrized as r(u, v) = ⟨x(u, v), y(u, v), z(u, v)⟩. The tangent vectors r_u and r_v span the tangent plane. The normal vector n = r_u × r_v is perpendicular to the surface and has magnitude equal to the local area scaling factor.

## Explainer

From your work with the Jacobian, you know that changing variables in an integral introduces a scaling factor that accounts for how the coordinate transformation stretches or compresses area. **Parametric surfaces** use the same idea to describe curved surfaces in R³: you have a flat parameter domain (a region in the uv-plane) and a function r(u, v) = ⟨x(u, v), y(u, v), z(u, v)⟩ that maps it to a surface in R³. Just as parametric curves trace paths in space as a single parameter moves, parametric surfaces fill out two-dimensional sheets as two parameters move simultaneously. For example, a sphere of radius 1 is parametrized by r(φ, θ) = ⟨sin φ cos θ, sin φ sin θ, cos φ⟩ for φ ∈ [0, π] and θ ∈ [0, 2π].

The **tangent vectors** r_u and r_v arise as partial derivatives of r with respect to each parameter. Holding v constant and varying u traces a curve on the surface; its velocity vector at any point is r_u = ⟨∂x/∂u, ∂y/∂u, ∂z/∂u⟩. Similarly, r_v is tangent to the u = constant curves. These two vectors lie in the **tangent plane** of the surface at the corresponding point — they are the tangent plane's natural basis vectors at that point, playing the same role that the columns of the Jacobian play for planar coordinate changes. Together they span the tangent plane, provided they are not parallel (i.e., they are linearly independent, which is the condition that r is a regular parametrization).

The **normal vector** n = r_u × r_v is constructed via the cross product, which automatically produces a vector perpendicular to both r_u and r_v — hence perpendicular to the tangent plane and therefore normal to the surface. Its direction points "outward" (or "inward," depending on orientation), and its magnitude |r_u × r_v| measures the local area scaling factor: a small rectangle du × dv in the parameter domain maps to a parallelogram on the surface with area |r_u × r_v| du dv. This is exactly the surface-area element dS = |r_u × r_v| du dv, the key piece in computing surface area integrals.

The connection to the Jacobian is direct. For a surface z = g(x, y) over a region in the xy-plane, you can parametrize with r(x, y) = ⟨x, y, g(x, y)⟩. Then r_x = ⟨1, 0, gₓ⟩ and r_y = ⟨0, 1, g_y⟩, and their cross product has magnitude √(gₓ² + g_y² + 1), recovering the classical surface area formula. For a general parametrization, the Jacobian of the map (u, v) ↦ (x, y, z) is the 3 × 2 matrix with columns r_u and r_v, and |r_u × r_v| is the "generalized Jacobian determinant" (the magnitude of the unique vector whose square equals the Gram determinant det(JᵀJ)). Everything downstream — surface area integrals, flux integrals, Stokes' theorem — builds on this local geometry of r_u, r_v, and their cross product.
