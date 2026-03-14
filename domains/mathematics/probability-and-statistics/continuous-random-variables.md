---
id: continuous-random-variables
title: Continuous Random Variables and Probability Density Functions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-intro
  type: hard
- id: definite-integral-definition
  type: hard
builds-toward:
- uniform-distribution-continuous
- exponential-distribution
- standard-normal-and-z-scores
tags:
- continuous-random-variable
- PDF
- probability-density-function
- CDF
stage: formal-systems
status: validated
---

# Continuous Random Variables and Probability Density Functions

## Core Idea
For continuous random variables, probability is represented by a probability density function (PDF) f(x), where P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx. The PDF itself is not a probability — it is a density — so f(x) can exceed 1. The cumulative distribution function (CDF) F(x) = P(X ≤ x) = ∫₋∞ˣ f(t) dt is non-decreasing from 0 to 1. For continuous distributions, P(X = x) = 0 for any single value.

## How It's Best Learned
The transition from PMF to PDF is conceptually difficult. Begin with the analogy: a PMF is like a histogram with discrete bars; a PDF is the limit as bars become infinitely thin. Emphasize that area under the curve gives probability, not height. Practice computing probabilities as definite integrals.

## Common Misconceptions
- Treating PDF values as probabilities directly — they are densities, not probabilities.
- Thinking P(X = 5) is small but positive for continuous distributions — it is exactly 0.
- Forgetting that the total area under a valid PDF must equal 1.
