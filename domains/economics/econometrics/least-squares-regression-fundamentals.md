---
id: least-squares-regression-fundamentals
title: 'Least Squares Regression: Fundamentals and Derivation'
domain: economics
course: econometrics
prerequisites:
- id: bivariate-regression
  type: hard
- id: ols-assumptions
  type: hard
builds-toward:
- gauss-markov-theorem-ols
- estimator-consistency-unbiasedness
tags:
- ols
- estimation
- regression
stage: formal-systems
status: draft
---

# Least Squares Regression: Fundamentals and Derivation

## Core Idea
Ordinary least squares (OLS) minimizes the sum of squared residuals to estimate regression coefficients. The OLS estimator has a closed-form solution and is the foundation of econometric analysis, with well-understood statistical properties that depend on assumptions about the data-generating process.

## How It's Best Learned
Work through matrix-form derivations minimizing the sum of squared residuals. Compare OLS to other loss functions and see why quadratic loss leads to the least squares solution.

## Common Misconceptions
OLS does not require normally distributed errors (normality is only needed for exact inference), and minimizing squared residuals alone does not ensure unbiasedness—additional assumptions about regressors are required.
