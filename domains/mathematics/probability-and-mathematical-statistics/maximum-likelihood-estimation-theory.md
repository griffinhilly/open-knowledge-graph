---
id: maximum-likelihood-estimation-theory
title: Maximum Likelihood Estimation (Theory)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: sufficient-statistics
  type: soft
- id: expectation-measure-theoretic
  type: soft
builds-toward:
- consistency-of-estimators
- asymptotic-normality-of-mle
tags:
- mle
- estimation
- likelihood
stage: abstract-reasoning
status: draft
---

# Maximum Likelihood Estimation (Theory)

## Core Idea
The maximum likelihood estimator θ̂_n = argmax L(θ) chooses the parameter maximizing the likelihood of observed data. Under regularity conditions, MLEs are consistent, asymptotically normal with variance 1/nI(θ), and asymptotically efficient. Theory covers existence, uniqueness, and limiting behavior.
