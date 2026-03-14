---
id: factor-theorem
title: Factor Theorem
domain: mathematics
course: algebra-2
prerequisites:
  - id: remainder-theorem
    type: hard
builds-toward:
  - rational-root-theorem
  - fundamental-theorem-of-algebra
tags: [polynomials, factor-theorem, zeros, roots]
stage: abstract-reasoning
status: validated
---

# Factor Theorem

## Core Idea
The Factor Theorem is a corollary of the Remainder Theorem: (x - c) is a factor of f(x) if and only if f(c) = 0. In other words, c is a zero (root) of f(x) exactly when (x - c) divides f(x) evenly. This connects the algebraic concept of factoring with the graphical concept of x-intercepts: every zero of the polynomial corresponds to a linear factor.

## How It's Best Learned
Given a polynomial and a candidate zero, use synthetic division or direct evaluation to test whether it is a root. If the remainder is 0, write the factorization. Practice finding all factors of a polynomial by combining the factor theorem with the rational root theorem. Connect zeros to x-intercepts on the graph.

## Common Misconceptions
- Confusing roots (values of x where f(x) = 0) with factors ((x - c) divides f(x)).
- Forgetting the sign: if c is a root, the factor is (x - c), not (x + c).
- Thinking the factor theorem provides a method for finding roots (it only tests candidates; the rational root theorem provides candidates).
