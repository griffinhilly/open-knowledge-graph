---
id: hausman-specification-test
title: 'Hausman Test: Fixed Effects Versus Random Effects'
domain: economics
course: econometrics
prerequisites:
- id: within-estimator-panel
  type: hard
- id: between-estimator-panel
  type: hard
builds-toward:
- dynamic-panel-gmm
tags:
- panel-data
- testing
- specification
stage: formal-systems
status: draft
---

# Hausman Test: Fixed Effects Versus Random Effects

## Core Idea
The Hausman test compares fixed and random effects estimators; a large difference suggests the random effects orthogonality assumption is violated. Under the null hypothesis, the test statistic is asymptotically chi-squared, guiding practitioners toward fixed effects when the assumption fails.
