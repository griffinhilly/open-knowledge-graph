---
id: within-estimator-panel
title: Within Estimator (Fixed Effects) for Panel Data
domain: economics
course: econometrics
prerequisites:
- id: panel-data-structure-advantages
  type: hard
- id: fixed-effects-models
  type: hard
builds-toward:
- between-estimator-panel
tags:
- panel-data
- fixed-effects
- within
stage: formal-systems
status: draft
---

# Within Estimator (Fixed Effects) for Panel Data

## Core Idea
The within estimator controls for unit-specific time-invariant unobserved heterogeneity by demeaning variables within each unit or including unit fixed effects. It is robust to selection based on stable individual characteristics but requires strict exogeneity: errors must be uncorrelated with past, present, and future regressors.
