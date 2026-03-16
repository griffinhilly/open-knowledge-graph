---
id: rational-functions-and-asymptotes
title: Rational Functions and Asymptotes
domain: mathematics
course: algebra-2
prerequisites:
  - id: polynomial-long-division
    type: hard
  - id: polynomial-functions-degree-and-leading-coefficient
    type: hard
builds-toward:
  - graphing-rational-functions
  - solving-rational-equations
tags: [rational-functions, asymptotes, vertical, horizontal, oblique]
stage: abstract-reasoning
status: validated
---

# Rational Functions and Asymptotes

## Core Idea
A rational function is a ratio of two polynomials: f(x) = p(x)/q(x). Vertical asymptotes occur at values where q(x) = 0 and p(x) != 0. Horizontal asymptotes depend on the degree comparison: if deg(p) < deg(q), the HA is y = 0; if deg(p) = deg(q), the HA is y = (leading coefficient of p)/(leading coefficient of q); if deg(p) > deg(q), there is no horizontal asymptote (but there may be an oblique asymptote found via polynomial long division). Holes occur where both p and q share a common factor.

## How It's Best Learned
Analyze the function algebraically before graphing: find domain restrictions, factor numerator and denominator, identify holes vs. vertical asymptotes, determine horizontal/oblique asymptotes by degree comparison. Build understanding incrementally with simpler rational functions (1/x, 1/x^2) before more complex ones.

## Common Misconceptions
- Confusing holes and vertical asymptotes (holes occur when a factor cancels; VAs occur when it does not).
- Thinking the graph cannot cross a horizontal asymptote (it can, in the middle of its domain; HAs describe end behavior only).
- Not factoring before identifying asymptotes, leading to missed holes.

## Explainer

A **rational function** is simply a fraction where both numerator and denominator are polynomials. From your study of polynomial functions and long division, you know how polynomials behave: degree controls end behavior, roots control zeros. A rational function inherits this, but the denominator adds new phenomena — places where the function breaks down or grows without bound.

The first thing to do with any rational function is **factor completely**. Why? Because a shared factor in numerator and denominator signals a **hole** (removable discontinuity), not a vertical asymptote. If f(x) = (x−2)(x+3)/[(x−2)(x−5)], then (x−2) cancels, leaving a hole at x = 2 (the function is undefined there but the graph approaches a finite value) and a vertical asymptote only at x = 5 (where the denominator is zero but the numerator isn't). Skipping factoring means misclassifying these features every time.

**Vertical asymptotes** occur where the denominator is zero after cancellation — the function grows without bound near these x-values. **Horizontal asymptotes** describe end behavior: what happens as x → ±∞. You can determine this by comparing the degrees of numerator and denominator, using the intuition that the highest-degree terms dominate. If the denominator wins (higher degree), the fraction shrinks toward 0. If they tie, the ratio of leading coefficients survives. If the numerator wins (higher degree by exactly 1), polynomial long division extracts an oblique (slant) asymptote — the quotient from the division is the line the function approaches. This is why polynomial long division was a prerequisite: it directly produces the oblique asymptote.

One subtlety worth sitting with: a horizontal asymptote describes *end behavior only*. The function can cross the horizontal asymptote at finite x-values — the asymptote is not a barrier, just a destination. This contrasts with vertical asymptotes, which the function can never cross (because it's undefined there). Keeping this distinction clear — vertical asymptotes are domain restrictions, horizontal asymptotes are behavioral limits — helps you sketch rational functions accurately and interpret them in applied contexts like rates and concentrations.
