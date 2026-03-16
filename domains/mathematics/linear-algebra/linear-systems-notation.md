---
id: linear-systems-notation
title: 'Linear Systems: Notation and Solution Existence'
domain: mathematics
course: linear-algebra
prerequisites:
- id: systems-of-three-variables
  type: hard
- id: matrices-intro
  type: hard
builds-toward:
- gaussian-elimination-method
- rank-nullity-theorem
- linear-systems-consistency
tags:
- systems
- Ax=b
- notation
- existence
stage: formal-systems
status: draft
---

# Linear Systems: Notation and Solution Existence

## Core Idea
A system of m linear equations in n unknowns is written as Ax = b, where A is m×n, x is the unknown vector, and b is the right-hand side. Solutions exist if and only if b is in the column space of A. The solution set is either empty, a single point, or an affine subspace (infinite solutions). Augmented matrices [A | b] encode the system compactly.

## Explainer

You already know how to solve a system of three equations in three unknowns by hand — substitution, elimination, back-substitution. You also know what a matrix is. The notation Ax = b packages everything you already know into a single symbolic object, and that packaging has enormous power.

In the system Ax = b, **A** is the **coefficient matrix** (m rows for equations, n columns for unknowns), **x** is the **unknown vector** (the column of variables you are solving for), and **b** is the **right-hand side vector** (the constants). The product Ax is a weighted sum of A's columns — specifically, the ith entry of Ax is the dot product of the ith row of A with x. Writing a system this way makes it easy to discuss systems of any size, not just 2×2 or 3×3.

The **augmented matrix** [A | b] is a further shorthand: you stack the coefficient matrix and the right-hand side together, separated by a vertical bar. This is the object you actually row-reduce. Writing [A | b] captures the entire system without writing out variables, making manipulations purely mechanical — you work with numbers and rows, not algebraic expressions.

The deepest idea in this topic is the **column space interpretation**. The product Ax is a linear combination of A's columns, using the entries of x as coefficients. So the question "does the system Ax = b have a solution?" becomes: "can b be written as a linear combination of A's columns?" If b lies in the column space of A, a solution exists. If not, there is no solution. Once a solution exists, there are exactly two cases: the solution is unique (if the null space of A contains only the zero vector) or there are infinitely many solutions (parameterized by the null space). These three outcomes — no solution, one solution, infinitely many — are the only possibilities for any linear system.
