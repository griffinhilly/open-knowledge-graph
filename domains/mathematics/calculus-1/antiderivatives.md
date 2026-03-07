---
id: antiderivatives
title: Antiderivatives
domain: mathematics
course: calculus-1
prerequisites:
  - id: power-rule
    type: hard
  - id: derivatives-of-trigonometric-functions
    type: hard
  - id: derivatives-of-exponential-functions
    type: hard
builds-toward:
  - indefinite-integrals
  - fundamental-theorem-of-calculus-part-1
tags: [integration, antiderivatives, reverse-differentiation]
stage: formal-systems
status: draft
---

# Antiderivatives

## Core Idea
An antiderivative of f(x) is a function F(x) whose derivative is f(x): F'(x) = f(x). Finding antiderivatives is "undoing" differentiation. The general antiderivative includes an arbitrary constant C because the derivative of a constant is zero: if F'(x) = f(x), then (F(x) + C)' = f(x) too. Antiderivatives are the key to evaluating definite integrals via the Fundamental Theorem of Calculus.

## How It's Best Learned
Start by reversing known derivative rules: if d/dx[x^3] = 3x^2, then an antiderivative of 3x^2 is x^3. Build a table of basic antiderivatives from the derivative rules. Emphasize the +C and why it is necessary (different antiderivatives differ by a constant).

## Common Misconceptions
- Forgetting the constant of integration C.
- Trying to antidifferentiate products by antidifferentiating each factor (the product rule does not reverse this simply).
- Confusing the antiderivative of x^n (which uses (n+1), not (n-1)) with the derivative.
