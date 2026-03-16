---
id: synthetic-division
title: Synthetic Division
domain: mathematics
course: algebra-2
prerequisites:
  - id: polynomial-long-division
    type: hard
builds-toward:
  - remainder-theorem
  - factor-theorem
  - rational-root-theorem
tags: [polynomials, division, synthetic-division, shortcut]
stage: abstract-reasoning
status: validated
---

# Synthetic Division

## Core Idea
Synthetic division is a shorthand method for dividing a polynomial by a linear divisor of the form (x - c). It uses only the coefficients and is faster than long division. The process: write c and the coefficients, bring down, multiply, add, repeat. The last number is the remainder, and the others are the quotient coefficients. Synthetic division is a computational shortcut, not a separate concept from long division.

## How It's Best Learned
First show synthetic division alongside long division for the same problem so students see the correspondence. Practice with various values of c, including negative and fractional. Emphasize including zero coefficients for missing terms. Show that it only works for linear divisors (x - c).

## Common Misconceptions
- Using the wrong sign for c (when dividing by x + 3, use c = -3, not +3).
- Forgetting placeholder zeros for missing degree terms.
- Trying to use synthetic division for divisors of degree 2 or higher (it only works for linear divisors).
- Confusing addition and multiplication steps.

## Explainer

You learned polynomial long division by analogy with numerical long division: divide, multiply, subtract, bring down, repeat. Synthetic division compresses that same process into a row of numbers, eliminating the x symbols entirely. It works only when the divisor is linear — of the form (x - c) — but that covers the most common case, and understanding why it works makes it easier to remember.

Consider dividing 2x³ - 3x² + x - 5 by (x - 2). In long division, every step either multiplies by 2 (the value of c) or subtracts. Synthetic division strips out the variables and just tracks what happens to the coefficients. Write c = 2 in a box, then the coefficients 2, -3, 1, -5 in a row. The algorithm is: bring down the first coefficient (2), multiply it by c (2 × 2 = 4), add it to the next coefficient (-3 + 4 = 1), multiply that result by c (1 × 2 = 2), add to the next (1 + 2 = 3), multiply by c again (3 × 2 = 6), add to the last (-5 + 6 = 1). The row reads 2, 1, 3, 1 — meaning the quotient is 2x² + x + 3 with remainder 1.

The crucial sign rule: when you write (x - c), c is the number you put in the box. For (x - 2), c = 2. For (x + 3) = (x - (-3)), c = -3. Getting the sign wrong flips all your multiplications wrong. Also, if a degree is missing in the original polynomial — say you're dividing x⁴ - 1 — you must include a 0 coefficient for every missing term: 1, 0, 0, 0, -1. Otherwise the positions of your result coefficients will all be wrong.

The reason synthetic division is worth learning is not just speed — it connects directly to the **Remainder Theorem** (which you will see next): when you synthetically divide p(x) by (x - c), the remainder equals p(c). So synthetic division simultaneously divides the polynomial and evaluates it at x = c. This makes it a fast way to test whether c is a zero, which feeds directly into the Factor Theorem and the Rational Root Theorem. Synthetic division is not just a shortcut — it is the computational engine for root-finding.
