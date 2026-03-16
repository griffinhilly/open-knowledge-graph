---
id: total-differential
title: Total Differential and Linear Approximation
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: differentiability-multivariate
  type: hard
builds-toward:
- tangent-planes-linear-approximation
- chain-rule-multivariable
tags:
- total-differential
- approximation
- exactness
stage: formal-systems
status: draft
---

# Total Differential and Linear Approximation

## Core Idea
The total differential df = (∂f/∂x)dx + (∂f/∂y)dy represents the change in a differentiable function f when x and y change by small amounts dx and dy. It defines the best linear approximation to f near a point.

## Explainer

From single-variable calculus, you know that the derivative f'(a) gives the slope of the tangent line, and the linear approximation f(a + Δx) ≈ f(a) + f'(a)Δx tells you how much f changes when x changes by a small amount Δx. The **total differential** is the precise multivariable generalization. For a function f(x, y), your prerequisite knowledge of partial derivatives gives you ∂f/∂x (rate of change with x fixed y) and ∂f/∂y (rate of change with x fixed). The total differential df = (∂f/∂x)dx + (∂f/∂y)dy combines both into a single expression that accounts for simultaneous changes in both variables.

The key insight is that **dx and dy are independent variables** in the differential — they represent arbitrary (small) changes in x and y, not specific increments. Given a specific displacement (Δx, Δy), the approximation becomes Δf ≈ (∂f/∂x)Δx + (∂f/∂y)Δy. This is the **best linear approximation** to the change in f: it is exact to first order, meaning the error |Δf − df| shrinks faster than the magnitude of the displacement |(Δx, Δy)| as the displacement goes to zero. This is precisely what differentiability means in the multivariate setting — your other prerequisite — and distinguishes it from merely having partial derivatives.

A concrete example: suppose f(x, y) = x²y and you want to estimate f(2.01, 2.98) without computing it exactly. Near (2, 3): ∂f/∂x = 2xy = 12, ∂f/∂y = x² = 4, f(2, 3) = 12. So Δf ≈ 12(0.01) + 4(−0.02) = 0.12 − 0.08 = 0.04, giving f ≈ 12.04. The actual value is (2.01)²(2.98) ≈ 12.04, confirming the approximation. Each partial derivative isolates the contribution of one variable; the total differential sums the contributions linearly.

The total differential extends naturally to more variables: df = (∂f/∂x)dx + (∂f/∂y)dy + (∂f/∂z)dz, and to **exact differentials** — expressions P dx + Q dy that equal the differential of some function f, which requires ∂P/∂y = ∂Q/∂x. This exactness condition connects directly to conservative vector fields and path independence in line integrals. The total differential is also the foundation for the multivariable **chain rule**: if x and y both depend on a parameter t, then df/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt) — literally the total differential divided by dt, with each term recording how f changes through one path of influence.
