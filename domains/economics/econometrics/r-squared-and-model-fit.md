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

## Explainer

From bivariate regression, you learned how to fit a line through data by minimizing squared residuals — the vertical distances between data points and the fitted line. Those residuals capture what the model fails to explain. **R²** formalizes this intuition into a single summary statistic: the fraction of the total variation in y that your regression accounts for.

The formula makes the decomposition explicit. **Total sum of squares** (SST) = Σ(yᵢ − ȳ)² measures the total variation in the outcome around its unconditional mean. **Residual sum of squares** (SSR) = Σ(yᵢ − ŷᵢ)² is the unexplained variation that remains after fitting the model. R² = 1 − SSR/SST. When the model perfectly fits every data point, SSR = 0 and R² = 1. When the model simply predicts the mean for every observation (no regressors at all), SSR = SST and R² = 0. An R² of 0.60 means the regressors collectively account for 60% of the variation in y; the remaining 40% is unexplained.

A crucial mechanical fact: **adding any variable to a regression can never decrease R²**. OLS can always set a new coefficient to zero if the variable adds nothing, so SSR can only stay flat or fall, meaning R² can only stay flat or rise. This is why comparing R² across models with different numbers of predictors is misleading — you could achieve R² = 0.99 by including enough noise variables. **Adjusted R²** corrects for this by penalizing the loss of degrees of freedom: R̄² = 1 − [SSR/(n−k−1)] / [SST/(n−1)], where k is the number of regressors. The adjustment means adding a truly uninformative variable can lower R̄², making it a better model comparison tool than raw R².

The deepest point — and the most consequential misconception — is that R² has nothing to do with whether your regression is correctly specified for causal inference. The key OLS assumption for unbiased estimation is E[u|x] = 0: the regressors are uncorrelated with the error term. R² measures explained variance regardless of whether this assumption holds. You can have R² = 0.95 with severe omitted variable bias, and R² = 0.04 with a clean randomized experiment delivering perfectly unbiased coefficients. As you move further into econometrics, you will regularly see researchers report very low R² without apology — they are pursuing credible identification of a causal effect, not maximizing explained variance. The two goals are genuinely separate.
