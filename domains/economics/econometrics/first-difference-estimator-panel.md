---
id: first-difference-estimator-panel
title: First-Difference Estimator for Panel Data
domain: economics
course: econometrics
prerequisites:
- id: panel-data-structure-advantages
  type: hard
- id: fixed-effects-models
  type: hard
builds-toward:
- within-estimator-panel
tags:
- panel-data
- estimation
- fixed-effects
stage: formal-systems
status: draft
---

# First-Difference Estimator for Panel Data

## Core Idea
The first-difference estimator eliminates time-invariant unobserved heterogeneity by taking successive period differences, then running OLS on differenced variables. Simple and intuitive, it loses information and performs poorly with persistent outcomes, motivating alternative estimators.
