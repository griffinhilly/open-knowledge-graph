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
stage: advanced
status: draft
---

# Newton-Cotes Quadrature Formulas

## Core Idea
Newton-Cotes formulas approximate ∫f(x)dx using weighted sums of f evaluated at equally-spaced points. Examples include the trapezoidal rule (2-point, O(h³) error) and Simpson's rule (3-point, O(h⁵) error), derived by integrating the Lagrange polynomial through sample points. Open formulas omit endpoints and are useful when f is singular or undefined at boundaries.

## Questions

```yaml
- question: "Simpson's rule uses a quadratic (degree-2) interpolating polynomial, yet it integrates cubic polynomials exactly. Why?"
  type: multiple-choice
  options:
    - "A quadratic polynomial can implicitly represent a cubic through the midpoint evaluation, which doubles its effective degree"
    - "The error term in Simpson's rule involves a fourth derivative, which vanishes for cubic polynomials—a consequence of the symmetric three-point arrangement"
    - "Simpson's rule uses adaptive step sizing that automatically improves for polynomial integrands"
    - "This is a coincidence specific to the interval [−1, 1] and does not hold for general intervals"
  answer: 1
  explanation: "This 'superconvergence' of Simpson's rule is the key insight of this topic. The error term for Simpson's rule (derived via Taylor series analysis of the residual) involves the fourth derivative f⁽⁴⁾(ξ) for some ξ in the interval. For any cubic polynomial, the fourth derivative is identically zero—so the error term vanishes exactly, even though the interpolating polynomial is only quadratic. This symmetry-driven cancellation means Simpson's rule integrates one degree higher than expected. Option A is the most tempting misconception: there is no adaptive mechanism; it is purely a consequence of the error term structure."

- question: "A student wants very high accuracy for a smooth integrand over [0, 1] and decides to use a single 10-point Newton-Cotes formula instead of applying Simpson's rule repeatedly over many small subintervals. What problem are they likely to encounter?"
  type: multiple-choice
  options:
    - "The 10-point formula requires solving a 10×10 linear system, making it computationally prohibitive"
    - "Higher-order Newton-Cotes formulas with equally-spaced points suffer from Runge's phenomenon: large oscillations near the endpoints cause the weights to become large and alternating in sign, potentially making accuracy worse"
    - "The 10-point formula has lower convergence order than Simpson's rule, so it always produces less accurate results"
    - "Newton-Cotes formulas are only defined for intervals of the form [0, 1] and cannot be applied to general domains"
  answer: 1
  explanation: "Runge's phenomenon is the central practical limitation of high-order Newton-Cotes formulas. With equally-spaced quadrature points, the Lagrange interpolating polynomial oscillates wildly near the endpoints as the degree grows, regardless of how smooth the integrand is. This causes the Newton-Cotes weights to alternate in sign and grow large, leading to catastrophic cancellation in the weighted sum. For smooth functions, composite Simpson's rule with many small subintervals outperforms a single high-order Newton-Cotes formula while remaining numerically stable."

- question: "Halving the step size h in the trapezoidal rule reduces the integration error by a factor of 4, because the trapezoidal rule has O(h²) global accuracy."
  type: true-false
  answer: true
  explanation: "Correct. The global error of the composite trapezoidal rule is O(h²): if you halve h (doubling the number of subintervals), the error decreases by a factor of 2² = 4. For composite Simpson's rule, the global error is O(h⁴), so halving h reduces the error by a factor of 16. Understanding these convergence rates is essential for choosing between methods and for error analysis—it tells you how much work (in terms of function evaluations) is needed to achieve a desired accuracy."

- question: "Higher-order Newton-Cotes formulas—those using more equally-spaced evaluation points—always produce more accurate results than lower-order formulas like Simpson's rule for the same interval."
  type: true-false
  answer: false
  explanation: "False. This is the misconception that Runge's phenomenon refutes. For high-degree Newton-Cotes formulas, the Lagrange interpolating polynomial oscillates wildly near the endpoints of equally-spaced nodes, causing the quadrature weights to become large and alternating in sign. The resulting formula can produce wildly inaccurate results even for smooth functions. In practice, Newton-Cotes formulas beyond degree 4 (Simpson's 3/8 rule) are rarely used directly. The preferred approach is composite quadrature: applying low-degree formulas over many small subintervals."

- question: "Why are composite quadrature methods preferred over single high-order Newton-Cotes formulas in practice, even when high accuracy is required?"
  type: short-answer
  answer: "High-order Newton-Cotes formulas with equally-spaced points suffer from Runge's phenomenon: the Lagrange interpolating polynomial oscillates increasingly near the endpoints as degree grows, making the integration weights large and alternating in sign. This causes numerical instability and potentially worse accuracy than lower-order formulas. Composite methods instead apply a stable low-degree formula (trapezoidal or Simpson's) repeatedly over many small subintervals of width h, achieving global accuracy of O(h²) or O(h⁴) that improves predictably as h decreases—without the instability of high-degree interpolation over the full interval."
  explanation: "The deeper lesson is that 'higher degree' does not automatically mean 'more accurate' in numerical methods. Stability and error behavior must both be considered. Composite quadrature exploits the fact that a low-degree formula applied over small intervals can be both accurate and numerically stable, whereas a single high-degree formula over the whole interval may be neither."
```

## Explainer

You already know **Lagrange polynomial interpolation**: given n+1 points, there is a unique polynomial of degree ≤ n passing through all of them. The Newton-Cotes idea is simple — if you want to integrate f over [a, b] but cannot find an antiderivative, replace f with its Lagrange interpolating polynomial through equally-spaced sample points, and integrate that polynomial exactly. The integral of the polynomial is a weighted sum of function values, and those weights are fixed numbers depending only on how many points you use and the interval width h.

The two most important cases illustrate the pattern. The **trapezoidal rule** uses two endpoints, fits a line through them, and integrates: ∫ ≈ (h/2)(f(a) + f(b)). Geometrically, you are computing the area of a trapezoid under the line connecting the two endpoints. The error is O(h³), meaning it scales with the cube of the interval width — halving h reduces the error by a factor of 8. **Simpson's rule** uses three equally-spaced points (including the midpoint), fits a parabola, and integrates: ∫ ≈ (h/6)(f(a) + 4f(m) + f(b)). The parabola is a better fit than the line, and the error is O(h⁵). Remarkably, Simpson's rule is exact for polynomials up to degree 3, even though it only uses a degree-2 interpolant — this "super-convergence" follows from a symmetry argument using **Taylor series** analysis of the error term.

The weights in Newton-Cotes formulas are derived by integrating the Lagrange basis polynomials: wᵢ = ∫Lᵢ(x)dx, where Lᵢ is the i-th Lagrange basis polynomial. These integrals can be computed once symbolically and tabulated. Higher-order Newton-Cotes formulas (using more points) can achieve very low errors for smooth functions but suffer from a serious problem: **Runge's phenomenon**. With equally-spaced points, the Lagrange polynomial oscillates wildly near the endpoints for high degrees, and the integration weights can become large and alternating in sign, causing catastrophic cancellation. This is why Newton-Cotes formulas beyond Simpson's rule are rarely used directly in practice.

The practical solution — which this topic builds toward — is **composite quadrature**: instead of using one high-degree formula over the whole interval, apply a low-degree formula (trapezoidal or Simpson's) repeatedly over many small subintervals. Each subinterval has width h, the error per subinterval is O(hᵏ) for a k-th order formula, and the errors combine to give overall O(hᵏ) global accuracy that improves predictably as h → 0. Newton-Cotes formulas are thus not primarily used raw; they are the building blocks from which composite and adaptive integration schemes are constructed.
