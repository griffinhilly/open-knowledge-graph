---
id: directional-derivatives-gradient
title: Directional Derivatives and the Gradient
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: directional-derivatives
  type: hard
- id: gradient-vector
  type: hard
- id: dot-product
  type: hard
builds-toward:
- optimization-multivariable-basics
- vector-fields
tags:
- gradient
- directional-derivative
stage: formal-systems
status: draft
---

# Directional Derivatives and the Gradient

## Core Idea
The directional derivative D_u f = ∇f · u gives the rate of change in direction u (unit vector). The gradient ∇f = ⟨f_x, f_y⟩ points in the direction of steepest ascent and has magnitude equal to the maximum directional derivative.

## Explainer

Partial derivatives tell you how fast f(x, y) changes when you move parallel to the x-axis or y-axis. But what if you walk diagonally, or in some arbitrary direction? The **directional derivative** answers the general question: how fast is f changing as I move in direction **u**? The answer turns out to be encoded entirely in the **gradient** ∇f, which you've already computed, combined with the **dot product**, which extracts components.

For a unit vector **u** = ⟨a, b⟩, the directional derivative is D_**u** f = ∇f · **u** = f_x · a + f_y · b. This formula says: project the gradient onto your direction of travel and read off the rate of change. Geometrically, the gradient ∇f = ⟨f_x, f_y⟩ is the "slope vector" of the surface — it captures all rate-of-change information in every direction simultaneously, and dotting with **u** extracts the slice relevant to your particular direction.

The deepest consequence follows from the geometry of dot products: D_**u** f = ‖∇f‖ cos θ, where θ is the angle between ∇f and **u**. This is maximized when θ = 0 — when you walk in the direction of ∇f itself. So the gradient points in the **direction of steepest ascent**, and ‖∇f‖ equals the maximum rate of increase. Walking in the direction of −∇f gives steepest descent. Walking perpendicular to ∇f gives D_**u** f = 0 — no change — meaning you're moving along a **level curve** where f is constant. The gradient is always perpendicular to the level curves of f.

To ground this concretely: take f(x, y) = x² + y² (a bowl-shaped paraboloid). At the point (1, 1), ∇f = ⟨2, 2⟩. Walking due east (**u** = ⟨1, 0⟩) gives D_**u** f = 2. Walking northeast in the gradient direction (**u** = ⟨1, 1⟩/√2) gives D_**u** f = ‖⟨2, 2⟩‖ = 2√2, a steeper climb. This is exactly why gradient descent algorithms — used throughout optimization and machine learning — follow −∇f to find function minima: the gradient tells you the direction of fastest increase, so its negative points most efficiently downhill.
