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
status: draft
---

# Arc Length of Curves in 3D

## Core Idea
For a parametric curve r(t) from t=a to t=b, the arc length is L = ∫[a,b] |r'(t)| dt. This integrates the speed along the path. Arc length is independent of the parametrization chosen.

## Explainer

From arc length in 2D parametric curves, you know that the length of a path traced by (x(t), y(t)) is ∫√((dx/dt)² + (dy/dt)²) dt. The extension to 3D is direct: for a curve r(t) = ⟨x(t), y(t), z(t)⟩, the derivative **r'(t) = ⟨x'(t), y'(t), z'(t)⟩** is the velocity vector, and its magnitude |r'(t)| = √(x'² + y'² + z'²) is the speed — the instantaneous rate at which distance is being traced along the curve. The arc length formula L = ∫ₐᵇ |r'(t)| dt just says: integrate speed over time to get distance traveled. This is the same logic you use in one dimension (distance = ∫ speed dt), now generalized to curves winding through three-dimensional space.

The concrete example of a **helix** makes the formula vivid. The helix r(t) = ⟨cos t, sin t, t⟩ winds around a cylinder, rising steadily in the z-direction. Its derivative is r'(t) = ⟨−sin t, cos t, 1⟩, with magnitude |r'(t)| = √(sin²t + cos²t + 1) = √2. The arc length from t = 0 to t = 2π is just √2 · 2π = 2π√2 — longer than a flat circle of radius 1 (which has length 2π) by the factor √2 accounting for the upward climb. Without the vector framework you learned for vector-valued functions, this calculation would be far more laborious.

**Parametrization independence** is one of the most important properties of arc length. The curve as a geometric object — the set of points it traces — has a definite length regardless of how you parametrize it. If you reparametrize by doubling the speed (replace t with 2t), the new integrand is larger but the integration interval is half as long, and the product is the same. This makes arc length a genuine geometric quantity, not an artifact of your choice of variable. It also motivates the idea of **arc length parametrization** — choosing the parameter s so that |r'(s)| = 1 everywhere, meaning you move along the curve at unit speed. This natural parametrization simplifies many formulas and is the foundation for the curvature and torsion calculations you'll encounter next.
