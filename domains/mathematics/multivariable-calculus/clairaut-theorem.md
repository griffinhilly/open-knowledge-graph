---
id: clairaut-theorem
title: 'Clairaut''s Theorem: Equality of Mixed Partials'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: higher-order-partials
  type: hard
builds-toward:
- hessian-matrix-second-derivative-test
tags:
- mixed-partials
- continuity
- symmetry
stage: formal-systems
status: draft
---

# Clairaut's Theorem: Equality of Mixed Partials

## Core Idea
If ∂²f/∂x∂y and ∂²f/∂y∂x are continuous at a point, then ∂²f/∂x∂y = ∂²f/∂y∂x. This 'equality of mixed partials' shows that (for most practical functions) the order of differentiation does not matter.

## Explainer

From your study of higher-order partial derivatives, you know that after taking a partial derivative of a multivariable function, the result is another function that you can differentiate again. The **mixed partial derivatives** ∂²f/∂x∂y and ∂²f/∂y∂x both measure how the function curves in both the x and y directions — but they arrive there by a different route. The first differentiates with respect to y first, then x; the second reverses the order. A natural question is whether the route matters.

**Clairaut's theorem** (also called Schwarz's theorem) says: if both mixed partials exist and are continuous at a point, they are equal there. For the smooth functions that appear in calculus courses — polynomials, exponentials, sines, cosines, and their combinations — continuity of the mixed partials is automatic, so the order of differentiation is irrelevant in practice. As a heuristic: if f is built from standard elementary functions and has no special piecewise behavior, assume the mixed partials commute.

To see why continuity matters, consider the classic counterexample: f(x, y) = xy(x² − y²)/(x² + y²) for (x, y) ≠ (0, 0) and f(0, 0) = 0. Careful computation shows ∂²f/∂x∂y|(0,0) = 1 while ∂²f/∂y∂x|(0,0) = −1. The mixed partials exist but are not equal because the continuity hypothesis fails at the origin. This example shows the theorem is not vacuous — the continuity condition is doing real work.

In practice, Clairaut's theorem means you can choose whichever order of differentiation is algebraically easier. When computing the **Hessian matrix** (the matrix of all second-order partial derivatives), the off-diagonal entries are mixed partials: H_ij = ∂²f/∂xᵢ∂xⱼ. Clairaut's theorem guarantees H is symmetric for smooth functions, which is a crucial structural fact — symmetric matrices have real eigenvalues, and the signs of those eigenvalues determine whether a critical point is a local min, local max, or saddle point. So this seemingly small commutativity result underpins the second derivative test in multiple dimensions.
