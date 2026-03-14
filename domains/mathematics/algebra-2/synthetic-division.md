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
