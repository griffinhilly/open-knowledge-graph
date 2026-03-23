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
stage: formal-systems
status: validated
---

# Newton-Cotes Quadrature

## Core Idea
Newton-Cotes quadrature rules approximate integrals using weighted sums of function values at equally-spaced nodes, with weights determined by integrating the Lagrange interpolating polynomial. Common examples are the trapezoidal rule (2 nodes, degree 1 accuracy) and Simpson's rule (3 nodes, degree 3 accuracy). Closed formulas include endpoints; open formulas exclude them.

## Questions

```yaml
- question: "Simpson's rule integrates polynomials of degree ≤ 3 exactly, even though it is derived from a degree-2 (quadratic) interpolating polynomial. Why does this 'bonus' degree of precision arise?"
  type: multiple-choice
  options:
    - "Simpson's rule secretly uses four nodes, not three, giving it one extra degree of precision"
    - "Degree-3 polynomials happen to be easier to integrate analytically than degree-2 polynomials"
    - "The error term for even-order Newton-Cotes rules contains a factor that integrates to zero by symmetry over the interval, canceling the leading error contribution"
    - "Simpson's rule applies adaptive refinement on the subinterval to improve precision"
  answer: 2
  explanation: "The degree of precision of a quadrature rule is the highest degree polynomial it integrates exactly. For Simpson's rule, the error term involves the fourth derivative of f and a symmetric factor that integrates to zero when the integrand is a cubic polynomial (which has zero fourth derivative anyway). This cancellation, arising from the symmetric placement of nodes and the symmetric structure of the error term, elevates the degree of precision from 2 to 3 — a 'free' improvement not available to odd-order rules like the trapezoidal rule."

- question: "A student proposes improving numerical integration accuracy by using a 20-node Newton-Cotes rule on a single large interval instead of applying Simpson's rule on many small subintervals. The most important reason this approach fails in practice is:"
  type: multiple-choice
  options:
    - "20-node rules violate the trapezoidal inequality, invalidating the error bounds"
    - "Newton-Cotes rules require the function to be periodic, which most integrands are not"
    - "Lagrange interpolation at 20 equally-spaced nodes suffers from Runge's phenomenon — wild oscillations near the endpoints that make the polynomial, and therefore the integral approximation, highly inaccurate"
    - "High-degree Newton-Cotes rules require more function evaluations than composite low-order rules"
  answer: 2
  explanation: "Runge's phenomenon is the key pathology: for equally-spaced nodes on a large interval, the high-degree Lagrange interpolating polynomial oscillates with growing amplitude near the endpoints, even for smooth functions. The formal order of the error bound improves with degree, but the polynomial diverges in practice. This is why practitioners prefer composite rules (applying low-order rules on many small subintervals) or Gaussian quadrature (which uses optimally placed, non-equally-spaced nodes). Option D is misleading — a single 20-node rule uses the same number of evaluations as a composite rule on 10 subintervals with Simpson's rule."

- question: "The weights in a Newton-Cotes quadrature rule depend on the values of the integrand f at the quadrature nodes."
  type: true-false
  answer: false
  explanation: "The weights wᵢ are computed by integrating the Lagrange basis polynomials Lᵢ(x) over the interval: wᵢ = ∫ Lᵢ(x) dx. The basis polynomials depend only on the positions of the nodes — not on f. This is what makes Newton-Cotes rules reusable: once the weights are computed for a given set of nodes, the same weights apply to any integrand. The rule is just a weighted sum of function values; the weights encode the 'importance' of each node's position in the integral approximation."

- question: "The trapezoidal rule approximates ∫ₐᵇ f(x) dx by replacing f with the straight line through (a, f(a)) and (b, f(b)) and computing the area of the resulting trapezoid."
  type: true-false
  answer: true
  explanation: "This is exactly the geometric interpretation of the trapezoidal rule: the linear interpolating polynomial through the two endpoints is integrated exactly, giving (b−a)/2 · [f(a) + f(b)] — the formula for the area of a trapezoid with parallel sides f(a) and f(b) and width (b−a). The error depends on how curved the function is over [a, b]: the more f deviates from a straight line (larger |f''|), the worse the approximation. This geometric clarity is one reason the trapezoidal rule is a natural starting point for teaching numerical integration."

- question: "Newton-Cotes rules use equally-spaced nodes because of their construction from Lagrange interpolation. Explain why this equal spacing becomes a serious problem for high-order rules, and how this motivates Gaussian quadrature."
  type: short-answer
  answer: "Equal spacing is natural for Newton-Cotes because the weights are derived by integrating Lagrange basis polynomials, and uniform spacing simplifies that computation. But for high-degree Lagrange interpolation on equally-spaced points, Runge's phenomenon causes the interpolating polynomial to oscillate wildly near the endpoints, even for smooth functions — so integrating this polynomial gives a poor approximation. Gaussian quadrature avoids this by choosing node positions (not equally spaced) to maximize the degree of precision for a given number of nodes: n Gaussian nodes exactly integrate polynomials of degree up to 2n−1, far better than the degree n−1 or n achieved by n Newton-Cotes nodes. The key trade-off is that Gaussian nodes must be recomputed for each interval and don't allow reuse across a composite rule as easily."
  explanation: "The Chebyshev nodes (clustering toward the endpoints) are another response to Runge's phenomenon: they are equally spaced in angle on the unit circle, which distributes interpolation error more evenly. But for integration, Gaussian quadrature with optimally placed nodes is usually preferred for smooth functions."
```

## Explainer

From **Lagrange polynomial interpolation**, you know how to construct the unique polynomial of degree ≤ n that passes through n+1 given points. Newton-Cotes quadrature takes that idea and turns it into a method for numerical integration: replace the integrand f(x) with its interpolating polynomial P(x), then integrate P(x) exactly. The result is a weighted sum of function values — a **quadrature rule**.

Here is the construction explicitly. On the interval [a, b], place n+1 equally-spaced nodes x₀ = a, x₁, …, xₙ = b (for closed rules). Construct the Lagrange interpolating polynomial P(x) = Σ f(xᵢ) Lᵢ(x), where Lᵢ is the i-th Lagrange basis polynomial. Then ∫ₐᵇ f(x) dx ≈ ∫ₐᵇ P(x) dx = Σ wᵢ f(xᵢ), where the weights wᵢ = ∫ₐᵇ Lᵢ(x) dx are determined entirely by the node positions, not by f. For two nodes (n = 1), this gives the **trapezoidal rule**: ∫ₐᵇ f(x) dx ≈ (b−a)/2 · [f(a) + f(b)], which is just the area of the trapezoid under the linear interpolant. For three equally-spaced nodes (n = 2), you get **Simpson's rule**: ∫ₐᵇ f(x) dx ≈ (b−a)/6 · [f(a) + 4f((a+b)/2) + f(b)]. Simpson's rule is exact for polynomials of degree ≤ 3, even though it only uses a degree-2 interpolant — this bonus accuracy (called a **degree of precision** boost) arises because the error term for even-order rules contains a factor that integrates to zero by symmetry.

The error analysis connects to how well a polynomial of degree n approximates f on [a, b]. For the trapezoidal rule, the error is O(h³ f″) where h = b − a; for Simpson's, O(h⁵ f⁽⁴⁾). Higher-order Newton-Cotes rules (Boole's rule at n = 4, etc.) have formally smaller errors, but they suffer from a practical problem: for large n, Lagrange interpolation at equally-spaced nodes is highly unstable due to **Runge's phenomenon** — the interpolating polynomial oscillates wildly near the endpoints. This is why in practice, composite rules (applying the trapezoidal or Simpson's rule on many small subintervals rather than one large one) are preferred over high-order rules on the whole interval. Newton-Cotes is therefore the foundation, and understanding why higher-order rules fail motivates the more sophisticated methods (Gaussian quadrature, adaptive integration) that follow.
