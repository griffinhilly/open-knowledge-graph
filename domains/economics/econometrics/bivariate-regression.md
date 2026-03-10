---
id: bivariate-regression
title: Simple (Bivariate) OLS Regression
domain: economics
course: econometrics
prerequisites:
- id: linear-regression
  type: hard
- id: correlation-coefficient
  type: hard
- id: residuals-and-goodness-of-fit
  type: hard
- id: variance-of-random-variables
  type: soft
builds-toward:
- ols-assumptions
- multiple-regression-model
- r-squared-and-model-fit
tags:
- OLS
- regression
- estimation
stage: formal-systems
status: draft
---

# Simple (Bivariate) OLS Regression

## Core Idea
Simple OLS regression fits the line ŷ = β₀ + β₁x that minimizes the sum of squared residuals between observed and predicted values of y. The slope estimator β̂₁ equals Cov(x,y)/Var(x), capturing how much y is predicted to change per unit increase in x. OLS is the default workhorse of empirical economics because it is computationally tractable and, under standard assumptions, produces unbiased and efficient estimates. The intercept β̂₀ gives the predicted value of y when x equals zero, though this is often not economically meaningful.

## How It's Best Learned
Derive the OLS formulas by hand from the minimization problem before using software. Then replicate published regressions in a dataset like wage-education data to see how coefficient interpretation works in context.

## Common Misconceptions
- The OLS line describes the conditional mean of y given x — it does not describe causation.
- A steep slope does not mean a strong fit; R² measures fit, not the magnitude of the slope.
