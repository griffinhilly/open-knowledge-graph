---
id: lagrange-multipliers
title: Lagrange Multipliers for Constrained Optimization
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: unconstrained-optimization
  type: hard
- id: gradient-vector-properties
  type: hard
builds-toward:
- constrained-optimization
tags:
- lagrange-multipliers
- constraints
- optimization
stage: formal-systems
status: draft
---

# Lagrange Multipliers for Constrained Optimization

## Core Idea
To extremize f(x, y, z) subject to g(x, y, z) = 0, solve ∇f = λ∇g (the gradients are parallel) together with the constraint. The scalar λ is the Lagrange multiplier; geometrically, extrema occur where level surfaces of f and g are tangent.
