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
status: validated
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

## Explainer

You've spent weeks learning to differentiate functions. Antidifferentiation is the reverse question: given a function f(x), can you find a function F(x) whose derivative is f(x)? The answer is almost always yes, and building the skill to find F(x) opens the door to the Fundamental Theorem of Calculus — one of the most important results in all of mathematics.

The basic strategy is to read your differentiation rules backwards. Since d/dx[x^n] = nx^(n-1), working backwards: if you see x^n, you need x^(n+1)/(n+1), because differentiating that gives x^n. The **power rule for antiderivatives** says: ∫x^n dx = x^(n+1)/(n+1) + C (for n ≠ -1). Notice the exponent *increases* by 1 — opposite of differentiation — and you divide by the new exponent. Similarly, since d/dx[sin x] = cos x, an antiderivative of cos x is sin x. Since d/dx[e^x] = e^x, an antiderivative of e^x is e^x itself. Build a table by reversing every derivative rule you know.

The **+C** — the constant of integration — is not optional bookkeeping. It's mathematically necessary. If F'(x) = f(x), then (F(x) + 7)' = f(x) too, and so does (F(x) - 12)'. All these functions have the same derivative because constants vanish when differentiated. The *general antiderivative* therefore represents an entire family of functions, all shifted vertically from each other. You can pin down C only when you have additional information — for instance, knowing that F(0) = 5 or that F passes through a specific point.

The constant of integration also reveals why antidifferentiating products is harder than differentiating them. The product rule d/dx[uv] = u'v + uv' means the derivative of a product is a sum of two terms. Going backwards, if you see a sum, you'd have to recognize it came from a product — which requires insight rather than a mechanical rule. This is why techniques like integration by parts are needed later: they translate difficult antiderivative problems back into solvable derivative computations. For now, the key skill is recognizing the basic patterns and applying the reverse rules accurately, always including +C.
