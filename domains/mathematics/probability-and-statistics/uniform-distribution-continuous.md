---
id: uniform-distribution-continuous
title: Continuous Uniform Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: continuous-random-variables
  type: hard
builds-toward:
- exponential-distribution
tags:
- uniform
- continuous-distribution
stage: formal-systems
status: draft
---

# Continuous Uniform Distribution

## Core Idea
The continuous uniform distribution on [a, b] has constant PDF f(x) = 1/(b-a) for a ≤ x ≤ b, and zero elsewhere. Every subinterval of equal length has equal probability. Mean is (a+b)/2 and variance is (b-a)²/12. Uniform distributions model scenarios where outcomes are equally likely throughout an interval, such as random selection from a continuous range.

## How It's Best Learned
Visualize the constant PDF. Compute probabilities as areas of rectangles. Compare variance across different interval widths.

## Common Misconceptions
Confusing PDF value (1/(b-a)) with probability for a single point. Misremembering the variance formula.

## Explainer

The **continuous uniform distribution** is the simplest continuous probability distribution: it assigns equal probability density to every point in an interval [a, b] and zero probability outside it. You already know from continuous random variables that a PDF describes density, not probability at a point, and that probability is computed as the area under the curve. For the uniform distribution, the PDF is f(x) = 1/(b − a) on [a, b] — a flat horizontal line. Every subinterval of equal length gets equal probability, regardless of where it sits within [a, b].

Computing probabilities is especially clean because they reduce to rectangle areas. The probability that X falls in [c, d] ⊆ [a, b] is simply (d − c)/(b − a) — the length of the sub-interval divided by the total length. This is the continuous analogue of classical probability ("favorable outcomes over total outcomes"), applied to lengths rather than counts.

The **mean** is (a + b)/2, the midpoint of the interval — intuitive by symmetry. The **variance** is (b − a)²/12, which grows with the square of the interval's width. A wider interval means outcomes are more spread out, so variance increases. The factor of 12 comes from evaluating the integral ∫ (x − μ)² · (1/(b − a)) dx; computing it yourself once cements the mechanics.

The uniform distribution plays a foundational role beyond its direct applications. The **probability integral transform** states that if X has any continuous CDF F, then F(X) ~ Uniform(0, 1). This means a uniform random variable is the "raw material" from which any continuous random variable can be constructed by applying an inverse CDF. Computers generate Uniform(0, 1) samples first, then transform them to whatever target distribution is needed — making the uniform distribution the invisible engine behind virtually all Monte Carlo simulation and statistical sampling.
