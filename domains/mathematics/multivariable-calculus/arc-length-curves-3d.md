---
id: arc-length-curves-3d
title: Arc Length of Curves in 3D
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-valued-functions-curves
  type: hard
- id: arc-length-parametric
  type: hard
builds-toward:
- curvature-and-torsion
tags:
- arc-length
- integral
- curves
stage: formal-systems
status: validated
---

# Arc Length of Curves in 3D

## Core Idea
For a parametric curve r(t) from t=a to t=b, the arc length is L = ∫[a,b] |r'(t)| dt. This integrates the speed along the path. Arc length is independent of the parametrization chosen.

## Questions

```yaml
- question: "The helix r(t) = ⟨cos t, sin t, t⟩ has derivative r'(t) = ⟨−sin t, cos t, 1⟩. What is the arc length from t = 0 to t = 2π?"
  type: multiple-choice
  options:
    - "2π, the same as a flat unit circle of radius 1"
    - "√2, the speed at any point along the helix"
    - "2π√2, found by integrating the constant speed √2 over the interval [0, 2π]"
    - "2π + 2π = 4π, adding the circular length and the vertical rise separately"
  answer: 2
  explanation: "|r'(t)| = √(sin²t + cos²t + 1) = √(1 + 1) = √2, which is constant. The arc length is ∫₀^{2π} √2 dt = 2π√2. This is longer than a flat circle (2π) by the factor √2, which accounts for the simultaneous upward climb. Adding lengths independently (option D) is not valid — the speed already captures both the circular and vertical components at once through the magnitude of the full velocity vector."

- question: "A curve r(t) traces a helix for t ∈ [0, 2π]. If you reparametrize it as r(2s) for s ∈ [0, π], which traces the same curve twice as fast, how does the arc length change?"
  type: multiple-choice
  options:
    - "The arc length halves, because the integration interval [0, π] is half as long"
    - "The arc length stays the same, because arc length is a property of the curve as a geometric object, independent of how it is parametrized"
    - "The arc length doubles, because the speed doubles under the reparametrization"
    - "The arc length changes unpredictably and must be recomputed from scratch"
  answer: 1
  explanation: "Arc length is parametrization-independent. Under reparametrization r(2s), the speed |dr/ds| = 2|r'(2s)| doubles, but the integration interval is half as long — [0, π] instead of [0, 2π]. These effects cancel exactly, giving the same arc length. This is not a coincidence: arc length is defined to capture a geometric property of the curve (the distance traveled), which cannot depend on whether you traverse it quickly or slowly."

- question: "Arc length of a parametric curve r(t) from a to b equals the integral of the speed |r'(t)| over [a, b]."
  type: true-false
  answer: true
  explanation: "This is the fundamental formula: L = ∫ₐᵇ |r'(t)| dt. The velocity vector r'(t) gives the direction and speed of travel along the curve; its magnitude |r'(t)| is the instantaneous speed. Integrating speed over time gives total distance — the same principle as distance = ∫ speed dt in one dimension, generalized to curves winding through 3D space."

- question: "Reparametrizing a curve changes its arc length, because the derivative r'(t) changes when you substitute a new parameter."
  type: true-false
  answer: false
  explanation: "Arc length is a geometric invariant — it measures the physical length of the curve as a set of points in space, which cannot depend on the parameter used to trace it. A reparametrization changes both the integrand (the speed |r'|) and the integration limits in compensating ways: faster traversal over a shorter interval yields the same total length. This is why arc length is called a 'parametrization-independent' quantity and why the arc-length parametrization (where speed = 1 everywhere) is considered the 'natural' one."

- question: "Explain why arc length is described as 'parametrization-independent,' and why this property motivates the definition of arc-length parametrization."
  type: short-answer
  answer: "Arc length measures the physical distance along the curve as a geometric object — the distance doesn't change just because you choose to traverse it faster or slower. Formally, any reparametrization t = φ(s) changes both |r'| and the integration limits such that the product remains the same. This geometric invariance motivates the arc-length parametrization s, defined so that |r'(s)| = 1 everywhere: moving along the curve at unit speed. Under this parametrization, the arc length from s₀ to s₁ is simply s₁ − s₀, simplifying formulas for curvature and torsion."
  explanation: "The arc-length parameter s is the 'natural' parametrization because it removes the arbitrary choice of traversal speed from all geometric calculations. Curvature κ = |r''(s)| under arc-length parametrization, for example, measures only how the curve bends — not how fast you happen to move along it. Without parametrization independence, geometric properties of curves would depend on how you describe them rather than on the curves themselves."
```

## Explainer

From arc length in 2D parametric curves, you know that the length of a path traced by (x(t), y(t)) is ∫√((dx/dt)² + (dy/dt)²) dt. The extension to 3D is direct: for a curve r(t) = ⟨x(t), y(t), z(t)⟩, the derivative **r'(t) = ⟨x'(t), y'(t), z'(t)⟩** is the velocity vector, and its magnitude |r'(t)| = √(x'² + y'² + z'²) is the speed — the instantaneous rate at which distance is being traced along the curve. The arc length formula L = ∫ₐᵇ |r'(t)| dt just says: integrate speed over time to get distance traveled. This is the same logic you use in one dimension (distance = ∫ speed dt), now generalized to curves winding through three-dimensional space.

The concrete example of a **helix** makes the formula vivid. The helix r(t) = ⟨cos t, sin t, t⟩ winds around a cylinder, rising steadily in the z-direction. Its derivative is r'(t) = ⟨−sin t, cos t, 1⟩, with magnitude |r'(t)| = √(sin²t + cos²t + 1) = √2. The arc length from t = 0 to t = 2π is just √2 · 2π = 2π√2 — longer than a flat circle of radius 1 (which has length 2π) by the factor √2 accounting for the upward climb. Without the vector framework you learned for vector-valued functions, this calculation would be far more laborious.

**Parametrization independence** is one of the most important properties of arc length. The curve as a geometric object — the set of points it traces — has a definite length regardless of how you parametrize it. If you reparametrize by doubling the speed (replace t with 2t), the new integrand is larger but the integration interval is half as long, and the product is the same. This makes arc length a genuine geometric quantity, not an artifact of your choice of variable. It also motivates the idea of **arc length parametrization** — choosing the parameter s so that |r'(s)| = 1 everywhere, meaning you move along the curve at unit speed. This natural parametrization simplifies many formulas and is the foundation for the curvature and torsion calculations you'll encounter next.
