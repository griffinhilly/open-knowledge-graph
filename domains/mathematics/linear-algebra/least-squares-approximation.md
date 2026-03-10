---
id: least-squares-approximation
title: Least Squares Approximation
domain: mathematics
course: linear-algebra
prerequisites:
- id: orthogonal-projections
  type: hard
- id: matrix-inverses
  type: hard
- id: matrix-transpose-properties
  type: soft
tags:
- least squares
- normal equations
- overdetermined system
- regression
- best fit
stage: formal-systems
status: draft
---

# Least Squares Approximation

## Core Idea
When a linear system Ax = b has no solution (overdetermined or inconsistent), the least squares solution x̂ minimizes ‖Ax − b‖², the squared Euclidean distance from b to Col(A). The solution satisfies the normal equations AᵀAx̂ = Aᵀb. If the columns of A are linearly independent, AᵀA is invertible and x̂ = (AᵀA)⁻¹Aᵀb uniquely. Geometrically, Ax̂ is the orthogonal projection of b onto Col(A). Least squares is the mathematical foundation for linear regression, curve fitting, and countless engineering applications.

## How It's Best Learned
Set up a simple overdetermined system (more equations than unknowns, e.g., fitting a line through 3 non-collinear points) and solve the normal equations. Verify that the residual b − Ax̂ is orthogonal to Col(A).

## Common Misconceptions
- The least squares solution x̂ does not satisfy Ax̂ = b; it minimizes the error ‖Ax − b‖, not eliminates it.
- If columns of A are linearly dependent, AᵀA is singular and the normal equations have infinitely many solutions; an additional constraint (e.g., minimum norm) is required.
- Least squares does not assume any probability model — it is purely a geometric minimization, though it aligns with maximum likelihood under Gaussian noise assumptions.
