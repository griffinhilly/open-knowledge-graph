---
id: newton-cotes-formulas
title: Newton-Cotes Quadrature Formulas
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: hard
- id: lagrange-polynomial-interpolation
  type: hard
builds-toward:
- composite-quadrature
- gaussian-quadrature
tags:
- quadrature
- newton-cotes
- integration
stage: abstract-reasoning
status: draft
---

# Newton-Cotes Quadrature Formulas

## Core Idea
Newton-Cotes formulas approximate ∫f(x)dx using weighted sums of f evaluated at equally-spaced points. Examples include the trapezoidal rule (2-point, O(h³) error) and Simpson's rule (3-point, O(h⁵) error), derived by integrating the Lagrange polynomial through sample points. Open formulas omit endpoints and are useful when f is singular or undefined at boundaries.

## Explainer

You already know **Lagrange polynomial interpolation**: given n+1 points, there is a unique polynomial of degree ≤ n passing through all of them. The Newton-Cotes idea is simple — if you want to integrate f over [a, b] but cannot find an antiderivative, replace f with its Lagrange interpolating polynomial through equally-spaced sample points, and integrate that polynomial exactly. The integral of the polynomial is a weighted sum of function values, and those weights are fixed numbers depending only on how many points you use and the interval width h.

The two most important cases illustrate the pattern. The **trapezoidal rule** uses two endpoints, fits a line through them, and integrates: ∫ ≈ (h/2)(f(a) + f(b)). Geometrically, you are computing the area of a trapezoid under the line connecting the two endpoints. The error is O(h³), meaning it scales with the cube of the interval width — halving h reduces the error by a factor of 8. **Simpson's rule** uses three equally-spaced points (including the midpoint), fits a parabola, and integrates: ∫ ≈ (h/6)(f(a) + 4f(m) + f(b)). The parabola is a better fit than the line, and the error is O(h⁵). Remarkably, Simpson's rule is exact for polynomials up to degree 3, even though it only uses a degree-2 interpolant — this "super-convergence" follows from a symmetry argument using **Taylor series** analysis of the error term.

The weights in Newton-Cotes formulas are derived by integrating the Lagrange basis polynomials: wᵢ = ∫Lᵢ(x)dx, where Lᵢ is the i-th Lagrange basis polynomial. These integrals can be computed once symbolically and tabulated. Higher-order Newton-Cotes formulas (using more points) can achieve very low errors for smooth functions but suffer from a serious problem: **Runge's phenomenon**. With equally-spaced points, the Lagrange polynomial oscillates wildly near the endpoints for high degrees, and the integration weights can become large and alternating in sign, causing catastrophic cancellation. This is why Newton-Cotes formulas beyond Simpson's rule are rarely used directly in practice.

The practical solution — which this topic builds toward — is **composite quadrature**: instead of using one high-degree formula over the whole interval, apply a low-degree formula (trapezoidal or Simpson's) repeatedly over many small subintervals. Each subinterval has width h, the error per subinterval is O(hᵏ) for a k-th order formula, and the errors combine to give overall O(hᵏ) global accuracy that improves predictably as h → 0. Newton-Cotes formulas are thus not primarily used raw; they are the building blocks from which composite and adaptive integration schemes are constructed.
