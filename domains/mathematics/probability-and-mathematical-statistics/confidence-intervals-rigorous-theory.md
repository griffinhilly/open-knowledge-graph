---
id: confidence-intervals-rigorous-theory
title: Confidence Intervals (Rigorous Theory)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: asymptotic-normality-mle
  type: hard
- id: uniformly-most-powerful-tests
  type: soft
builds-toward:
- bayesian-inference-foundations
tags:
- confidence-intervals
- interval-estimation
- statistics
stage: advanced
status: draft
---

# Confidence Intervals (Rigorous Theory)

## Core Idea
A (1-α) confidence interval [L(X), U(X)] for θ satisfies P(L(X) ≤ θ ≤ U(X)) = 1 - α. Confidence intervals can be inverted from hypothesis tests: the (1-α) CI is {θ: θ is not rejected at level α}. Shortest confidence intervals use the critical region from the UMP test. Asymptotic CIs rely on asymptotic normality of estimators.
