---
id: regression-discontinuity
title: Regression Discontinuity Design
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: potential-outcomes-framework
  type: hard
- id: bivariate-regression
  type: hard
tags:
- RDD
- regression-discontinuity
- threshold
- local-ATE
- bandwidth
stage: formal-systems
status: draft
---

# Regression Discontinuity Design

## Core Idea
Regression discontinuity (RD) exploits a sharp threshold in a 'running variable' x that determines treatment assignment: units just above the cutoff receive treatment while units just below do not. The key insight is that units near the threshold are nearly identical in all respects — observed and unobserved — making the discontinuous jump in outcomes at the threshold a credible causal effect estimate. The RD estimator is the difference in the intercepts of the regression lines fitted on each side of the cutoff. Identification requires that agents cannot precisely manipulate their position around the threshold; the McCrary density test checks for sorting.

## How It's Best Learned
Study Thistlethwaite and Campbell's (1960) original scholarship threshold study, then examine Lee (2008)'s incumbency advantage study to understand how running variables and cutoffs are chosen and validated.

## Common Misconceptions
- RD estimates a Local ATE at the threshold, not the ATE for the full population — external validity is often limited.
- Choosing a very narrow bandwidth around the cutoff reduces bias but also reduces precision; bandwidth selection involves a bias-variance tradeoff.
