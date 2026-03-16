---
id: newton-cotes-quadrature
title: Newton-Cotes Quadrature
domain: mathematics
course: numerical-analysis
prerequisites:
- id: lagrange-polynomial-interpolation
  type: hard
builds-toward:
- composite-quadrature-rules
- romberg-integration
tags:
- numerical-integration
- quadrature
- newton-cotes
stage: advanced
status: draft
---

# Newton-Cotes Quadrature

## Core Idea
Newton-Cotes quadrature rules approximate integrals using weighted sums of function values at equally-spaced nodes, with weights determined by integrating the Lagrange interpolating polynomial. Common examples are the trapezoidal rule (2 nodes, degree 1 accuracy) and Simpson's rule (3 nodes, degree 3 accuracy). Closed formulas include endpoints; open formulas exclude them.

## Explainer

From **Lagrange polynomial interpolation**, you know how to construct the unique polynomial of degree ≤ n that passes through n+1 given points. Newton-Cotes quadrature takes that idea and turns it into a method for numerical integration: replace the integrand f(x) with its interpolating polynomial P(x), then integrate P(x) exactly. The result is a weighted sum of function values — a **quadrature rule**.

Here is the construction explicitly. On the interval [a, b], place n+1 equally-spaced nodes x₀ = a, x₁, …, xₙ = b (for closed rules). Construct the Lagrange interpolating polynomial P(x) = Σ f(xᵢ) Lᵢ(x), where Lᵢ is the i-th Lagrange basis polynomial. Then ∫ₐᵇ f(x) dx ≈ ∫ₐᵇ P(x) dx = Σ wᵢ f(xᵢ), where the weights wᵢ = ∫ₐᵇ Lᵢ(x) dx are determined entirely by the node positions, not by f. For two nodes (n = 1), this gives the **trapezoidal rule**: ∫ₐᵇ f(x) dx ≈ (b−a)/2 · [f(a) + f(b)], which is just the area of the trapezoid under the linear interpolant. For three equally-spaced nodes (n = 2), you get **Simpson's rule**: ∫ₐᵇ f(x) dx ≈ (b−a)/6 · [f(a) + 4f((a+b)/2) + f(b)]. Simpson's rule is exact for polynomials of degree ≤ 3, even though it only uses a degree-2 interpolant — this bonus accuracy (called a **degree of precision** boost) arises because the error term for even-order rules contains a factor that integrates to zero by symmetry.

The error analysis connects to how well a polynomial of degree n approximates f on [a, b]. For the trapezoidal rule, the error is O(h³ f″) where h = b − a; for Simpson's, O(h⁵ f⁽⁴⁾). Higher-order Newton-Cotes rules (Boole's rule at n = 4, etc.) have formally smaller errors, but they suffer from a practical problem: for large n, Lagrange interpolation at equally-spaced nodes is highly unstable due to **Runge's phenomenon** — the interpolating polynomial oscillates wildly near the endpoints. This is why in practice, composite rules (applying the trapezoidal or Simpson's rule on many small subintervals rather than one large one) are preferred over high-order rules on the whole interval. Newton-Cotes is therefore the foundation, and understanding why higher-order rules fail motivates the more sophisticated methods (Gaussian quadrature, adaptive integration) that follow.
