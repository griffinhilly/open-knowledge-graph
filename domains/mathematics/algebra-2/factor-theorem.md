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

## Explainer

The **Remainder Theorem**, your prerequisite, tells you that when you divide a polynomial f(x) by (x − c), the remainder is exactly f(c). The Factor Theorem asks: what if the remainder is zero? If f(c) = 0, then (x − c) divides f(x) with no remainder — meaning (x − c) is a **factor** of f(x). And if (x − c) is a factor, then substituting x = c into f(x) gives zero. These two directions together form an "if and only if": c is a root of f exactly when (x − c) is a factor.

This creates a three-way equivalence connecting algebra and geometry. For a polynomial f(x): (1) c is a **zero** — f(c) = 0. (2) (x − c) is a **factor** — f(x) = (x − c) · q(x) for some polynomial q. (3) c is an **x-intercept** — the graph of y = f(x) crosses or touches the x-axis at the point (c, 0). These three descriptions say the same thing. When you find a root graphically, you know the factor. When you confirm a factor algebraically, you know the intercept.

In practice, the theorem is used as a testing and peeling tool. Suppose f(x) = x³ − 6x² + 11x − 6 and you suspect x = 2 is a root. Evaluate: f(2) = 8 − 24 + 22 − 6 = 0. ✓ So (x − 2) is a factor. Divide f(x) by (x − 2) — using synthetic division or long division — to get the quotient q(x) = x² − 4x + 3. Now factor q: (x − 1)(x − 3). The full factorization is (x − 2)(x − 1)(x − 3), and all three roots appear as the constants with reversed sign: 1, 2, 3.

Notice what the theorem does and does not do: it **confirms** a root and **extracts** the corresponding factor, but it does not tell you which c to try first. That job belongs to the Rational Root Theorem, which provides the candidates. The Factor Theorem is the test — once you have a candidate, evaluate f(c); if the result is zero, you've found a factor. Together, these two tools let you systematically dismantle a polynomial into linear (and eventually irreducible quadratic) pieces, which is the foundation for everything from solving higher-degree equations to analyzing rational functions.
