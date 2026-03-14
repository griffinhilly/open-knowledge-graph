---
id: systems-of-three-variables
title: Systems of Three Variables
domain: mathematics
course: algebra-2
prerequisites:
  - id: systems-elimination
    type: hard
  - id: equations-variables-both-sides
    type: hard
builds-toward:
  - matrices-intro
  - matrix-operations
tags: [systems, three-variables, elimination, substitution]
stage: abstract-reasoning
status: validated
---

# Systems of Three Variables

## Core Idea
A system of three linear equations in three variables (x, y, z) represents three planes in 3D space. The solution is the point (or set of points) where all three planes intersect. Solving methods: elimination (reduce to a 2-variable system, then to 1 variable) or substitution. Solutions can be a single point (planes intersect at one point), infinitely many (planes share a line or are identical), or no solution (inconsistent). This extends the 2-variable methods to higher dimensions.

## How It's Best Learned
Start by solving 2x2 systems as review, then extend to 3x3. Use Gaussian elimination systematically: eliminate one variable from two pairs of equations to get a 2x2 system, solve it, then back-substitute. Show geometric interpretations (three planes intersecting). Practice identifying inconsistent and dependent systems.

## Common Misconceptions
- Losing track of which variable to eliminate (be systematic).
- Arithmetic errors compounding through multiple elimination steps.
- Thinking three equations always have a unique solution (they can be inconsistent or dependent).
- Not checking the solution in all three original equations.
