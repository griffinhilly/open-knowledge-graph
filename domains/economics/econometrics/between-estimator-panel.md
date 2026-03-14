---
id: between-estimator-panel
title: Between and Random Effects Estimators for Panel Data
domain: economics
course: econometrics
prerequisites:
- id: within-estimator-panel
  type: hard
- id: random-effects-models
  type: hard
builds-toward:
- hausman-specification-test
tags:
- panel-data
- random-effects
- between
stage: formal-systems
status: draft
---

# Between and Random Effects Estimators for Panel Data

## Core Idea
The random effects estimator assumes unobserved heterogeneity is uncorrelated with regressors, treating the unit-specific effect as random. When this orthogonality condition holds, random effects is more efficient than fixed effects because it exploits both within-unit and between-unit variation; the between estimator uses only cross-sectional variation.
