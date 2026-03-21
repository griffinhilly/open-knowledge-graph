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
status: validated
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

## Questions

```yaml
- question: "A particle moves along the curve r(t) = ⟨cos t, sin t, t⟩. A student computes r′(t) = ⟨−sin t, cos t, 1⟩ and concludes this is the particle's speed. What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "r′(t) is computed incorrectly — the derivative of a vector-valued function is a scalar"
    - "r′(t) is the velocity vector, not the speed; speed is the scalar |r′(t)| = √(sin²t + cos²t + 1) = √2"
    - "r′(t) gives speed only if the parameter t represents time, which is not stated here"
    - "r′(t) is correct as the speed, since each component is differentiated independently"
  answer: 1
  explanation: "r′(t) is a vector — the tangent (velocity) vector — not a scalar speed. Speed is the magnitude |r′(t)|, which here equals √((-sin t)² + (cos t)² + 1²) = √(sin²t + cos²t + 1) = √2, a constant. Confusing a vector with its magnitude is the most common error with vector-valued derivatives. The vector tells you direction AND encodes speed through its magnitude; the magnitude extracts only the scalar speed."

- question: "A particle travels along a space curve r(t) for t ∈ [0, 2π], beginning and ending at the same point. What does ∫₀²π r′(t) dt equal?"
  type: multiple-choice
  options:
    - "The total arc length of the curve"
    - "The magnitude of the average velocity"
    - "The zero vector ⟨0, 0, 0⟩"
    - "The position vector r(2π)"
  answer: 2
  explanation: "The definite integral ∫_a^b r′(t) dt gives net displacement — the vector from starting position to ending position. Since the particle returns to its start, net displacement is the zero vector. This is distinct from arc length, which is ∫₀²π |r′(t)| dt — a positive scalar measuring total distance traveled. A particle can travel a great distance along a winding path while having zero net displacement."

- question: "Differentiating a vector-valued function r(t) = ⟨f(t), g(t), h(t)⟩ produces a scalar — the rate at which the magnitude |r(t)| changes."
  type: true-false
  answer: false
  explanation: "r′(t) = ⟨f′(t), g′(t), h′(t)⟩ is a vector, computed component-wise. It represents the velocity (tangent vector) at each point on the curve, not the rate of change of |r(t)|. To find how the magnitude changes, you would need d/dt |r(t)|, a separate calculation using the chain rule. The derivative of a vector-valued function is always a vector of the same dimension."

- question: "Integrating a vector-valued function r(t) = ⟨f(t), g(t), h(t)⟩ over an interval [a, b] produces a vector whose components are the definite integrals of each scalar component."
  type: true-false
  answer: true
  explanation: "Integration of vector-valued functions is component-wise: ∫_a^b r(t) dt = ⟨∫_a^b f(t) dt, ∫_a^b g(t) dt, ∫_a^b h(t) dt⟩. The result is a vector, not a scalar. This component-wise principle carries through all of vector calculus — limits, continuity, differentiation, and integration each reduce to the corresponding scalar operation applied independently to each component."

- question: "Explain the difference between net displacement and arc length for a particle moving along a space curve. When, if ever, are they equal in magnitude?"
  type: short-answer
  answer: "Net displacement is the vector ∫_a^b r′(t) dt — how far and in what direction the particle moved from start to finish. Arc length is the scalar ∫_a^b |r′(t)| dt — total distance traveled along the path, regardless of direction. They are equal in magnitude only when the particle moves in a straight line without reversing direction, so every infinitesimal step contributes positively in the same direction."
  explanation: "The distinction mirrors displacement vs. distance in one-dimensional motion. A particle that traces a closed loop has zero net displacement but positive arc length. Net displacement is a vector and can be zero even after extensive travel; arc length is always nonnegative. This difference becomes crucial when studying arc-length parameterization, where the goal is to reparameterize a curve so that |r′(t)| = 1 everywhere, making arc length and parameter advance at the same rate."
```

## Explainer

You've worked with parametric curves in single-variable calculus — a curve traced by (x(t), y(t)) as t varies. A vector-valued function r(t) = ⟨f(t), g(t), h(t)⟩ is exactly that idea extended to three dimensions. The scalar parameter t can represent time, arc length, or any convenient variable. As t runs through its domain, the tip of the vector r(t) traces a **space curve** through ℝ³. Every point on the curve corresponds to a t-value, and the entire trajectory is encoded in a single vector expression.

Limits, continuity, and derivatives are defined **component-wise**, meaning all the machinery from single-variable calculus carries over directly: r′(t) = ⟨f′(t), g′(t), h′(t)⟩ just differentiates each component independently. All derivative rules apply component-wise as well — the product rule, quotient rule, and chain rule each work on individual components. The chain rule for r(s(t)) gives dr/dt = r′(s(t)) · s′(t), where the scalar s′(t) scales the entire output vector.

The geometric meaning of r′(t) is the **tangent vector** to the curve at r(t). It points in the direction of travel and its magnitude |r′(t)| is the instantaneous **speed**. Speed and velocity are distinct: **velocity** is the vector r′(t) (directional), **speed** is its scalar magnitude |r′(t)|. The **unit tangent vector** T(t) = r′(t)/|r′(t)| discards speed to preserve only direction — it will be essential when you study curvature and the Frenet-Serret frame for space curves.

Integration also works component-wise: ∫r(t)dt = ⟨∫f(t)dt, ∫g(t)dt, ∫h(t)dt⟩, producing a vector antiderivative. A definite integral ∫_a^b r(t)dt produces a single vector representing **net displacement** — where you end up minus where you started. This is distinct from **arc length** ∫_a^b |r′(t)|dt, which is a scalar measuring total distance traveled along the curve. Net displacement and arc length agree only for straight-line motion in one direction; in general, a winding curve travels far more distance than its net displacement suggests. Keeping these two quantities conceptually separate is one of the key organizational skills in this part of multivariable calculus.
