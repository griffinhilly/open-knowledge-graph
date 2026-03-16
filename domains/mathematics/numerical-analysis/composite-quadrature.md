---
id: composite-quadrature
title: Composite Quadrature Rules
domain: mathematics
course: numerical-analysis
prerequisites:
- id: newton-cotes-formulas
  type: hard
builds-toward:
- gaussian-quadrature
- romberg-integration
tags:
- composite-quadrature
- integration
- error-control
stage: abstract-reasoning
status: draft
---

# Composite Quadrature Rules

## Core Idea
Composite quadrature divides the integration interval into n subintervals and applies a simple rule (e.g., Simpson's rule) to each, summing the results. This approach achieves high accuracy with far fewer function evaluations than using high-order rules on the full interval. Composite rules enable adaptive refinement, with finer divisions in regions where f varies rapidly.

## How It's Best Learned
Compute integrals using composite trapezoidal and Simpson's rules with increasing numbers of subintervals, observing convergence rates and comparing to exact values.

## Common Misconceptions
- Thinking composite rules are less efficient than single high-order rules; composites often win in accuracy-per-evaluation.
- Assuming uniform subinterval spacing is optimal; adaptive methods concentrate evaluations where needed.

## Explainer

From your study of **Newton-Cotes formulas**, you know that rules like the trapezoidal rule and Simpson's rule approximate ∫ₐᵇ f(x) dx by evaluating f at a small number of points and fitting a polynomial through them. These work well when f behaves nicely over [a, b], but for functions that vary rapidly or have sharp features, a single polynomial over the whole interval fits poorly, leading to large errors. **Composite quadrature** solves this by dividing the interval into n subintervals, applying the simple rule to each subinterval, and summing the results. The accuracy comes not from a more sophisticated rule but from using many small panels.

To see why this helps dramatically, consider the error analysis. The basic trapezoidal rule on [a, b] has error proportional to (b − a)³ times the second derivative of f. The **composite trapezoidal rule** with n equal subintervals of width h = (b − a)/n has error proportional to h²(b − a), or equivalently (b − a)³/n². Doubling n reduces the error by a factor of 4. Similarly, the **composite Simpson's rule** — applying Simpson's rule to each pair of adjacent subintervals — has error proportional to h⁴(b − a), so doubling n reduces error by a factor of 16. This rapid convergence is why composite rules dominate practical numerical integration.

The practical recipe for composite Simpson's rule is particularly clean. With n even subintervals and nodes x₀, x₁, ..., xₙ, the formula is (h/3)[f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ... + 4f(xₙ₋₁) + f(xₙ)], where the coefficients alternate 4-2-4-2 in the interior. You can derive this by noticing that each pair of subintervals contributes a standard Simpson's-rule panel, and the shared endpoints count twice — except the alternating pattern handles it automatically.

The most powerful extension of composite quadrature is **adaptive integration**: instead of using uniform subintervals, the method estimates the local error on each panel and automatically refines the mesh where f is difficult (oscillatory, rapidly varying, nearly singular). The algorithm uses a composite rule at two refinement levels, compares the results as an error estimate, and subdivides panels that fail a tolerance test. This is how modern numerical integration libraries (like `scipy.integrate.quad`) work under the hood — they are sophisticated adaptive composite schemes. The key insight is that uniform spacing wastes function evaluations on easy regions; adapting the mesh gives you high accuracy with far fewer evaluations than any fixed-mesh approach could achieve.
