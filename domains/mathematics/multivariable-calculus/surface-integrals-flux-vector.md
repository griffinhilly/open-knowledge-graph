---
id: surface-integrals-flux-vector
title: Surface Integrals and Flux of Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: surface-integrals-scalar-function
  type: hard
- id: surface-integrals-flux
  type: hard
builds-toward:
- stokes-theorem-applications
- divergence-theorem-applications
tags:
- flux
- vector-fields
- surface-integrals
stage: formal-systems
status: validated
---

# Surface Integrals and Flux of Vector Fields

## Core Idea
The flux of F through oriented surface S is ∬_S F · n dS = ∬_S F · (r_u × r_v) du dv, measuring flow through the surface. When F is the curl of another vector field, Stokes' theorem relates this to a line integral around the boundary.

## Questions

```yaml
- question: "A vector field F is tangent to every point on surface S — it lies parallel to the surface at each point. What is the flux ∬_S F · n dS?"
  type: multiple-choice
  options:
    - "It depends on the magnitude of F"
    - "It equals the surface area of S"
    - "Zero, because F has no component perpendicular to S"
    - "It requires knowing the parameterization to determine"
  answer: 2
  explanation: "Flux is F · n — the dot product projects F onto the unit normal. If F is everywhere tangent to S, it is everywhere perpendicular to n, so F · n = 0 at every point and the integral is zero. The magnitude of F is irrelevant; only the component in the normal direction contributes to flow through the surface."

- question: "After computing r_u × r_v for a closed surface parameterization, you find the cross product points inward rather than outward. How do you correct the flux calculation?"
  type: multiple-choice
  options:
    - "Multiply the area element |r_u × r_v| by −1"
    - "Negate the entire flux integral"
    - "Swap u and v in the parameterization to reverse the cross product"
    - "Either negating the integral or swapping u and v achieves the correct outward flux"
  answer: 3
  explanation: "Both approaches work and produce the same result. Swapping u and v reverses r_u × r_v (since r_v × r_u = −(r_u × r_v)), which negates the integral. Alternatively, just multiplying the final answer by −1 is equivalent. The key point is that orientation is a choice that determines sign — if your parameterization produces the wrong normal direction, you fix it by flipping the sign of the result, not by recomputing everything."

- question: "The flux of a vector field through a surface is generally non-negative, since it measures how much field passes through."
  type: true-false
  answer: false
  explanation: "Flux is a signed quantity. The sign depends on the orientation: if F has a component opposing the chosen normal direction n, the dot product F · n is negative at those points, and the integral can be negative. Negative flux simply means net flow in the direction opposite to n. For example, outward flux through a closed surface can be negative if the field converges inward more than it diverges outward."

- question: "For an incompressible fluid with velocity field F satisfying ∇·F = 0, the net flux of F through any closed surface is zero."
  type: true-false
  answer: true
  explanation: "By the Divergence Theorem, the net outward flux through a closed surface S equals ∭_V ∇·F dV over the enclosed volume. If ∇·F = 0 everywhere inside, this triple integral is zero. Physically, an incompressible fluid has no sources or sinks — exactly as much fluid flows into any closed region as flows out of it, so the net flux is zero."

- question: "Why does the orientation of a surface (the choice of normal direction) matter when computing flux, and what determines which direction the normal points?"
  type: short-answer
  answer: "Orientation determines the sign of the flux. Flux measures flow through a surface in a specific direction — positive when F has a component in the direction of n, negative when it opposes n. The normal direction is set by the parameterization: the cross product r_u × r_v points in one of two possible normal directions, and swapping the order u ↔ v reverses it. For closed surfaces, the convention is the outward normal (pointing away from the enclosed region). After computing r_u × r_v, you verify it points the intended way — if not, negate the integral. Getting orientation wrong doesn't change the magnitude; it flips the sign."
  explanation: "This is not merely a formality. In the Divergence Theorem, orientation must be consistent (outward for the closed surface) for the theorem to hold. In Stokes' Theorem, the boundary orientation and surface normal are linked by the right-hand rule. Every flux computation requires specifying orientation explicitly, because without it the integral is ambiguous in sign."
```

## Explainer

From your work with scalar surface integrals, you know how to integrate a function f over a surface S: parameterize the surface as r(u, v), compute the cross product r_u × r_v to get the area element dS = |r_u × r_v| du dv, and integrate ∬_D f(r(u,v)) |r_u × r_v| du dv. This measures "how much of f accumulates on S." The **flux of a vector field** through a surface asks a different question entirely: not how much of a scalar quantity sits on S, but how much of a vector field F passes through S. This requires the surface to be **oriented** — equipped with a consistent choice of "which side is the outside," specified by a unit normal vector **n** at each point.

The central idea is that only the component of F perpendicular to the surface contributes to flow through it. If F points directly along the normal, it passes through the surface at full strength. If F is tangent to the surface (perpendicular to n), it slides along without crossing. The contribution at each point is F · **n** — the dot product projects F onto the normal direction. The total **flux** is the surface integral ∬_S F · **n** dS. Since **n** = (r_u × r_v)/|r_u × r_v| and dS = |r_u × r_v| du dv, the magnitude |r_u × r_v| cancels, leaving the clean formula: ∬_S F · **n** dS = ∬_D F(r(u,v)) · (r_u × r_v) du dv. The cross product encodes both the surface area element and the normal direction in one object.

Orientation is not a formality — it changes the sign of the flux. The cross product r_u × r_v points in one of two possible normal directions depending on the parameterization; reversing the parameterization's order (swapping u and v) reverses the cross product and negates the integral. For a closed surface (like a sphere), the convention is that the outward normal points away from the enclosed region. For a surface with boundary (like a hemisphere or a disk), the orientation of the boundary curve and the surface normal are linked by the right-hand rule. Getting orientation right means checking, after computing r_u × r_v, that the result points in the intended direction — and if not, negating the entire integral.

The physical interpretation is the reason all of this machinery matters. For a fluid with velocity field F, the flux of F through a surface S measures the volume of fluid crossing S per unit time — positive if the flow is in the direction of **n**, negative if it opposes **n**. For an electric field, it is electric flux. This quantity is the foundation of the Divergence Theorem: the total flux of F outward through a closed surface equals the integral of ∇·F over the enclosed volume. If ∇·F = 0 (an incompressible fluid or a divergence-free field), exactly as much flows in as flows out through any closed surface, and the net flux is zero. The flux integral is therefore not just a computation — it is the precise formalization of "how much of a vector field crosses a boundary," which is the central object in all three fundamental theorems of vector calculus you are about to encounter.
