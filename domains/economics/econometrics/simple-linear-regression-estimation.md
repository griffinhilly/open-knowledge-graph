---
id: simple-linear-regression-estimation
title: Simple Linear Regression Estimation
domain: economics
course: econometrics
prerequisites:
- id: least-squares-regression-fundamentals
  type: hard
- id: bivariate-regression
  type: soft
builds-toward:
- normal-linear-regression-model
- coefficient-interpretation-regression
tags:
- ols
- estimation
- regression
- foundations
stage: formal-systems
status: draft
---

# Simple Linear Regression Estimation

## Core Idea
OLS estimation for Y = β₀ + β₁X + u minimizes the sum of squared residuals to estimate coefficients. The estimators β̂₀ and β̂₁ are closed-form linear combinations of the data that produce the best linear prediction in the sense of minimizing squared errors.

## How It's Best Learned
Compute β̂₁ = Cov(X,Y)/Var(X) by hand using simple numeric examples. Then plot regression lines on scatter plots to visualize how OLS finds the line that minimizes residuals.

## Common Misconceptions
OLS does not assume Y is normally distributed—only errors need normality for inference. A high R² does not imply causality; causality requires exogeneity assumptions not testable from the regression alone.
