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
status: validated
---

# Orthogonal Polynomials and Weights

## Core Idea
Orthogonal polynomials (Legendre, Hermite, Laguerre, Chebyshev) form orthogonal bases with respect to weighted inner products. Each family corresponds to a domain and weight function: Legendre for [-1,1] with uniform weight, Hermite for ℝ with Gaussian weight, Laguerre for [0,∞) with exponential weight. Orthogonal polynomials are fundamental to Gaussian quadrature and spectral methods for PDEs.

## Questions

```yaml
- question: "A 5-point Gaussian-Legendre quadrature rule exactly integrates all polynomials of degree up to:"
  type: multiple-choice
  options:
    - "4"
    - "5"
    - "9"
    - "10"
  answer: 2
  explanation: "An n-point Gaussian quadrature rule exactly integrates all polynomials of degree up to 2n − 1. With n = 5 points, this is 2(5) − 1 = 9. The common mistake is thinking a 5-point rule handles only degree-5 polynomials. The reason for the 2n − 1 exactness comes from orthogonal polynomial theory: any degree-(2n−1) polynomial can be written as P_n(x)·s(x) + r(x) where s and r have degree less than n; the first term integrates to zero by orthogonality, and the n-point rule captures r(x) exactly."

- question: "Chebyshev polynomials and Legendre polynomials both form orthogonal families on [-1, 1]. What is the key difference between them?"
  type: multiple-choice
  options:
    - "Legendre polynomials have more roots on [-1, 1] than Chebyshev polynomials of the same degree"
    - "They are orthogonal with respect to different weight functions: Legendre uses w(x) = 1, Chebyshev uses w(x) = 1/√(1−x²)"
    - "Chebyshev polynomials are not actually orthogonal — they just minimize approximation error"
    - "Legendre polynomials are only defined for even degrees"
  answer: 1
  explanation: "Both families are orthogonal polynomials on [-1, 1], but the inner product differs. Legendre: ⟨f,g⟩ = ∫₋₁¹ f(x)g(x) dx (uniform weight). Chebyshev: ⟨f,g⟩ = ∫₋₁¹ f(x)g(x)/√(1−x²) dx (endpoint-upweighting). The Chebyshev weight concentrates attention near the endpoints, which is why Chebyshev polynomials have the minimax property — they minimize the maximum deviation from zero among all monic polynomials, making them optimal for polynomial approximation in the sup-norm sense."

- question: "The n roots of the nth orthogonal polynomial P_n are the optimal node locations for an n-point Gaussian quadrature rule."
  type: true-false
  answer: true
  explanation: "This is the central connection between orthogonal polynomials and Gaussian quadrature. The roots of P_n are called Gauss points or quadrature nodes. Using them as evaluation points, with carefully chosen quadrature weights, produces a rule that integrates all polynomials of degree up to 2n−1 exactly. No other choice of n nodes achieves this degree of exactness — the orthogonal polynomial roots are uniquely optimal."

- question: "Gaussian quadrature with n points is generally less accurate than an n-point equally-spaced rule (like the composite trapezoidal rule) for smooth functions."
  type: true-false
  answer: false
  explanation: "The opposite is true — Gaussian quadrature is dramatically more accurate. For smooth functions, Gaussian quadrature converges exponentially fast as n increases, not just algebraically. A 5-point Gaussian rule integrates all polynomials of degree up to 9 exactly, while a 5-point composite trapezoidal or Simpson's rule achieves only algebraic convergence. The orthogonal polynomial node placement exploits the full polynomial-exactness budget of n function evaluations."

- question: "Why does a 5-point Gaussian-Legendre rule exactly integrate polynomials of degree up to 9, rather than just up to 4? What property of orthogonal polynomials makes this possible?"
  type: short-answer
  answer: "An n-point rule has 2n free parameters (n node locations plus n weights). By choosing nodes at the roots of P_n and weights optimally, the rule is exact for all polynomials of degree up to 2n−1 — not just n−1. The key is that any degree-(2n−1) polynomial can be decomposed as P_n(x)·s(x) + r(x) where s and r have degree less than n. The first term integrates to zero by orthogonality of P_n; the second is captured exactly by the n-point rule. This doubles the polynomial exactness degree."
  explanation: "The orthogonality of P_n is doing crucial work: it guarantees that the 'high-degree' component P_n·s integrates to zero for free, without using any of the n function evaluations. Only the degree-(n−1) remainder r(x) needs to be handled explicitly, which n points can do exactly. This argument breaks down for degree ≥ 2n because the remainder r would have degree ≥ n and would not be exactly integrable."
```

## Explainer

You already know that an **inner product space** equips a vector space with a way to measure "angle" and "orthogonality" between vectors. Polynomials form a vector space, and you can define inner products on them by integrating: (f, g)_w = ∫ f(x)g(x)w(x)dx, where w(x) ≥ 0 is a **weight function**. Starting from the monomials 1, x, x², ... and applying the Gram-Schmidt process with respect to this weighted inner product, you obtain a sequence of **orthogonal polynomials** P_0, P_1, P_2, ... where deg(P_n) = n and (P_m, P_n)_w = 0 for m ≠ n. The choice of domain and weight function determines which classical family emerges.

The four main families each arise from a natural mathematical setting. **Legendre polynomials** live on [-1, 1] with constant weight w(x) = 1 — the uniform measure, with no preference for any part of the interval. **Chebyshev polynomials** also live on [-1, 1] but with w(x) = 1/√(1-x²), which upweights the endpoints. This seemingly odd choice is deeply motivated: Chebyshev polynomials have the smallest maximum deviation from zero among all monic polynomials, making them optimal for polynomial approximation. **Hermite polynomials** live on all of ℝ with Gaussian weight w(x) = e^(-x²), making them the natural basis for quantum harmonic oscillator wavefunctions and probability theory. **Laguerre polynomials** live on [0, ∞) with exponential weight w(x) = e^(-x).

A key property of any orthogonal polynomial family is that P_n has exactly n distinct real roots within its domain. This is not a coincidence — it follows from the orthogonality relations. These roots are called **Gauss points** or **quadrature nodes**, and they are the secret ingredient in Gaussian quadrature. To numerically integrate ∫ f(x)w(x)dx using n function evaluations, evaluate f at the n roots of P_n and form a weighted sum with carefully chosen **quadrature weights**. This n-point Gaussian rule integrates all polynomials of degree up to 2n-1 exactly. The reason is that any degree-(2n-1) polynomial q(x) can be written as q(x) = P_n(x) · s(x) + r(x) where deg(s), deg(r) < n; the first term integrates to zero by orthogonality, and the second is captured exactly by the n-point rule.

The practical consequence is dramatic. A 5-point Gaussian-Legendre rule integrates all polynomials up to degree 9 exactly — the same accuracy would require many more equally-spaced points with the trapezoidal or Simpson's rule. For smooth functions, Gaussian quadrature converges exponentially fast as n increases, not just algebraically. The orthogonal polynomial structure is not just theoretical elegance — it is the direct source of this computational power.
