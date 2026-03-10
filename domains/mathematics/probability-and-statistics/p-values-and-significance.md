---
id: p-values-and-significance
title: P-Values and Statistical Significance
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: standard-normal-and-z-scores
  type: hard
builds-toward:
- type-i-and-type-ii-errors
- z-test-for-means
- t-test-for-means
tags:
- p-value
- significance-level
- alpha
- reject-null
- statistical-significance
stage: formal-systems
status: draft
---

# P-Values and Statistical Significance

## Core Idea
The p-value is the probability of observing a test statistic as extreme as or more extreme than the observed value, assuming H₀ is true. A small p-value indicates that the observed result would be rare if H₀ were true, providing evidence against H₀. The significance level α (commonly 0.05) is the pre-specified threshold: if p-value < α, we reject H₀. Statistical significance does not imply practical significance — a large sample can make a tiny, meaningless effect statistically significant.

## How It's Best Learned
Walk through the logic: if the p-value is 0.03, there's a 3% chance of seeing data this extreme by chance alone. That's the probability of the data given H₀, not the probability H₀ is true. Use simulation to show that p-values are uniformly distributed under H₀, reinforcing their probabilistic interpretation.

## Common Misconceptions
- 'The p-value is the probability H₀ is true' — fundamentally wrong; it is P(data | H₀).
- Treating α = 0.05 as a universal law of nature rather than a conventional threshold.
- Confusing statistical significance with practical or scientific importance.
