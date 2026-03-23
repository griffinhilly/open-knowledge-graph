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
status: validated
---

# Secant Method

## Core Idea
The secant method approximates Newton's method by replacing f'(x_n) with a finite difference: x_{n+1} = x_n - f(x_n)[x_n - x_{n-1}]/[f(x_n) - f(x_{n-1})]. It avoids computing derivatives, requiring only function values at two initial points. The secant method converges superlinearly (faster than linear, slower than quadratic) with order ≈ 1.618.

## Questions

```yaml
- question: "Why does the secant method require two initial points rather than one, unlike Newton's method?"
  type: multiple-choice
  options:
    - "Because the secant method applies only to polynomials, which need two roots specified to initialize"
    - "Because it approximates the derivative using a finite difference slope between two known function values, requiring two previous points at every step"
    - "Because it checks convergence by comparing consecutive iterates, and convergence checking needs two points"
    - "Because two starting points allow the method to bracket the root, guaranteeing convergence"
  answer: 1
  explanation: "Newton's method uses the tangent line at xₙ, requiring only f(xₙ) and f'(xₙ). The secant method replaces f'(xₙ) with the finite difference [f(xₙ) − f(xₙ₋₁)] / [xₙ − xₙ₋₁]. This approximation of the slope requires two points on the curve. At startup, there is no previous iterate, so you must supply two starting points x₀ and x₁. Option D is wrong: unlike bisection, the secant method does not maintain a bracket and does not guarantee convergence."

- question: "A function f(x) has an expensive-to-compute but analytically available derivative. Which root-finding method is most appropriate, and why?"
  type: multiple-choice
  options:
    - "Secant method — because it always uses fewer function evaluations regardless of derivative cost"
    - "Bisection — because its guaranteed convergence outweighs any speed advantage"
    - "Newton's method — the cheap derivative makes quadratic convergence dominant, minimizing total steps to full precision"
    - "Secant method — because avoiding the derivative is always safer than using it"
  answer: 2
  explanation: "The secant method's advantage is specifically when computing f' is expensive relative to f. If the derivative is cheap, Newton's method is superior: its quadratic convergence (order 2) doubles the digits of accuracy per step, reaching 16-digit precision in roughly 5 iterations from a good start. The secant method would need 7–8 iterations for the same accuracy. When f and f' cost equally, Newton's wins on total computational work. Only when f' significantly exceeds f in cost does the secant method's per-step saving compensate for its lower convergence order."

- question: "The secant method converges faster than the bisection method, though it does not guarantee convergence from arbitrary starting points."
  type: true-false
  answer: true
  explanation: "The secant method has superlinear convergence with order φ ≈ 1.618 (the golden ratio), while bisection has linear convergence (order 1) — adding only about one bit of precision per step. The secant method is much faster when it converges. However, unlike bisection, the secant method does not maintain a bracket around the root and can diverge if starting points are poorly chosen or if the function has pathological behavior near the root."

- question: "The secant method's convergence order is exactly 2, the same as Newton's method, because the finite difference approximation becomes exact near the root."
  type: true-false
  answer: false
  explanation: "The secant method's convergence order is φ = (1+√5)/2 ≈ 1.618, not 2. The golden ratio arises from the two-point error recurrence |eₙ₊₁| ≈ C|eₙ||eₙ₋₁|, which leads to the equation α² = α + 1 when you assume order α. Newton's quadratic convergence (order 2) comes from a one-point recurrence |eₙ₊₁| ≈ C|eₙ|², which is possible only because it uses the exact derivative. The finite difference is never exact — even near the root, it introduces an approximation error that costs convergence order."

- question: "Explain why the secant method's convergence order is the golden ratio φ ≈ 1.618 rather than a simpler value like 1.5 or 2.0."
  type: short-answer
  answer: "The golden ratio emerges from the error recurrence. Near the root, |eₙ₊₁| ≈ C|eₙ||eₙ₋₁| for some constant C. To find the order α such that |eₙ| ~ |eₙ₋₁|^α, substitute |eₙ| ≈ |eₙ₋₁|^α into the recurrence: |eₙ₋₁|^α ≈ C|eₙ₋₁|^α · |eₙ₋₁|, which gives α = 1 + 1/α, or equivalently α² − α − 1 = 0. The positive solution is (1+√5)/2 = φ. The golden ratio is not arbitrary — it is the fixed point of this two-step recurrence."
  explanation: "The golden ratio appears because the secant method couples two consecutive errors (it uses the two most recent iterates), while Newton's method couples only one. The recurrence α = 1 + 1/α defines the golden ratio uniquely among positive reals, making φ the natural and exact convergence order for this two-point structure. Any method using only one previous iterate in its error recurrence will generically have order 2 (Newton's) or order 1 (simple iterations)."
```

## Explainer

Newton's method is powerful but has a cost: it requires evaluating both f(x) and f'(x) at every step. The **secant method** eliminates the derivative by approximating f'(xₙ) with a **finite difference** — the slope of the line connecting the two most recent iterates. Instead of the tangent line at xₙ, you draw a line through (xₙ₋₁, f(xₙ₋₁)) and (xₙ, f(xₙ)) — the secant line — and find where it crosses zero. This gives x_{n+1} = xₙ − f(xₙ) · (xₙ − xₙ₋₁) / (f(xₙ) − f(xₙ₋₁)).

A key structural difference from Newton's method is that the secant method requires **two starting points** x₀ and x₁, not one, because the finite difference needs two function evaluations to approximate the slope. At each step, you carry the two most recent iterates, discard the oldest, and compute the next. Each step costs one new function evaluation (the other point is already known), compared to Newton's one function evaluation plus one derivative evaluation. When derivatives are expensive to compute — or unavailable, as when f comes from a black-box simulation — this trade is attractive.

The **convergence order** of the secant method is approximately φ = (1 + √5)/2 ≈ 1.618, the golden ratio. This sits between linear convergence (order 1, like bisection) and Newton's quadratic convergence (order 2). The golden ratio emerges from the error recurrence: letting eₙ = xₙ − r be the error at step n, the secant method satisfies |e_{n+1}| ≈ C|eₙ||eₙ₋₁| for some constant C near the root. To find the order α such that |eₙ| ~ C'|eₙ₋₁|^α, substitute |eₙ| ~ |eₙ₋₁|^α into the recurrence: |eₙ₋₁|^α ≈ C|eₙ₋₁|^α · |eₙ₋₁| requires α = 1 + 1/α, giving α² = α + 1 — the defining equation of the golden ratio.

When should you choose the secant method over Newton's? Use the secant method when (1) computing f'(x) is significantly more expensive than computing f(x), (2) a closed-form derivative is unavailable, or (3) f is given only numerically. The trade-off is clear in terms of work per accuracy: Newton reaches 16-digit precision in roughly 5 iterations from a good start (quadratic convergence doubles the digits each step), while the secant method may need 7–8 iterations for the same accuracy. But if each derivative evaluation costs more than one function evaluation, the secant method's total computational cost can be lower. For functions where f and f' cost equally, Newton's is usually faster in practice.
