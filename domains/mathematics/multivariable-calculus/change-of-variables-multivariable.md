---
id: change-of-variables-multivariable
title: Change of Variables and the Jacobian
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: jacobian-change-of-variables
  type: hard
- id: determinant-computation
  type: hard
builds-toward:
- surface-integrals
tags:
- jacobian
- determinant
stage: formal-systems
status: draft
---

# Change of Variables and the Jacobian

## Core Idea
To change variables in integrals: ∬_R f(x,y) dx dy = ∬_S f(x(u,v), y(u,v)) |det(J)| du dv, where J is the Jacobian matrix. The determinant's absolute value scales area/volume.
