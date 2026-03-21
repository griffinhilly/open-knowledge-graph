---
id: riemann-sums
title: Riemann Sums
domain: mathematics
course: calculus-1
prerequisites:
- id: sequences-and-series-review
  type: soft
- id: basic-integration-rules
  type: soft
builds-toward:
- definite-integral-definition
tags:
- integration
- Riemann-sums
- area
- approximation
stage: formal-systems
status: validated
---
# Riemann Sums

## Core Idea
A Riemann sum approximates the area under a curve by dividing the region into n rectangles and summing their areas. The width of each rectangle is Delta_x = (b - a)/n, and the height is f(x_i*) for some sample point x_i* in each subinterval (left endpoint, right endpoint, or midpoint). As n increases, the approximation improves. The limit of the Riemann sum as n approaches infinity defines the definite integral.

## How It's Best Learned
Compute Riemann sums by hand for small n (3, 4, 5 rectangles) to see the approximation improve. Visualize the rectangles on a graph. Compare left, right, and midpoint sums. Observe that for increasing functions, left sums underestimate and right sums overestimate.

## Common Misconceptions
- Confusing the number of rectangles n with the width Delta_x.
- Not understanding that Riemann sums are approximations, not exact values (until the limit).
- Believing that left/right/midpoint sums always give different limits (they all converge to the same integral).

## Questions

```yaml
- question: "A student computes both a left-endpoint and a right-endpoint Riemann sum for the same integral using n = 100 rectangles. She concludes that these two approximations will converge to different values as n → ∞. What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "She is correct — left and right sums always converge to different limits"
    - "Both sums converge to the same limit — the definite integral — regardless of which endpoint rule is used"
    - "Only the midpoint sum converges to the definite integral; endpoint rules do not converge"
    - "The sums converge to different limits only for non-monotone functions"
  answer: 1
  explanation: "The key insight is that all valid Riemann sum choices — left endpoint, right endpoint, midpoint, or any sample point — converge to the same limit as n → ∞, which is the definite integral. The sums differ for finite n (and the direction of the error depends on monotonicity), but the limit is unique. This is what makes the definite integral well-defined."

- question: "You approximate ∫₀² x² dx using n = 4 right-endpoint rectangles. The right endpoints are x = 0.5, 1.0, 1.5, 2.0 and Δx = 0.5. What is the Riemann sum, and is it an overestimate or underestimate?"
  type: multiple-choice
  options:
    - "2.67 — an exact value since x² is a polynomial"
    - "3.75 — an overestimate, because x² is increasing on [0, 2] and right endpoints sample the taller side of each rectangle"
    - "2.25 — an underestimate, because right-endpoint sums always undershoot"
    - "3.75 — but whether it over- or underestimates depends on n, not the function"
  answer: 1
  explanation: "f(0.5) + f(1.0) + f(1.5) + f(2.0) = 0.25 + 1.0 + 2.25 + 4.0 = 7.5; multiply by Δx = 0.5 to get 3.75. Since x² is strictly increasing on [0, 2], each rectangle's right endpoint is the maximum of f on that subinterval, so the rectangle overshoots the curve — giving an overestimate. The exact integral is 8/3 ≈ 2.67."

- question: "For an increasing function on [a, b], the left-endpoint Riemann sum underestimates the definite integral for any finite n."
  type: true-false
  answer: true
  explanation: "For an increasing function, f is smallest at the left endpoint of each subinterval. The left-endpoint sum uses this minimum as the rectangle height, so every rectangle falls below the curve — meaning the sum underestimates the area. Symmetrically, the right-endpoint sum overestimates. These inequalities hold for any finite n; both converge to the integral as n → ∞."

- question: "A Riemann sum with a very large number of rectangles (say, n = 10,000) is equal to the definite integral."
  type: true-false
  answer: false
  explanation: "A Riemann sum, no matter how large n is, is always an approximation — it equals the definite integral only in the limit as n → ∞. The definite integral is defined as this limit, not as any finite sum. For n = 10,000 the error is tiny but nonzero. This distinction is precisely the conceptual leap from finite approximation to the exact integral."

- question: "What is the definite integral, precisely defined in terms of Riemann sums? Why must we take a limit rather than simply use a very large n?"
  type: short-answer
  answer: "The definite integral ∫_a^b f(x) dx is defined as the limit of the Riemann sum Σᵢ f(xᵢ*) Δx as n → ∞ (and Δx → 0). No finite Riemann sum equals the integral exactly; the integral is the value that all valid Riemann sums approach. Taking the limit is necessary because rectangles can only approximate curved regions — no matter how thin, they have flat tops and the curve is (generally) curved. The limit captures the precise area by making the approximation error arbitrarily small."
  explanation: "This distinction matters because it makes the integral a precisely defined mathematical object, not just an approximation. In practice, numerical integration uses large-n Riemann sums as approximations. In theory, the integral is the limit. Understanding this duality — finite approximation vs. exact limit — is the foundational insight of integral calculus."
```

## Explainer

The definite integral asks: what is the total signed area between the curve y = f(x) and the x-axis from x = a to x = b? Riemann sums are the constructive answer. The idea is ancient and intuitive: divide the region into thin vertical **rectangles**, compute each rectangle's area (base × height), and sum them. Rectangle areas are elementary; the only question is how many rectangles to use and how to pick the height of each one.

For a partition of [a, b] into n equal subintervals, each rectangle has width **Δx = (b − a)/n**. The height comes from evaluating f at a **sample point** x_i* in the i-th subinterval. The three standard choices are the **left endpoint** (x_i* = a + (i−1)Δx), the **right endpoint** (x_i* = a + iΔx), and the **midpoint**. Each gives a different numerical sum — a different approximation. For a function increasing on [a, b], the left-endpoint sum always undershoots (the left edge of each rectangle is shorter than the curve within it) and the right-endpoint sum always overshoots. The midpoint rule typically achieves better accuracy for the same n.

To see the computation concretely: approximate ∫₀² x² dx using n = 4 right-endpoint rectangles. Δx = 2/4 = 0.5, so the right endpoints are x = 0.5, 1.0, 1.5, 2.0. The four heights are f(0.5) = 0.25, f(1.0) = 1.0, f(1.5) = 2.25, f(2.0) = 4.0. The Riemann sum is 0.5 × (0.25 + 1.0 + 2.25 + 4.0) = 3.75. The exact integral is 8/3 ≈ 2.667, so the right-endpoint sum overshoots — consistent with x² being an increasing function on [0, 2]. Doubling n to 8 gives a sum closer to 2.667; as n → ∞ the sum converges to the exact value.

The profound fact is that as n → ∞ and Δx → 0, all three versions — left, right, midpoint, or any valid sample-point choice — converge to the same limit. This limit is the **definite integral**: ∫_a^b f(x) dx = lim_{n→∞} Σᵢ f(x_i*) Δx. Riemann sums thus serve two roles: a practical approximation method when n is finite, and the rigorous definition of what an integral is when the limit is taken. The transition from finite approximation to exact limit is the conceptual leap at the heart of integral calculus — it's what makes the integral more than just "the area under the curve" and turns it into a precisely defined mathematical object.
