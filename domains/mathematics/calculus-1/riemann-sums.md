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

## Explainer

The definite integral asks: what is the total signed area between the curve y = f(x) and the x-axis from x = a to x = b? Riemann sums are the constructive answer. The idea is ancient and intuitive: divide the region into thin vertical **rectangles**, compute each rectangle's area (base × height), and sum them. Rectangle areas are elementary; the only question is how many rectangles to use and how to pick the height of each one.

For a partition of [a, b] into n equal subintervals, each rectangle has width **Δx = (b − a)/n**. The height comes from evaluating f at a **sample point** x_i* in the i-th subinterval. The three standard choices are the **left endpoint** (x_i* = a + (i−1)Δx), the **right endpoint** (x_i* = a + iΔx), and the **midpoint**. Each gives a different numerical sum — a different approximation. For a function increasing on [a, b], the left-endpoint sum always undershoots (the left edge of each rectangle is shorter than the curve within it) and the right-endpoint sum always overshoots. The midpoint rule typically achieves better accuracy for the same n.

To see the computation concretely: approximate ∫₀² x² dx using n = 4 right-endpoint rectangles. Δx = 2/4 = 0.5, so the right endpoints are x = 0.5, 1.0, 1.5, 2.0. The four heights are f(0.5) = 0.25, f(1.0) = 1.0, f(1.5) = 2.25, f(2.0) = 4.0. The Riemann sum is 0.5 × (0.25 + 1.0 + 2.25 + 4.0) = 3.75. The exact integral is 8/3 ≈ 2.667, so the right-endpoint sum overshoots — consistent with x² being an increasing function on [0, 2]. Doubling n to 8 gives a sum closer to 2.667; as n → ∞ the sum converges to the exact value.

The profound fact is that as n → ∞ and Δx → 0, all three versions — left, right, midpoint, or any valid sample-point choice — converge to the same limit. This limit is the **definite integral**: ∫_a^b f(x) dx = lim_{n→∞} Σᵢ f(x_i*) Δx. Riemann sums thus serve two roles: a practical approximation method when n is finite, and the rigorous definition of what an integral is when the limit is taken. The transition from finite approximation to exact limit is the conceptual leap at the heart of integral calculus — it's what makes the integral more than just "the area under the curve" and turns it into a precisely defined mathematical object.
