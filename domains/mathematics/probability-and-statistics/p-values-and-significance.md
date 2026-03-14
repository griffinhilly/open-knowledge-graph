---
id: p-values-and-significance
title: P-values and Statistical Significance
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-test-framework
  type: hard
builds-toward:
- type-i-type-ii-errors-tradeoff
- effect-size-in-hypothesis-tests
tags:
- hypothesis-testing
- p-value
- significance
stage: formal-systems
status: draft
---

# P-values and Statistical Significance

## Core Idea
The p-value is the probability of observing data as extreme as ours (or more extreme) if H₀ were true. A result is 'statistically significant' if p < α (typically 0.05). Small p-values suggest data are inconsistent with H₀.

## How It's Best Learned
Calculate p-values for simple test statistics. Simulate null distributions to understand p-value as tail probability. Compare p-values to critical values. Recognize that significance ≠ importance.

## Common Misconceptions
Interpreting p-value as probability H₀ is true (backward; p-value is P(data|H₀)). Thinking p > 0.05 means H₀ is true. Confusing statistical significance with practical significance. Using p-value as a measure of effect size.
