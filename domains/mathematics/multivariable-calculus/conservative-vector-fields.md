---
id: conservative-vector-fields
title: Conservative Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: conservative-fields
  type: hard
- id: fundamental-theorem-line-integrals
  type: hard
builds-toward:
- greens-theorem
- curl-divergence
tags:
- conservative
- potential
stage: formal-systems
status: draft
---

# Conservative Vector Fields

## Core Idea
A vector field F is conservative if F = ∇f for some potential f. Line integrals are path-independent: ∫_C F · dr = f(endpoint) - f(startpoint). In 2D, F = (P, Q) is conservative iff P_y = Q_x.
