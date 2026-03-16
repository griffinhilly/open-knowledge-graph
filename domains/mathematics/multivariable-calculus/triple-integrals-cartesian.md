---
id: triple-integrals-cartesian
title: Triple Integrals in Cartesian Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: applications-integrals-area-mass
  type: hard
builds-toward:
- triple-integrals-cylindrical-spherical
tags:
- triple-integrals
- cartesian
- volume
stage: formal-systems
status: draft
---

# Triple Integrals in Cartesian Coordinates

## Core Idea
For a region W in 3D, the triple integral ∭_W f(x, y, z) dV = ∫∫∫ f(x, y, z) dz dy dx represents volume (when f = 1) or weighted volume. Fubini's theorem permits changing order of integration. Setting up bounds for W requires careful description as a region in 3D.

## Explainer

From double integrals, you know that ∬_R f(x, y) dA accumulates f over a two-dimensional region R, and that when f = 1, it returns the area of R. Triple integrals extend this pattern by one more dimension: ∭_W f(x, y, z) dV accumulates f over a three-dimensional region W. When f = 1, the triple integral gives the **volume** of W. When f is a density function (mass per unit volume), the triple integral gives total mass. The structure is the same; only the dimensionality changes.

Evaluating a triple integral means converting it to three nested single-variable integrals, applied from the inside out. For a region W, you first choose an order of integration — say dz dy dx — and then describe W as nested bounds: z ranges from z_low(x, y) to z_high(x, y) for fixed (x, y); y ranges from y_low(x) to y_high(x) for fixed x; and x ranges over a fixed interval [a, b]. The key skill is reading off these bounds from a geometric description of W. For a unit cube [0,1]³ the bounds are all constants. For a tetrahedron or a ball, they depend on the outer variables.

**Fubini's theorem** says the order of integration doesn't matter (for well-behaved f): you can integrate dz dy dx, or dx dy dz, or any of the six orderings, and get the same answer. This is powerful because some orderings produce far simpler integrals than others. The classic strategy is: if one ordering leads to a hard inner integral, try a different order. To change the order, you must re-describe the region W in terms of the new order of nesting — draw a sketch of W and re-read the bounds from the new perspective.

A common challenge is setting up bounds for regions defined by curved surfaces. For the region inside the sphere x² + y² + z² ≤ 1, Cartesian bounds require z ∈ [−√(1−x²−y²), √(1−x²−y²)] and y ∈ [−√(1−x²), √(1−x²)] and x ∈ [−1, 1] — correct but messy. This is exactly why cylindrical and spherical coordinates (the natural next topic) exist: they describe curved regions with clean constant bounds. Mastering triple integrals in Cartesian coordinates first builds the geometric intuition needed to recognize when a coordinate change will simplify a problem.
