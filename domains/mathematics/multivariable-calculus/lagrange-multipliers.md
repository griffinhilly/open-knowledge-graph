---
id: lagrange-multipliers
title: Lagrange Multipliers
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: lagrange-multipliers
  type: hard
- id: implicit-differentiation-multivariable
  type: hard
builds-toward:
- constrained-optimization
tags:
- lagrange
- constraints
stage: formal-systems
status: draft
---

# Lagrange Multipliers

## Core Idea
To optimize f(x, y) subject to g(x, y) = 0, solve ∇f = λ∇g along with the constraint. The Lagrange multiplier λ represents the sensitivity of the optimum to relaxing the constraint.
