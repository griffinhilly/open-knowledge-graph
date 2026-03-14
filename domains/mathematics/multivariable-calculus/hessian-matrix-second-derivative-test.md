---
id: hessian-matrix-second-derivative-test
title: The Hessian Matrix and Second Derivative Test
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: critical-points-extrema-saddle
  type: hard
- id: higher-order-partials
  type: hard
builds-toward:
- unconstrained-optimization
tags:
- hessian
- second-derivative-test
- eigenvalues
stage: formal-systems
status: draft
---

# The Hessian Matrix and Second Derivative Test

## Core Idea
The Hessian matrix H = [[f_xx, f_xy], [f_yx, f_yy]] contains all second partial derivatives. At a critical point, the determinant det(H) and trace tr(H) determine whether it is a local max (det > 0, f_xx > 0), local min (det > 0, f_xx < 0), or saddle point (det < 0).
