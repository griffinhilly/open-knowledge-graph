---
id: confidence-intervals-rigorous
title: Confidence Intervals (Rigorous Theory)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: asymptotic-normality-of-mle
  type: hard
builds-toward:
- bayesian-inference-foundations
tags:
- confidence-intervals
- coverage
- inversion
stage: abstract-reasoning
status: draft
---

# Confidence Intervals (Rigorous Theory)

## Core Idea
A confidence interval [L(X), U(X)] has level 1-α if P(θ ∈ [L,U]) = 1-α for all θ (exact) or approximately (asymptotic). Intervals are constructed by inverting hypothesis tests or using pivotal quantities. Asymptotic CIs rely on the CLT and estimator asymptotics. Confidence is frequentist; different from Bayesian credible intervals.
