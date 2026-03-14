---
id: lagged-dependent-variable-regression
title: Lagged Dependent Variable Regression
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: time-series-basics-econometrics
  type: hard
builds-toward:
- dynamic-panel-arellano-bond-estimator
tags:
- dynamic-models
- time-series
- lagged-variables
stage: formal-systems
status: draft
---

# Lagged Dependent Variable Regression

## Core Idea
The model Yₜ = β₀ + β₁Yₜ₋₁ + β₂Xₜ + uₜ includes lagged Y; β₁ measures persistence and dynamic adjustment. OLS remains consistent if uₜ is serially uncorrelated and exogenous, but standard errors require adjustment for the correlation between Yₜ₋₁ and subsequent errors.
