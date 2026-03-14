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
- exponential-family
- posterior
stage: abstract-reasoning
status: draft
---

# Conjugate Priors

## Core Idea
A prior π(θ) is conjugate to the likelihood if the posterior is in the same family as the prior. For exponential family likelihoods, conjugate priors exist with natural forms. Example: Beta prior for Bernoulli gives Beta posterior. Conjugate priors enable closed-form computation and have intuitive interpretation.
