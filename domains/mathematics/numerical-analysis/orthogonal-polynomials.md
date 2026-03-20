---
id: orthogonal-polynomials
title: Orthogonal Polynomials and Weights
domain: mathematics
course: numerical-analysis
prerequisites:
- id: inner-product-spaces
  type: hard
builds-toward:
- gaussian-quadrature
tags:
- orthogonal-polynomials
- weights
- quadrature
stage: formal-systems
status: draft
---

# Orthogonal Polynomials and Weights

## Core Idea
Orthogonal polynomials (Legendre, Hermite, Laguerre, Chebyshev) form orthogonal bases with respect to weighted inner products. Each family corresponds to a domain and weight function: Legendre for [-1,1] with uniform weight, Hermite for ℝ with Gaussian weight, Laguerre for [0,∞) with exponential weight. Orthogonal polynomials are fundamental to Gaussian quadrature and spectral methods for PDEs.

## Explainer

You already know that an **inner product space** equips a vector space with a way to measure "angle" and "orthogonality" between vectors. Polynomials form a vector space, and you can define inner products on them by integrating: (f, g)_w = ∫ f(x)g(x)w(x)dx, where w(x) ≥ 0 is a **weight function**. Starting from the monomials 1, x, x², ... and applying the Gram-Schmidt process with respect to this weighted inner product, you obtain a sequence of **orthogonal polynomials** P_0, P_1, P_2, ... where deg(P_n) = n and (P_m, P_n)_w = 0 for m ≠ n. The choice of domain and weight function determines which classical family emerges.

The four main families each arise from a natural mathematical setting. **Legendre polynomials** live on [-1, 1] with constant weight w(x) = 1 — the uniform measure, with no preference for any part of the interval. **Chebyshev polynomials** also live on [-1, 1] but with w(x) = 1/√(1-x²), which upweights the endpoints. This seemingly odd choice is deeply motivated: Chebyshev polynomials have the smallest maximum deviation from zero among all monic polynomials, making them optimal for polynomial approximation. **Hermite polynomials** live on all of ℝ with Gaussian weight w(x) = e^(-x²), making them the natural basis for quantum harmonic oscillator wavefunctions and probability theory. **Laguerre polynomials** live on [0, ∞) with exponential weight w(x) = e^(-x).

A key property of any orthogonal polynomial family is that P_n has exactly n distinct real roots within its domain. This is not a coincidence — it follows from the orthogonality relations. These roots are called **Gauss points** or **quadrature nodes**, and they are the secret ingredient in Gaussian quadrature. To numerically integrate ∫ f(x)w(x)dx using n function evaluations, evaluate f at the n roots of P_n and form a weighted sum with carefully chosen **quadrature weights**. This n-point Gaussian rule integrates all polynomials of degree up to 2n-1 exactly. The reason is that any degree-(2n-1) polynomial q(x) can be written as q(x) = P_n(x) · s(x) + r(x) where deg(s), deg(r) < n; the first term integrates to zero by orthogonality, and the second is captured exactly by the n-point rule.

The practical consequence is dramatic. A 5-point Gaussian-Legendre rule integrates all polynomials up to degree 9 exactly — the same accuracy would require many more equally-spaced points with the trapezoidal or Simpson's rule. For smooth functions, Gaussian quadrature converges exponentially fast as n increases, not just algebraically. The orthogonal polynomial structure is not just theoretical elegance — it is the direct source of this computational power.
