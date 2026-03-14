---
id: hypothesis-testing-framework-theory
title: 'Hypothesis Testing: Framework and Logic'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: conditional-probability-fundamentals
  type: hard
builds-toward:
- z-test-for-means
- chi-square-test
tags:
- hypothesis-testing
stage: formal-systems
status: draft
---

# Hypothesis Testing: Framework and Logic

## Core Idea
Test H₀ vs H₁. Compute test statistic under H₀. P-value=P(statistic this extreme or more|H₀ true). Reject H₀ if p<α; fail to reject otherwise. Significance level α controls Type I error. Logical structure: assume H₀ true, ask if data are surprising.
