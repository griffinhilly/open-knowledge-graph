---
id: generalized-method-of-moments
title: Generalized Method of Moments (GMM)
domain: economics
course: econometrics
prerequisites:
- id: maximum-likelihood-econometrics
  type: soft
- id: instrumental-variables
  type: hard
builds-toward:
- dynamic-panel-arellano-bond-estimator
tags:
- estimation
- gmm
- moment-conditions
stage: formal-systems
status: draft
---

# Generalized Method of Moments (GMM)

## Core Idea
GMM exploits moment conditions E[f(Yᵢ, θ)] = 0 to estimate θ by minimizing a quadratic form in sample moments. It generalizes OLS, IV, and MLE; yields efficient estimators when moment conditions are correctly specified. The Hansen J-test checks overidentification.
