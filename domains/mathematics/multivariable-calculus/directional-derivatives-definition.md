---
id: directional-derivatives-definition
title: Directional Derivatives and Rate of Change
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector-definition
  type: hard
- id: directional-derivatives
  type: hard
builds-toward:
- tangent-planes
- chain-rule-multivariable
tags:
- directional-derivatives
- rate-of-change
- dot-product
stage: formal-systems
status: draft
---

# Directional Derivatives and Rate of Change

## Core Idea
The directional derivative D_u f(a, b) = ∇f(a, b) · u measures the rate of change of f at (a, b) in direction u (where u is a unit vector). It equals |∇f| cos(θ), where θ is the angle between ∇f and u.

## Explainer

You know the **gradient** ∇f = ⟨f_x, f_y⟩: it packages both partial derivatives into a single vector. You also have an introduction to directional derivatives. Now the key insight is how these connect: the **directional derivative** D_u f at a point is the rate of change of f in the direction of unit vector u, and it is computed simply as the dot product D_u f = ∇f · u. This formula unifies all rate-of-change information about f into a single object — once you know the gradient, you can find the rate of change in any direction instantly.

The geometric picture is clearest with an analogy. Imagine f(x,y) describes the elevation of a hillside, and you are standing at point (a,b). The gradient ∇f(a,b) is a vector that points in the direction of steepest ascent, with magnitude equal to that maximum slope. If you walk in direction u (a unit vector), the directional derivative D_u f = ∇f · u tells you the slope you experience. This is just the dot product formula: ∇f · u = |∇f| cos(θ), where θ is the angle between your walking direction u and the steepest-ascent direction ∇f.

Three special cases follow immediately from the cosine formula. When θ = 0 (you walk directly uphill, in the direction of ∇f), cos θ = 1 and D_u f = |∇f| — the maximum rate of increase. When θ = π (you walk directly downhill, opposite to ∇f), D_u f = −|∇f| — the maximum rate of decrease. When θ = π/2 (you walk perpendicular to ∇f, along a **level curve**), cos θ = 0 and D_u f = 0 — no change in elevation. This is why the gradient is always perpendicular to level curves: moving along a level curve produces zero rate of change in f, which means the direction of travel must be perpendicular to ∇f.

Requiring u to be a **unit vector** is essential: without it, D_u f would depend on how fast you walk, not just the direction. Scaling u by 2 would double the dot product, but the slope of the hill does not depend on your speed. By normalizing u to length 1, you ensure D_u f measures slope — rate of change per unit distance traveled — rather than an arbitrary scaled version. Always normalize your direction vector before computing a directional derivative.
