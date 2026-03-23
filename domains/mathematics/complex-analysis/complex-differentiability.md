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
status: validated
---

# Complex Differentiability

## Core Idea
A function f is differentiable at z₀ if the limit f'(z₀) = lim(h→0) [f(z₀+h) - f(z₀)]/h exists and is independent of the direction in which h approaches 0. This requirement — that the derivative exists along all paths and is the same value — is far more restrictive than real differentiability and is the gateway to rigid complex analysis.

## How It's Best Learned
Compute derivatives directly from the definition for f(z) = z² and f(z) = 1/z. Attempt this for f(z) = |z|² and observe that the limit fails (depends on direction). This contrast shows why complex differentiability is special.

## Common Misconceptions
Thinking complex differentiability is just real differentiability of u and v separately; that gives only a function of two real variables, not an analytic function. Assuming all functions satisfying Cauchy-Riemann are differentiable; continuity of partials is needed too.

## Questions

```yaml
- question: "The function f(z) = |z|² is smooth as a function of two real variables (x,y), yet it fails to be complex differentiable except at one point. Why?"
  type: multiple-choice
  options:
    - "Because |z|² is not continuous in the complex plane"
    - "Because the limit of the difference quotient depends on the direction h approaches 0"
    - "Because |z|² cannot be expressed in the form u + iv"
    - "Because the partial derivatives of u and v do not exist anywhere"
  answer: 1
  explanation: "In the complex sense, the difference quotient [|z₀+h|² − |z₀|²]/h must give the same result regardless of the direction h → 0. Computing along the real axis (h = a) versus the imaginary axis (h = bi) gives different limits, so the derivative doesn't exist. Real differentiability only requires that a linear approximation exists as a map ℝ² → ℝ² — it doesn't enforce path-independence of the complex ratio [f(z₀+h)−f(z₀)]/h."

- question: "A function f(z) is complex differentiable at every point in an open region. Which of the following is an immediate consequence?"
  type: multiple-choice
  options:
    - "f has exactly one complex derivative at each point, but not necessarily two"
    - "f must be a polynomial"
    - "f is automatically differentiable infinitely many times and equals its Taylor series on that region"
    - "f must satisfy the triangle inequality at every point"
  answer: 2
  explanation: "This is the remarkable rigidity of holomorphic functions. In real analysis, being once differentiable says nothing about twice differentiable. In complex analysis, one 'free' derivative on an open set — holomorphicity — implies infinite differentiability and analyticity (equality with the Taylor series) for free. This has no real analogue and is one of the defining features of complex analysis."

- question: "Complex differentiability is equivalent to real differentiability when f is viewed as a map from ℝ² to ℝ²."
  type: true-false
  answer: false
  explanation: "Real differentiability (as a map ℝ² → ℝ²) requires only that a linear approximation exists, placing no constraint on direction. Complex differentiability additionally requires that the ratio [f(z₀+h)−f(z₀)]/h gives the same complex number regardless of the direction h approaches zero — the Cauchy-Riemann condition. This rules out many real-differentiable functions, including f(z) = |z|², which is smooth on ℝ² but not complex differentiable."

- question: "If a function satisfies the Cauchy-Riemann equations at a point, it is necessarily complex differentiable at that point."
  type: true-false
  answer: false
  explanation: "Satisfying the Cauchy-Riemann equations is necessary but not sufficient. The partial derivatives of u and v must also be continuous at that point. A function can satisfy the Cauchy-Riemann equations at an isolated point while having discontinuous partials there, and in that case the complex derivative does not exist. The complete theorem requires: Cauchy-Riemann equations hold AND the partial derivatives are continuous."

- question: "Explain why the requirement that the complex derivative be path-independent is so much more restrictive than real differentiability."
  type: short-answer
  answer: "In ℝ, h can only approach 0 from two directions (positive or negative). In ℂ, h is a complex number and can approach 0 from infinitely many directions — along the real axis, imaginary axis, any angle, any curved path. The derivative limit must give exactly the same complex number along all of them. This single constraint algebraically forces the Cauchy-Riemann equations, which rigidly link the partial derivatives of the real and imaginary parts. Real differentiability only requires a linear approximation to exist with no constraint coupling different directions."
  explanation: "Path-independence is the gateway to all of complex analysis. It forces harmonic conjugates, conformal mappings, and the remarkable rigidity that makes holomorphic functions infinitely differentiable from a single differentiability assumption."
```

## Explainer

From your work on limits and continuity in the complex plane, you know that a complex limit lim_{z→z₀} f(z) must be the same regardless of the path z takes toward z₀. Complex differentiability imposes this same path-independence on the difference quotient [f(z₀+h) − f(z₀)]/h as h → 0. The requirement is far more severe than real differentiability: in ℝ, h can only approach 0 from two directions (left or right). In ℂ, h is complex and can approach 0 from infinitely many directions — along the real axis, the imaginary axis, diagonals, spirals, any curve. The limit must give the same value along all of them.

Compare f(z) = z² with g(z) = |z|². For f(z) = z², the difference quotient is [(z₀+h)² − z₀²]/h = 2z₀ + h → 2z₀ regardless of the direction of h. For g(z) = |z|², write h = a + bi (with a,b real). The quotient becomes [|z₀+h|² − |z₀|²]/h; letting h approach 0 along the real axis (b = 0) gives a different limit than along the imaginary axis (a = 0). The limit depends on direction, so g(z) = |z|² is not differentiable anywhere, even though it is smooth when viewed as a function of two real variables.

This direction-independence requirement is algebraically equivalent to the **Cauchy-Riemann equations**. If f(z) = u(x,y) + iv(x,y) where z = x + iy, then f is differentiable at z₀ if and only if u and v satisfy ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x at that point (and the partial derivatives are continuous there). These two equations encode the constraint that the horizontal-direction limit and the vertical-direction limit of the difference quotient agree — which forces all directions to agree simultaneously.

The payoff is enormous. In real analysis, a function can be differentiable once but not twice. In complex analysis, if a function is differentiable on an open set — making it **holomorphic** — it is automatically differentiable infinitely many times, equal to its Taylor series everywhere, and satisfies Laplace's equation. One "free" derivative in ℂ buys you all derivatives for free. This remarkable rigidity, which has no real counterpart, is the defining feature of complex analysis and the reason the subject behaves so differently from calculus on ℝ.
