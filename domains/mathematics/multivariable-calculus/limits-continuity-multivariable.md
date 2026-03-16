---
id: limits-continuity-multivariable
title: Limits and Continuity in Multivariable Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: functions-of-several-variables
  type: hard
- id: limit-definition-intuitive
  type: hard
builds-toward:
- partial-derivatives
- differentiability-multivariate
tags:
- limits
- continuity
- epsilon-delta
stage: formal-systems
status: draft
---

# Limits and Continuity in Multivariable Functions

## Core Idea
For a multivariable function, lim_(x,y)→(a,b) f(x,y) = L if for every ε > 0 there exists δ > 0 such that |f(x,y) − L| < ε whenever 0 < √[(x−a)² + (y−b)²] < δ. Continuity requires the limit to exist and equal f(a, b). Multiple paths to a point complicate convergence analysis.

## Explainer

From single-variable limits, you know that lim_{x→a} f(x) = L means f(x) can be made arbitrarily close to L by taking x close enough to a — from either side. In one dimension, "from either side" covers all possible directions of approach. In two dimensions, the situation is fundamentally harder: there are infinitely many paths through (a, b) — lines at every angle, parabolas, spirals, spirals that spiral inward — and the limit lim_{(x,y)→(a,b)} f(x,y) = L must hold along every single one of them simultaneously.

This is the key new difficulty. If even one path to (a, b) gives a different limiting value, or no limit at all, then the two-variable limit does not exist. The **path test** exploits this: substitute y = mx (approach along straight lines of varying slope m) or y = x² (approach along a parabola) and check whether the result depends on the choice. For f(x,y) = xy/(x² + y²), the limit along y = 0 gives 0, but along y = x gives x²/(2x²) = 1/2. Because two paths give different values, no limit exists at the origin. The path test can efficiently disprove a limit's existence, but it can never prove existence — checking finitely many paths leaves infinitely many unchecked.

To prove a limit exists, you need the full epsilon-delta definition with the Euclidean distance r = √[(x−a)² + (y−b)²] replacing |x−a|. The strategy is to bound |f(x,y) − L| in terms of r and show the bound goes to zero. **Polar coordinates** (x = a + r cos θ, y = b + r sin θ) are often the cleanest tool near the origin: r → 0 corresponds to approaching along any path whatsoever, and if the expression in polar form tends to L independently of θ, the limit is established for all paths at once. The **squeeze theorem** applies in exactly the same way as in one dimension.

**Continuity** at (a, b) means three things hold simultaneously: f is defined there, the limit exists, and the limit equals f(a, b). Polynomials, exponentials, and trigonometric functions are continuous everywhere they are defined — for these, limit evaluation is just substitution. The interesting cases are rational functions where the denominator vanishes, and piecewise-defined functions where you must check whether the pieces agree at the boundary. Continuity is the foundational hypothesis for everything that follows: partial derivatives assume it, the chain rule requires it, and differentiability (which is stronger than continuity) implies it. Getting comfortable with the multi-path nature of limits is the essential step before any further calculus in higher dimensions.
