---
id: second-partials-test-extrema
title: Second Partial Test for Local Extrema (Hessian)
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: higher-order-partials-mixed
  type: hard
- id: critical-points-multivariable-classification
  type: hard
builds-toward:
- constrained-optimization-lagrange
tags:
- second-derivative-test
- hessian
- eigenvalues
stage: formal-systems
status: draft
---

# Second Partial Test for Local Extrema (Hessian)

## Core Idea
At critical point (a, b), compute the Hessian matrix H = [[f_xx, f_xy], [f_xy, f_yy]]. If det(H) > 0 and f_xx > 0, it's a local min; if f_xx < 0, local max. If det(H) < 0, it's a saddle point. If det(H) = 0, test is inconclusive.
