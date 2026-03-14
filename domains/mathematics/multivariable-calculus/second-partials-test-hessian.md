---
id: second-partials-test-hessian
title: Second Partial Test and the Hessian
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: second-partials-test
  type: hard
- id: mixed-partials-clairaut
  type: hard
builds-toward:
- optimization-multivariable-basics
tags:
- hessian
- classification
stage: formal-systems
status: draft
---

# Second Partial Test and the Hessian

## Core Idea
The Hessian H = [[f_xx, f_xy], [f_xy, f_yy]] classifies critical points. If det(H) > 0 and f_xx > 0, it's a local minimum. If det(H) > 0 and f_xx < 0, it's a maximum. If det(H) < 0, it's a saddle point.
