---
id: complex-differentiability
title: Complex Differentiability
domain: mathematics
course: complex-analysis
prerequisites:
- id: limits-continuity-complex-functions
  type: hard
builds-toward:
- holomorphic-functions
- cauchy-riemann-equations
tags:
- differentiability
- derivatives
- holomorphic
stage: advanced
status: draft
---

# Complex Differentiability

## Core Idea
A function f is differentiable at z₀ if the limit f'(z₀) = lim(h→0) [f(z₀+h) - f(z₀)]/h exists and is independent of the direction in which h approaches 0. This requirement — that the derivative exists along all paths and is the same value — is far more restrictive than real differentiability and is the gateway to rigid complex analysis.

## How It's Best Learned
Compute derivatives directly from the definition for f(z) = z² and f(z) = 1/z. Attempt this for f(z) = |z|² and observe that the limit fails (depends on direction). This contrast shows why complex differentiability is special.

## Common Misconceptions
Thinking complex differentiability is just real differentiability of u and v separately; that gives only a function of two real variables, not an analytic function. Assuming all functions satisfying Cauchy-Riemann are differentiable; continuity of partials is needed too.

## Explainer

From your work on limits and continuity in the complex plane, you know that a complex limit lim_{z→z₀} f(z) must be the same regardless of the path z takes toward z₀. Complex differentiability imposes this same path-independence on the difference quotient [f(z₀+h) − f(z₀)]/h as h → 0. The requirement is far more severe than real differentiability: in ℝ, h can only approach 0 from two directions (left or right). In ℂ, h is complex and can approach 0 from infinitely many directions — along the real axis, the imaginary axis, diagonals, spirals, any curve. The limit must give the same value along all of them.

Compare f(z) = z² with g(z) = |z|². For f(z) = z², the difference quotient is [(z₀+h)² − z₀²]/h = 2z₀ + h → 2z₀ regardless of the direction of h. For g(z) = |z|², write h = a + bi (with a,b real). The quotient becomes [|z₀+h|² − |z₀|²]/h; letting h approach 0 along the real axis (b = 0) gives a different limit than along the imaginary axis (a = 0). The limit depends on direction, so g(z) = |z|² is not differentiable anywhere, even though it is smooth when viewed as a function of two real variables.

This direction-independence requirement is algebraically equivalent to the **Cauchy-Riemann equations**. If f(z) = u(x,y) + iv(x,y) where z = x + iy, then f is differentiable at z₀ if and only if u and v satisfy ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x at that point (and the partial derivatives are continuous there). These two equations encode the constraint that the horizontal-direction limit and the vertical-direction limit of the difference quotient agree — which forces all directions to agree simultaneously.

The payoff is enormous. In real analysis, a function can be differentiable once but not twice. In complex analysis, if a function is differentiable on an open set — making it **holomorphic** — it is automatically differentiable infinitely many times, equal to its Taylor series everywhere, and satisfies Laplace's equation. One "free" derivative in ℂ buys you all derivatives for free. This remarkable rigidity, which has no real counterpart, is the defining feature of complex analysis and the reason the subject behaves so differently from calculus on ℝ.
