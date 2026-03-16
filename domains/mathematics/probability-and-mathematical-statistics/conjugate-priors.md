---
id: conjugate-priors
title: Conjugate Priors
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: bayesian-inference-foundations
  type: hard
- id: exponential-family
  type: soft
builds-toward:
- bayesian-point-estimation
tags:
- conjugate-priors
- bayesian-inference
- statistics
stage: advanced
status: draft
---

# Conjugate Priors

## Core Idea
A prior π is conjugate for a likelihood if the posterior π(θ|X) is in the same family as the prior. For exponential family likelihoods, conjugate priors exist and have closed-form posteriors. Examples: Beta prior for Binomial likelihood, Normal prior for Normal likelihood with known variance. Conjugate priors simplify Bayesian computation.
