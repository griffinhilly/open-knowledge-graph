---
id: gaussian-quadrature
title: Gaussian Quadrature
domain: mathematics
course: numerical-analysis
prerequisites:
- id: composite-quadrature
  type: hard
builds-toward:
- romberg-integration
tags:
- gaussian-quadrature
- optimal
- integration
stage: abstract-reasoning
status: draft
---

# Gaussian Quadrature

## Core Idea
Gaussian quadrature optimally chooses both sample points x_i and weights w_i to integrate polynomials of degree up to 2n-1 exactly using only n function evaluations. The sample points are roots of orthogonal polynomials (Legendre, Hermite, Laguerre, Chebyshev) with respect to a weight function. Gaussian quadrature achieves exponential convergence for smooth integrands and is the most efficient for general-purpose integration.

## Explainer

From composite quadrature, you know the basic framework: approximate ∫f(x)dx ≈ Σ wᵢ f(xᵢ) by evaluating f at a set of **nodes** xᵢ and combining the results with **weights** wᵢ. The trapezoidal rule and Simpson's rule are examples: they fix the nodes at equally spaced points first, then solve for the weights that make the formula exact for polynomials up to some degree. With n+1 equally spaced nodes, Simpson-type rules achieve exactness up to degree n (roughly). This is called a **Newton-Cotes** approach.

Gaussian quadrature asks a more ambitious question: what if we are free to choose *both* the nodes and the weights? With n nodes, we have 2n free parameters (n node locations + n weights). A degree-d polynomial has d+1 coefficients, and being exact for all polynomials up to degree d means matching d+1 conditions. So 2n free parameters should, in principle, allow exactness for polynomials up to degree 2n−1 — roughly *twice* the degree achievable with Newton-Cotes. This is the central claim of Gaussian quadrature.

The optimal node locations turn out to be the **roots of orthogonal polynomials**. For the standard interval [−1,1] with weight function w(x) = 1, the correct polynomials are the **Legendre polynomials** P_n(x), and the n-point Gauss-Legendre rule places nodes at the n zeros of P_n(x). The weights are then determined by requiring exact integration of polynomials of each degree up to n−1. For other integration domains or weight functions (e.g., ∫₀^∞ e^{−x} f(x) dx), different polynomial families apply: Laguerre polynomials for the half-line with exponential weight, Hermite for the full line with Gaussian weight.

The payoff is dramatic for smooth functions. Newton-Cotes rules converge at an algebraic rate as you add nodes — roughly O(h^p) where h is the step size. Gaussian quadrature converges **exponentially** for analytic functions: doubling the number of nodes can square the accuracy. In practice, a 5-point Gauss-Legendre rule often outperforms a 100-point trapezoidal rule on smooth integrands. The trade-off is that Gaussian nodes are not equally spaced (they cluster toward the endpoints), so you cannot reuse function evaluations when increasing the node count — each new n requires a fresh set of n evaluations.
