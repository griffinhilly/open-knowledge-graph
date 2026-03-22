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

## Explainer

From your study of random variables and expected value, you know that a random variable assigns a number to each outcome of a random experiment. A **discrete** random variable takes values from a countable set (a die roll can be 1 through 6; a coin-flip count can be 0, 1, 2, ...). A **continuous** random variable, by contrast, can take any value in an interval — the height of a randomly selected person, the exact time until a bus arrives, the temperature at noon. The set of possible values is uncountably infinite, and this changes the mathematics fundamentally: you can no longer assign positive probability to individual values.

The distribution of a continuous random variable is described by a **probability density function** (PDF) f(x). The PDF is not itself a probability — it is a density, measuring how rapidly probability accumulates near a point. Probability comes from integrating the density over an interval: P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx. Graphically, probability equals area under the PDF curve. The two requirements on any valid PDF are that f(x) ≥ 0 everywhere and that the total area under the curve equals 1: ∫₋∞^∞ f(x) dx = 1. Crucially, f(x) itself can exceed 1 — the PDF f(x) = 3x² on [0, 1] reaches a value of 3 at x = 1, which is perfectly valid because it is a density (probability per unit length), not a probability.

The most counterintuitive fact about continuous random variables is that **P(X = c) = 0** for any specific value c. The integral from c to c has zero width, hence zero area, hence zero probability. This does not mean the event is impossible — it means a continuous variable spreads its probability across an uncountable infinity of values, and no single point receives a positive share. In practice, you never ask "what is the probability that someone is exactly 170.000... cm tall?" — you ask "what is the probability that someone is between 169 and 171 cm?" This interval question is what the PDF answers through integration.

The **cumulative distribution function** (CDF) F(x) = P(X ≤ x) = ∫₋∞ˣ f(t) dt provides a complementary view: it accumulates probability from the left. The CDF is non-decreasing, starts at 0 as x → −∞, and approaches 1 as x → ∞. The relationship between the PDF and CDF is differentiation: f(x) = F'(x) wherever F is differentiable. Because P(X = c) = 0 for continuous variables, it makes no difference whether inequalities are strict or inclusive: P(X ≤ 3) = P(X < 3). This simplification does not hold for discrete variables, where P(X = 3) can be positive and the distinction between ≤ and < matters.

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
