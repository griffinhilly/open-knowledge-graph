---
id: space-curves
title: Space Curves and Arc Length
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-valued-functions
  type: hard
- id: arc-length-parametric
  type: hard
builds-toward:
- curvature
tags:
- arc-length
- space-curves
- parametric
- integration
stage: formal-systems
status: validated
---

# Space Curves and Arc Length

## Core Idea
The arc length of a space curve r(t) from t = a to t = b is L = ∫_a^b |r′(t)| dt, a direct generalization of the parametric arc length formula from single-variable calculus. The arc length parameter s(t) = ∫_a^t |r′(u)| du reparametrizes the curve so that |r′(s)| = 1 at every point, making s a natural measure of distance along the curve. Reparametrization by arc length simplifies many formulas but is rarely computed explicitly.

## How It's Best Learned
Students should first compute arc length for simple curves (helix, straight line) to build intuition. Emphasize that the formula is the same as in 2D parametric calculus, just with a third component under the square root. The concept of reparametrization by arc length is best understood geometrically before any formulas are introduced.

## Common Misconceptions
- Arc length is always non-negative; it measures total distance traveled, not net displacement.
- If the curve is traced multiple times over [a, b], arc length counts repeated portions multiple times.
