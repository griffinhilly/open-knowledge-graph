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

## Explainer

Recall how arc length works for a curve. If a curve is parametrized by r(t) for t ∈ [a, b], then the arc length element is ds = ||r'(t)|| dt — the speed of the parametrization. You integrate a scalar function f along the curve as ∫f ds = ∫f(r(t))||r'(t)|| dt. The ||r'(t)|| factor converts from the parametrization's time variable to actual geometric length. **Surface integrals of scalar functions** are the exact analogue in one dimension higher: instead of a curve with a 1D parametrization r(t), you have a surface with a 2D parametrization r(u, v).

The surface element dS is the infinitesimal area patch corresponding to a small rectangle [u, u+du] × [v, v+dv] in the parameter domain. The two partial derivatives r_u = ∂r/∂u and r_v = ∂r/∂v are tangent vectors to the surface in the u- and v-directions. From your work with the cross product in 3D, you know that ||r_u × r_v|| equals the area of the parallelogram spanned by r_u and r_v. So the area of the small patch is exactly ||r_u × r_v|| du dv. This is **dS**, the surface area element — the 2D analogue of ||r'(t)|| dt.

The full integral is ∬_S f dS = ∬_D f(r(u,v)) ||r_u × r_v|| du dv, where D is the parameter domain. Three steps: parametrize the surface as r(u, v) over a region D; compute the cross product r_u × r_v and its magnitude; substitute the parametrization into f and multiply by the magnitude. The result is an ordinary double integral over D. The magnitude ||r_u × r_v|| is the Jacobian of the parametrization — it accounts for how the map from parameter space to the surface stretches or compresses area.

A concrete example clarifies the computation. For the hemisphere z = √(1 − x² − y²) of radius 1, parametrize using r(x, y) = (x, y, √(1 − x² − y²)) over the unit disk D. Compute r_x = (1, 0, −x/z) and r_y = (0, 1, −y/z), then r_x × r_y = (x/z, y/z, 1), so ||r_x × r_y|| = √(x²/z² + y²/z² + 1) = 1/z. Integrating f = 1 gives the surface area: ∬_D (1/z) dx dy, which in polar coordinates evaluates to 2π — the expected area of a unit hemisphere. The factor 1/z reflects how the hemisphere tilts away from vertical as you move toward the equator, stretching the area element relative to its projection on the xy-plane.

Surface integrals of scalar functions compute physical quantities like total mass (integrate density over a thin shell), total charge on a surface, or simply surface area. They are the foundation for the next step: surface integrals of vector fields (flux integrals), where the integrand is a dot product with the surface normal rather than a scalar function evaluated on the surface.
