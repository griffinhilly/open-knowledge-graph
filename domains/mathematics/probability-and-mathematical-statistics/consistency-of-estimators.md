---
id: consistency-of-estimators
title: Consistency of Estimators
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: convergence-in-probability
  type: hard
- id: maximum-likelihood-estimation-theory
  type: soft
builds-toward:
- asymptotic-normality-mle
tags:
- consistency
- asymptotics
- estimation
stage: formal-systems
status: draft
---

# Consistency of Estimators

## Core Idea
An estimator θ̂ₙ is consistent if θ̂ₙ converges in probability to θ as n → ∞. Consistency is a minimum requirement for reasonable estimators—as sample size grows, the estimator should approach the truth. Under regularity conditions, MLEs and method of moments estimators are consistent.
