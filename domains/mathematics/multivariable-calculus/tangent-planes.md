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
