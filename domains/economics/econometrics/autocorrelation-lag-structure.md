---
id: autocorrelation-lag-structure
title: 'Autocorrelation: Structure and Sources'
domain: economics
course: econometrics
prerequisites:
- id: ols-assumptions
  type: hard
- id: time-series-basics-econometrics
  type: hard
builds-toward:
- durbin-watson-statistic
tags:
- autocorrelation
- time-series
- diagnostics
stage: formal-systems
status: draft
---

# Autocorrelation: Structure and Sources

## Core Idea
Autocorrelation (serial correlation) occurs when errors are correlated over time: Cov(uₜ, uₛ) ≠ 0 for t ≠ s, often following an AR(1) structure. Sources include omitted variables, model misspecification, or true dynamics. Autocorrelation does not bias OLS but inflates standard errors, invalidating inference.
