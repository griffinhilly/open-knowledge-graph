---
id: elastic-net-ridge-lasso-regression
title: Ridge, Lasso, and Elastic Net Regression
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: multicollinearity
  type: hard
tags:
- regularization
- ridge
- lasso
- elastic-net
stage: formal-systems
status: draft
---

# Ridge, Lasso, and Elastic Net Regression

## Core Idea
Ridge (L2), Lasso (L1), and Elastic Net add penalty terms to OLS loss. Ridge shrinks all coefficients; Lasso zeros out weak variables; Elastic Net combines both. These methods address multicollinearity and perform variable selection.

## How It's Best Learned
Fit models with varying penalty parameters (lambda) and plot coefficient paths. Use cross-validation to choose the optimal lambda that balances fit and parsimony.
