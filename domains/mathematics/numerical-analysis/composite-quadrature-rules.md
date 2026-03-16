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
stage: advanced
status: draft
---

# Composite Quadrature Rules

## Core Idea
Composite quadrature rules improve accuracy by dividing the integration interval into many subintervals and applying a basic Newton-Cotes rule to each piece. The total error is the sum of subinterval errors, giving O(h^p) convergence where h is the subinterval width. This approach is much more practical than single Newton-Cotes rules with many nodes.

## Explainer

From Newton-Cotes quadrature you know how to approximate ∫f dx over an interval by a weighted sum of function values at equally spaced nodes. The trapezoidal rule uses two endpoints; Simpson's rule adds a midpoint. The problem is that these basic rules have limited accuracy — the error depends on high derivatives of f over the whole interval, which can be large. The remedy is not to use more nodes in a single high-degree formula, but to **divide and conquer**: split [a, b] into n subintervals of width h = (b-a)/n and apply the simple rule on each piece. This is the composite approach.

For the **composite trapezoidal rule**, each subinterval [xᵢ, xᵢ₊₁] contributes (h/2)(f(xᵢ) + f(xᵢ₊₁)). Summing these, interior points appear twice (as right endpoint of one interval and left endpoint of the next), giving the familiar formula h[f(x₀)/2 + f(x₁) + f(x₂) + ... + f(x_{n-1}) + f(xₙ)/2]. The global error for the composite trapezoidal rule is O(h²): halving h reduces error by a factor of four. For **composite Simpson's rule**, each pair of subintervals uses three points with the (h/6)(f_left + 4f_mid + f_right) weight, and the global error is O(h⁴) — halving h reduces error by sixteen. The higher the order of the base rule, the faster the error decays with mesh refinement.

The reason composite rules outperform single high-degree Newton-Cotes rules is stability. High-degree polynomial interpolation over a single interval suffers from **Runge's phenomenon**: oscillations near the endpoints can make the approximation worse as you add nodes. Composite low-degree rules avoid this entirely. Each local piece only sees a small portion of f, over which a low-degree polynomial is an excellent approximation. The price is more function evaluations, but each evaluation is cheap.

Error analysis connects directly to derivatives. The composite trapezoidal error is -(b-a)h²f''(ξ)/12 for some ξ in (a, b). If you halve h, h² drops by four, so the error drops by four. This is the **order of convergence** — the exponent of h in the error formula. Composite Simpson's rule has error -(b-a)h⁴f⁽⁴⁾(ξ)/180, so it converges at order 4. In practice, you choose the rule based on how smooth f is: for very smooth functions, high-order rules with moderate n are efficient; for rough or sampled data, lower-order rules with fine grids are safer.
