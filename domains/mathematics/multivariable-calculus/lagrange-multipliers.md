---
id: lagrange-multipliers
title: Lagrange Multipliers
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector
  type: hard
- id: critical-points-multivariable
  type: hard
- id: systems-substitution
  type: soft
- id: second-partials-test
  type: soft
tags:
- Lagrange-multipliers
- constrained-optimization
- constraint
- level-curves
stage: formal-systems
status: validated
---
# Lagrange Multipliers

## Core Idea
To optimize f(x, y) subject to a constraint g(x, y) = c, the method of Lagrange multipliers states that at an optimum, ∇f = λ∇g for some scalar λ (the Lagrange multiplier). Geometrically, this means the level curves of f and g are tangent — the constrained extrema occur where f stops changing along the constraint curve. The method converts a constrained optimization problem into solving the system ∇f = λ∇g and g = c simultaneously.

## How It's Best Learned
Draw overlapping level curves of f and the constraint curve g = c. Show geometrically that at a constrained maximum, the level curve of f is tangent to the constraint — i.e., their gradients are parallel. Then introduce λ as the proportionality constant. This builds intuition before algebra. Practice with classic problems: box of given surface area, point on a surface closest to the origin.

## Common Misconceptions
- λ is an auxiliary variable to be eliminated; its value alone rarely has direct meaning.
- Lagrange multipliers find candidates for optima — you must compare the objective function values at all candidates to identify the actual maximum or minimum.
- The method fails if ∇g = 0 at the optimum (a degenerate constraint); this is the regularity condition.
