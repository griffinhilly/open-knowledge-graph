---
id: systems-elimination
title: Systems of Equations — Elimination Method
domain: mathematics
course: algebra-1
prerequisites:
  - id: systems-graphing
    type: soft
  - id: solving-multi-step-equations
    type: hard
  - id: standard-form-linear-equations
    type: soft
builds-toward:
  - systems-word-problems
  - matrices-intro
tags: [systems, elimination, solving, linear-equations]
stage: abstract-reasoning
status: validated
---

# Systems of Equations — Elimination Method

## Core Idea
The elimination (or addition) method solves a system by adding or subtracting the equations to eliminate one variable. For 3x + 2y = 16 and 3x − 2y = 2, adding the equations gives 6x = 18, so x = 3. Then substitute back to find y = 3.5. When coefficients do not align, multiply one or both equations by constants first. Elimination works especially well when the system is in standard form and when substitution would create messy fractions. It is the algebraic precursor to Gaussian elimination and matrix methods in linear algebra.

## How It's Best Learned
Start with systems where one variable naturally cancels when added. Then practice multiplying one equation to create opposite coefficients. Finally, practice multiplying both equations. Compare with substitution and discuss when each is more efficient. Check solutions in both original equations. Show special cases (0 = 0 for infinitely many, 0 = 5 for no solution).

## Common Misconceptions
- Adding when you should subtract (or vice versa) — focus on making the coefficients of one variable opposites.
- Multiplying only one term of an equation instead of every term.
- Forgetting to substitute back to find the second variable.

## Explainer

From graphing systems, you know that the solution to a system of two equations is the point where the two lines intersect — it satisfies both equations simultaneously. Elimination gives you an algebraic way to find that point without drawing anything. The core idea is simple: if you add two true equations together, the result is also a true equation. If the coefficients of one variable happen to be opposites in the two equations, adding them makes that variable disappear, leaving you with one equation in one unknown you already know how to solve.

Consider the system 3x + 2y = 16 and 3x − 2y = 2. The y terms have coefficients +2 and −2, which are opposites. Adding the equations gives 6x = 18, so x = 3. Substitute back into either original equation — say 3(3) + 2y = 16 — and you get 2y = 7, so y = 3.5. The solution is (3, 3.5). The key move was recognizing the **opposite coefficients** and exploiting them by addition. If the coefficients had been equal (say both +2), subtraction would have worked instead.

When coefficients are not already opposites, you create them by **scaling an equation**. Multiplying every term in an equation by the same constant produces an equivalent equation — one that has the same solution set. For example, to solve 2x + 3y = 11 and 5x − 2y = 4, notice that 2 and 3 are not opposite, nor are 5 and 2. Multiply the first equation by 2 and the second by 3 to get 4x + 6y = 22 and 15x − 6y = 12. Now y has opposite coefficients (+6 and −6), so adding gives 19x = 34. Continue from there. The choice of which variable to eliminate is yours — pick whichever requires simpler scaling.

The elimination method connects directly to the matrix methods you will use later. When you write the equations in standard form (ax + by = c) and stack them vertically, you are setting up a matrix of coefficients. Adding a multiple of one row to another to create a zero — which is exactly what you do here — is called a **row operation**, and it is the foundation of Gaussian elimination in linear algebra. The method you are learning now is not just an algebra trick; it is the manual version of the algorithm computers use to solve large systems of equations.
