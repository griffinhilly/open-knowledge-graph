---
id: inference-in-linear-regression
title: Inference in Linear Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: regression-diagnostics
  type: hard
- id: t-test-for-means
  type: soft
builds-toward:
- prediction-intervals-regression
tags:
- regression
- inference
- testing
stage: formal-systems
status: draft
---

# Inference in Linear Regression

## Core Idea
Under standard regression assumptions, regression coefficients are normally distributed. We construct confidence intervals and tests for slope using t-distributions. F-test assesses overall model significance. Inference requires assumptions about errors.

## How It's Best Learned
Examine regression output with coefficients, SE, t-statistics, and p-values. Test whether slope differs from zero. Construct confidence intervals for slope and intercept. Compare F-test to t-test for single predictor.

## Explainer

In simple linear regression, you fit a line ŷ = β₀ + β₁x to data by ordinary least squares. The estimated coefficients β̂₀ and β̂₁ come from one particular sample — a different sample would give different values. To make statements about the true population relationship, you need to understand the sampling distribution of β̂₁. The model assumes errors εᵢ = yᵢ - (β₀ + β₁xᵢ) are independent with mean zero and constant variance σ². Under these assumptions, the OLS estimators are linear combinations of the y values. Since the y values are the fixed x values plus normal errors, a linear combination of normal random variables is itself normal. This is why **β̂₁ is normally distributed** with mean β₁ (it is unbiased) and variance σ²/Σ(xᵢ - x̄)².

Because σ² is unknown, substitute the mean squared error s² = SSE/(n-2). The ratio (β̂₁ - β₁)/(s/√Σ(xᵢ - x̄)²) follows a t-distribution with n-2 degrees of freedom — the same form as the one-sample t-test you studied, just with a different standard error formula. The denominator s/√Σ(xᵢ - x̄)² is the **standard error of the slope**, written SE(β̂₁). Every regression output table reports: the estimate β̂₁, its SE(β̂₁), the t-statistic t = β̂₁/SE(β̂₁) (testing H₀: β₁ = 0), and the associated p-value. A confidence interval for β₁ is β̂₁ ± t* · SE(β̂₁), exactly parallel to the one-sample t-interval.

The **F-test** assesses overall model significance: is the regression model better than predicting with the mean alone? It computes F = (explained variance / k) / (unexplained variance / (n - k - 1)), where k is the number of predictors. For simple linear regression (k = 1), F = t², so the F-test and t-test for the slope test the same null hypothesis and always give the same p-value. With multiple predictors, the F-test becomes a joint test — all slopes are zero simultaneously — while t-tests address individual coefficients. The F-test answers "does this model explain anything?" while t-tests answer "does this specific predictor matter given the others?"

All of these inference procedures rest on the regression assumptions your diagnostics verify: linearity of the mean function, independence of errors, constant variance across all x values (homoskedasticity), and approximate normality of residuals. If residuals fan out at high fitted values, heteroskedasticity inflates or deflates standard errors and makes p-values misleading. If the residual plot curves, the linear form is wrong and the slope coefficient is not meaningfully estimating any population quantity. Inference in regression is inseparable from diagnostics — the t and F statistics are only trustworthy when the model's foundations are sound.
