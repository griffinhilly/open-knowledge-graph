---
id: surface-area-integrals
title: Surface Area and Surface Integrals
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: surface-parametrization-tangent
  type: hard
builds-toward:
- surface-integrals-flux
tags:
- surface-area
- integrals
- parametric
stage: formal-systems
status: draft
---

# Surface Area and Surface Integrals

## Core Idea
The surface area of a parametrized surface r(u, v) is A = ∬_D |r_u × r_v| du dv. For a scalar integral over surface S, ∬_S f dS = ∬_D f(r(u, v)) |r_u × r_v| du dv. This extends to vector integrals via flux.

## Explainer

From your study of surface parametrization, you know how to describe a surface as a map r(u, v) from a parameter domain D ⊂ R² into R³. The partial derivatives r_u = ∂r/∂u and r_v = ∂r/∂v are tangent vectors lying in the tangent plane at each surface point. Their cross product r_u × r_v is perpendicular to the surface, and its magnitude |r_u × r_v| measures how much the parametrization stretches a small patch du × dv of parameter space into actual surface area. This **area element** |r_u × r_v| du dv is the central object in surface integration, playing the role that |r'(t)| dt plays for arc length on curves.

For total surface area, the idea is the same as arc length. Partition the parameter domain into tiny rectangles of area du dv. The corresponding patch on the surface is approximately a parallelogram spanned by the vectors r_u du and r_v dv, with area |r_u × r_v| du dv. Summing over all patches and taking the limit gives A = ∬_D |r_u × r_v| du dv. This formula applies to any smooth surface — sphere, torus, graph of a function, saddle shape — as long as you have a valid parametrization with the tangent vectors not parallel.

A **scalar surface integral** ∬_S f dS integrates a function f over the surface rather than just computing area. For each patch of surface, multiply the function value f(r(u,v)) by the area element |r_u × r_v| du dv, then sum. When f = 1, you recover total area. When f represents surface mass density (mass per unit area), the integral gives total mass. The formula is ∬_D f(r(u,v)) |r_u × r_v| du dv — the surface integral has been pulled back to an ordinary double integral over the parameter domain, with the area element providing the correct weighting for the distortion of the parametrization.

A practically important special case is a **graph surface** z = g(x, y), parametrized by r(x, y) = ⟨x, y, g(x, y)⟩. Then r_x = ⟨1, 0, g_x⟩ and r_y = ⟨0, 1, g_y⟩, so |r_x × r_y| = √(1 + g_x² + g_y²). The surface area formula becomes ∬_D √(1 + (∂z/∂x)² + (∂z/∂y)²) dA — a direct generalization of the single-variable arc length formula √(1 + (dy/dx)²) dx. When g is constant (a flat horizontal plane), the gradient terms vanish and the formula reduces to the plain area of D, which is the right answer.
