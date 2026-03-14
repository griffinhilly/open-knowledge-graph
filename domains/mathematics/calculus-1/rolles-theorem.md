---
id: rolles-theorem
title: "Rolle's Theorem"
domain: mathematics
course: calculus-1
prerequisites:
  - id: continuity-definition
    type: hard
  - id: derivative-as-slope-of-tangent
    type: hard
builds-toward:
  - mean-value-theorem
tags: [theorems, Rolle, existence-theorems]
stage: formal-systems
status: validated
---

# Rolle's Theorem

## Core Idea
Rolle's Theorem is a special case of the Mean Value Theorem: if f is continuous on [a, b], differentiable on (a, b), and f(a) = f(b), then there exists at least one c in (a, b) where f'(c) = 0. Geometrically, if a smooth curve starts and ends at the same height, it must have at least one horizontal tangent in between. Rolle's Theorem is the stepping stone to proving the full MVT.

## How It's Best Learned
Visualize: draw curves that start and end at the same height and find where the tangent is horizontal. Verify with specific polynomial examples. Emphasize the three hypotheses and what can go wrong if any is violated.

## Common Misconceptions
- Applying Rolle's Theorem when f(a) does not equal f(b).
- Forgetting to check differentiability (|x| satisfies continuity and f(-1) = f(1) but has no horizontal tangent).
- Assuming the c given by Rolle's Theorem must be unique.
