---
id: secant-method-root-finding
title: Secant Method
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: soft
builds-toward:
- order-of-convergence
tags:
- secant-method
- root-finding
- derivative-free
stage: advanced
status: draft
---

# Secant Method

## Core Idea
The secant method approximates Newton's method by replacing the derivative with a finite difference quotient: x_{n+1} = x_n - f(x_n)(x_n - x_{n-1})/(f(x_n) - f(x_{n-1})). This avoids derivative computation but requires two initial points and achieves superlinear convergence (order ≈ 1.618), between linear and quadratic convergence.

## Questions

```yaml
- question: "The secant method and Newton's method are both applied to find a root of an expensive-to-evaluate function where computing the derivative costs approximately the same as one function evaluation. Considering total function evaluations, which method converges faster?"
  type: multiple-choice
  options:
    - "Newton's method, because its convergence order (2) exceeds the secant method's (≈1.618)"
    - "The secant method, because it needs only one new evaluation per step while Newton's requires two, making its per-evaluation convergence rate higher"
    - "They are equivalent per function evaluation since their rates average out over many iterations"
    - "Bisection, because its guaranteed convergence makes it more efficient overall"
  answer: 1
  explanation: "Newton's method achieves order-2 convergence but costs 2 evaluations per step (f and f'), giving an effective per-evaluation order of 2^(1/2) ≈ 1.41. The secant method achieves order ≈1.618 per step but reuses the previous function value, costing only 1 new evaluation per step — giving an effective per-evaluation order of ≈1.618. So when derivatives are expensive, the secant method actually wins on a per-evaluation basis, despite having a lower per-iteration order."

- question: "The secant method update formula x_{n+1} = x_n − f(x_n)·(x_n − x_{n-1})/(f(x_n) − f(x_{n-1})) is derived from the x-intercept of which geometric object?"
  type: multiple-choice
  options:
    - "The tangent line to f at the current iterate (x_n, f(x_n))"
    - "The line passing through the two most recent iterates (x_{n-1}, f(x_{n-1})) and (x_n, f(x_n))"
    - "The quadratic polynomial interpolating the three most recent iterates"
    - "The horizontal line at height f(x_n)/2"
  answer: 1
  explanation: "The secant method replaces Newton's tangent line with a secant line through the two most recent iterates. The slope of this line is (f(x_n) − f(x_{n-1}))/(x_n − x_{n-1}), which substitutes for f'(x_n) in Newton's formula. This is the key derivative-free approximation — it uses information already computed rather than requiring analytic or numerical differentiation at each step."

- question: "The convergence order of the secant method is exactly equal to the golden ratio (≈1.618)."
  type: true-false
  answer: true
  explanation: "The convergence order φ = (1+√5)/2 ≈ 1.618 arises from the error recurrence e_{n+1} ≈ C·e_n·e_{n-1}. Assuming |e_n| ~ A^(φ^n), substituting gives the recurrence φ² = φ + 1, whose positive root is the golden ratio. This is a precise mathematical result, not an approximation — and the appearance of the golden ratio here is genuinely surprising, connecting root-finding to classical geometry."

- question: "The secant method can fail catastrophically when f(x_n) and f(x_{n-1}) are nearly equal in value, even if x_n and x_{n-1} are far apart."
  type: true-false
  answer: true
  explanation: "When f(x_n) ≈ f(x_{n-1}), the denominator f(x_n) − f(x_{n-1}) approaches zero, and the next iterate x_{n+1} flies off toward infinity. Geometrically, a nearly horizontal secant line has its x-intercept arbitrarily far from both points. This is the primary failure mode of the secant method: not that the iterates are close together, but that the function is nearly flat between them, creating a near-zero denominator."

- question: "Why does the secant method require two initial points rather than one, and how does this differ from Newton's method?"
  type: short-answer
  answer: "The secant method needs two points (x_0, x_1) because it approximates the derivative using a finite difference — the slope of the secant line — which requires two function values. Newton's method needs only one starting point because it evaluates the derivative analytically at that point. After the first step, the secant method always uses only the two most recent iterates, discarding older history, so memory requirements stay constant."
  explanation: "Newton's single-point requirement is essentially that a tangent line at one point is well-defined without any additional data. The secant method's two-point requirement is the price of avoiding derivative computation. Importantly, the secant method does not accumulate more points as it runs — each new iterate replaces the oldest in a sliding window of size two."
```

## Explainer

Newton's method finds roots by linearizing f at the current guess: draw the tangent line at (xₙ, f(xₙ)) and take its x-intercept as the next guess. This requires evaluating f'(xₙ) at each step. For many real-world functions — defined by numerical simulations, legacy code, or empirical data — computing derivatives is expensive, unreliable, or simply impossible. The secant method solves this by replacing the tangent line with a **secant line** through the two most recent iterates (xₙ₋₁, f(xₙ₋₁)) and (xₙ, f(xₙ)).

The update formula drops out directly from the slope of the secant line. The tangent slope f'(xₙ) in Newton's formula xₙ₊₁ = xₙ − f(xₙ)/f'(xₙ) is replaced by the finite difference (f(xₙ) − f(xₙ₋₁))/(xₙ − xₙ₋₁), giving xₙ₊₁ = xₙ − f(xₙ)·(xₙ − xₙ₋₁)/(f(xₙ) − f(xₙ₋₁)). This requires two starting points x₀ and x₁ instead of one, and each subsequent iteration uses only the most recent pair — so you always need two function evaluations in memory, not the whole history.

The convergence rate of the secant method is **superlinear** with order φ = (1 + √5)/2 ≈ 1.618 — the golden ratio. This is a beautiful and somewhat surprising fact. The order arises because the error sequence satisfies eₙ₊₁ ≈ C·eₙ·eₙ₋₁, and if you assume |eₙ| ≈ |e₀|^(αⁿ) for some growth rate α, the recurrence forces α = φ. To put the rate in perspective: Newton's method has order 2 (the number of correct digits roughly doubles each step), the bisection method has order 1 (you gain one binary digit per step), and the secant method is in between — it roughly multiplies the number of correct digits by φ ≈ 1.618 each iteration. In terms of function evaluations, the secant method actually competes favorably with Newton's method because Newton requires two evaluations per step (f and f'), while the secant method requires only one new evaluation per step (reusing the previous value).

Where the secant method can fail is worth understanding. If f(xₙ) ≈ f(xₙ₋₁) but xₙ ≠ xₙ₋₁, the denominator near-vanishes and the next iterate flies off to infinity — a near-horizontal secant line. This can happen if the two initial points are poorly chosen or if the iteration wanders into a flat region of f. It is also not guaranteed to converge from arbitrary starting points the way bisection is, though in practice it converges quickly once the iterates are near the root. For well-behaved functions with a good initial bracket, the secant method is the workhorse choice when derivatives are unavailable.
