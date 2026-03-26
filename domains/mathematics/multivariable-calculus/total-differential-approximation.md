---
id: total-differential-approximation
title: Total Differential and Linear Approximation
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector
  type: hard
builds-toward:
- tangent-planes
tags:
- differential
- approximation
- linear
stage: formal-systems
status: validated
---

# Total Differential and Linear Approximation

## Core Idea
The total differential df = (∂f/∂x)dx + (∂f/∂y)dy approximates the change in f when x and y change by small amounts dx and dy. For small changes, f(a+dx, b+dy) ≈ f(a, b) + df provides a linear approximation.

## Questions

```yaml
- question: "You are estimating the volume V = πr²h of a cylinder with r = 3 cm and h = 10 cm, with measurement errors dr = 0.1 cm and dh = 0.2 cm. What is the approximate error in V using the total differential?"
  type: multiple-choice
  options:
    - "π(0.1)(0.2) ≈ 0.063 cm³ — multiply the errors together"
    - "π(0.1 + 0.2) ≈ 0.94 cm³ — add the errors"
    - "2πrh · dr + πr² · dh = 2π(3)(10)(0.1) + π(9)(0.2) = 6π + 1.8π = 7.8π ≈ 24.5 cm³"
    - "π(dr)²(dh) — use second-order terms since the errors are small"
  answer: 2
  explanation: "The total differential gives dV = (∂V/∂r)dr + (∂V/∂h)dh = 2πrh·dr + πr²·dh. At r = 3, h = 10: dV = 2π(3)(10)(0.1) + π(9)(0.2) = 6π + 1.8π = 7.8π ≈ 24.5 cm³. The partial derivatives act as sensitivity coefficients — r appears squared in V, so errors in r are amplified by 2πh = 62.8, while errors in h are amplified by πr² = 28.3. Options A and D multiply errors together, which gives second-order terms — negligible compared to the first-order differential."

- question: "The total differential df = (∂f/∂x)dx + (∂f/∂y)dy represents:"
  type: multiple-choice
  options:
    - "The exact change in f when x changes by dx and y changes by dy"
    - "The area enclosed by the tangent plane to the surface z = f(x, y)"
    - "The linear (first-order) approximation to the change in f — exact on the tangent plane and increasingly accurate as dx and dy approach zero"
    - "The second-derivative correction that improves upon the tangent line approximation"
  answer: 2
  explanation: "The total differential is a linear approximation, not an exact computation. The actual change Δf = f(a+dx, b+dy) − f(a,b) differs from df by second-order terms (proportional to dx², dxdy, dy²). The approximation df ≈ Δf becomes more accurate as the displacement (dx, dy) shrinks. The key insight is that df computes the change predicted by the tangent plane — the best flat (linear) approximation to the surface. Option A is the most tempting wrong answer: confusing the linear approximation with the exact change."

- question: "The total differential df = (∂f/∂x)dx + (∂f/∂y)dy can be written as the dot product ∇f · (dx, dy), revealing it as a special case of the directional derivative."
  type: true-false
  answer: true
  explanation: "The gradient ∇f = (∂f/∂x, ∂f/∂y) and the displacement vector (dx, dy) have dot product (∂f/∂x)dx + (∂f/∂y)dy = df. This connection is geometrically meaningful: it says the total differential measures how much f changes when you step in the direction (dx, dy), with the gradient acting as the linear functional that performs this measurement. The tangent plane, the gradient, and the total differential are all the same first-order approximation viewed from different angles."

- question: "If both partial derivatives ∂f/∂x and ∂f/∂y equal zero at a point, the total differential predicts no change, which means the function is locally constant near that point."
  type: true-false
  answer: false
  explanation: "A zero total differential means the tangent plane is horizontal — the linear approximation predicts no change. But the function itself can still vary via second-order (quadratic) terms. The point could be a local maximum, minimum, or a saddle point — all have zero gradient but non-constant behavior in a neighborhood. The total differential captures only the linear part of the change; it says nothing about what the function does beyond first order. Equating a horizontal tangent plane with local constancy confuses the approximation with the function."

- question: "In what sense is the total differential the 'best linear approximation' to Δf, and how does this connect geometrically to the tangent plane?"
  type: short-answer
  answer: "The total differential df = (∂f/∂x)dx + (∂f/∂y)dy is 'best' in the sense that it is the unique linear function of (dx, dy) that agrees with Δf up to first order: the error Δf − df shrinks faster than |(dx, dy)| as the displacement approaches zero. Geometrically, df computes the vertical displacement along the tangent plane to z = f(x, y) at the base point. The tangent plane z = f(a,b) + (∂f/∂x)(x−a) + (∂f/∂y)(y−b) is the best flat approximation to the surface near (a, b), and df is the amount of height that plane gains for a step of size (dx, dy). The tangent plane, the gradient vector, and the total differential are three descriptions of the same linear object."
  explanation: "This unification is the key insight of multivariable differentiation: the derivative is not a slope but a linear map — the total differential — and the tangent plane is its graph."
```

## Explainer

From single-variable calculus, you know that near a point a, a differentiable function satisfies f(a + h) ≈ f(a) + f′(a)·h. The derivative f′(a) is the slope of the tangent line, and f′(a)·h is the linear change predicted by that tangent. The **total differential** extends this idea to functions of several variables: if x changes by a small amount dx and y changes by dy, the predicted change in f is df = (∂f/∂x)dx + (∂f/∂y)dy. This is a weighted sum of the input changes, where the weights are the partial derivatives — the local sensitivity of f to each variable.

The geometric picture is the **tangent plane**. A surface z = f(x,y) is approximated near (a, b, f(a,b)) by the plane z = f(a,b) + (∂f/∂x)(x−a) + (∂f/∂y)(y−b). The total differential df computes the vertical displacement along this tangent plane when you step from (a, b) to (a + dx, b + dy). Just as the tangent line is the best linear approximation to a curve, the tangent plane is the best linear approximation to a surface, and the total differential is exactly the machinery for reading off that approximation.

The connection to the **gradient vector** (your prerequisite) is direct. The gradient ∇f = (∂f/∂x, ∂f/∂y) collects the partial derivatives, and the total differential can be written compactly as df = ∇f · (dx, dy) — the dot product of the gradient with the displacement vector. This reveals the total differential as a special case of the directional derivative: it measures the change in f due to a displacement (dx, dy), and the gradient is the linear functional that performs this measurement. The tangent plane, the total differential, and the gradient are all the same linear object viewed from different angles.

In practice, the total differential gives a quick and useful **error estimate**. If f(x, y) = x²y and you measure x ≈ 3, y ≈ 2 with small measurement errors dx and dy, then the resulting error in f is approximately df = 2xy·dx + x²·dy = 12dx + 9dy. This linearization principle appears throughout applied mathematics — error propagation in physics, sensitivity analysis in engineering, and Newton's method for solving systems of equations. It is also the foundation for the multivariable chain rule, implicit differentiation in higher dimensions, and the inverse function theorem, all of which formalize the idea of tracking how small input changes propagate into output changes.
