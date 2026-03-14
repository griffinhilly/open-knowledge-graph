---
id: hypothesis-testing-fundamentals
title: Hypothesis Testing Fundamentals
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-axioms
  type: soft
- id: sampling-distributions
  type: hard
builds-toward:
- type-i-and-type-ii-errors
- z-test-and-t-test-for-means
tags:
- hypothesis-testing
- null-hypothesis
- alternative-hypothesis
stage: formal-systems
status: draft
---

# Hypothesis Testing Fundamentals

## Core Idea
Hypothesis testing is a method for deciding between two competing claims about a population parameter. The null hypothesis (H₀) represents the status quo or 'no effect'; the alternative hypothesis (H₁ or H_a) represents what we're testing for. A test statistic is computed from sample data, and a p-value gives the probability of observing such an extreme statistic if H₀ is true. We reject H₀ when the p-value is smaller than a predetermined significance level α (typically 0.05), but this does not prove H₀ is false—only that the data provide evidence against it.

## How It's Best Learned
Set up hypotheses for realistic scenarios. Interpret p-values correctly: probability of data given H₀, not probability H₀ is true. Distinguish statistical significance from practical significance.

## Common Misconceptions
Thinking p-value is the probability that H₀ is true. Confusing 'fail to reject' with 'accept.' Believing p < α proves the alternative is true. Forgetting that p-values measure evidence, not truth of hypotheses.
