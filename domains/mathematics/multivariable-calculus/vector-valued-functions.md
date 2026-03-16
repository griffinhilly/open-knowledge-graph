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

## Explainer

You've worked with parametric curves in single-variable calculus — a curve traced by (x(t), y(t)) as t varies. A vector-valued function r(t) = ⟨f(t), g(t), h(t)⟩ is exactly that idea extended to three dimensions. The scalar parameter t can represent time, arc length, or any convenient variable. As t runs through its domain, the tip of the vector r(t) traces a **space curve** through ℝ³. Every point on the curve corresponds to a t-value, and the entire trajectory is encoded in a single vector expression.

Limits, continuity, and derivatives are defined **component-wise**, meaning all the machinery from single-variable calculus carries over directly: r′(t) = ⟨f′(t), g′(t), h′(t)⟩ just differentiates each component independently. All derivative rules apply component-wise as well — the product rule, quotient rule, and chain rule each work on individual components. The chain rule for r(s(t)) gives dr/dt = r′(s(t)) · s′(t), where the scalar s′(t) scales the entire output vector.

The geometric meaning of r′(t) is the **tangent vector** to the curve at r(t). It points in the direction of travel and its magnitude |r′(t)| is the instantaneous **speed**. Speed and velocity are distinct: **velocity** is the vector r′(t) (directional), **speed** is its scalar magnitude |r′(t)|. The **unit tangent vector** T(t) = r′(t)/|r′(t)| discards speed to preserve only direction — it will be essential when you study curvature and the Frenet-Serret frame for space curves.

Integration also works component-wise: ∫r(t)dt = ⟨∫f(t)dt, ∫g(t)dt, ∫h(t)dt⟩, producing a vector antiderivative. A definite integral ∫_a^b r(t)dt produces a single vector representing **net displacement** — where you end up minus where you started. This is distinct from **arc length** ∫_a^b |r′(t)|dt, which is a scalar measuring total distance traveled along the curve. Net displacement and arc length agree only for straight-line motion in one direction; in general, a winding curve travels far more distance than its net displacement suggests. Keeping these two quantities conceptually separate is one of the key organizational skills in this part of multivariable calculus.
