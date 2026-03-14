---
id: maximum-likelihood-estimation-theory
title: Maximum Likelihood Estimation
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-mass-functions-theory
  type: hard
builds-toward:
- bayesian-inference-intro
tags:
- mle
- estimation
stage: formal-systems
status: draft
---

# Maximum Likelihood Estimation

## Core Idea
MLE θ̂ maximizes likelihood L(θ)=∏p(x_i|θ) or L(θ)=∏f(x_i|θ). Under regularity, MLEs are consistent, asymptotically normal, and efficient. Often found via log-likelihood ℓ(θ)=Σlog p(x_i|θ) by solving dℓ/dθ=0.
