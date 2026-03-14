---
id: bayesian-point-estimation
title: Bayesian Point Estimation
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: conditional-expectation
  type: hard
- id: bayesian-inference-foundations
  type: soft
tags:
- bayesian
- point-estimation
- posterior
stage: abstract-reasoning
status: draft
---

# Bayesian Point Estimation

## Core Idea
Bayesian point estimates are derived from the posterior: the posterior mean E[θ|x] minimizes squared loss; the posterior mode (MAP) minimizes 0-1 loss; the posterior median minimizes absolute error loss. The posterior mean is often preferred as it incorporates the full posterior and minimizes squared error.
