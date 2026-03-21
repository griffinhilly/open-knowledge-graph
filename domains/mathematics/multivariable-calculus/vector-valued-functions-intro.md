---
id: vector-valued-functions-intro
title: Vector-Valued Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vectors-in-rn
  type: hard
- id: parametric-equations-intro
  type: hard
builds-toward:
- parametric-curves-calculus
- space-curves
tags:
- vectors
- parametric
- curves
stage: formal-systems
status: draft
---

# Vector-Valued Functions

## Core Idea
A vector-valued function maps real numbers to vectors in n-dimensional space: r(t) = ⟨f₁(t), f₂(t), …, fₙ(t)⟩. These functions describe curves, trajectories, and parametric paths. Calculus operations (limits, derivatives, integrals) apply component-wise.

## How It's Best Learned
Start with 2D and 3D examples: projectile motion, circles, helices. Compute derivatives by differentiating components.

## Common Misconceptions
Treating a vector-valued function like a scalar function; remember each input gives a vector output.
Assuming a single parameterization is unique; multiple parameterizations describe the same curve.

## Questions

```yaml
- question: "Consider r(t) = ⟨cos(2t), sin(2t)⟩ and q(t) = ⟨cos(t), sin(t)⟩, both defined for t ∈ [0, 2π]. What is the relationship between these two functions?"
  type: multiple-choice
  options:
    - "They are the same function — both produce the same output for every input t"
    - "They trace different geometric curves — r traces an ellipse, q traces a circle"
    - "They trace the same geometric circle, but r traverses it twice as fast as q"
    - "They are unrelated because their formulas are different"
  answer: 2
  explanation: "Both r(t) and q(t) trace the unit circle — the set of points (x, y) with x² + y² = 1. But they are different parameterizations: r(t) completes the circle twice in [0, 2π] while q(t) completes it once. This illustrates that the same geometric curve can have infinitely many valid parameterizations. The geometric object (the circle) and the function (which includes speed and direction of traversal) are distinct concepts. A vector-valued function encodes more than just the shape of the curve."

- question: "For the vector-valued function r(t) = ⟨t², sin(t), e^t⟩, what is r'(t)?"
  type: multiple-choice
  options:
    - "The magnitude of the vector ⟨t², sin(t), e^t⟩"
    - "⟨2t, cos(t), e^t⟩ — each component differentiated independently"
    - "The scalar function t² + sin(t) + e^t, then differentiated"
    - "r'(t) cannot be computed because r(t) is a vector, not a scalar"
  answer: 1
  explanation: "Calculus on vector-valued functions is component-wise: r'(t) = ⟨(t²)', (sin t)', (e^t)'⟩ = ⟨2t, cos t, e^t⟩. Each component is an ordinary real-valued function, and standard single-variable differentiation applies in each slot. The vector structure does not interfere. Option D is a common misconception — the derivative of a vector-valued function is itself a vector-valued function, not undefined. Option C erroneously collapses the vector to a scalar first."

- question: "A vector-valued function r(t) outputs a single number for each value of t."
  type: true-false
  answer: false
  explanation: "A vector-valued function maps each real input t to a vector in ℝⁿ — a list of n numbers, not a single number. For r(t) = ⟨f₁(t), f₂(t), f₃(t)⟩, each input t produces a 3-dimensional vector (a point in 3D space). The function is vector-valued precisely because its outputs are vectors. Treating the output as a scalar is the most fundamental error when learning this topic, leading to mistakes in differentiation, integration, and geometric interpretation."

- question: "Two different vector-valued functions can trace the same geometric curve in space."
  type: true-false
  answer: true
  explanation: "Parameterization is not unique. The circle x² + y² = 1, for example, is traced by r(t) = ⟨cos t, sin t⟩, by q(t) = ⟨cos(2t), sin(2t)⟩, by s(t) = ⟨cos(−t), sin(−t)⟩, and infinitely many other functions. They all trace the same geometric set of points but traverse it at different speeds, in different directions, or with different starting points. The geometric curve is the image of the function; the function itself encodes additional information (speed, direction, timing)."

- question: "What does the derivative vector r'(t) represent geometrically, and how does it differ from a derivative in single-variable calculus?"
  type: short-answer
  answer: "r'(t) is the tangent vector to the curve at the point r(t) — it points in the direction the curve is heading at that moment, with magnitude equal to the speed of traversal. Unlike a scalar derivative (a single number giving slope), r'(t) is itself a vector. Different parameterizations of the same curve produce tangent vectors with the same direction but different magnitudes at the same point."
  explanation: "The tangent vector r'(t) = ⟨f₁'(t), f₂'(t), …⟩ has both direction and magnitude. If r(t) describes a particle's position, r'(t) is its velocity vector — encoding which way it is going and how fast. Dividing by the magnitude gives the unit tangent T(t) = r'(t)/‖r'(t)‖, which captures pure direction and is the entry point to curvature. This geometric interpretation is what makes vector-valued functions the natural language of motion in physics and differential geometry."
```

## Explainer

From vectors in ℝⁿ, you know how to add, scale, and compute norms of individual vectors. From parametric equations, you know how to describe curves by letting coordinates be functions of a parameter t: x = f(t), y = g(t). A **vector-valued function** fuses both ideas: **r**(t) = ⟨f₁(t), f₂(t), …, fₙ(t)⟩ maps a real number t to a vector in ℝⁿ. As t varies over an interval, **r**(t) traces out a curve in space. The function is not just describing a static set of points — it is a moving point, a trajectory, where t acts as a time parameter (or any other kind of parameter you choose to interpret it as).

The simplest examples make the idea concrete. A circle of radius r: **r**(t) = ⟨r cos t, r sin t⟩ for t ∈ [0, 2π] traces the circle counterclockwise starting at (r, 0). A helix: **r**(t) = ⟨cos t, sin t, t⟩ circles around the z-axis while climbing upward, combining the circle's x and y components with a linear z component. A straight line through point P₀ in direction **d**: **r**(t) = P₀ + t**d**, your parametric equation for a line expressed as a vector equation. In each case, t is an index — not an x-coordinate — and **r**(t) is an output vector, not a scalar. A single input t produces an entire vector: a location in space.

**Calculus on vector-valued functions works component-wise.** The limit lim_{t→a} **r**(t) = ⟨lim f₁(t), lim f₂(t), …⟩ exists when each component limit exists. The **derivative** **r**'(t) = ⟨f₁'(t), f₂'(t), …, fₙ'(t)⟩ differentiates each component separately. This works because the components are independent real-valued functions — the vector structure does not interfere. The **integral** ∫ **r**(t) dt = ⟨∫f₁ dt, ∫f₂ dt, …⟩ integrates component-wise. All single-variable calculus rules apply in each slot: products of a scalar function with **r**(t), quotients, chain rule — each applies to individual components.

The **derivative vector r'**(t) is geometrically the **tangent vector** to the curve at the point **r**(t): it points in the direction the curve is heading at that moment, with magnitude equal to the speed of traversal. If **r**(t) gives a particle's position at time t, then **r**'(t) is its velocity vector and **r**''(t) is its acceleration vector — connecting directly to Newtonian mechanics. The same curve can be parameterized in infinitely many ways (fast, slow, reversed), and each parameterization produces a different tangent vector at the same point, but they all point in the same (or opposite) direction. The **unit tangent vector** T(t) = **r**'(t) / ‖**r**'(t)‖ strips away the speed and captures direction alone, which is the gateway to curvature and the geometry of space curves.
