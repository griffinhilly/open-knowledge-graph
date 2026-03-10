---
id: vector-valued-functions
title: Vector-Valued Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vectors-in-3d
  type: hard
- id: parametric-curves-calculus
  type: hard
- id: derivative-notation
  type: hard
builds-toward:
- space-curves
- curvature
tags:
- vector-valued
- parametric
- calculus
- differentiation
stage: formal-systems
status: draft
---

# Vector-Valued Functions

## Core Idea
A vector-valued function r(t) = ⟨f(t), g(t), h(t)⟩ maps a scalar parameter to a vector in ℝ³, tracing a curve through space as t varies. Limits, continuity, and derivatives are defined component-wise: r′(t) = ⟨f′(t), g′(t), h′(t)⟩. The derivative r′(t) is the tangent vector to the curve at each point, and its magnitude |r′(t)| is the instantaneous speed. Integration of vector-valued functions is also component-wise.

## How It's Best Learned
Connect to parametric curves from single-variable calculus — a vector-valued function in ℝ³ is just a parametric curve with three components instead of two. Visualize the curve in 3D before computing derivatives. Emphasize that r′(t) gives direction (tangent) while |r′(t)| gives speed; these are distinct pieces of information.

## Common Misconceptions
- r′(t) is a vector, not a scalar. Confusing magnitude with the derivative itself is common.
- Integration of a vector-valued function produces a vector, not a number.
- The chain rule still applies: if r(t) = r(g(t)), then dr/dt = r′(g(t))·g′(t).
