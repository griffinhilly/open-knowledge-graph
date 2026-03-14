---
id: linear-regression-simple-theory
title: 'Simple Linear Regression: Theory and Estimation'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression-basics
  type: soft
- id: covariance-correlation-theory
  type: hard
builds-toward:
- inference-in-linear-regression
- regression-diagnostics
tags:
- linear-regression
stage: formal-systems
status: draft
---

# Simple Linear Regression: Theory and Estimation

## Core Idea
Fit Y=β₀+β₁X+ε by minimizing Σε². Least squares: β₁=Cov(X,Y)/Var(X)=r(s_Y/s_X), β₀=Ȳ−β₁X̄. Under normality, LS is MLE. R²=correlation² is proportion of Y variance explained. Residuals ê_i=y_i−ŷ_i should be random.
