---
id: flux-integrals
title: Flux Integrals of Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: surface-integrals-scalar
  type: hard
builds-toward:
- stokes-theorem
- divergence-theorem
tags:
- flux
- surface-integral
stage: formal-systems
status: draft
---

# Flux Integrals of Vector Fields

## Core Idea
The flux of F through surface S: ∬_S F · dS = ∬_S F · n dS, where n is the unit normal. If S is parametrized, ∬_S F · dS = ∬_D F · (r_u × r_v) du dv. Flux measures flow rate through the surface.

## Explainer

From scalar surface integrals, you know how to integrate a real-valued function over a surface — you weigh each area element dS by the function's value and sum. A **flux integral** extends this to vector fields: instead of a scalar function, you have a vector field F assigning a flow vector to every point in space, and you want to measure how much of that flow passes through the surface. Think of F as the velocity field of a fluid. Flux answers the question: how many liters per second pass through this membrane?

The physical insight is that only the component of F *perpendicular* to the surface contributes to flow through it. Flow parallel to the surface skims along without crossing. To isolate the perpendicular component, you take the dot product of F with the **unit normal** n̂ to the surface at each point. The scalar F · n̂ tells you the flow rate per unit area at that point (positive if flowing "outward," negative if flowing "inward"). The flux integral ∬_S F · n̂ dS then sums this rate over the entire surface. Choosing an orientation — which side of the surface is "positive" — amounts to choosing a consistent direction for n̂, and flux changes sign if you reverse the orientation.

To compute this in practice, you parametrize the surface as r(u, v) over a domain D in the uv-plane. The partial derivatives r_u and r_v span the tangent plane at each point, so their cross product r_u × r_v is perpendicular to the surface and its magnitude equals the area scaling factor — exactly the role played by the area element ‖r_u × r_v‖ du dv in scalar surface integrals. For flux, you take the *vector* area element **dS** = (r_u × r_v) du dv (without normalizing), so the integral becomes ∬_D F(r(u,v)) · (r_u × r_v) du dv. This bundles the dot product with the normal and the area scaling into a single expression, making computation direct.

Orientation choices matter carefully here. The cross product r_u × r_v points to one side of the surface; if you swap u and v, it points to the other side. For a closed surface like a sphere, the convention is outward-pointing normals; for an open surface like an upper hemisphere, you specify the orientation explicitly. Getting orientation wrong flips the sign of the answer — the flux of an outward-flowing field is positive for outward normals, negative if you accidentally use inward normals.

Flux integrals are the key ingredient in the two great theorems that follow: **Stokes' theorem** relates the flux of a curl through a surface to a line integral around its boundary, and the **Divergence theorem** relates the flux of a vector field through a closed surface to the triple integral of its divergence over the enclosed volume. Both theorems generalize the Fundamental Theorem of Calculus to higher dimensions, and both reduce abstract spatial relationships to computable integrals. Flux is the quantity that makes these connections precise.
