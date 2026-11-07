---
id: transformations-of-random-variables
title: Transformations of Random Variables
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
  - id: probability-density-functions
    type: hard
  - id: cumulative-distribution-function
    type: hard
  - id: linear-transformations-of-random-variables
    type: soft
  - id: jacobian-change-of-variables
    type: soft
builds-toward:
  - order-statistics
tags: [probability, random-variables, change-of-variables, distributions, jacobian, cdf-method]
stage: advanced
status: validated
---

# Transformations of Random Variables

## Core Idea
If X has a known distribution and Y = g(X), the distribution of Y can be derived from that of X. The CDF method computes F_Y(y) = P(g(X) ≤ y) directly and then differentiates. When g is strictly monotone and differentiable, this gives the change-of-variables formula f_Y(y) = f_X(g⁻¹(y)) · |d g⁻¹(y)/dy|. For several variables the absolute derivative is replaced by the absolute value of a Jacobian determinant. Many standard distributions arise this way, such as the chi-square distribution as the square of a standard normal.

## How It's Best Learned
Begin every problem with the CDF method, since it works for any g and shows where the formula comes from. Then derive the monotone formula once and use it as a shortcut. Draw the graph of g to see which x-values map below a given y, especially for functions such as x² that are not one-to-one. Finish with two-variable examples that need a Jacobian, such as the sum or ratio of independent variables.

## Common Misconceptions
- The density of Y = g(X) is f_X(g⁻¹(y)). (A density must be rescaled by |d g⁻¹(y)/dy|, because g stretches or compresses intervals; without the factor the result usually does not integrate to 1.)
- The monotone formula works for any transformation. (For a function like g(x) = x² on ℝ, each y > 0 has two preimages, and their contributions must be added.)
- The transformed variable has the same support as X. (The support changes with g; if X is uniform on (0, 1), then -ln X takes values in (0, ∞).)

## Questions

```yaml
- question: "X is uniform on (0, 1) and Y = -ln X. What is the distribution of Y?"
  type: multiple-choice
  options:
    - "Uniform on (0, ∞)"
    - "Exponential with rate 1"
    - "Normal with mean 0 and variance 1"
    - "Uniform on (-∞, 0)"
  answer: 1
  explanation: "For y > 0, F_Y(y) = P(-ln X ≤ y) = P(X ≥ e⁻ʸ) = 1 - e⁻ʸ. That is the CDF of an exponential distribution with rate 1. There is no uniform distribution on an infinite interval."

- question: "If X has density f_X and Y = 2X, then f_Y(y) = f_X(y/2)."
  type: true-false
  answer: false
  explanation: "The correct density is f_Y(y) = (1/2) f_X(y/2). Doubling X spreads its probability over an interval twice as long, so the density must be halved for the total area to stay 1."

- question: "Let Z be standard normal and Y = Z². Use the CDF method to find f_Y(y) for y > 0."
  type: short-answer
  answer: "f_Y(y) = (1/√(2πy)) e^(-y/2) for y > 0, the chi-square distribution with 1 degree of freedom."
  explanation: "F_Y(y) = P(-√y ≤ Z ≤ √y) = Φ(√y) - Φ(-√y). Differentiating gives φ(√y)·(1/(2√y)) + φ(-√y)·(1/(2√y)) = φ(√y)/√y, which equals (1/√(2πy)) e^(-y/2). Both preimages ±√y contribute."

- question: "X is continuous with strictly increasing CDF F. What is the distribution of U = F(X)?"
  type: short-answer
  answer: "Uniform on (0, 1)."
  explanation: "For 0 < u < 1, P(F(X) ≤ u) = P(X ≤ F⁻¹(u)) = F(F⁻¹(u)) = u, which is the uniform CDF. This is the probability integral transform, and running it backward (X = F⁻¹(U)) is a standard way to generate samples from a given distribution."
```

## Explainer

Statistics constantly produces new random variables from old ones: a measurement converted to other units, the square of an error, the logarithm of an income. If we know the distribution of X and set Y = g(X), we want the distribution of Y.

The CDF method always works. Write F_Y(y) = P(Y ≤ y) = P(g(X) ≤ y), turn the event {g(X) ≤ y} into an event about X, and compute its probability from the distribution of X. Then differentiate to get f_Y. For example, if X is uniform on (0, 1) and Y = -ln X, then for y > 0, the event -ln X ≤ y is the same as X ≥ e⁻ʸ. So F_Y(y) = 1 - e⁻ʸ, and Y is exponential with rate 1.

When g is strictly increasing and differentiable, the method gives a general formula. F_Y(y) = P(X ≤ g⁻¹(y)) = F_X(g⁻¹(y)), and the chain rule gives f_Y(y) = f_X(g⁻¹(y)) · (g⁻¹)'(y). A decreasing g produces a minus sign that cancels the negative derivative, so both cases combine into

f_Y(y) = f_X(g⁻¹(y)) · |d g⁻¹(y)/dy|.

The derivative factor is the stretching factor. Probability is conserved: P(y < Y < y + dy) must equal P(x < X < x + dx) for the matching interval. If g stretches a short interval near x by a factor of 3, the density near y = g(x) must be one third as tall.

If g is not one-to-one, add the contributions from every preimage. For Y = Z² with Z standard normal, each y > 0 comes from z = √y and z = -√y. The CDF method gives F_Y(y) = Φ(√y) - Φ(-√y), and differentiating yields f_Y(y) = (1/√(2πy)) e^(-y/2), the chi-square distribution with one degree of freedom.

With several variables, (Y₁, Y₂) = g(X₁, X₂), the same reasoning uses the multivariable change of variables: the joint density of Y equals the joint density of X at the preimage, times the absolute value of the Jacobian determinant of the inverse map. This is how one derives the distributions of sums, products and ratios, such as the t and F distributions.

Finally, if X is continuous with CDF F, then F(X) is uniform on (0, 1). Read backward, F⁻¹(U) has CDF F when U is uniform, which is a standard way to simulate samples from F.
