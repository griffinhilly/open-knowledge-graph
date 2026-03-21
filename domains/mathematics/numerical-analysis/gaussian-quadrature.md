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
stage: advanced
status: draft
---

# Gaussian Quadrature

## Core Idea
Gaussian quadrature optimally chooses both sample points x_i and weights w_i to integrate polynomials of degree up to 2n-1 exactly using only n function evaluations. The sample points are roots of orthogonal polynomials (Legendre, Hermite, Laguerre, Chebyshev) with respect to a weight function. Gaussian quadrature achieves exponential convergence for smooth integrands and is the most efficient for general-purpose integration.

## Questions

```yaml
- question: "A 5-point Gauss-Legendre rule is compared to a 50-point trapezoidal rule for integrating a smooth, analytic function. Which claim best describes the likely outcome?"
  type: multiple-choice
  options:
    - "The 50-point trapezoidal rule is more accurate because it uses more evaluation points"
    - "The 5-point Gauss-Legendre rule may well outperform the 50-point trapezoidal rule because it converges exponentially for smooth integrands"
    - "Both achieve similar accuracy because both are quadrature rules using weighted sums"
    - "The trapezoidal rule is better because equally spaced nodes avoid aliasing errors"
  answer: 1
  explanation: "Gaussian quadrature converges exponentially for smooth analytic functions — doubling the number of nodes can square the accuracy. Newton-Cotes rules (trapezoidal, Simpson's) converge only algebraically at rate O(h^p). In practice, a 5-point Gauss-Legendre rule routinely outperforms much larger trapezoidal rules on smooth integrands. The key is that Gaussian quadrature optimizes both node locations and weights, squeezing maximum polynomial exactness from each evaluation."

- question: "What is the fundamental freedom that allows Gaussian quadrature to achieve exactness for polynomials of degree up to 2n−1 using only n points?"
  type: multiple-choice
  options:
    - "Gaussian quadrature evaluates the integrand at complex-valued points, accessing more information"
    - "Gaussian quadrature uses adaptive refinement to concentrate points where the function varies most"
    - "Gaussian quadrature optimizes both node locations and weights simultaneously, doubling the free parameters compared to fixed-node rules"
    - "Gaussian quadrature applies a correction term derived from the function's derivatives at the boundary"
  answer: 2
  explanation: "Newton-Cotes rules fix nodes at equally spaced points first, then solve for weights — only n+1 free parameters (the weights) are used to match polynomial conditions. Gaussian quadrature treats both node locations and weights as free, giving 2n free parameters for n nodes. This is enough to enforce exactness for all polynomials up to degree 2n−1, roughly double what equally-spaced nodes can achieve."

- question: "Gaussian quadrature with n points is exact for polynomials of degree up to n."
  type: true-false
  answer: false
  explanation: "Gaussian quadrature with n points is exact for polynomials of degree up to 2n−1 — roughly twice what you might expect. This is the central payoff of optimizing node locations: with n nodes and n weights (2n free parameters), you can match the 2n conditions required to integrate all polynomials through degree 2n−1 exactly. A common misconception is to expect only degree n exactness, conflating Gaussian quadrature with Newton-Cotes rules."

- question: "One practical disadvantage of Gaussian quadrature is that increasing the node count from n to n+1 requires computing an entirely new set of nodes and weights, discarding the previous n function evaluations."
  type: true-false
  answer: true
  explanation: "Gaussian nodes (roots of orthogonal polynomials) are not nested — the n-point rule and the (n+1)-point rule use completely different node locations. This means you cannot reuse prior function evaluations when refining accuracy, unlike equally-spaced rules where you can insert midpoints. This is a real practical cost when adaptive accuracy control is needed. Gauss-Kronrod rules partially address this by nesting extended rule families."

- question: "Why are the optimal nodes for Gaussian quadrature placed at the roots of orthogonal polynomials rather than at equally spaced points?"
  type: short-answer
  answer: "The roots of orthogonal polynomials are precisely the node locations that maximize the degree of polynomial exactness for a given number of evaluations. Orthogonality ensures that the n-th degree polynomial (whose roots give the nodes) is orthogonal to all lower-degree polynomials, which is the algebraic condition that guarantees the resulting quadrature rule is exact for polynomials up to degree 2n−1. Equally spaced nodes fix locations before optimizing weights, sacrificing roughly half the potential exactness."
  explanation: "The connection between orthogonal polynomials and optimal quadrature is one of the beautiful results of approximation theory. The orthogonality condition is not merely convenient — it is precisely what makes the node placement optimal. Different weight functions and domains (Gauss-Hermite for ∫e^{-x²}f dx, Gauss-Laguerre for ∫₀^∞ e^{-x}f dx) require different orthogonal polynomial families, but the principle is always the same: orthogonal roots = optimal nodes."
```

## Explainer

From composite quadrature, you know the basic framework: approximate ∫f(x)dx ≈ Σ wᵢ f(xᵢ) by evaluating f at a set of **nodes** xᵢ and combining the results with **weights** wᵢ. The trapezoidal rule and Simpson's rule are examples: they fix the nodes at equally spaced points first, then solve for the weights that make the formula exact for polynomials up to some degree. With n+1 equally spaced nodes, Simpson-type rules achieve exactness up to degree n (roughly). This is called a **Newton-Cotes** approach.

Gaussian quadrature asks a more ambitious question: what if we are free to choose *both* the nodes and the weights? With n nodes, we have 2n free parameters (n node locations + n weights). A degree-d polynomial has d+1 coefficients, and being exact for all polynomials up to degree d means matching d+1 conditions. So 2n free parameters should, in principle, allow exactness for polynomials up to degree 2n−1 — roughly *twice* the degree achievable with Newton-Cotes. This is the central claim of Gaussian quadrature.

The optimal node locations turn out to be the **roots of orthogonal polynomials**. For the standard interval [−1,1] with weight function w(x) = 1, the correct polynomials are the **Legendre polynomials** P_n(x), and the n-point Gauss-Legendre rule places nodes at the n zeros of P_n(x). The weights are then determined by requiring exact integration of polynomials of each degree up to n−1. For other integration domains or weight functions (e.g., ∫₀^∞ e^{−x} f(x) dx), different polynomial families apply: Laguerre polynomials for the half-line with exponential weight, Hermite for the full line with Gaussian weight.

The payoff is dramatic for smooth functions. Newton-Cotes rules converge at an algebraic rate as you add nodes — roughly O(h^p) where h is the step size. Gaussian quadrature converges **exponentially** for analytic functions: doubling the number of nodes can square the accuracy. In practice, a 5-point Gauss-Legendre rule often outperforms a 100-point trapezoidal rule on smooth integrands. The trade-off is that Gaussian nodes are not equally spaced (they cluster toward the endpoints), so you cannot reuse function evaluations when increasing the node count — each new n requires a fresh set of n evaluations.
