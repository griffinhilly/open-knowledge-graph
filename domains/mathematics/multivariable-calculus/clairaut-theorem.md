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

## Questions

```yaml
- question: "You need to compute ∂²f/∂y∂x for a complicated smooth function f(x,y). Clairaut's theorem lets you compute ∂²f/∂x∂y instead. Under what condition is this substitution valid?"
  type: multiple-choice
  options:
    - "Always — the order of partial differentiation never matters for any function"
    - "Only when f is a polynomial, since those are the only provably smooth functions"
    - "When both mixed partial derivatives exist and are continuous at the point of interest"
    - "Only when f is defined on all of ℝ², not just an open neighborhood"
  answer: 2
  explanation: "Clairaut's theorem requires both mixed partials to exist AND be continuous at the point. For smooth functions built from standard elementary operations (polynomials, trig, exponentials), this is automatic — so practitioners routinely swap the order. But the condition is doing real work: the classic counterexample has mixed partials that exist but are unequal precisely because continuity fails. Option A is false — the counterexample disproves it. Option B is too restrictive; continuity of mixed partials holds far more broadly than just polynomials."

- question: "The Hessian matrix H of a smooth function f: ℝⁿ → ℝ has entries H_ij = ∂²f/∂xᵢ∂xⱼ. Which structural property follows directly from Clairaut's theorem?"
  type: multiple-choice
  options:
    - "The Hessian is always invertible at every point"
    - "The Hessian is symmetric: H_ij = H_ji for all i, j"
    - "The diagonal entries of the Hessian are always positive"
    - "The Hessian has positive determinant at every local minimum"
  answer: 1
  explanation: "Clairaut's theorem guarantees that ∂²f/∂xᵢ∂xⱼ = ∂²f/∂xⱼ∂xᵢ for smooth functions, which means H_ij = H_ji — the Hessian is symmetric. This is a crucial structural fact: symmetric matrices have real eigenvalues, and the signs of those eigenvalues determine whether a critical point is a local min, max, or saddle. Without Clairaut, the Hessian test for critical points would not work as cleanly."

- question: "For smooth functions built from standard elementary operations (polynomials, trig functions, exponentials, and their combinations), the order of mixed partial differentiation can always be swapped without affecting the result."
  type: true-false
  answer: true
  explanation: "Such functions have continuous mixed partial derivatives everywhere on their domain, so Clairaut's theorem applies at every point. In practice, this means you can always choose whichever order of differentiation is algebraically easier. The theorem's continuity hypothesis is automatically satisfied for these function classes."

- question: "Clairaut's theorem guarantees that mixed partial derivatives are equal whenever they both exist, even without requiring continuity."
  type: true-false
  answer: false
  explanation: "Existence alone is not sufficient. The classic counterexample — f(x,y) = xy(x²−y²)/(x²+y²) at the origin — has both mixed partial derivatives existing at (0,0), but ∂²f/∂x∂y = 1 while ∂²f/∂y∂x = −1. Continuity of the mixed partials fails at the origin, and the conclusion fails too. The theorem is precisely: existence + continuity → equality. The continuity condition is not a technicality; it is load-bearing."

- question: "Why does the continuity hypothesis in Clairaut's theorem matter — what goes wrong if it fails?"
  type: short-answer
  answer: "Without continuity of the mixed partials, the two differentiation orders can produce different results. The standard counterexample is f(x,y) = xy(x²−y²)/(x²+y²) at the origin, where careful computation gives ∂²f/∂x∂y|(0,0) = 1 and ∂²f/∂y∂x|(0,0) = −1. Both mixed partials exist, but they disagree because the function is not smooth enough at that point. Continuity ensures that the limiting processes involved in the two differentiation orders converge to the same value."
  explanation: "This example shows the theorem is not vacuous — it is not just saying 'well-behaved functions behave well.' The specific condition (continuity of mixed partials) is exactly the right hypothesis: it can fail for pathological functions, and when it does, the conclusion fails too. For functions encountered in most applied work, continuity is automatic, but knowing the theorem's hypothesis is important for understanding when commutativity of differentiation can be assumed."
```

## Explainer

From your study of higher-order partial derivatives, you know that after taking a partial derivative of a multivariable function, the result is another function that you can differentiate again. The **mixed partial derivatives** ∂²f/∂x∂y and ∂²f/∂y∂x both measure how the function curves in both the x and y directions — but they arrive there by a different route. The first differentiates with respect to y first, then x; the second reverses the order. A natural question is whether the route matters.

**Clairaut's theorem** (also called Schwarz's theorem) says: if both mixed partials exist and are continuous at a point, they are equal there. For the smooth functions that appear in calculus courses — polynomials, exponentials, sines, cosines, and their combinations — continuity of the mixed partials is automatic, so the order of differentiation is irrelevant in practice. As a heuristic: if f is built from standard elementary functions and has no special piecewise behavior, assume the mixed partials commute.

To see why continuity matters, consider the classic counterexample: f(x, y) = xy(x² − y²)/(x² + y²) for (x, y) ≠ (0, 0) and f(0, 0) = 0. Careful computation shows ∂²f/∂x∂y|(0,0) = 1 while ∂²f/∂y∂x|(0,0) = −1. The mixed partials exist but are not equal because the continuity hypothesis fails at the origin. This example shows the theorem is not vacuous — the continuity condition is doing real work.

In practice, Clairaut's theorem means you can choose whichever order of differentiation is algebraically easier. When computing the **Hessian matrix** (the matrix of all second-order partial derivatives), the off-diagonal entries are mixed partials: H_ij = ∂²f/∂xᵢ∂xⱼ. Clairaut's theorem guarantees H is symmetric for smooth functions, which is a crucial structural fact — symmetric matrices have real eigenvalues, and the signs of those eigenvalues determine whether a critical point is a local min, local max, or saddle point. So this seemingly small commutativity result underpins the second derivative test in multiple dimensions.
