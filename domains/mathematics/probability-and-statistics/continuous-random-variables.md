---
id: continuous-random-variables
title: Continuous Random Variables
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-intro
  type: hard
- id: expected-value-and-variance
  type: soft
builds-toward:
- uniform-distribution-continuous
- exponential-distribution
- normal-distribution
tags:
- continuous
- probability-density-function
- pdf
- cdf
stage: formal-systems
status: draft
---

# Continuous Random Variables

## Core Idea
A continuous random variable can take any value in an interval. Its distribution is characterized by a probability density function (PDF) f(x) where P(a ≤ X ≤ b) = ∫ₐᵇ f(x)dx. The PDF must be non-negative and integrate to 1. The cumulative distribution function (CDF) F(x) = P(X ≤ x) is non-decreasing and relates to the PDF by F'(x) = f(x).

## How It's Best Learned
Visualize both PDF and CDF. Practice computing probabilities by integrating the PDF. Understand that P(X = c) = 0 for any single point c.

## Common Misconceptions
Thinking f(x) is a probability (it's a density). Confusing PDF and CDF graphically. Computing P(X = c) as non-zero for continuous X.

## Questions

```yaml
- question: "A continuous random variable X has PDF f(x) = 3x² for 0 ≤ x ≤ 1. What is f(0.9)?"
  type: multiple-choice
  options:
    - "This is impossible — a probability value can never exceed 1"
    - "2.43, which is the probability of X equaling 0.9"
    - "2.43, which is a valid density value even though it exceeds 1"
    - "0.81, after normalizing f(0.9) to ensure it stays below 1"
  answer: 2
  explanation: "f(0.9) = 3(0.81) = 2.43. This is perfectly valid — f(x) is a *density*, not a probability, so it can exceed 1. The constraint on a PDF is not that f(x) ≤ 1; it is that f(x) ≥ 0 everywhere and that the total integral ∫f(x)dx = 1. Option A is the classic misconception: confusing a density value with a probability. A density measures probability per unit length, and there is no reason that rate must stay below 1."

- question: "A classmate computes P(X = 2.7) for a continuous random variable by evaluating f(2.7). What is the correct answer, and why is f(2.7) wrong?"
  type: multiple-choice
  options:
    - "f(2.7) is correct; the PDF gives the probability at each point for continuous variables"
    - "P(X = 2.7) = 0; probability at a single point equals the integral over zero width, which is zero"
    - "P(X = 2.7) = F(2.7), the CDF evaluated at 2.7"
    - "P(X = 2.7) = f(2.7)·Δx for some small Δx around 2.7"
  answer: 1
  explanation: "For any continuous random variable, P(X = c) = 0 for every specific value c. Probability is obtained by integrating the PDF over an interval: P(a ≤ X ≤ b) = ∫ₐᵇ f(x)dx. The integral over a single point has zero width and therefore zero area — giving zero probability. f(x) is a density, measuring how rapidly probability accumulates near a point, not the probability itself. Evaluating f(2.7) gives a density value that has no direct interpretation as a probability."

- question: "For a continuous random variable X, P(X ≤ 3) = P(X < 3)."
  type: true-false
  answer: true
  explanation: "For a continuous distribution, P(X = 3) = 0, so including or excluding the endpoint makes no difference: P(X ≤ 3) = P(X < 3) + P(X = 3) = P(X < 3) + 0 = P(X < 3). This contrasts with discrete random variables, where P(X = 3) can be positive and the distinction between ≤ and < matters significantly."

- question: "If f(x) is the PDF of a continuous random variable X, then f(x) represents the probability that X equals x."
  type: true-false
  answer: false
  explanation: "f(x) is a probability *density*, not a probability. Probabilities are obtained by integrating the PDF over an interval: P(a ≤ X ≤ b) = ∫ₐᵇ f(x)dx. At any single point, f(x) represents probability per unit length in the neighborhood of x — a rate, not an amount. Consequently, f(x) can take any non-negative value, including values greater than 1, as long as the total integral equals 1."

- question: "Explain why the probability that a continuous random variable X takes any specific value c is exactly zero, and what this means for computing probabilities in practice."
  type: short-answer
  answer: "P(X = c) = 0 because probability comes from integrating the PDF over an interval. The integral from c to c has zero width, giving zero area and therefore zero probability. This doesn't mean c is impossible — it means a continuous variable has uncountably many possible values and probability is spread continuously rather than concentrated at points. In practice, we always compute P(a ≤ X ≤ b) = ∫ₐᵇ f(x)dx; asking for the probability at a single point is the wrong question for a continuous distribution."
  explanation: "This is the fundamental distinction between continuous and discrete distributions. A discrete variable concentrates probability mass at specific values. A continuous variable spreads probability across intervals, and any single point gets zero. The PDF encodes density — how rapidly probability accumulates near a point — not probability itself. This is why computing P(X = 2.7) using f(2.7) is a category error: you need an integral, not a function evaluation."
```
