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
