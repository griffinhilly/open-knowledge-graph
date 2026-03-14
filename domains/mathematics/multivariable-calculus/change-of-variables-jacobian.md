---
id: change-of-variables-jacobian
title: Change of Variables and the Jacobian Determinant
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: triple-integrals-cylindrical-spherical
  type: hard
- id: determinant-computation
  type: hard
builds-toward:
- applications-triple-integrals
tags:
- jacobian
- change-of-variables
- transformation
stage: formal-systems
status: draft
---

# Change of Variables and the Jacobian Determinant

## Core Idea
When substituting x = x(u, v), y = y(u, v) in a double integral, ∬_R f(x,y) dx dy = ∬_S f(x(u,v), y(u,v)) |J| du dv, where J is the Jacobian determinant J = (∂x/∂u)(∂y/∂v) − (∂x/∂v)(∂y/∂u). This scales area elements by |J|.
