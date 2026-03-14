---
id: probability-density-functions
title: Probability Density Functions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: continuous-random-variables-basics
  type: hard
- id: definite-integral-definition
  type: soft
builds-toward:
- expected-value
- variance-of-random-variables
- cumulative-distribution-function
tags:
- pdf
- continuous-distributions
- probability
stage: formal-systems
status: draft
---

# Probability Density Functions

## Core Idea
The probability density function (PDF), denoted f(x), describes the relative likelihood of a continuous random variable taking values near x. Probabilities are found by integrating: P(a ≤ X ≤ b) = ∫ₐᵇ f(x)dx. The PDF is always non-negative and integrates to 1.

## How It's Best Learned
Sketch PDFs and visualize integration as areas under curves. Compare PDFs of different distributions. Practice finding probabilities by integration. Use properties of PDFs to identify valid densities.

## Common Misconceptions
Thinking f(x) is a probability (it's a density, not probability). Reading probability directly from PDF height. Forgetting to integrate to find probabilities. Confusing PDF with PMF.
