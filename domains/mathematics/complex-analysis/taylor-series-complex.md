---
id: taylor-series-complex
title: Taylor Series for Complex Functions
domain: mathematics
course: complex-analysis
prerequisites:
- id: cauchys-integral-formula-derivatives
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- power-series-complex-plane
- laurent-series
tags:
- taylor-series
- power-series
- analytic
stage: advanced
status: draft
---

# Taylor Series for Complex Functions

## Core Idea
Every holomorphic function f on a disk |z - z₀| < R is equal to its Taylor series f(z) = Σ f^(n)(z₀)/n! (z - z₀)^n, which converges for |z - z₀| < R. The radius of convergence R is the distance to the nearest singularity. This makes complex analytic functions completely rigid: the Taylor coefficients encode all information.

## How It's Best Learned
Compute the Taylor series of f(z) = 1/(1-z) around z = 0 and verify the radius of convergence is 1. Understand why: the function has a singularity at z = 1, which is distance 1 from the center.

## Common Misconceptions
Assuming every power series converges everywhere or nowhere; the radius of convergence is finite for holomorphic functions with singularities. Confusing the radius of convergence with the domain of the function.

## Explainer

In real analysis, Taylor series are an approximation tool: a smooth function is approximated by polynomials near a point, with an error that shrinks as you include more terms, but equality holds only in the limit and only under additional conditions. The complex case is different in kind: if f is holomorphic on a disk |z - z₀| < R, then f **equals** its Taylor series everywhere on that disk — not approximately, but exactly, with zero error. This equality is a theorem, not a hope, and it follows directly from Cauchy's Integral Formula for derivatives.

This rigidity has a striking implication. Because the Taylor coefficients aₙ = f^(n)(z₀)/n! are determined entirely by the behavior of f near z₀, two holomorphic functions that agree on any open set — even a tiny disk — must agree on their entire shared domain. You cannot patch together two different holomorphic functions smoothly the way you can with real functions. The function is "frozen" by its local behavior. This property is called the **identity theorem** and it has no real-analysis analogue.

The **radius of convergence** R is the distance from the center z₀ to the nearest **singularity** of f in the complex plane. This is one of the most clarifying results in all of analysis. For f(z) = 1/(1 + z²), the real function 1/(1 + x²) is perfectly smooth for all real x — it has no real singularity. Yet its Taylor series around x = 0 has radius of convergence 1, a fact that puzzled mathematicians before complex analysis was developed. The resolution: in the complex plane, f has singularities at z = ±i, which are distance 1 from the origin. The singularities are invisible on the real line but they govern the radius of convergence.

To find Taylor series in practice, you can either compute derivatives directly or manipulate known series algebraically. The geometric series 1/(1 - z) = Σ zⁿ for |z| < 1 is the most useful starting point. Substituting -z² for z gives 1/(1 + z²) = Σ (-1)ⁿ z²ⁿ for |z| < 1. Substituting z² for z gives 1/(1 - z²) = Σ z²ⁿ for |z| < 1. These substitution tricks are the same algebraic manipulations you know from real Taylor series — the complex setting adds no new algebraic rules, only a geometric interpretation (via singularity locations) of why the radius of convergence is what it is.
