---
id: directional-derivatives
title: Directional Derivatives
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector
  type: hard
- id: dot-product
  type: hard
builds-toward:
- conservative-fields
tags:
- directional-derivative
- gradient
- unit-vector
- rate-of-change
stage: formal-systems
status: validated
---

# Directional Derivatives

## Core Idea
The directional derivative D_u f gives the rate of change of f in an arbitrary direction specified by a unit vector u. It is computed as D_u f = ∇f · u — the dot product of the gradient with the unit direction vector. This unifies partial derivatives (which are directional derivatives along coordinate axes) with the gradient (which is the direction of maximum directional derivative). The maximum value of D_u f over all unit vectors u is |∇f|, achieved when u = ∇f/|∇f|.

## How It's Best Learned
Present directional derivatives as answering the question: 'How fast does f change if I walk in direction u?' Then show that the formula D_u f = ∇f · u follows naturally. Have students compute directional derivatives for several directions at a single point and verify that the maximum occurs in the gradient direction.

## Common Misconceptions
- The direction vector u must be a unit vector; using a non-unit vector gives a scaled result.
- D_u f = ∇f · u, not |∇f| · |u|; the dot product formula includes the angle between ∇f and u.
- Directional derivatives can be negative (when moving in a direction that decreases f).

## Explainer

From partial derivatives, you know how to measure the rate of change of f in the x-direction (holding y fixed) and the y-direction (holding x fixed). But these are just two special directions among infinitely many. The **directional derivative** D_u f answers the more general question: how fast does f change if you move in an arbitrary direction u? The answer turns out to be completely determined by the gradient you already know: D_u f = ∇f · u, the dot product of the gradient with the unit direction vector.

The dot product formula is not a coincidence — it is the content of the theorem. Since |u| = 1, the dot product gives D_u f = |∇f| cos θ, where θ is the angle between ∇f and u. This single formula encodes all directional information. When u points in the gradient direction (θ = 0°), you get the maximum rate of change: D_u f = |∇f|. When u is perpendicular to ∇f (θ = 90°), the rate of change is zero — you are moving along a **level curve** where f is momentarily constant. When u points directly opposite to ∇f (θ = 180°), you get the steepest descent: D_u f = −|∇f|. The gradient is not just one derivative among many; it is the master object from which every directional derivative is computed as a projection.

This gives the **gradient a precise geometric meaning**: its direction is the direction of steepest ascent, and its magnitude is the rate of steepest ascent in that direction. Every other directional derivative is the cosine-scaled shadow of this maximum onto your chosen direction. The practical consequence is immediate: in gradient descent (used throughout optimization and machine learning), the update step moves in the direction of −∇f because that is exactly the direction that decreases f most steeply per unit step.

The requirement that u be a **unit vector** is not pedantry. Without normalization, the formula ∇f · v for an arbitrary vector v conflates two different things: the direction of travel and the distance of the step. A unit vector encodes pure direction; scaling by |v| changes the rate of change, not the direction. If you use a non-unit vector v, you get ∇f · v = (D_{v/|v|} f) · |v|, which is the directional derivative scaled by the step length. The unit-vector convention ensures that D_u f is purely a geometric quantity about the slope of f in direction u, independent of any chosen step size.
