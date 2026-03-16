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
status: validated
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

## Explainer

From your study of limit laws, you know how to compute limits of sums, products, and quotients algebraically. But some functions resist those techniques — particularly functions like sin(x)/x near x = 0, where direct substitution gives 0/0, an indeterminate form. The Squeeze Theorem is a geometric argument that sidesteps algebraic manipulation by trapping the function between two simpler ones.

The logic is intuitive: if you know a value lies between 3.99 and 4.01, you know it's close to 4. The Squeeze Theorem makes this precise for limits. If g(x) ≤ f(x) ≤ h(x) for all x near a (but not necessarily at a), and both g and h approach the same limit L as x → a, then f is permanently trapped between values approaching L — so f must also approach L. There is no room for f to wander off to a different value.

The canonical application is proving **lim(x→0) sin(x)/x = 1**, which is essential for deriving d/dx[sin x] = cos x. The proof uses a geometric argument on the unit circle: comparing the areas of a small triangle, a circular sector, and a larger triangle, one obtains sin x ≤ x ≤ tan x for small positive x (in radians). Dividing through by sin x and taking reciprocals gives the bounds cos x ≤ sin(x)/x ≤ 1. Since lim(x→0) cos x = 1 and lim(x→0) 1 = 1, the Squeeze Theorem forces lim(x→0) sin(x)/x = 1. Every trigonometric derivative you will compute from this point onward rests on this single limit.

A second class of applications involves functions like f(x) = x² sin(1/x) near x = 0. Direct substitution fails (1/x is undefined at 0), and algebraic manipulation is impossible because sin(1/x) oscillates infinitely rapidly. But you know −1 ≤ sin(1/x) ≤ 1 always, so −x² ≤ x² sin(1/x) ≤ x². Both bounding functions approach 0 as x → 0, so the limit is 0. The **bounding strategy** — find a function that is always ≥ f and one always ≤ f, both with the same limit — is the skill to internalize. The bounds do not need to be tight everywhere, only near the point of interest.
