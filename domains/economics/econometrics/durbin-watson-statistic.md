---
id: durbin-watson-statistic
title: Durbin-Watson Statistic for Autocorrelation
domain: economics
course: econometrics
prerequisites:
- id: autocorrelation-lag-structure
  type: hard
builds-toward:
- breusch-godfrey-test
tags:
- autocorrelation
- diagnostics
- testing
stage: formal-systems
status: draft
---

# Durbin-Watson Statistic for Autocorrelation

## Core Idea
The Durbin-Watson statistic DW = Σ(ûₜ - ûₜ₋₁)² / Σûₜ² approximates 2(1 - ρ̂) where ρ̂ is the first-order autocorrelation. Values near 2 suggest no autocorr, < 2 suggests positive autocorr, and > 2 suggests negative autocorr, providing a quick diagnostic.

## Questions

```yaml
- question: "A time-series regression yields a Durbin-Watson statistic of 0.4. What does this indicate about the residuals?"
  type: multiple-choice
  options:
    - "Strong negative autocorrelation — residuals alternate in sign"
    - "No autocorrelation — residuals are approximately independent"
    - "Strong positive autocorrelation — consecutive residuals tend to be similar in sign and magnitude"
    - "The test is inconclusive and no inference can be drawn"
  answer: 2
  explanation: "DW ≈ 2(1 − ρ̂), so DW = 0.4 implies ρ̂ ≈ 0.8 — strong positive first-order autocorrelation. This means ûₜ and ûₜ₋₁ tend to be similar, making consecutive differences small, shrinking the numerator, and pushing DW toward 0. This violates OLS assumptions: standard errors are biased downward, inflating t-statistics and making coefficients appear more significant than they are."

- question: "A researcher estimates Yₜ = α + βYₜ₋₁ + εₜ, computes DW = 1.95, and concludes there is no autocorrelation. Is this valid?"
  type: multiple-choice
  options:
    - "Yes — DW near 2 always indicates no autocorrelation regardless of model specification"
    - "No — DW is biased toward 2 when a lagged dependent variable is included, making it unreliable"
    - "No — DW only applies to cross-sectional data, not time-series regressions"
    - "Yes — the lagged dependent variable controls for autocorrelation, so DW remains valid"
  answer: 1
  explanation: "When a lagged dependent variable appears as a regressor, the DW statistic is biased toward 2, making it appear that there is no autocorrelation even when true autocorrelation exists. The residuals are mechanically correlated with the lagged regressor in a way that violates the test's assumptions. For models with lagged dependent variables, the Breusch-Godfrey test is the appropriate diagnostic — it explicitly handles this structure."

- question: "A Durbin-Watson value near 4 indicates strong negative first-order autocorrelation in the residuals."
  type: true-false
  answer: true
  explanation: "DW ≈ 2(1 − ρ̂). If ρ̂ ≈ −1, then DW ≈ 2(1 − (−1)) = 4. Negative autocorrelation means consecutive residuals alternate in sign: positive, then negative, then positive. This makes consecutive differences (ûₜ − ûₜ₋₁) large, inflating the numerator and pushing DW toward 4. Like positive autocorrelation, negative autocorrelation biases OLS standard errors and invalidates inference."

- question: "The Durbin-Watson test can detect autocorrelation at any lag order, making it a comprehensive diagnostic for time-series residuals."
  type: true-false
  answer: false
  explanation: "DW only tests for first-order autocorrelation — whether ûₜ is correlated with ûₜ₋₁. It has no power to detect higher-order patterns such as quarterly seasonality (correlation at lag 4) or annual cycles (lag 12). A series with AR(4) structure but no AR(1) component could produce a DW near 2, falsely suggesting clean residuals. The Breusch-Godfrey test generalizes DW to test autocorrelation at any specified lag order."

- question: "Why does the Durbin-Watson test give invalid results when a lagged dependent variable appears as a regressor?"
  type: short-answer
  answer: "The DW test assumes that, under the null of no autocorrelation, the residuals are uncorrelated with each other and with the regressors. When a lagged dependent variable (Yₜ₋₁) is a regressor, OLS residuals ûₜ are mechanically correlated with the lagged regressor by construction. This correlation causes the DW statistic to be biased toward 2, making it appear that autocorrelation is absent even when it exists. The test's asymptotic distribution is no longer valid under this specification."
  explanation: "Intuitively, the model already 'absorbs' some time structure through the lagged DV, making residuals look more random than they truly are. The Breusch-Godfrey test handles this by explicitly modeling the relationship between residuals and lagged regressors in an auxiliary regression, making it robust to situations where DW is not."
```

## Explainer

From your study of autocorrelation and lag structures, you know that when regression residuals are correlated over time, OLS standard errors are biased and t-statistics are unreliable. The Durbin-Watson statistic is the standard first-pass diagnostic for detecting this problem. Its formula — the sum of squared *differences* between consecutive residuals, divided by the sum of squared residuals — is designed to measure exactly how much each residual resembles the one that came before it.

The key insight is the relationship DW ≈ 2(1 − ρ̂). If there is no autocorrelation, ρ̂ ≈ 0, so DW ≈ 2. If residuals are strongly **positively autocorrelated** (ρ̂ close to +1, meaning each residual is similar to the previous one), then consecutive differences are small, making the numerator small, and DW approaches 0. If residuals are strongly **negatively autocorrelated** (ρ̂ close to −1, meaning residuals alternate in sign), then each difference is large, and DW approaches 4. So the full scale runs 0 to 4, with 2 as the "clean" value.

In practice, you compare the computed DW statistic to critical bounds dL and dU from the Durbin-Watson tables (which depend on sample size n and the number of regressors k). If DW < dL, reject the null of no positive autocorrelation. If DW > 4 − dL, reject the null of no negative autocorrelation. Between dL and dU is an inconclusive zone — not evidence of no autocorrelation, but not decisive evidence against it either. This inconclusive region is one of the test's known limitations.

The Durbin-Watson statistic has two important restrictions to internalize. First, it only tests for **first-order** autocorrelation — whether ûₜ is correlated with ûₜ₋₁. It will miss higher-order patterns (e.g., quarterly seasonality where ûₜ correlates with ûₜ₋₄). Second, it is invalid when a lagged dependent variable appears as a regressor, because in that case the residuals are mechanically correlated with the regressor, violating the test's assumptions. For those more complex situations, you will next encounter the Breusch-Godfrey test, which handles both higher-order autocorrelation and lagged-dependent-variable models.
