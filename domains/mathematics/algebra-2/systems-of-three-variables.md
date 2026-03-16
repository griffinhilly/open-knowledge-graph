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

## Explainer

You already know how to solve a two-equation system in two unknowns. Each equation defines a line, and the solution is the intersection point. Now extend that geometric picture one dimension: three equations in three variables (x, y, z) each define a **plane** in three-dimensional space. The solution to the system is whatever geometric object all three planes share — most often a single point (x, y, z), but sometimes a line, sometimes all of space (if the planes are identical), and sometimes nothing (if the planes are inconsistent).

The strategy is a direct extension of elimination you already know, applied in two stages. Pick one variable to eliminate — say z. Eliminate z from two different pairs of equations. Each elimination step produces one equation in just x and y. After two eliminations, you have a standard 2×2 system to solve. Once x and y are known, substitute back into any original equation to find z. This staged reduction is **Gaussian elimination**: systematically lower the number of variables per equation until one variable can be solved outright, then back-substitute.

A worked example: given (1) x + y + z = 6, (2) 2x − y + z = 3, (3) x + 2y − z = 2. To eliminate z, add (1) and (3): 2x + 3y = 8. Subtract (2) from (1): −x + 2y = 3. Now solve this 2×2 system: from the second equation, x = 2y − 3. Substitute into the first: 2(2y − 3) + 3y = 8 → 7y = 14 → y = 2. Then x = 1. Back-substitute into (1): 1 + 2 + z = 6 → z = 3. Always verify by plugging (1, 2, 3) into all three originals — this catches arithmetic errors that compound through multiple steps.

Not every 3×3 system has a unique solution. If during elimination you reach a **contradiction** like 0 = 5, the system is **inconsistent** — the planes have no common point (imagine three planes arranged like a triangle's faces, meeting pairwise in lines but never all at once). If you reach a **tautology** like 0 = 0, the system is **dependent** — infinitely many solutions lie on a shared line or plane. The algebraic signals (contradiction vs. tautology) map directly onto the geometric configurations, and recognizing them is as important as solving the unique case.
