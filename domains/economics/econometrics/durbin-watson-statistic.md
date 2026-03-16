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

## Explainer

From your study of autocorrelation and lag structures, you know that when regression residuals are correlated over time, OLS standard errors are biased and t-statistics are unreliable. The Durbin-Watson statistic is the standard first-pass diagnostic for detecting this problem. Its formula — the sum of squared *differences* between consecutive residuals, divided by the sum of squared residuals — is designed to measure exactly how much each residual resembles the one that came before it.

The key insight is the relationship DW ≈ 2(1 − ρ̂). If there is no autocorrelation, ρ̂ ≈ 0, so DW ≈ 2. If residuals are strongly **positively autocorrelated** (ρ̂ close to +1, meaning each residual is similar to the previous one), then consecutive differences are small, making the numerator small, and DW approaches 0. If residuals are strongly **negatively autocorrelated** (ρ̂ close to −1, meaning residuals alternate in sign), then each difference is large, and DW approaches 4. So the full scale runs 0 to 4, with 2 as the "clean" value.

In practice, you compare the computed DW statistic to critical bounds dL and dU from the Durbin-Watson tables (which depend on sample size n and the number of regressors k). If DW < dL, reject the null of no positive autocorrelation. If DW > 4 − dL, reject the null of no negative autocorrelation. Between dL and dU is an inconclusive zone — not evidence of no autocorrelation, but not decisive evidence against it either. This inconclusive region is one of the test's known limitations.

The Durbin-Watson statistic has two important restrictions to internalize. First, it only tests for **first-order** autocorrelation — whether ûₜ is correlated with ûₜ₋₁. It will miss higher-order patterns (e.g., quarterly seasonality where ûₜ correlates with ûₜ₋₄). Second, it is invalid when a lagged dependent variable appears as a regressor, because in that case the residuals are mechanically correlated with the regressor, violating the test's assumptions. For those more complex situations, you will next encounter the Breusch-Godfrey test, which handles both higher-order autocorrelation and lagged-dependent-variable models.
