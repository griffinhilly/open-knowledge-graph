---
id: multicollinearity
title: Multicollinearity
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: correlation-coefficient
  type: hard
builds-toward:
- robust-standard-errors
tags:
- multicollinearity
- variance-inflation
- VIF
- identification
stage: formal-systems
status: draft
---

# Multicollinearity

## Core Idea
Multicollinearity arises when two or more regressors are highly (but not perfectly) correlated, making it difficult for OLS to separately identify their individual effects. It inflates standard errors, widens confidence intervals, and makes individual t-tests unreliable — but it does not bias the coefficient estimates. Variance Inflation Factors (VIFs) quantify how much each regressor's standard error is inflated relative to the case of no correlation. Perfect multicollinearity (e.g., including both a variable and its exact linear combination) makes (X'X) singular and OLS undefined.

## Common Misconceptions
- Multicollinearity is a data problem, not a model misspecification — it does not violate any Gauss-Markov assumption.
- Dropping a correlated variable 'fixes' multicollinearity but may introduce omitted variable bias.
