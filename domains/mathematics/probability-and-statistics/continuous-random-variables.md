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
