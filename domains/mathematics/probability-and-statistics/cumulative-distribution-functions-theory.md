---
id: cumulative-distribution-functions-theory
title: Cumulative Distribution Functions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-mass-functions-theory
  type: soft
- id: probability-density-functions-theory
  type: soft
builds-toward:
- standard-normal-and-z-scores
tags:
- cdf
stage: formal-systems
status: draft
---

# Cumulative Distribution Functions

## Core Idea
The cumulative distribution function F(x) = P(X ≤ x) gives the probability that a random variable takes a value at or below x. Every CDF is non-decreasing, right-continuous, with F(−∞) = 0 and F(∞) = 1. For continuous random variables, the PDF is the derivative of the CDF: f(x) = F'(x). For discrete variables, the CDF is a step function with jumps at each possible value. CDFs provide a unified framework for computing tail probabilities, quantiles, and comparing distributions regardless of whether the variable is discrete, continuous, or mixed.

## How It's Best Learned
Plot CDFs for familiar distributions (uniform, normal, geometric) side by side. Practice reading probabilities as vertical differences: P(a < X ≤ b) = F(b) − F(a). This graphical approach builds stronger intuition than formulas alone.

## Common Misconceptions
Students often confuse F(x) with f(x), treating the CDF as a density. The CDF gives cumulative probability, not probability at a point. Also, P(X = x) is not always F(x) − F(x⁻) for continuous variables—it is zero.

## Questions

```yaml
- question: "For a continuous random variable X with CDF F(x), what is P(2 < X ≤ 5)?"
  type: multiple-choice
  options:
    - "F(5) × F(2)"
    - "F(5) − F(2)"
    - "f(5) − f(2), where f is the probability density function"
    - "F(5) + F(2)"
  answer: 1
  explanation: "P(a < X ≤ b) = F(b) − F(a) for any random variable. The CDF gives cumulative probability up to a point, so the probability of the interval (a, b] is the difference of two CDF values. This formula works for both discrete and continuous variables. Option C is wrong because the PDF value at a point is not a probability — it is a density, and subtracting densities gives nothing meaningful."

- question: "The PDF of a continuous random variable X at x = 3 is f(3) = 0.4. What is P(X = 3)?"
  type: multiple-choice
  options:
    - "0.4, since f(3) is the probability at x = 3"
    - "0, because for any continuous random variable, the probability at any exact point is zero"
    - "F(3) − F(3⁻) = 0.4, since the CDF jumps by the density value"
    - "Cannot be determined without integrating the PDF"
  answer: 1
  explanation: "For a continuous random variable, P(X = x) = 0 for every individual point. Probability is area under the PDF; a single point has zero width, so zero area, regardless of how large f(x) is. The value f(3) = 0.4 means that near x = 3, probability accumulates at rate 0.4 per unit — f(x)·Δx approximates P(3 < X ≤ 3 + Δx). CDF jumps of nonzero size at a point occur only for discrete distributions."

- question: "For any random variable X — whether discrete, continuous, or mixed — P(a < X ≤ b) = F(b) − F(a)."
  type: true-false
  answer: true
  explanation: "This is the fundamental use of the CDF, and it holds universally. The CDF F(x) = P(X ≤ x) accumulates probability up to x; the interval probability is the difference of two such cumulative values. This unifying property is precisely why the CDF is more broadly useful than the PMF or PDF, which apply only to discrete or continuous cases respectively."

- question: "The value of the CDF at x = 3, written F(3), can be read directly off the probability density function as the height f(3)."
  type: true-false
  answer: false
  explanation: "F(3) is not the height of the PDF at 3 — it is the area under the PDF from −∞ to 3, i.e., F(3) = ∫₋∞³ f(t) dt. The height of the PDF gives the rate of probability accumulation, not the accumulated probability itself. Confusing height with area is the core misconception between f(x) and F(x)."

- question: "Explain why P(X = x) = 0 for a continuous random variable, even when the PDF value f(x) is large and positive at that point."
  type: short-answer
  answer: "For a continuous random variable, probability equals area under the PDF. A single point has zero width, so its area is zero: P(X = x) = ∫ₓˣ f(t) dt = 0. The value f(x) is a probability density — not a probability — and represents the rate at which probability accumulates near x. The probability of an interval [x, x + Δx] is approximately f(x)·Δx for small Δx, but the probability of the exact point x itself is zero regardless of how large f(x) is."
  explanation: "This is one of the most important conceptual shifts from discrete to continuous probability. In the discrete case, P(X = x) can be directly read from the PMF. In the continuous case, individual points have zero probability, and only intervals have positive probability. The PDF encodes local probability density, not probability itself."
```

