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
- id: multiple-regression-intro
  type: soft
builds-toward:
- prediction-intervals-regression
tags:
- regression
- inference
- testing
stage: formal-systems
status: validated
---
# Inference in Linear Regression

## Core Idea
Under standard regression assumptions, regression coefficients are normally distributed. We construct confidence intervals and tests for slope using t-distributions. F-test assesses overall model significance. Inference requires assumptions about errors.

## How It's Best Learned
Examine regression output with coefficients, SE, t-statistics, and p-values. Test whether slope differs from zero. Construct confidence intervals for slope and intercept. Compare F-test to t-test for single predictor.

## Questions

```yaml
- question: "A regression output shows a slope estimate with p < 0.001, suggesting a highly significant predictor. However, the residual plot shows a strong funnel pattern — residuals spread much wider at high fitted values than at low ones. What should you conclude?"
  type: multiple-choice
  options:
    - "The regression is reliable; a significant p-value overrides any concerns about the residual plot"
    - "The p-value may be misleading because heteroskedasticity distorts standard errors, making inference invalid"
    - "The funnel pattern is normal and only affects predictions at the extremes, not inference on the slope"
    - "The solution is to remove the high-leverage points and refit the model"
  answer: 1
  explanation: "Heteroskedasticity — non-constant error variance — violates a core regression assumption. The standard error SE(β̂₁) is derived assuming constant variance σ²; if variance grows with fitted values, this formula is wrong, which means the t-statistic and p-value are both wrong. A very small p-value may be inflated by underestimated standard errors, or a real effect may be masked by overestimated errors. Diagnostics are not optional decoration — they determine whether inference is trustworthy at all."

- question: "In a simple linear regression with one predictor, the t-test for the slope yields a p-value of 0.04. What does the F-test for overall model significance return?"
  type: multiple-choice
  options:
    - "0.0016 (= 0.04²), because F = t²"
    - "0.04 — the same p-value, because F = t² and the F and t tests are equivalent here"
    - "A different p-value that depends on the residual degrees of freedom"
    - "Cannot be determined without knowing the number of observations"
  answer: 1
  explanation: "For simple linear regression (exactly one predictor), the F-statistic equals the square of the t-statistic for the slope: F = t². But F and t² have the same p-value because the F distribution with (1, n−2) degrees of freedom and the t distribution with n−2 degrees of freedom are related in exactly this way. Both tests answer the same question: does the predictor explain any variance beyond the mean? The F-test becomes distinct from individual t-tests only in multiple regression, where it tests whether *all* predictors are jointly zero."

- question: "The standard error of the slope SE(β̂₁) decreases when the predictor values are more spread out — i.e., when Σ(xᵢ − x̄)² is larger."
  type: true-false
  answer: true
  explanation: "SE(β̂₁) = s / √Σ(xᵢ − x̄)², so larger spread in x (larger Σ(xᵢ − x̄)²) shrinks the standard error and increases precision. Intuitively, if your data spans a wide range of x values, the slope is more tightly estimated because you have more 'leverage' on the line's tilt. If all x values are clustered near x̄, even a small amount of noise can swing the slope dramatically, yielding a large SE."

- question: "In simple linear regression, the F-test for overall model significance and the t-test for the slope test different null hypotheses, which is why they can give different p-values."
  type: true-false
  answer: false
  explanation: "In simple linear regression (one predictor), the F-test and the t-test for the slope test exactly the same null hypothesis — H₀: β₁ = 0 — and always give the same p-value, because F = t². They differ only in multiple regression: there, the F-test jointly tests all slope coefficients simultaneously (H₀: β₁ = β₂ = ⋯ = 0), while each t-test assesses one predictor conditional on the others. For one predictor, the distinction collapses."

- question: "Why does heteroskedasticity (non-constant residual variance) threaten the validity of t-tests and confidence intervals for regression coefficients, even when the slope estimate β̂₁ itself remains unbiased?"
  type: short-answer
  answer: "OLS gives an unbiased estimate of β₁ regardless of whether variance is constant — heteroskedasticity does not cause bias in the estimate itself. But the t-statistic is computed as β̂₁ divided by its estimated standard error SE(β̂₁), and SE(β̂₁) is derived assuming errors have the same variance σ² at every x value. When variance is not constant, the formula produces a wrong SE — either too small (making effects look more significant than they are) or too large (masking real effects). Since p-values and confidence intervals are built on SE(β̂₁), they are unreliable whenever the homoskedasticity assumption fails."
  explanation: "Unbiasedness of β̂₁ and validity of inference are separate properties. Bias concerns the center of the sampling distribution; inference concerns its spread (standard error). Heteroskedasticity corrupts the spread estimate without shifting the center, so estimates can be accurate but their uncertainty can be wrongly characterized."
```

## Explainer

In simple linear regression, you fit a line ŷ = β₀ + β₁x to data by ordinary least squares. The estimated coefficients β̂₀ and β̂₁ come from one particular sample — a different sample would give different values. To make statements about the true population relationship, you need to understand the sampling distribution of β̂₁. The model assumes errors εᵢ = yᵢ - (β₀ + β₁xᵢ) are independent with mean zero and constant variance σ². Under these assumptions, the OLS estimators are linear combinations of the y values. Since the y values are the fixed x values plus normal errors, a linear combination of normal random variables is itself normal. This is why **β̂₁ is normally distributed** with mean β₁ (it is unbiased) and variance σ²/Σ(xᵢ - x̄)².

Because σ² is unknown, substitute the mean squared error s² = SSE/(n-2). The ratio (β̂₁ - β₁)/(s/√Σ(xᵢ - x̄)²) follows a t-distribution with n-2 degrees of freedom — the same form as the one-sample t-test you studied, just with a different standard error formula. The denominator s/√Σ(xᵢ - x̄)² is the **standard error of the slope**, written SE(β̂₁). Every regression output table reports: the estimate β̂₁, its SE(β̂₁), the t-statistic t = β̂₁/SE(β̂₁) (testing H₀: β₁ = 0), and the associated p-value. A confidence interval for β₁ is β̂₁ ± t* · SE(β̂₁), exactly parallel to the one-sample t-interval.

The **F-test** assesses overall model significance: is the regression model better than predicting with the mean alone? It computes F = (explained variance / k) / (unexplained variance / (n - k - 1)), where k is the number of predictors. For simple linear regression (k = 1), F = t², so the F-test and t-test for the slope test the same null hypothesis and always give the same p-value. With multiple predictors, the F-test becomes a joint test — all slopes are zero simultaneously — while t-tests address individual coefficients. The F-test answers "does this model explain anything?" while t-tests answer "does this specific predictor matter given the others?"

All of these inference procedures rest on the regression assumptions your diagnostics verify: linearity of the mean function, independence of errors, constant variance across all x values (homoskedasticity), and approximate normality of residuals. If residuals fan out at high fitted values, heteroskedasticity inflates or deflates standard errors and makes p-values misleading. If the residual plot curves, the linear form is wrong and the slope coefficient is not meaningfully estimating any population quantity. Inference in regression is inseparable from diagnostics — the t and F statistics are only trustworthy when the model's foundations are sound.
