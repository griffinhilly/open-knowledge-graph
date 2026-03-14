---
id: bayesian-statistics-fundamentals
title: 'Bayesian Statistics: Prior, Posterior, Credible Intervals'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: bayes-theorem-and-inference
  type: hard
- id: probability-density-functions-theory
  type: hard
builds-toward:
- conjugate-priors
tags:
- bayesian
- inference
stage: formal-systems
status: draft
---

# Bayesian Statistics: Prior, Posterior, Credible Intervals

## Core Idea
Bayesian updating: posterior ∝ likelihood × prior. Posterior distribution of θ summarizes belief after seeing data. Credible intervals [a,b] satisfy P(θ∈[a,b]|data)=0.95, directly answering 'where is θ?' Unlike frequentist CIs, these are probability statements about θ.
