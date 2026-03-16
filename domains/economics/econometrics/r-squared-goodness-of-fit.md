---
id: r-squared-goodness-of-fit
title: 'R-Squared: Goodness of Fit'
domain: economics
course: econometrics
prerequisites:
- id: simple-linear-regression-estimation
  type: hard
builds-toward:
- adjusted-r-squared-model-comparison
tags:
- model-fit
- goodness-of-fit
stage: formal-systems
status: draft
---

# R-Squared: Goodness of Fit

## Core Idea
R² = 1 - (RSS / TSS) measures the fraction of variation in Y explained by regressors, ranging from 0 to 1. Higher values indicate better fit, but R² cannot determine whether the model is causal or whether omitted variables bias estimates.

## Explainer

From your study of simple linear regression, you know that OLS finds the line that minimizes the sum of squared residuals — the vertical distances between the data points and the fitted line. R² is built from two quantities derived from those residuals. **Total Sum of Squares (TSS)** is the total variation in Y around its mean: how spread out the outcome variable is before you add any predictors. **Residual Sum of Squares (RSS)** is the variation left over after fitting your model — the variation your regressors failed to explain. R² = 1 - (RSS/TSS) is then simply the fraction of total variation that the model accounts for.

The formula has a clean geometric interpretation. If your model explained nothing, RSS would equal TSS and R² = 0. If your model explained everything perfectly, RSS = 0 and R² = 1. In practice R² lives between these extremes, and interpreting it is context-dependent. A model explaining household income from age and education might achieve R² = 0.35 and be considered quite good, because income is driven by dozens of unobserved factors. A model predicting tomorrow's temperature from yesterday's temperature might achieve R² = 0.97. The benchmark is never "how close to 1?" but rather "how much variation was plausibly explainable by these specific predictors?"

The most important limitation of R² is that it rises mechanically whenever you add a variable — even a completely irrelevant one. Because OLS fits the sample data, adding noise variables never hurts in-sample fit. A model with 50 predictors will always have higher R² than a model with 5 predictors on the same data, even if 45 of those predictors are uncorrelated with Y in the population. This motivates the **adjusted R²**, which penalizes for the number of parameters, and cross-validation methods that assess out-of-sample fit.

The deeper limitation is that R² says nothing about causality. A model with R² = 0.95 might be severely confounded, with biased coefficient estimates, if key variables are omitted or endogenous. Conversely, a randomized experiment might produce a regression with R² = 0.02, but the estimate of the treatment effect is unbiased and causally interpretable. R² is a measure of descriptive fit, not of the quality of causal identification. This is why econometricians often care more about whether their estimates are consistent and unbiased than about whether R² is high.
