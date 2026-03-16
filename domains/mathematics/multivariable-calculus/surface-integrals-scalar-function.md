---
id: surface-integrals-scalar-function
title: Surface Integrals of Scalar Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: surface-area-integrals
  type: hard
builds-toward:
- surface-integrals-flux
tags:
- surface-integrals
- scalar-functions
stage: formal-systems
status: draft
---

# Surface Integrals of Scalar Functions

## Core Idea
∬_S f(x, y, z) dS integrates a scalar function over a surface. For parametrization r(u, v), this equals ∬_D f(r(u, v)) |r_u × r_v| du dv. Applications include mass of a thin shell (integrating density ρ) and average value on a surface.

## Explainer

From surface area integrals, you know that the area of a parametric surface r(u, v) over a region D is ∬_D |r_u × r_v| du dv. The factor |r_u × r_v| is the area magnification: it converts the flat (u, v) area element du dv into the actual curved surface area element dS. A surface integral of a scalar function is conceptually one small step beyond this: instead of summing up area elements equally, you weight each area element by the value of a function f at that point on the surface.

Formally, ∬_S f(x, y, z) dS = ∬_D f(r(u, v)) |r_u × r_v| du dv. The dS notation stands for "scalar surface area element" — each infinitesimal patch of surface contributes its area |r_u × r_v| du dv, multiplied by the function value f at that patch. If f = 1 everywhere, you recover the surface area formula as a special case, which confirms the geometry is consistent. If f is a **density** (mass per unit area), then ∬_S ρ dS gives the total mass of a thin shell with that density distribution — exactly analogous to how ∫_a^b ρ(x) dx gives mass of a rod.

The analogy with line integrals is worth making explicit. A line integral ∫_C f ds integrates a scalar function along a curve by weighting arc length elements ds = |r′(t)| dt by the function value. A surface integral does the same thing one dimension up: it weights surface area elements dS by the function value. The pattern is consistent across dimensions — in each case you replace the geometric measure element (arc length, surface area) with a "function-weighted" version.

Computing a surface integral in practice is a three-step process: (1) parametrize the surface with r(u, v), (2) compute the cross product r_u × r_v and its magnitude, and (3) substitute and integrate over the parameter domain D. The choice of parametrization doesn't change the answer — different valid parametrizations will give the same integral value, just as different parametrizations of a curve give the same line integral. This invariance is what makes dS a geometric quantity attached to the surface rather than to any particular coordinate system. The next topic, surface integrals of vector fields, will add a direction to dS, turning it into a vector area element dS = (r_u × r_v) du dv — but the scalar case here is the foundation for that more powerful construction.
