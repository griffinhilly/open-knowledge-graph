---
id: margin-of-error-and-sample-size
title: Margin of Error and Sample Size
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: confidence-intervals-framework
  type: hard
builds-toward:
- confidence-intervals-means
- confidence-intervals-proportions
tags:
- inference
- planning
- sample-size
stage: formal-systems
status: draft
---

# Margin of Error and Sample Size

## Core Idea
The margin of error is the half-width of a confidence interval: ME = (critical value) × (standard error). It quantifies precision. To achieve desired margin of error m: n = (z/m)² · σ² or n = z² · p(1-p)/m² for proportions.

## How It's Best Learned
Calculate required sample sizes for various scenarios. Verify that doubling sample size reduces margin of error by √2. Understand the tradeoff between sample size and precision in practice.
