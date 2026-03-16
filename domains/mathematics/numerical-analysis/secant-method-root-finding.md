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

## Explainer

Newton's method finds roots by linearizing f at the current guess: draw the tangent line at (xₙ, f(xₙ)) and take its x-intercept as the next guess. This requires evaluating f'(xₙ) at each step. For many real-world functions — defined by numerical simulations, legacy code, or empirical data — computing derivatives is expensive, unreliable, or simply impossible. The secant method solves this by replacing the tangent line with a **secant line** through the two most recent iterates (xₙ₋₁, f(xₙ₋₁)) and (xₙ, f(xₙ)).

The update formula drops out directly from the slope of the secant line. The tangent slope f'(xₙ) in Newton's formula xₙ₊₁ = xₙ − f(xₙ)/f'(xₙ) is replaced by the finite difference (f(xₙ) − f(xₙ₋₁))/(xₙ − xₙ₋₁), giving xₙ₊₁ = xₙ − f(xₙ)·(xₙ − xₙ₋₁)/(f(xₙ) − f(xₙ₋₁)). This requires two starting points x₀ and x₁ instead of one, and each subsequent iteration uses only the most recent pair — so you always need two function evaluations in memory, not the whole history.

The convergence rate of the secant method is **superlinear** with order φ = (1 + √5)/2 ≈ 1.618 — the golden ratio. This is a beautiful and somewhat surprising fact. The order arises because the error sequence satisfies eₙ₊₁ ≈ C·eₙ·eₙ₋₁, and if you assume |eₙ| ≈ |e₀|^(αⁿ) for some growth rate α, the recurrence forces α = φ. To put the rate in perspective: Newton's method has order 2 (the number of correct digits roughly doubles each step), the bisection method has order 1 (you gain one binary digit per step), and the secant method is in between — it roughly multiplies the number of correct digits by φ ≈ 1.618 each iteration. In terms of function evaluations, the secant method actually competes favorably with Newton's method because Newton requires two evaluations per step (f and f'), while the secant method requires only one new evaluation per step (reusing the previous value).

Where the secant method can fail is worth understanding. If f(xₙ) ≈ f(xₙ₋₁) but xₙ ≠ xₙ₋₁, the denominator near-vanishes and the next iterate flies off to infinity — a near-horizontal secant line. This can happen if the two initial points are poorly chosen or if the iteration wanders into a flat region of f. It is also not guaranteed to converge from arbitrary starting points the way bisection is, though in practice it converges quickly once the iterates are near the root. For well-behaved functions with a good initial bracket, the secant method is the workhorse choice when derivatives are unavailable.
