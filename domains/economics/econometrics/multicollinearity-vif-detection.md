---
id: multicollinearity-vif-detection
title: 'Multicollinearity: Detection Using VIF'
domain: economics
course: econometrics
prerequisites:
- id: multicollinearity
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: condition-number-of-a-matrix
  type: soft
- id: linear-independence
  type: soft
tags:
- multicollinearity
- diagnostics
stage: formal-systems
status: draft
---

# Multicollinearity: Detection Using VIF

## Core Idea
The Variance Inflation Factor VIFⱼ = 1 / (1 - Rⱼ²) measures how much variance of β̂ⱼ is inflated by collinearity with other regressors. Rules of thumb: VIF > 10 indicates severe multicollinearity; values 5-10 suggest moderate concern. Correlation matrix and condition number also reveal collinearity patterns.
