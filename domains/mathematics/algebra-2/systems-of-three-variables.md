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

## Questions

```yaml
- question: "While solving a 3×3 linear system by elimination, you correctly reduce to two equations in x and y, then derive the equation 0 = 5. What does this mean?"
  type: multiple-choice
  options:
    - "The system is inconsistent — there is no point where all three planes intersect"
    - "You made an arithmetic error — a valid system always yields a solvable equation at this stage"
    - "The system has infinitely many solutions — 0 = 5 indicates the planes coincide"
    - "You need to switch to substitution to proceed"
  answer: 0
  explanation: "A contradiction like 0 = 5 is a meaningful algebraic signal, not an error. It means the three planes have no common intersection — the system is inconsistent. Geometrically, the planes may intersect each other pairwise in lines but never all three at one point (like the three faces of a triangular prism). If instead you reached 0 = 0, that would indicate infinitely many solutions (a dependent system). Only an equation with a variable term yields a unique value for that variable."

- question: "A system of three linear equations in three variables has a unique solution. What does this mean geometrically?"
  type: multiple-choice
  options:
    - "All three planes intersect at exactly one point in three-dimensional space"
    - "The three planes are all parallel to each other"
    - "Two of the planes are parallel and the third crosses both"
    - "All three planes are identical — they occupy the same region of space"
  answer: 0
  explanation: "Each equation in three variables defines a plane. A unique solution means there is exactly one point (x, y, z) satisfying all three equations simultaneously — one point all three planes share. Options B and C describe configurations with no solution (inconsistent). Option D describes infinitely many solutions (dependent). The geometry of three planes in 3D offers exactly these outcomes: one point, a line or plane of overlap, or no overlap."

- question: "A system of three linear equations in three variables typically has exactly one solution, since three equations should uniquely determine three unknowns."
  type: true-false
  answer: false
  explanation: "Three equations and three unknowns do not guarantee a unique solution. The system can be inconsistent (no solution — the planes have no common intersection point) or dependent (infinitely many solutions — the planes share a line or are identical). The algebraic signals during elimination reveal which case applies: a contradiction (0 = 5) means inconsistent; a tautology (0 = 0) means dependent. Assuming uniqueness without checking leads to incorrect conclusions."

- question: "If reducing a 3×3 system by elimination produces the equation 0 = 0, the system has infinitely many solutions."
  type: true-false
  answer: true
  explanation: "0 = 0 is a tautology — always true and carrying no information about the variables. This means the equations are not fully independent: one is a linear combination of the others, so they do not together constrain the solution to a single point. Geometrically, the planes share more than a point — they intersect in a line or one plane contains another. Infinitely many points on that shared object satisfy all three equations."

- question: "Describe the two-stage process for solving a 3×3 linear system by elimination. Why must you eliminate the same variable from two different pairs of equations in the first stage, rather than just one pair?"
  type: short-answer
  answer: "In the first stage, choose one variable (say z) and eliminate it from two different pairs of equations — for example, equations 1 & 2, then equations 1 & 3. Each elimination produces one equation in only x and y, giving a 2×2 system. In the second stage, solve that 2×2 system for x and y, then substitute back into any original equation to find z. You must use two different pairs because a single elimination only removes z from one pair, giving you just one equation in x and y — not enough to solve for two unknowns."
  explanation: "The strategy is staged reduction: each stage reduces the number of variables per equation by 1. With 3 variables, you need two independent eliminations in the first stage to produce two independent equations in 2 variables. Using the same pair twice would yield two copies of the same equation — not two independent constraints — leaving the 2×2 system unsolvable. Independence of the derived equations is as important as the mechanics of elimination."
```

## Explainer

You already know how to solve a two-equation system in two unknowns. Each equation defines a line, and the solution is the intersection point. Now extend that geometric picture one dimension: three equations in three variables (x, y, z) each define a **plane** in three-dimensional space. The solution to the system is whatever geometric object all three planes share — most often a single point (x, y, z), but sometimes a line, sometimes all of space (if the planes are identical), and sometimes nothing (if the planes are inconsistent).

The strategy is a direct extension of elimination you already know, applied in two stages. Pick one variable to eliminate — say z. Eliminate z from two different pairs of equations. Each elimination step produces one equation in just x and y. After two eliminations, you have a standard 2×2 system to solve. Once x and y are known, substitute back into any original equation to find z. This staged reduction is **Gaussian elimination**: systematically lower the number of variables per equation until one variable can be solved outright, then back-substitute.

A worked example: given (1) x + y + z = 6, (2) 2x − y + z = 3, (3) x + 2y − z = 2. To eliminate z, add (1) and (3): 2x + 3y = 8. Subtract (2) from (1): −x + 2y = 3. Now solve this 2×2 system: from the second equation, x = 2y − 3. Substitute into the first: 2(2y − 3) + 3y = 8 → 7y = 14 → y = 2. Then x = 1. Back-substitute into (1): 1 + 2 + z = 6 → z = 3. Always verify by plugging (1, 2, 3) into all three originals — this catches arithmetic errors that compound through multiple steps.

Not every 3×3 system has a unique solution. If during elimination you reach a **contradiction** like 0 = 5, the system is **inconsistent** — the planes have no common point (imagine three planes arranged like a triangle's faces, meeting pairwise in lines but never all at once). If you reach a **tautology** like 0 = 0, the system is **dependent** — infinitely many solutions lie on a shared line or plane. The algebraic signals (contradiction vs. tautology) map directly onto the geometric configurations, and recognizing them is as important as solving the unique case.
