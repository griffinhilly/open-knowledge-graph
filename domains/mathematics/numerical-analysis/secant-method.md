---
id: secant-method
title: Secant Method
domain: mathematics
course: numerical-analysis
prerequisites:
- id: newton-method-convergence
  type: hard
builds-toward:
- order-of-convergence
tags:
- secant-method
- root-finding
- finite-difference
stage: formal-systems
status: draft
---

# Secant Method

## Core Idea
The secant method approximates Newton's method by replacing f'(x_n) with a finite difference: x_{n+1} = x_n - f(x_n)[x_n - x_{n-1}]/[f(x_n) - f(x_{n-1})]. It avoids computing derivatives, requiring only function values at two initial points. The secant method converges superlinearly (faster than linear, slower than quadratic) with order ≈ 1.618.

## Explainer

Newton's method is powerful but has a cost: it requires evaluating both f(x) and f'(x) at every step. The **secant method** eliminates the derivative by approximating f'(xₙ) with a **finite difference** — the slope of the line connecting the two most recent iterates. Instead of the tangent line at xₙ, you draw a line through (xₙ₋₁, f(xₙ₋₁)) and (xₙ, f(xₙ)) — the secant line — and find where it crosses zero. This gives x_{n+1} = xₙ − f(xₙ) · (xₙ − xₙ₋₁) / (f(xₙ) − f(xₙ₋₁)).

A key structural difference from Newton's method is that the secant method requires **two starting points** x₀ and x₁, not one, because the finite difference needs two function evaluations to approximate the slope. At each step, you carry the two most recent iterates, discard the oldest, and compute the next. Each step costs one new function evaluation (the other point is already known), compared to Newton's one function evaluation plus one derivative evaluation. When derivatives are expensive to compute — or unavailable, as when f comes from a black-box simulation — this trade is attractive.

The **convergence order** of the secant method is approximately φ = (1 + √5)/2 ≈ 1.618, the golden ratio. This sits between linear convergence (order 1, like bisection) and Newton's quadratic convergence (order 2). The golden ratio emerges from the error recurrence: letting eₙ = xₙ − r be the error at step n, the secant method satisfies |e_{n+1}| ≈ C|eₙ||eₙ₋₁| for some constant C near the root. To find the order α such that |eₙ| ~ C'|eₙ₋₁|^α, substitute |eₙ| ~ |eₙ₋₁|^α into the recurrence: |eₙ₋₁|^α ≈ C|eₙ₋₁|^α · |eₙ₋₁| requires α = 1 + 1/α, giving α² = α + 1 — the defining equation of the golden ratio.

When should you choose the secant method over Newton's? Use the secant method when (1) computing f'(x) is significantly more expensive than computing f(x), (2) a closed-form derivative is unavailable, or (3) f is given only numerically. The trade-off is clear in terms of work per accuracy: Newton reaches 16-digit precision in roughly 5 iterations from a good start (quadratic convergence doubles the digits each step), while the secant method may need 7–8 iterations for the same accuracy. But if each derivative evaluation costs more than one function evaluation, the secant method's total computational cost can be lower. For functions where f and f' cost equally, Newton's is usually faster in practice.
