---
id: gaussian-elimination
title: Gaussian Elimination
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrices-intro
  type: hard
- id: systems-elimination
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- row-echelon-form
- lu-decomposition
- determinant-properties
tags:
- Gaussian elimination
- row operations
- augmented matrix
- systems
- back substitution
stage: formal-systems
status: validated
---

# Gaussian Elimination

## Core Idea
Gaussian elimination is a systematic algorithm for solving systems of linear equations by applying three elementary row operations to an augmented matrix: swapping two rows, multiplying a row by a nonzero scalar, and adding a multiple of one row to another. These operations preserve the solution set while simplifying the system into a triangular form from which back-substitution yields the solution. The algorithm scales to systems with any number of equations and unknowns. Gaussian elimination is the computational engine underlying nearly every major result in linear algebra.

## How It's Best Learned
Work through 2×2 and 3×3 systems by hand to build the algorithm's logic, then practice on systems with infinitely many or no solutions. Explicitly track what each row operation does to the system of equations before compressing to pure matrix notation.

## Common Misconceptions
- Students often perform row operations on only one side of the augmented matrix, forgetting to apply the operation to the right-hand-side column.
- Dividing a row by its leading entry prematurely can introduce fractions; it is valid but often creates more arithmetic errors.
- Gaussian elimination on a system with no solution terminates with a row of the form [0 0 … 0 | c] where c ≠ 0, not with an error.
