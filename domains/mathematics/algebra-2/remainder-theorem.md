---
id: remainder-theorem
title: Remainder Theorem
domain: mathematics
course: algebra-2
prerequisites:
  - id: synthetic-division
    type: hard
  - id: polynomial-long-division
    type: hard
builds-toward:
  - factor-theorem
tags: [polynomials, remainder-theorem, evaluation]
stage: abstract-reasoning
status: validated
---

# Remainder Theorem

## Core Idea
The Remainder Theorem states that when a polynomial f(x) is divided by (x - c), the remainder equals f(c). This provides a quick way to evaluate polynomials: instead of substituting c into f(x), perform synthetic division and read the remainder. It also connects polynomial division to polynomial evaluation and lays the groundwork for the Factor Theorem.

## How It's Best Learned
Verify the theorem with examples: divide f(x) by (x - c) using synthetic division, then compute f(c) directly, and confirm they match. Practice using the theorem to evaluate polynomials efficiently. Give problems where the remainder is given and students must find unknown coefficients.

## Common Misconceptions
- Confusing the remainder theorem with the factor theorem (the factor theorem is the special case where the remainder is 0).
- Evaluating f(-c) instead of f(c) when dividing by (x - c).
- Thinking the theorem applies to non-polynomial functions.

## Explainer

From polynomial long division and synthetic division, you know how to divide f(x) by a linear factor (x − c) to get a quotient q(x) and a remainder r: f(x) = (x − c)·q(x) + r. Notice that r is a constant — when you divide by a degree-1 polynomial, the remainder is degree 0 (just a number). The **Remainder Theorem** follows immediately: substitute x = c into both sides. The left side gives f(c). The right side gives (c − c)·q(c) + r = 0 + r = r. So f(c) = r. The remainder is not just any number — it is exactly the value of the polynomial at x = c.

This is a shortcut for polynomial evaluation. To find f(7) for f(x) = x⁴ − 3x³ + 2x − 5, you could substitute 7 directly and grind through four multiplications. Alternatively, perform synthetic division with c = 7 and read the remainder — it equals f(7). For high-degree polynomials or repeated evaluations, synthetic division is often faster than direct substitution, and the Remainder Theorem is the theorem that lets you interpret the remainder as a function value.

The theorem also inverts the question. Suppose you know that when f(x) = 2x³ + kx − 1 is divided by (x − 3), the remainder is 8. Then f(3) = 8, so 2(27) + 3k − 1 = 8, giving 54 + 3k − 1 = 8, so 3k = −45 and k = −15. The Remainder Theorem turns remainder information into an equation you can solve for unknown coefficients — a class of problems that would be awkward to approach any other way.

The natural special case is when the remainder equals zero: f(c) = 0 means c is a root of f. This is the **Factor Theorem** (your next topic): f(c) = 0 if and only if (x − c) is a factor of f(x). The Remainder Theorem is the general version; the Factor Theorem is the zero-remainder case. Together they form the bridge between roots of polynomials, factors of polynomials, and the synthetic division process — a trio of ideas that will dominate your work with higher-degree polynomials.


