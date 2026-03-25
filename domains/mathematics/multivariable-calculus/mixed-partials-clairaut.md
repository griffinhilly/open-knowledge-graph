---
id: mixed-partials-clairaut
title: Mixed Partial Derivatives and Clairaut's Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: higher-order-partial-derivatives
  type: hard
- id: clairaut-theorem
  type: soft
builds-toward:
- critical-points-multivariable
- second-partials-test
tags:
- partials
- symmetry
stage: formal-systems
status: validated
---
# Mixed Partial Derivatives and Clairaut's Theorem

## Core Idea
Mixed partial derivatives are equal when they are continuous: ∂²f/∂x∂y = ∂²f/∂y∂x, by Clairaut's theorem. This equality simplifies computation and reflects symmetry in the function's behavior.

## Questions

```yaml
- question: "A student claims: 'To compute ∂²f/∂x∂y, I must differentiate first with respect to x, then y — the notation shows the order.' For f(x,y) = x²y + e^(xy), what is actually correct?"
  type: multiple-choice
  options:
    - "The student is right — ∂²f/∂x∂y means differentiate with respect to x first, then y"
    - "The notation ∂²f/∂x∂y means differentiate with respect to y first (rightmost denominator variable), then x — but by Clairaut's theorem the result equals ∂²f/∂y∂x for smooth functions"
    - "The order is arbitrary and neither convention is standard"
    - "Clairaut's theorem only applies to polynomials, not to functions involving exponentials"
  answer: 1
  explanation: "In denominator notation, you differentiate right-to-left: ∂²f/∂x∂y means first ∂/∂y, then ∂/∂x. The student has the order backwards. The deeper point is Clairaut's theorem: since f(x,y) = x²y + e^(xy) is smooth (continuous mixed partials everywhere), the order doesn't matter — ∂²f/∂x∂y = ∂²f/∂y∂x. Differentiate in whichever order is computationally easier."

- question: "Under what condition does Clairaut's theorem guarantee that ∂²f/∂x∂y = ∂²f/∂y∂x at a point?"
  type: multiple-choice
  options:
    - "Whenever f is defined and differentiable at the point"
    - "Whenever both mixed partial derivatives exist and are continuous at the point"
    - "Only when f is a polynomial or trigonometric function"
    - "Whenever f has no critical points in a neighborhood of the point"
  answer: 1
  explanation: "Clairaut's theorem (also called Schwarz's theorem) requires continuity of both mixed partials at the point, not merely their existence. Differentiability alone is insufficient — there exist differentiable functions whose mixed partials exist at a point but are discontinuous there, and for these the mixed partials can differ. The continuity condition is sufficient (not necessary), so any smooth function you encounter in practice will satisfy it."

- question: "For any differentiable function f(x, y), the mixed partial derivatives ∂²f/∂x∂y and ∂²f/∂y∂x are always equal."
  type: true-false
  answer: false
  explanation: "Differentiability alone is not sufficient. Clairaut's theorem requires the mixed partials themselves to be continuous. A canonical counterexample: f(x,y) = xy(x²−y²)/(x²+y²) for (x,y) ≠ (0,0) and f(0,0) = 0, where ∂²f/∂x∂y at the origin equals 1 but ∂²f/∂y∂x at the origin equals −1. The function is differentiable but its mixed partials are discontinuous at the origin."

- question: "Clairaut's theorem implies that the Hessian matrix of a smooth function f(x₁, ..., xₙ) is always a symmetric matrix."
  type: true-false
  answer: true
  explanation: "The Hessian H(f) has entry (i,j) equal to ∂²f/∂xᵢ∂xⱼ. By Clairaut's theorem, ∂²f/∂xᵢ∂xⱼ = ∂²f/∂xⱼ∂xᵢ whenever the mixed partials are continuous, meaning H(i,j) = H(j,i) — the definition of a symmetric matrix. This symmetry gives the Hessian real eigenvalues and an orthogonal eigenbasis, which is what makes the second-partials test for classifying critical points work."

- question: "Why does Clairaut's theorem matter practically? What would change about computing second derivatives if the theorem were false for smooth functions?"
  type: short-answer
  answer: "Clairaut's theorem allows you to differentiate in whichever order is computationally convenient, knowing the result is the same. Without it, every mixed partial would need to be computed in both orders to confirm the result — doubling the work. More critically, the Hessian would not be symmetric, losing its real eigenvalues and making the second-partials test for critical points inapplicable."
  explanation: "The practical importance extends further: Lagrangian mechanics, optimization theory, and differential geometry all rely on commutativity of partial derivatives. Clairaut's theorem is one of those background guarantees so ubiquitous that its absence would make modern analysis deeply complicated."
```

## Explainer

You already know how to compute higher-order partial derivatives: differentiate once with respect to one variable, then differentiate the result with respect to another. A **mixed partial derivative** ∂²f/∂x∂y means: first differentiate with respect to y (the rightmost variable in denominator notation), then differentiate with respect to x. The question is: does the order matter? Could ∂²f/∂x∂y differ from ∂²f/∂y∂x?

In general, for badly-behaved functions, the answer is yes — the mixed partials can differ. But for almost every function you encounter in practice, they are equal, and **Clairaut's theorem** (also called the symmetry of second derivatives or Schwarz's theorem) makes this precise: if both mixed partials ∂²f/∂x∂y and ∂²f/∂y∂x are continuous at a point, then they are equal at that point. Continuity of the mixed partials is the key condition — it is sufficient, though not necessary.

The intuition is that if f is smooth, then at the infinitesimal level, "how the x-slope changes in the y-direction" and "how the y-slope changes in the x-direction" both measure the same feature of the function's curvature. Think of a surface z = f(x, y): ∂²f/∂y∂x asks how the tilt in the x-direction changes as you move in the y-direction, while ∂²f/∂x∂y asks how the tilt in the y-direction changes as you move in the x-direction. For a smooth surface, both measure the same "twisting" of the surface, so they must agree.

The practical consequence is significant: for smooth functions, you can differentiate in whichever order is computationally convenient. This matters when computing the **Hessian matrix** H(f), whose (i, j) entry is ∂²f/∂xᵢ∂xⱼ. Clairaut's theorem guarantees that H is a **symmetric matrix** (H = Hᵀ) whenever the second partials are continuous — which gives the Hessian all the nice spectral properties of symmetric matrices, including real eigenvalues. This symmetry is directly used in the second partials test for classifying critical points as local maxima, minima, or saddle points, which is the next topic in your path.
