---
id: continuity-multivariable
title: Continuity in Multiple Variables
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: multivariable-limits
  type: hard
- id: epsilon-delta-continuity
  type: soft
builds-toward:
- partial-derivatives
- differentiability-multivariable
tags:
- continuity
- limits
stage: advanced
status: draft
---

# Continuity in Multiple Variables

## Core Idea
Function f(x, y) is continuous at (a, b) if lim_{(x,y)→(a,b)} f(x, y) = f(a, b). In multiple variables, the limit must be the same approaching from all directions, making the concept richer than in one dimension.

## Explainer

In single-variable calculus, continuity at a point means the limit equals the function value — and a limit in ℝ can only be approached from two directions (left and right). In multiple variables, a point like (a, b) in ℝ² can be approached along infinitely many paths: along the x-axis, along the y-axis, along any line y = mx, along parabolas y = cx², along spirals. From your study of multivariable limits, you know that the limit lim_{(x,y)→(a,b)} f(x,y) exists only if *all* these paths give the same value. **Continuity** builds directly on this: f is continuous at (a, b) if the limit exists, equals f(a, b), and f(a, b) is defined.

The richer path structure creates failure modes that don't exist in one dimension. The classic example is f(x, y) = xy/(x² + y²) at the origin (with f(0,0) = 0). Along any line y = mx, the limit as (x, y) → (0, 0) is mx²/(x²(1 + m²)) = m/(1 + m²) — which depends on m. Different lines give different limits, so the limit doesn't exist and f is not continuous at the origin. Yet both iterated limits lim_{x→0} lim_{y→0} f and lim_{y→0} lim_{x→0} f equal 0. This shows that checking continuity by fixing one variable at a time is insufficient — the joint limit is the true test.

Geometrically, continuity of f(x, y) means the surface z = f(x, y) has no holes or jumps — it is a connected surface without tears. The ε-δ definition transfers from single-variable calculus: for every ε > 0 there exists δ > 0 such that whenever ||(x, y) − (a, b)|| < δ, we have |f(x, y) − f(a, b)| < ε. Here the distance is the Euclidean distance in ℝ², capturing all directions simultaneously.

Continuity in multiple variables has the same stability properties you learned in one dimension: sums, products, and compositions of continuous functions are continuous, and quotients are continuous where the denominator is nonzero. Polynomials in x and y are continuous everywhere; rational functions are continuous on their domain. Continuity is the prerequisite for differentiability: just as in one variable, a function must be continuous at a point to be differentiable there. The converse fails sharply — partial derivatives can exist at a point even if the function is discontinuous there — which is why the stronger condition of **differentiability** will require more than just the existence of partial derivatives.
