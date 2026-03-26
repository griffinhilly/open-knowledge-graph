---
id: surface-integrals-scalar
title: Surface Integrals of Scalar Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: parametric-surfaces
  type: hard
- id: cross-product
  type: hard
builds-toward:
- surface-integrals-vector
- stokes-theorem
tags:
- surface-integral
- area
stage: formal-systems
status: validated
---

# Surface Integrals of Scalar Functions

## Core Idea
The surface integral ∬_S f dS integrates f over surface S. If S is parametrized as r(u,v), then dS = ||r_u × r_v|| du dv, and ∬_S f dS = ∬_D f(r(u,v)) ||r_u × r_v|| du dv.

## Questions

```yaml
- question: "What role does the factor ||r_u × r_v|| play in the surface integral ∬_S f dS = ∬_D f(r(u,v)) ||r_u × r_v|| du dv?"
  type: multiple-choice
  options:
    - "It gives the unit normal direction to orient the surface"
    - "It converts from parameter space area to actual surface area, accounting for how the parametrization stretches or compresses the surface"
    - "It ensures the integral converges by bounding the integrand"
    - "It computes the volume enclosed beneath the surface"
  answer: 1
  explanation: "The factor ||r_u × r_v|| is the Jacobian of the parametrization — it measures how much area in the parameter domain (du dv) corresponds to actual surface area (dS). When the surface tilts or stretches relative to parameter space (as with a hemisphere tilting toward its equator), this factor compensates. Option A describes the direction of r_u × r_v (a normal vector), not its magnitude."

- question: "For the flat surface r(x, y) = (x, y, 0) parametrized over a region D in the xy-plane, what is ||r_x × r_y||?"
  type: multiple-choice
  options:
    - "0, because the flat surface has no curvature"
    - "1, because this parametrization maps the parameter domain to the surface without any stretching"
    - "x² + y², accounting for the distance from the origin"
    - "√2, because two coordinate vectors are combined"
  answer: 1
  explanation: "r_x = (1, 0, 0) and r_y = (0, 1, 0), so r_x × r_y = (0, 0, 1), which has magnitude 1. A flat surface parametrized directly by its own coordinates has no stretching — the parameter area equals the surface area exactly. This makes intuitive sense: integrating f = 1 over D with dS = 1 · dx dy gives the ordinary area of D, as expected."

- question: "The surface area element dS = ||r_u × r_v|| du dv is the 2D analogue of the arc length element ds = ||r'(t)|| dt."
  type: true-false
  answer: true
  explanation: "The analogy is precise. For a curve, ||r'(t)|| converts from the parameter t to arc length — it is the 'speed' of the curve. For a surface, ||r_u × r_v|| converts from the 2D parameter area du dv to actual surface area dS. In both cases, the magnitude of the derivative(s) is the Jacobian that accounts for how the parametrization maps to geometry."

- question: "The value of a surface integral ∬_S f dS depends on which parametrization of S you choose — different parametrizations give different answers."
  type: true-false
  answer: false
  explanation: "The surface integral is a geometric quantity intrinsic to the surface S and the function f — it does not depend on the parametrization. Different parametrizations produce different integrands (different ||r_u × r_v||), but these differences exactly cancel when the domain of integration changes accordingly. The final numerical value is the same. This is analogous to how the arc length of a curve is independent of how you parametrize it."

- question: "Explain why the cross product r_u × r_v appears in the surface integral formula. What geometric quantity does its magnitude represent?"
  type: short-answer
  answer: "The partial derivatives r_u and r_v are tangent vectors to the surface in the u- and v-directions. A small rectangle [u, u+du] × [v, v+dv] in parameter space maps to a small parallelogram on the surface spanned by r_u · du and r_v · dv. The area of a parallelogram spanned by two vectors equals the magnitude of their cross product, so ||r_u × r_v|| du dv is the area of that surface patch — the infinitesimal surface area element dS."
  explanation: "This connects the formula back to the cross product's geometric meaning. The cross product r_u × r_v simultaneously gives the area (via its magnitude) and the normal direction (via its direction) of the surface patch. For scalar surface integrals, only the magnitude matters; for vector surface integrals (flux), the direction matters too, which is why orientation becomes significant in the next topic."
```

## Explainer

Recall how arc length works for a curve. If a curve is parametrized by r(t) for t ∈ [a, b], then the arc length element is ds = ||r'(t)|| dt — the speed of the parametrization. You integrate a scalar function f along the curve as ∫f ds = ∫f(r(t))||r'(t)|| dt. The ||r'(t)|| factor converts from the parametrization's time variable to actual geometric length. **Surface integrals of scalar functions** are the exact analogue in one dimension higher: instead of a curve with a 1D parametrization r(t), you have a surface with a 2D parametrization r(u, v).

The surface element dS is the infinitesimal area patch corresponding to a small rectangle [u, u+du] × [v, v+dv] in the parameter domain. The two partial derivatives r_u = ∂r/∂u and r_v = ∂r/∂v are tangent vectors to the surface in the u- and v-directions. From your work with the cross product in 3D, you know that ||r_u × r_v|| equals the area of the parallelogram spanned by r_u and r_v. So the area of the small patch is exactly ||r_u × r_v|| du dv. This is **dS**, the surface area element — the 2D analogue of ||r'(t)|| dt.

The full integral is ∬_S f dS = ∬_D f(r(u,v)) ||r_u × r_v|| du dv, where D is the parameter domain. Three steps: parametrize the surface as r(u, v) over a region D; compute the cross product r_u × r_v and its magnitude; substitute the parametrization into f and multiply by the magnitude. The result is an ordinary double integral over D. The magnitude ||r_u × r_v|| is the Jacobian of the parametrization — it accounts for how the map from parameter space to the surface stretches or compresses area.

A concrete example clarifies the computation. For the hemisphere z = √(1 − x² − y²) of radius 1, parametrize using r(x, y) = (x, y, √(1 − x² − y²)) over the unit disk D. Compute r_x = (1, 0, −x/z) and r_y = (0, 1, −y/z), then r_x × r_y = (x/z, y/z, 1), so ||r_x × r_y|| = √(x²/z² + y²/z² + 1) = 1/z. Integrating f = 1 gives the surface area: ∬_D (1/z) dx dy, which in polar coordinates evaluates to 2π — the expected area of a unit hemisphere. The factor 1/z reflects how the hemisphere tilts away from vertical as you move toward the equator, stretching the area element relative to its projection on the xy-plane.

Surface integrals of scalar functions compute physical quantities like total mass (integrate density over a thin shell), total charge on a surface, or simply surface area. They are the foundation for the next step: surface integrals of vector fields (flux integrals), where the integrand is a dot product with the surface normal rather than a scalar function evaluated on the surface.
