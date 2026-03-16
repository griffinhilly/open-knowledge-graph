---
id: total-differential-approximation
title: Total Differential and Linear Approximation
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector-definition
  type: hard
builds-toward:
- tangent-planes
tags:
- differential
- approximation
- linear
stage: formal-systems
status: draft
---

# Total Differential and Linear Approximation

## Core Idea
The total differential df = (∂f/∂x)dx + (∂f/∂y)dy approximates the change in f when x and y change by small amounts dx and dy. For small changes, f(a+dx, b+dy) ≈ f(a, b) + df provides a linear approximation.

## Explainer

From single-variable calculus, you know that near a point a, a differentiable function satisfies f(a + h) ≈ f(a) + f′(a)·h. The derivative f′(a) is the slope of the tangent line, and f′(a)·h is the linear change predicted by that tangent. The **total differential** extends this idea to functions of several variables: if x changes by a small amount dx and y changes by dy, the predicted change in f is df = (∂f/∂x)dx + (∂f/∂y)dy. This is a weighted sum of the input changes, where the weights are the partial derivatives — the local sensitivity of f to each variable.

The geometric picture is the **tangent plane**. A surface z = f(x,y) is approximated near (a, b, f(a,b)) by the plane z = f(a,b) + (∂f/∂x)(x−a) + (∂f/∂y)(y−b). The total differential df computes the vertical displacement along this tangent plane when you step from (a, b) to (a + dx, b + dy). Just as the tangent line is the best linear approximation to a curve, the tangent plane is the best linear approximation to a surface, and the total differential is exactly the machinery for reading off that approximation.

The connection to the **gradient vector** (your prerequisite) is direct. The gradient ∇f = (∂f/∂x, ∂f/∂y) collects the partial derivatives, and the total differential can be written compactly as df = ∇f · (dx, dy) — the dot product of the gradient with the displacement vector. This reveals the total differential as a special case of the directional derivative: it measures the change in f due to a displacement (dx, dy), and the gradient is the linear functional that performs this measurement. The tangent plane, the total differential, and the gradient are all the same linear object viewed from different angles.

In practice, the total differential gives a quick and useful **error estimate**. If f(x, y) = x²y and you measure x ≈ 3, y ≈ 2 with small measurement errors dx and dy, then the resulting error in f is approximately df = 2xy·dx + x²·dy = 12dx + 9dy. This linearization principle appears throughout applied mathematics — error propagation in physics, sensitivity analysis in engineering, and Newton's method for solving systems of equations. It is also the foundation for the multivariable chain rule, implicit differentiation in higher dimensions, and the inverse function theorem, all of which formalize the idea of tracking how small input changes propagate into output changes.
