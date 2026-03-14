---
id: second-partials-test
title: The Second Partials Test
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: critical-points-multivariable
  type: hard
- id: higher-order-partial-derivatives
  type: hard
- id: second-derivative-test
  type: soft
builds-toward:
- lagrange-multipliers
tags:
- second-derivative-test
- Hessian
- discriminant
- local-extrema
stage: formal-systems
status: validated
---

# The Second Partials Test

## Core Idea
At a critical point (a, b) of f(x, y), the discriminant D = f_xx f_yy − (f_xy)² classifies the critical point. If D > 0 and f_xx > 0, it is a local minimum; if D > 0 and f_xx < 0, it is a local maximum; if D < 0, it is a saddle point; if D = 0, the test is inconclusive. Geometrically, D is the determinant of the Hessian matrix H = [[f_xx, f_xy], [f_xy, f_yy]], which encodes all second-order curvature information at the critical point.

## How It's Best Learned
Connect D to the Hessian determinant explicitly. Have students practice with examples where each case occurs, including D = 0 (to show the test's limits). Emphasize that D > 0 means the surface curves the same way in all directions (definite curvature), while D < 0 means it curves differently in different directions (indefinite curvature — a saddle).

## Common Misconceptions
- D > 0 alone is not sufficient; you must also check the sign of f_xx to distinguish max from min.
- D = 0 is genuinely inconclusive — all three outcomes (max, min, saddle) are possible, and higher-order terms must be examined.
- The second partials test applies to interior critical points only; boundary behavior requires separate analysis.
