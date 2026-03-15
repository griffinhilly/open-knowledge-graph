---
id: change-of-variables-jacobian
title: Change of Variables and the Jacobian Determinant
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: triple-integrals-cylindrical-spherical
  type: hard
builds-toward:
- surface-parametrization
tags:
- jacobian
- change-of-variables
- transformation
stage: formal-systems
status: draft
---

# Change of Variables and the Jacobian Determinant

## Core Idea
For transformation (u, v) = T(x, y), the Jacobian J = ∂(x, y)/∂(u, v) = det([∂x/∂u, ∂x/∂v; ∂y/∂u, ∂y/∂v]) scales area. Thus ∬_D f(x, y) dA = ∬_S f(x(u, v), y(u, v)) |J| du dv. Cylindrical and spherical coordinates are special cases.
