---
id: composite-quadrature-rules
title: Composite Quadrature Rules
domain: mathematics
course: numerical-analysis
prerequisites:
- id: newton-cotes-quadrature
  type: hard
builds-toward:
- romberg-integration
tags:
- composite-rules
- piecewise-integration
- accuracy
stage: formal-systems
status: draft
---

# Composite Quadrature Rules

## Core Idea
Composite quadrature rules improve accuracy by dividing the integration interval into many subintervals and applying a basic Newton-Cotes rule to each piece. The total error is the sum of subinterval errors, giving O(h^p) convergence where h is the subinterval width. This approach is much more practical than single Newton-Cotes rules with many nodes.

## Questions

```yaml
- question: "You are numerically integrating a smooth function using the composite Simpson's rule. If you halve the subinterval width h (doubling the number of subintervals), by approximately what factor does the global error decrease?"
  type: multiple-choice
  options:
    - "2 — error halves as h halves"
    - "4 — error is O(h²), so halving h cuts error by 4"
    - "8 — because Simpson's rule uses 3 points per subinterval"
    - "16 — error is O(h⁴), so halving h cuts error by 16"
  answer: 3
  explanation: "Composite Simpson's rule has global error O(h⁴) — specifically -(b-a)h⁴f⁽⁴⁾(ξ)/180. When h → h/2, h⁴ → h⁴/16, so the error decreases by a factor of 16. The composite trapezoidal rule, by contrast, has O(h²) error, which decreases by only 4 when h is halved. Knowing the convergence order tells you exactly how much mesh refinement buys you."

- question: "A numerical analyst proposes computing ∫₀¹ f(x)dx using a single Newton-Cotes formula with 50 equally spaced nodes (degree-49 polynomial interpolation). A colleague suggests using composite Simpson's rule with 50 nodes instead. Who is likely right, and why?"
  type: multiple-choice
  options:
    - "The first analyst — more nodes in a single formula always gives a higher-degree approximation with lower error"
    - "The colleague — composite rules avoid Runge's phenomenon, which causes high-degree interpolation at equally spaced nodes to oscillate wildly near endpoints"
    - "They are equivalent — both use the same function evaluations, so accuracy is identical"
    - "The first analyst — composite rules introduce extra error at subinterval boundaries that outweighs any benefit"
  answer: 1
  explanation: "High-degree polynomial interpolation over a single interval at equally spaced nodes suffers from Runge's phenomenon: oscillations near the interval endpoints that grow worse as degree increases, even for smooth functions. Composite low-degree rules avoid this entirely because each subinterval only needs to fit a low-degree polynomial over a small region, where it is an excellent local approximation. The same number of function evaluations produces much more reliable results with the composite approach — which is why composite rules are the standard in practice."

- question: "For the composite trapezoidal rule, if you increase the number of subintervals from n to 4n (making h four times smaller), the global error is reduced by a factor of approximately 16."
  type: true-false
  answer: true
  explanation: "The composite trapezoidal rule has global error O(h²) — specifically -(b-a)h²f''(ξ)/12. If h is reduced by a factor of 4 (h → h/4), then h² → h²/16, and the error decreases by a factor of 16. This quadratic convergence is the defining feature of the composite trapezoidal rule: every factor-of-2 reduction in h yields a factor-of-4 reduction in error."

- question: "Composite quadrature rules are most beneficial when the integrand is non-smooth or has discontinuities. For smooth functions, a single high-degree Newton-Cotes formula using the same nodes is preferable."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Even for perfectly smooth functions, composite low-degree rules typically outperform single high-degree Newton-Cotes formulas because of Runge's phenomenon: high-degree polynomial interpolation at equally spaced points develops large oscillations near the interval endpoints, causing large errors even when f is smooth. Composite rules are the standard practical approach for smooth and non-smooth functions alike, because the error on each small subinterval is reliably controlled and the global error converges predictably."

- question: "Explain why composite quadrature rules are preferred over single high-degree Newton-Cotes formulas, even when both use the same number of function evaluations."
  type: short-answer
  answer: "Composite rules divide the interval into many subintervals and apply a low-degree formula on each piece. Each small subinterval sees only a local portion of f, where a low-degree polynomial is an excellent approximation, and the total error is O(h^p) — shrinking to zero as h → 0. A single high-degree Newton-Cotes formula with the same nodes uses degree-n polynomial interpolation over the entire interval at equally spaced points, which suffers from Runge's phenomenon: the interpolating polynomial oscillates wildly near the endpoints as n grows, producing large errors even for smooth integrands. Composite rules make the approximation problem local and tractable; single high-degree rules make it global and unstable."
  explanation: "The key insight is that error in Newton-Cotes rules is controlled by high derivatives of f over the whole interval — a global quantity that can be large. Composite rules localize this: each subinterval bounds high derivatives over a small region, which is much smaller. The price is more function evaluations, but each evaluation is cheap and the convergence is reliable and predictable."
```

## Explainer

From Newton-Cotes quadrature you know how to approximate ∫f dx over an interval by a weighted sum of function values at equally spaced nodes. The trapezoidal rule uses two endpoints; Simpson's rule adds a midpoint. The problem is that these basic rules have limited accuracy — the error depends on high derivatives of f over the whole interval, which can be large. The remedy is not to use more nodes in a single high-degree formula, but to **divide and conquer**: split [a, b] into n subintervals of width h = (b-a)/n and apply the simple rule on each piece. This is the composite approach.

For the **composite trapezoidal rule**, each subinterval [xᵢ, xᵢ₊₁] contributes (h/2)(f(xᵢ) + f(xᵢ₊₁)). Summing these, interior points appear twice (as right endpoint of one interval and left endpoint of the next), giving the familiar formula h[f(x₀)/2 + f(x₁) + f(x₂) + ... + f(x_{n-1}) + f(xₙ)/2]. The global error for the composite trapezoidal rule is O(h²): halving h reduces error by a factor of four. For **composite Simpson's rule**, each pair of subintervals uses three points with the (h/6)(f_left + 4f_mid + f_right) weight, and the global error is O(h⁴) — halving h reduces error by sixteen. The higher the order of the base rule, the faster the error decays with mesh refinement.

The reason composite rules outperform single high-degree Newton-Cotes rules is stability. High-degree polynomial interpolation over a single interval suffers from **Runge's phenomenon**: oscillations near the endpoints can make the approximation worse as you add nodes. Composite low-degree rules avoid this entirely. Each local piece only sees a small portion of f, over which a low-degree polynomial is an excellent approximation. The price is more function evaluations, but each evaluation is cheap.

Error analysis connects directly to derivatives. The composite trapezoidal error is -(b-a)h²f''(ξ)/12 for some ξ in (a, b). If you halve h, h² drops by four, so the error drops by four. This is the **order of convergence** — the exponent of h in the error formula. Composite Simpson's rule has error -(b-a)h⁴f⁽⁴⁾(ξ)/180, so it converges at order 4. In practice, you choose the rule based on how smooth f is: for very smooth functions, high-order rules with moderate n are efficient; for rough or sampled data, lower-order rules with fine grids are safer.
