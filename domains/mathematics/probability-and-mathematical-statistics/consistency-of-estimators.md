---
id: consistency-of-estimators
title: Consistency of Estimators
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: convergence-in-probability
  type: hard
- id: weak-law-of-large-numbers
  type: soft
builds-toward:
- asymptotic-normality-of-mle
tags:
- consistency
- convergence
- estimation
stage: abstract-reasoning
status: draft
---

# Consistency of Estimators

## Core Idea
An estimator T̂_n is consistent for θ if T̂_n converges in probability to θ as n → ∞. Consistency ensures that with sufficient data, the estimator approaches the true parameter. MLEs are consistent under regularity conditions; method of moments estimators are consistent by the WLLN. Inconsistent estimators should be rejected.
