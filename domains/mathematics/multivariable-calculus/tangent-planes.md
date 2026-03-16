---
id: tangent-planes
title: Tangent Planes and Linear Approximation
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: linear-approximation
  type: hard
- id: gradient-vector
  type: soft
builds-toward:
- chain-rule-multivariable
tags:
- tangent-plane
- linearization
- differentiability
- approximation
stage: formal-systems
status: validated
---

# Tangent Planes and Linear Approximation

## Core Idea
The tangent plane to z = f(x, y) at the point (a, b, f(a,b)) has equation z = f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b). This is the multivariable analogue of the tangent line: it best approximates the surface near the point. The linear approximation L(x,y) = f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b) is the linearization of f at (a,b). A function is differentiable at (a,b) if this linear approximation is a good approximation (the error vanishes faster than the distance to (a,b)).

## How It's Best Learned
Connect to single-variable linearization: L(x) = f(a) + f′(a)(x−a) becomes L(x,y) = f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b). Have students compute the tangent plane for a simple surface like z = x² + y² and verify visually that it is flat (horizontal) at the minimum.

## Common Misconceptions
- Existence of both partial derivatives at a point does not guarantee differentiability (the tangent plane exists only when f is 'smooth enough').
- The tangent plane equation requires evaluated (numerical) partial derivatives at the specific point, not general formulas.
- For a level surface F(x,y,z) = c, the tangent plane normal is ∇F, which is a different setup than z = f(x,y).

## Explainer

In single-variable calculus, the **tangent line** to y = f(x) at the point (a, f(a)) was your best linear approximation: L(x) = f(a) + f′(a)(x − a). It matched the function's value and slope at x = a, and it was a good local approximation nearby. The **tangent plane** to z = f(x, y) is the exact multivariable analogue — now the surface has slopes in two independent directions, and the tangent plane must match both.

The formula z = f(a, b) + f_x(a, b)(x − a) + f_y(a, b)(y − b) encodes this: the partial derivative f_x is the slope of the surface in the x-direction, and f_y is the slope in the y-direction. Together, these two numbers uniquely determine a plane through the point (a, b, f(a, b)). Just as the tangent line was the unique line through (a, f(a)) with slope f′(a), the tangent plane is the unique plane through (a, b, f(a, b)) with the correct x-slope and y-slope. No other plane is as "flat" against the surface at that point.

The **linear approximation** L(x, y) uses this plane to estimate f(x, y) for points (x, y) near (a, b). Instead of computing f(1.01, 1.99) exactly, if you know f(1, 2), f_x(1, 2), and f_y(1, 2), you can evaluate L(1.01, 1.99) = f(1, 2) + f_x(1, 2)(0.01) + f_y(1, 2)(−0.01). The accuracy of this approximation is governed by **differentiability**: f is differentiable at (a, b) if and only if the error |f(x, y) − L(x, y)| goes to zero faster than the distance ‖(x, y) − (a, b)‖ as (x, y) → (a, b). This is a stronger condition than just having both partial derivatives — it rules out surfaces with creases or corners.

For **implicit surfaces** defined by F(x, y, z) = c (rather than z = f(x, y)), the tangent plane takes a cleaner form. The gradient ∇F(a, b, c) is perpendicular to the level surface at P = (a, b, c), so the tangent plane is {(x, y, z) : ∇F(a, b, c) · ⟨x − a, y − b, z − c⟩ = 0}. For example, on the unit sphere F(x, y, z) = x² + y² + z² = 1 at the point (1, 0, 0), we get ∇F = ⟨2, 0, 0⟩, so the tangent plane is 2(x − 1) = 0, i.e., x = 1 — the vertical plane touching the sphere at its rightmost point. This implicit approach handles surfaces that cannot be globally written as z = f(x, y).
