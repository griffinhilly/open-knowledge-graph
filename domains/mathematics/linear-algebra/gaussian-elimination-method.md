---
id: gaussian-elimination-method
title: Gaussian Elimination and Row Reduction
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-systems-notation
  type: hard
builds-toward:
- row-echelon-form-rref
- gaussian-elimination-pivoting
- rank-nullity-theorem
tags:
- gaussian-elimination
- row-operations
- solving-systems
stage: formal-systems
status: draft
---

# Gaussian Elimination and Row Reduction

## Core Idea
Gaussian elimination transforms an augmented matrix [A | b] via row operations (row swap, row scaling, row addition) into row echelon form, then back-substitution solves the system. Row operations preserve the solution set, making the system equivalent but simpler to solve. Computational cost is O(n³) for an n×n system.

## Explainer

From linear systems notation, you know how to write a system of equations as an augmented matrix [A | b], where each row represents one equation and each column represents one variable (with the last column holding the right-hand side constants). **Gaussian elimination** is a systematic algorithm for solving this system by transforming the matrix into a simpler form without changing its solutions.

The key idea is that three types of **elementary row operations** are solution-preserving: (1) swapping two rows (just reordering the equations), (2) multiplying a row by a nonzero constant (scaling an equation), and (3) adding a multiple of one row to another (combining equations). These operations produce an equivalent system — same solutions, different appearance. The goal is to use these operations strategically to create zeros below the main diagonal, producing a staircase shape called **row echelon form**. In this form, the system is much easier to solve because the last equation involves only one variable, the second-to-last involves at most two, and so on.

Once the matrix is in row echelon form, **back-substitution** solves it from the bottom up. Solve the last equation for its variable, substitute that value into the second-to-last equation, solve for the next variable, and continue upward. This is exactly the process you would follow if you systematically solved one equation at a time from the simplest. The leading entry in each row — the first nonzero entry, called a **pivot** — determines which variable that row "controls."

The algorithm generalizes naturally to any number of variables and equations. Depending on the structure of the matrix, you will encounter one of three outcomes: a unique solution (one pivot per variable), infinitely many solutions (a free variable — some column has no pivot), or no solution (a contradictory row like [0 0 0 | 5]). Reading these outcomes from the final matrix is a core skill in linear algebra. Gaussian elimination also sets the stage for more refined procedures like reduced row echelon form and reveals the rank of a matrix — both of which you will need for deeper results like the rank-nullity theorem.
