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

## Explainer

From vectors in ℝⁿ, you know how to add, scale, and compute norms of individual vectors. From parametric equations, you know how to describe curves by letting coordinates be functions of a parameter t: x = f(t), y = g(t). A **vector-valued function** fuses both ideas: **r**(t) = ⟨f₁(t), f₂(t), …, fₙ(t)⟩ maps a real number t to a vector in ℝⁿ. As t varies over an interval, **r**(t) traces out a curve in space. The function is not just describing a static set of points — it is a moving point, a trajectory, where t acts as a time parameter (or any other kind of parameter you choose to interpret it as).

The simplest examples make the idea concrete. A circle of radius r: **r**(t) = ⟨r cos t, r sin t⟩ for t ∈ [0, 2π] traces the circle counterclockwise starting at (r, 0). A helix: **r**(t) = ⟨cos t, sin t, t⟩ circles around the z-axis while climbing upward, combining the circle's x and y components with a linear z component. A straight line through point P₀ in direction **d**: **r**(t) = P₀ + t**d**, your parametric equation for a line expressed as a vector equation. In each case, t is an index — not an x-coordinate — and **r**(t) is an output vector, not a scalar. A single input t produces an entire vector: a location in space.

**Calculus on vector-valued functions works component-wise.** The limit lim_{t→a} **r**(t) = ⟨lim f₁(t), lim f₂(t), …⟩ exists when each component limit exists. The **derivative** **r**'(t) = ⟨f₁'(t), f₂'(t), …, fₙ'(t)⟩ differentiates each component separately. This works because the components are independent real-valued functions — the vector structure does not interfere. The **integral** ∫ **r**(t) dt = ⟨∫f₁ dt, ∫f₂ dt, …⟩ integrates component-wise. All single-variable calculus rules apply in each slot: products of a scalar function with **r**(t), quotients, chain rule — each applies to individual components.

The **derivative vector r'**(t) is geometrically the **tangent vector** to the curve at the point **r**(t): it points in the direction the curve is heading at that moment, with magnitude equal to the speed of traversal. If **r**(t) gives a particle's position at time t, then **r**'(t) is its velocity vector and **r**''(t) is its acceleration vector — connecting directly to Newtonian mechanics. The same curve can be parameterized in infinitely many ways (fast, slow, reversed), and each parameterization produces a different tangent vector at the same point, but they all point in the same (or opposite) direction. The **unit tangent vector** T(t) = **r**'(t) / ‖**r**'(t)‖ strips away the speed and captures direction alone, which is the gateway to curvature and the geometry of space curves.
