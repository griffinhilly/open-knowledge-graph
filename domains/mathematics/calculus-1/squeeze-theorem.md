---
id: squeeze-theorem
title: Squeeze Theorem
domain: mathematics
course: calculus-1
prerequisites:
  - id: limit-laws
    type: hard
builds-toward:
  - derivatives-of-trigonometric-functions
tags: [limits, squeeze-theorem, special-limits]
stage: formal-systems
status: draft
---

# Squeeze Theorem

## Core Idea
The Squeeze Theorem states that if g(x) <= f(x) <= h(x) near x = a, and lim g(x) = lim h(x) = L, then lim f(x) = L. The function f is "squeezed" between two functions that converge to the same limit. The most famous application is proving lim(x->0) sin(x)/x = 1, a result needed for the derivative of sin(x).

## How It's Best Learned
Prove lim(x->0) sin(x)/x = 1 geometrically using the unit circle area argument. Then apply the squeeze theorem to related limits like lim(x->0) (1 - cos(x))/x = 0. Practice identifying bounding functions in other squeeze theorem problems (e.g., x^2 * sin(1/x) near 0).

## Common Misconceptions
- Trying to apply the squeeze theorem when the bounding functions do not converge to the same limit.
- Confusing the squeeze theorem with limit comparison (they are different tools).
- Not verifying the inequality g(x) <= f(x) <= h(x) holds near the point of interest.
