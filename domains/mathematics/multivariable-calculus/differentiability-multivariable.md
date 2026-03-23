---
id: differentiability-multivariable
title: Differentiability in Multiple Variables
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: continuity-multivariable
  type: hard
- id: partial-derivatives-basics
  type: hard
builds-toward:
- chain-rule-multivariable
- tangent-planes
tags:
- differentiability
- smoothness
stage: formal-systems
status: validated
---

# Differentiability in Multiple Variables

## Core Idea
A function f(x, y) is differentiable at (a, b) if it is well-approximated by its tangent plane, with error going to zero faster than distance. Differentiability implies continuity but not vice versa.

## Questions

```yaml
- question: "Consider f(x,y) = xy/(x²+y²) for (x,y) ≠ (0,0) and f(0,0) = 0. Both partial derivatives fₓ(0,0) and f_y(0,0) equal 0. Is f differentiable at the origin?"
  type: multiple-choice
  options:
    - "Yes, because both partial derivatives exist at the origin"
    - "Yes, because fₓ = f_y = 0 confirms a horizontal tangent plane z = 0"
    - "No, because the partial derivatives don't exist at the origin"
    - "No, because the limit of f(x,y) as (x,y)→(0,0) depends on the direction of approach — along y = x the function equals 1/2, not 0"
  answer: 3
  explanation: "The existence of partial derivatives is necessary but not sufficient for differentiability. Partial derivatives only probe the function along axis-aligned directions (the x- and y-axes). For differentiability, the tangent plane approximation must work in *all* directions simultaneously. Along y = x, f(x,x) = x²/2x² = 1/2 for all x ≠ 0, so f does not approach 0 as required for the tangent plane z = 0 to be a valid approximation. Options A and B represent the classic misconception that 'existing partial derivatives = differentiable.'"

- question: "Which chain of implications correctly describes the relationship between continuity, differentiability, and continuous partial derivatives for multivariable functions?"
  type: multiple-choice
  options:
    - "Continuous ⟹ differentiable ⟹ continuous partial derivatives"
    - "Continuous partial derivatives ⟹ differentiable ⟹ continuous"
    - "Differentiable ⟹ continuous partial derivatives ⟹ continuous"
    - "Continuous ⟹ continuous partial derivatives ⟹ differentiable"
  answer: 1
  explanation: "The correct chain is: continuous partial derivatives ⟹ differentiable ⟹ continuous. None of the arrows reverses. Continuous partials are a sufficient (not necessary) condition for differentiability. Differentiability implies continuity but not vice versa. Options A and D both incorrectly place continuity at the start — mere continuity implies nothing about derivatives in the multivariable setting."

- question: "A function f(x,y) that is differentiable at (a,b) must be continuous at (a,b)."
  type: true-false
  answer: true
  explanation: "Differentiability implies continuity in both single-variable and multivariable calculus. If the tangent plane approximation L(x,y) is valid (error going to zero faster than distance), then as (x,y)→(a,b), f(x,y) must approach L(a,b) = f(a,b), which is exactly the definition of continuity. This implication holds; the reverse does not — a function can be continuous at a point yet not differentiable there."

- question: "If both partial derivatives fₓ(a,b) and f_y(a,b) exist, then f is differentiable at (a,b)."
  type: true-false
  answer: false
  explanation: "This is the central misconception of multivariable differentiability. Partial derivatives only measure rates of change along the coordinate axes — they say nothing about behavior in other directions. The classic counterexample is f(x,y) = xy/(x²+y²) at the origin: both partials exist and equal 0, yet the function is not differentiable there because its behavior along diagonal directions contradicts the tangent plane. The correct sufficient condition requires that the partial derivatives *exist and are continuous* in a neighborhood of (a,b)."

- question: "Why is the existence of partial derivatives at a point insufficient to guarantee differentiability? What additional condition is sufficient?"
  type: short-answer
  answer: "Partial derivatives only measure the function's rate of change along axis-aligned directions (parallel to the x- or y-axis). Differentiability requires that the tangent plane approximation be valid for *all* directions of approach — not just the coordinate directions. A function can have well-defined partial derivatives yet behave pathologically along diagonal or other directions. A sufficient condition is that the partial derivatives exist *and are continuous* in a neighborhood of the point; this guarantees that the function is approximable by its tangent plane from all directions simultaneously."
  explanation: "The key distinction is between 'probing along two special directions' (what partial derivatives do) and 'being approximable by a linear function in every direction' (what differentiability requires). This is precisely why directional derivatives in non-axis directions are not automatically determined by the partial derivatives unless differentiability holds — and why differentiability is the correct generalization of smoothness to multiple variables."
```

## Explainer

In single-variable calculus, a function f is differentiable at a if f(a + h) ≈ f(a) + f'(a)h, with the error term going to zero faster than h. The derivative f'(a) is the slope of the unique straight line that best approximates f near a. **Differentiability in multiple variables** extends this idea to higher dimensions, replacing the tangent line with a **tangent plane**. A function f(x, y) is differentiable at (a, b) if there exists a linear function L(x, y) = f(a, b) + A(x − a) + B(y − b) such that the error |f(x, y) − L(x, y)| goes to zero faster than the distance √((x−a)² + (y−b)²) as (x, y) → (a, b). The coefficients A and B, when they exist, turn out to equal the partial derivatives fₓ(a, b) and f_y(a, b).

The subtlety — and the most important insight of this topic — is that having partial derivatives exist at a point is **not sufficient** for differentiability. Partial derivatives only probe f along axis-aligned directions. A function can have well-defined partial derivatives at (a, b) and yet fail to be approximated by any linear function when you approach from an arbitrary direction. The classic example is f(x, y) = xy/(x² + y²) for (x, y) ≠ (0, 0) and f(0, 0) = 0. Both fₓ(0, 0) and f_y(0, 0) equal 0, suggesting the tangent plane would be z = 0. But along the line y = x, the function equals 1/2 everywhere, so it doesn't approach 0 as required. The function is not differentiable at the origin even though its partial derivatives exist there.

Differentiability is the correct multivariable analog of smoothness because it guarantees the existence and consistency of **directional derivatives** in all directions simultaneously, not just along the axes. If f is differentiable at (a, b), then the directional derivative in any unit direction u = ⟨u₁, u₂⟩ exists and equals the dot product ∇f(a, b) · u, where ∇f is the gradient vector ⟨fₓ, f_y⟩. This unified formula for all directional derivatives is what the tangent plane approximation buys you.

A sufficient (though not necessary) condition for differentiability is that the partial derivatives fₓ and f_y **exist and are continuous** in a neighborhood of (a, b). This is the condition you will most often verify in practice. It implies that f is differentiable, which in turn implies f is continuous at (a, b). The chain of implications is: continuous partials ⟹ differentiable ⟹ continuous. None of the arrows reverses. Understanding where each implication can fail is what separates a precise understanding of multivariable smoothness from the naive assumption that "having partial derivatives" is the right definition.
