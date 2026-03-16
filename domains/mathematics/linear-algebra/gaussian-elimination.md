---
id: gaussian-elimination
title: Gaussian Elimination and Row Reduction
domain: mathematics
course: linear-algebra
prerequisites:
- id: systems-of-linear-equations
  type: hard
builds-toward:
- row-echelon-form
- reduced-row-echelon-form
tags:
- systems
- gaussian elimination
- row operations
stage: formal-systems
status: draft
---

# Gaussian Elimination and Row Reduction

## Core Idea
Gaussian elimination solves linear systems by applying elementary row operations (swapping rows, scaling, adding multiples) to transform the augmented matrix into simpler form. These operations preserve the solution set. The algorithm produces row echelon form or reduced row echelon form for direct solution.

## Explainer

You already know how to solve systems of linear equations by substitution or elimination — adding equations together, multiplying one by a constant, and using one equation to simplify another. **Gaussian elimination** is that same process, made systematic and organized through a powerful notational shorthand: the **augmented matrix**.

The key insight is that what matters in a linear system is not the variable names — it's the coefficients and constants. The system 2x + 3y = 7 and x − y = 1 carries all its information in the numbers 2, 3, 7, 1, −1, 1. An augmented matrix writes those numbers in a grid: [2 3 | 7] and [1 −1 | 1]. Now instead of "multiply the second equation by 2 and subtract from the first," you do the same thing to rows of the matrix. The variables become implicit; the structure becomes visible.

There are three **elementary row operations**: swap two rows, multiply a row by a nonzero constant, and add a multiple of one row to another. Each operation corresponds to something you already did when solving systems — they are just algebraic manipulations on equations. The crucial fact is that all three operations are **reversible** and preserve the solution set. Any solution to the original system is a solution to the transformed system, and vice versa. This means you can manipulate the matrix freely without worrying about losing or gaining solutions.

The goal is to reach **row echelon form**: a staircase shape where each row starts with a **pivot** (a leading nonzero entry) that is further to the right than the pivot in the row above, and all entries below each pivot are zero. Once you have this form, the bottom row gives you one variable directly, and you solve the rest by **back substitution** — plugging the known value up into the next row, then the next, until all variables are resolved. If you continue further to clear entries *above* each pivot too, you reach **reduced row echelon form**, where back substitution becomes trivial: each pivot row directly gives you one variable's value, and the solution can be read off immediately.
