---
id: random-effects-models
title: Random Effects Models
domain: economics
course: econometrics
prerequisites:
- id: fixed-effects-models
  type: hard
tags:
- random-effects
- GLS
- Hausman-test
- panel
stage: formal-systems
status: draft
---

# Random Effects Models

## Core Idea
The random effects (RE) model treats the unit-specific component α_i as a random variable drawn from a distribution, rather than a fixed unknown parameter. RE estimation uses Generalized Least Squares (GLS), which exploits both within-unit and between-unit variation, yielding more efficient estimates than FE when the key assumption holds: the individual effect α_i must be uncorrelated with the regressors. Unlike FE, RE can estimate the effects of time-invariant covariates. The Hausman test compares FE and RE estimates — a significant difference indicates the RE assumption is violated and FE is preferred.

## How It's Best Learned
Apply the Hausman test to a panel dataset, interpret the test result, and explain why FE is preferred when the null is rejected. Understanding what 'correlation between α_i and x_it' means economically is the key insight.

## Common Misconceptions
- Random effects does not mean the effects are random in a colloquial sense — it is a modeling assumption about the distribution of unit heterogeneity.
- The Hausman test rejects the null when RE is inconsistent, but a failure to reject does not guarantee RE is correct — it may just be low-powered.
