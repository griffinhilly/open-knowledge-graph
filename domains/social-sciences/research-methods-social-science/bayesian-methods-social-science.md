---
id: bayesian-methods-social-science
title: Bayesian Methods in Social Science
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: probability-and-statistics
  type: hard
- id: research-design-advanced
  type: soft
- id: bayes-theorem
  type: hard
- id: conditional-probability-fundamentals
  type: hard
- id: probability-axioms
  type: hard
- id: conditional-probability
  type: soft
builds-toward:
- bayesian-network-models-causal
- hierarchical-bayesian-models
tags:
- bayesian
- inference
- statistical-modeling
stage: advanced
status: draft
---

# Bayesian Methods in Social Science

## Core Idea
Bayesian methods use prior knowledge and observed data to estimate posterior probability distributions. They provide a principled framework for incorporating uncertainty, updating beliefs as new evidence arrives, and comparing competing theoretical models. Unlike frequentist approaches, Bayesian inference allows direct probability statements about parameters and is particularly useful for small samples and complex hierarchical social phenomena.

## How It's Best Learned
Start with simple binomial models and conjugate priors, then progress to MCMC methods using Stan or JAGS. Apply to real social science datasets comparing prior specifications.

## Common Misconceptions
- Assuming all priors are equally subjective when domain expertise can justify informative priors.
- Confusing posterior probability intervals with frequentist confidence intervals (they have different interpretations).
- Overestimating computational burden—modern software makes Bayesian estimation accessible.
