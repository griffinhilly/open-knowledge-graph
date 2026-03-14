---
id: polynomial-long-division
title: Polynomial Long Division
domain: mathematics
course: algebra-2
prerequisites:
- id: polynomial-functions-degree-and-leading-coefficient
  type: hard
- id: multiplying-polynomials
  type: hard
- id: graphing-polynomial-functions
  type: soft
builds-toward:
- synthetic-division
- remainder-theorem
- rational-functions-and-asymptotes
tags:
- polynomials
- division
- long-division
- quotient-remainder
stage: abstract-reasoning
status: validated
---
# Polynomial Long Division

## Core Idea
Polynomial long division divides a polynomial by another polynomial, producing a quotient and remainder, analogous to integer long division. If f(x) = d(x)*q(x) + r(x), where deg(r) < deg(d). The process: divide leading terms, multiply, subtract, bring down, repeat. This is essential for simplifying rational expressions, finding oblique asymptotes, and applying the remainder and factor theorems.

## How It's Best Learned
Draw the explicit parallel to integer long division. Start with divisors of degree 1 (linear), then degree 2. Emphasize including placeholder terms for missing powers (e.g., 0x^2). Practice verifying answers by multiplying quotient by divisor and adding the remainder.

## Common Misconceptions
- Forgetting to include terms with zero coefficients as placeholders.
- Subtracting incorrectly (sign errors are the most common mistake).
- Stopping too early or too late in the division process.
- Not knowing when the process is complete (when the remainder's degree is less than the divisor's degree).
