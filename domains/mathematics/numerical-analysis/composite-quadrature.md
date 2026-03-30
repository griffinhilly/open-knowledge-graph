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
stage: advanced
status: validated
---

# Composite Quadrature Rules

## Core Idea
Composite quadrature divides the integration interval into n subintervals and applies a simple rule (e.g., Simpson's rule) to each, summing the results. This approach achieves high accuracy with far fewer function evaluations than using high-order rules on the full interval. Composite rules enable adaptive refinement, with finer divisions in regions where f varies rapidly.

## How It's Best Learned
Compute integrals using composite trapezoidal and Simpson's rules with increasing numbers of subintervals, observing convergence rates and comparing to exact values.

## Common Misconceptions
- Thinking composite rules are less efficient than single high-order rules; composites often win in accuracy-per-evaluation.
- Assuming uniform subinterval spacing is optimal; adaptive methods concentrate evaluations where needed.

## Questions

```yaml
- question: "A function has a sharp spike in a small region and is nearly flat everywhere else. To achieve high accuracy with the fewest function evaluations, which approach is best?"
  type: multiple-choice
  options:
    - "Apply a very high-degree polynomial rule to the entire interval"
    - "Use composite Simpson's rule with uniform subinterval spacing"
    - "Use adaptive composite quadrature that refines subintervals near the spike"
    - "Use the basic trapezoidal rule with a large fixed number of uniform panels"
  answer: 2
  explanation: "Adaptive composite quadrature concentrates evaluations where the function varies rapidly and uses coarser panels where it is smooth. A uniform mesh wastes evaluations on the flat regions. A single high-degree polynomial over the whole interval fits the spike poorly (Runge's phenomenon is a related failure). The key insight is that uniform spacing is optimal only for uniformly well-behaved functions; adapting the mesh to the function's local behavior delivers the same accuracy with far fewer evaluations."

- question: "You apply composite Simpson's rule to an integral, then double the number of subintervals. By approximately what factor does the error decrease?"
  type: multiple-choice
  options:
    - "2"
    - "4"
    - "8"
    - "16"
  answer: 3
  explanation: "Composite Simpson's rule has error proportional to h⁴(b−a), where h is the subinterval width. Doubling n halves h, so the error scales as (h/2)⁴ = h⁴/16 — a factor of 16 reduction. This is why composite rules achieve high accuracy quickly: each doubling of the number of panels produces a large error reduction. Composite trapezoidal rule achieves only a factor of 4 per doubling (error ∝ h²). This rapid convergence is the main reason composite rules dominate practical integration."

- question: "Using a single high-order polynomial rule over an entire interval is generally more accurate than a composite rule with the same total number of function evaluations."
  type: true-false
  answer: false
  explanation: "This is a common misconception. For smooth, well-behaved functions, high-order rules can be very accurate. But for functions with local features, rapid variation, or near-singularities, high-degree polynomials over large intervals fit poorly — the Runge phenomenon is an extreme example. Composite rules use low-order formulas on small panels, so local behavior is well-captured everywhere. In practice, composite rules often win on accuracy-per-evaluation precisely because real-world integrands are rarely uniform in their smoothness."

- question: "Doubling the number of subintervals in composite Simpson's rule reduces the error by approximately a factor of 16."
  type: true-false
  answer: true
  explanation: "Composite Simpson's rule has global error O(h⁴), where h = (b−a)/n is the subinterval width. Doubling n halves h, so error scales as h⁴ → (h/2)⁴ = h⁴/16. This fourth-order convergence is what makes Simpson's rule far preferable to the trapezoidal rule (which has O(h²) error, giving only a factor of 4 improvement per doubling). The rapid convergence rate is the core reason to prefer composite Simpson's rule for smooth integrands."

- question: "Why do composite quadrature rules typically outperform single high-order polynomial rules for integrands with local features or rapid variation? What is the structural reason for this advantage?"
  type: short-answer
  answer: "Composite rules keep the polynomial degree low and reduce the panel width h, concentrating accuracy where it is needed. Error in a composite rule depends on h raised to a power, so smaller panels dramatically reduce local errors. A single high-order polynomial over the full interval must simultaneously represent all the function's variation — a task it fails when the function has sharp local features, since high-degree polynomial fits tend to oscillate (Runge's phenomenon). Composite rules sidestep this by never asking any single panel to represent more than a locally smooth piece of the function."
  explanation: "The structural insight is that dividing the domain trades polynomial degree for panel width, and panel width enters the error formula at a high power. Adaptive methods take this further: they automatically apply more panels (smaller h) where the integrand is difficult and fewer where it is easy, so the error budget is spent efficiently. This is why modern numerical integration libraries use adaptive composite schemes rather than fixed high-order rules."
```

## Explainer

From your study of **Newton-Cotes formulas**, you know that rules like the trapezoidal rule and Simpson's rule approximate ∫ₐᵇ f(x) dx by evaluating f at a small number of points and fitting a polynomial through them. These work well when f behaves nicely over [a, b], but for functions that vary rapidly or have sharp features, a single polynomial over the whole interval fits poorly, leading to large errors. **Composite quadrature** solves this by dividing the interval into n subintervals, applying the simple rule to each subinterval, and summing the results. The accuracy comes not from a more sophisticated rule but from using many small panels.

To see why this helps dramatically, consider the error analysis. The basic trapezoidal rule on [a, b] has error proportional to (b − a)³ times the second derivative of f. The **composite trapezoidal rule** with n equal subintervals of width h = (b − a)/n has error proportional to h²(b − a), or equivalently (b − a)³/n². Doubling n reduces the error by a factor of 4. Similarly, the **composite Simpson's rule** — applying Simpson's rule to each pair of adjacent subintervals — has error proportional to h⁴(b − a), so doubling n reduces error by a factor of 16. This rapid convergence is why composite rules dominate practical numerical integration.

The practical recipe for composite Simpson's rule is particularly clean. With n even subintervals and nodes x₀, x₁, ..., xₙ, the formula is (h/3)[f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ... + 4f(xₙ₋₁) + f(xₙ)], where the coefficients alternate 4-2-4-2 in the interior. You can derive this by noticing that each pair of subintervals contributes a standard Simpson's-rule panel, and the shared endpoints count twice — except the alternating pattern handles it automatically.

The most powerful extension of composite quadrature is **adaptive integration**: instead of using uniform subintervals, the method estimates the local error on each panel and automatically refines the mesh where f is difficult (oscillatory, rapidly varying, nearly singular). The algorithm uses a composite rule at two refinement levels, compares the results as an error estimate, and subdivides panels that fail a tolerance test. This is how modern numerical integration libraries (like `scipy.integrate.quad`) work under the hood — they are sophisticated adaptive composite schemes. The key insight is that uniform spacing wastes function evaluations on easy regions; adapting the mesh gives you high accuracy with far fewer evaluations than any fixed-mesh approach could achieve.
