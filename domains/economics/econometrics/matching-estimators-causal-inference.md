---
id: matching-estimators-causal-inference
title: 'Matching Estimators: Nearest Neighbor and Kernel Methods'
domain: economics
course: econometrics
prerequisites:
- id: propensity-score-matching
  type: hard
- id: treatment-effect-estimation
  type: hard
builds-toward:
- difference-in-differences
tags:
- causal-inference
- matching
- nonparametric
stage: formal-systems
status: draft
---

# Matching Estimators: Nearest Neighbor and Kernel Methods

## Core Idea
Matching estimators (nearest neighbor, kernel, local polynomial) estimate treatment effects nonparametrically by comparing outcomes between treated and control units with similar covariates. These methods avoid functional form assumptions but require sufficient overlap in covariate distributions and careful choice of bandwidth or neighborhood size.
