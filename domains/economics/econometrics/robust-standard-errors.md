---
id: robust-standard-errors
title: Robust Standard Errors
domain: economics
course: econometrics
prerequisites:
- id: heteroskedasticity
  type: hard
- id: hypothesis-testing-regression
  type: hard
builds-toward:
- panel-data-basics
tags:
- robust-SE
- sandwich-estimator
- clustered-errors
- inference
stage: formal-systems
status: draft
---

# Robust Standard Errors

## Core Idea
Robust standard errors (Huber-White or 'sandwich' estimators) produce valid standard errors and confidence intervals in the presence of heteroskedasticity of unknown form, without requiring knowledge of the specific variance structure. Clustered standard errors extend this to settings where observations within groups (e.g., workers in the same firm, students in the same school) share common unobserved factors, inducing within-cluster correlation. Using clustered standard errors when observations are not truly independent is essential for valid inference in panel and grouped data. Modern applied econometrics routinely reports clustered standard errors as a default.

## Common Misconceptions
- Robust standard errors are never smaller than OLS standard errors on average; they can be larger or smaller in any given regression.
- Clustering at too fine a level (few clusters) produces unreliable estimates; the rule of thumb requires at least 30-50 clusters.
