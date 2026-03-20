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
stage: advanced
status: draft
---

# Differentiability in Multiple Variables

## Core Idea
A function f(x, y) is differentiable at (a, b) if it is well-approximated by its tangent plane, with error going to zero faster than distance. Differentiability implies continuity but not vice versa.

## Explainer

In single-variable calculus, a function f is differentiable at a if f(a + h) ≈ f(a) + f'(a)h, with the error term going to zero faster than h. The derivative f'(a) is the slope of the unique straight line that best approximates f near a. **Differentiability in multiple variables** extends this idea to higher dimensions, replacing the tangent line with a **tangent plane**. A function f(x, y) is differentiable at (a, b) if there exists a linear function L(x, y) = f(a, b) + A(x − a) + B(y − b) such that the error |f(x, y) − L(x, y)| goes to zero faster than the distance √((x−a)² + (y−b)²) as (x, y) → (a, b). The coefficients A and B, when they exist, turn out to equal the partial derivatives fₓ(a, b) and f_y(a, b).

The subtlety — and the most important insight of this topic — is that having partial derivatives exist at a point is **not sufficient** for differentiability. Partial derivatives only probe f along axis-aligned directions. A function can have well-defined partial derivatives at (a, b) and yet fail to be approximated by any linear function when you approach from an arbitrary direction. The classic example is f(x, y) = xy/(x² + y²) for (x, y) ≠ (0, 0) and f(0, 0) = 0. Both fₓ(0, 0) and f_y(0, 0) equal 0, suggesting the tangent plane would be z = 0. But along the line y = x, the function equals 1/2 everywhere, so it doesn't approach 0 as required. The function is not differentiable at the origin even though its partial derivatives exist there.

Differentiability is the correct multivariable analog of smoothness because it guarantees the existence and consistency of **directional derivatives** in all directions simultaneously, not just along the axes. If f is differentiable at (a, b), then the directional derivative in any unit direction u = ⟨u₁, u₂⟩ exists and equals the dot product ∇f(a, b) · u, where ∇f is the gradient vector ⟨fₓ, f_y⟩. This unified formula for all directional derivatives is what the tangent plane approximation buys you.

A sufficient (though not necessary) condition for differentiability is that the partial derivatives fₓ and f_y **exist and are continuous** in a neighborhood of (a, b). This is the condition you will most often verify in practice. It implies that f is differentiable, which in turn implies f is continuous at (a, b). The chain of implications is: continuous partials ⟹ differentiable ⟹ continuous. None of the arrows reverses. Understanding where each implication can fail is what separates a precise understanding of multivariable smoothness from the naive assumption that "having partial derivatives" is the right definition.
