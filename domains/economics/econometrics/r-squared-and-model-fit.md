---
id: r-squared-and-model-fit
title: R-Squared and Model Fit
domain: economics
course: econometrics
prerequisites:
- id: bivariate-regression
  type: hard
- id: residuals-and-goodness-of-fit
  type: hard
- id: f-test-joint-significance
  type: soft
- id: correlation-coefficient
  type: soft
builds-toward:
- omitted-variable-bias
- multicollinearity
tags:
- R-squared
- goodness-of-fit
- adjusted-R-squared
- model-selection
stage: formal-systems
status: validated
---

# R-Squared and Model Fit

## Core Idea
R² measures the fraction of variation in y explained by the regressors: R² = 1 − SSR/SST, where SSR is the sum of squared residuals and SST is total variance. It always lies between 0 and 1, and adding any regressor — even irrelevant — cannot decrease it. The adjusted R² penalizes for additional regressors, making it more appropriate for model comparison: R̄² = 1 − [SSR/(n−k−1)]/[SST/(n−1)]. High R² does not imply unbiased coefficient estimates; low R² does not imply the estimates are wrong or the model is useless for causal inference.

## How It's Best Learned
Compare R² and adjusted R² across nested models (same data, different regressors). Note that adding noise variables can raise R² but lower R̄².

## Common Misconceptions
- A low R² (e.g., 0.05) does not invalidate a regression — causal identification is about E[u|x]=0, not explained variance.
- R² is not comparable across datasets or when the dependent variable is transformed (e.g., log y vs y).
