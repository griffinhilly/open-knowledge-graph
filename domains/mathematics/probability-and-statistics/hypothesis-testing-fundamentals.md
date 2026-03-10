---
id: hypothesis-testing-fundamentals
title: Fundamentals of Hypothesis Testing
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sampling-distributions
  type: hard
- id: confidence-intervals-means
  type: soft
builds-toward:
- p-values-and-significance
- z-test-for-means
- t-test-for-means
- chi-square-test
- anova-one-way
- type-i-and-type-ii-errors
tags:
- hypothesis-testing
- null-hypothesis
- alternative-hypothesis
- test-statistic
- significance
stage: formal-systems
status: draft
---

# Fundamentals of Hypothesis Testing

## Core Idea
Hypothesis testing is a formal decision-making procedure using sample data to evaluate a claim about a population parameter. The null hypothesis H₀ states the default (no effect, no difference), and the alternative hypothesis Hₐ is what the test seeks evidence for. A test statistic quantifies how far the sample result is from what H₀ predicts. The decision to reject or fail to reject H₀ is based on whether the evidence is sufficiently unlikely under H₀.

## How It's Best Learned
Use legal reasoning as an analogy: H₀ is 'innocent until proven guilty.' We reject H₀ only when evidence is overwhelming. Work through a full test from the beginning — stating hypotheses, computing the test statistic, making a decision — before introducing p-values or significance levels.

## Common Misconceptions
- 'Accepting' H₀ vs. 'failing to reject' it — we never prove H₀ true.
- Thinking H₀ is always that the parameter equals zero.
- Confusing one-tailed and two-tailed tests — the choice must be made before seeing the data.
