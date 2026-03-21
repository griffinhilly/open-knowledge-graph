---
id: autocorrelation-lag-structure
title: 'Autocorrelation: Structure and Sources'
domain: economics
course: econometrics
prerequisites:
- id: ols-assumptions
  type: hard
- id: time-series-basics-econometrics
  type: hard
builds-toward:
- durbin-watson-statistic
tags:
- autocorrelation
- time-series
- diagnostics
stage: formal-systems
status: draft
---

# Autocorrelation: Structure and Sources

## Core Idea
Autocorrelation (serial correlation) occurs when errors are correlated over time: Cov(uₜ, uₛ) ≠ 0 for t ≠ s, often following an AR(1) structure. Sources include omitted variables, model misspecification, or true dynamics. Autocorrelation does not bias OLS but inflates standard errors, invalidating inference.

## Questions

```yaml
- question: "You estimate an OLS regression on time-series data and diagnostic tests reveal AR(1) autocorrelation (ρ ≈ 0.75) in the residuals. What is the primary statistical consequence you should be concerned about?"
  type: multiple-choice
  options:
    - "The coefficient estimates are biased and do not represent the true population parameters"
    - "The standard errors are wrong (typically too small), making t-statistics and p-values unreliable"
    - "The R² statistic is inflated, overstating the model's explanatory power"
    - "The coefficient estimates are inefficient, but since they are unbiased, inference proceeds normally"
  answer: 1
  explanation: "Autocorrelation does not bias OLS coefficient estimates — they remain unbiased (and consistent). But the OLS standard error formula assumes uncorrelated errors; with autocorrelation, those formula-derived standard errors are incorrect, typically too small. This makes t-statistics appear larger than they should be and p-values smaller, leading to false confidence in statistical significance. Option D correctly identifies that coefficients are unbiased but wrongly concludes that inference proceeds normally — the standard errors are broken."

- question: "A researcher fits a linear trend to GDP data that grows exponentially. Even if the true underlying shocks are independent white noise, what will the residuals likely show?"
  type: multiple-choice
  options:
    - "No autocorrelation, since the shocks are independent by assumption"
    - "Negative autocorrelation, because the model alternates between over- and under-prediction"
    - "Positive autocorrelation, because the misspecified model leaves a systematic curved pattern in residuals"
    - "Heteroskedasticity but not autocorrelation, since the variance grows with the level"
  answer: 2
  explanation: "Model misspecification can generate apparent autocorrelation even when the true errors are white noise. A linear trend fitted to exponential growth will under-predict in the early and late periods and over-predict in the middle (or vice versa), leaving a systematic curved residual pattern that manifests as positive autocorrelation. This is a crucial diagnostic insight: residual autocorrelation may signal misspecification (wrong functional form, wrong trend specification) rather than a fundamentally autocorrelated error process."

- question: "When OLS is applied to time-series data with AR(1) autocorrelation, the regression coefficients are biased."
  type: true-false
  answer: false
  explanation: "Autocorrelation violates one of the classical OLS assumptions, but it does not cause bias in the coefficient estimates. OLS remains unbiased (and consistent) under autocorrelation. What breaks is the validity of the standard error formulas, which assume Cov(uₜ, uₛ) = 0 for t ≠ s. With correlated errors, the true sampling variance of the estimates is different from what the OLS formula computes. The practical consequence is invalid inference, not biased estimates."

- question: "An ACF plot that decays slowly and geometrically across many lags is diagnostic of AR-type autocorrelation structure."
  type: true-false
  answer: true
  explanation: "AR(p) processes produce an ACF that decays gradually (often geometrically for AR(1)) and a PACF that cuts off sharply after lag p. A slow, exponential decay in the ACF across many lags is the signature pattern of autoregressive structure. By contrast, an MA(q) process shows the opposite: the ACF cuts off sharply after lag q while the PACF decays slowly. Correctly reading these patterns from ACF/PACF plots is essential for diagnosing the type of autocorrelation and choosing the appropriate correction."

- question: "Why does autocorrelation in OLS residuals lead to incorrect statistical inferences even though the coefficient estimates themselves are still correct?"
  type: short-answer
  answer: "OLS coefficient estimates are unbiased and consistent under autocorrelation — the same conditional expectation formula applies. But the OLS standard error formula is derived under the assumption of uncorrelated errors (Cov(uₜ, uₛ) = 0). With positive autocorrelation, adjacent observations carry redundant information, and the effective sample size is smaller than the actual n. The standard errors that assume independent observations therefore understate the true uncertainty around the estimates, making the t-ratios too large and the p-values too small. Researchers who trust those standard errors will reject null hypotheses too often — a false precision problem."
  explanation: "A useful analogy: if you survey the same 100 people twice and pool the 200 responses as if they were independent, your standard errors will be too small because the two observations from each person are correlated. Autocorrelation in time-series data creates an analogous problem: observations close in time are not independent, so treating them as if they are overstates the information content of the sample."
```

## Explainer

You already know that OLS assumes the errors are uncorrelated with each other — that's one of the core OLS assumptions. In cross-sectional data, this is often plausible: the measurement error on one person's wage has nothing to do with another's. But in time-series data, this assumption is routinely violated. If GDP was above trend last quarter, it tends to be above trend this quarter too. That persistence in the outcome bleeds into the residuals if your model doesn't fully explain it, creating **autocorrelation** — each error is correlated with its own past.

The most common pattern is **AR(1) autocorrelation**, where the error today is a scaled version of yesterday's error plus a new shock: uₜ = ρuₜ₋₁ + εₜ. The parameter ρ (rho) measures how persistent the correlation is. If ρ = 0.8, today's error is strongly predicted by yesterday's. If ρ = 0, errors are independent and you're fine. When autocorrelation exists, OLS still finds the same coefficient estimates — it remains unbiased — but the formula it uses to compute standard errors assumes independent errors, so those standard errors are wrong. Typically they are too small, making t-statistics too large and inference too confident.

The sources of autocorrelation give you a diagnostic roadmap. **Omitted variables** that are themselves persistent will inject their dynamics into your residuals — if you're modeling consumption but omit consumer sentiment (which drifts slowly), the omitted variable's autocorrelation becomes your residuals' autocorrelation. **Model misspecification** — for instance, fitting a linear trend to an exponentially growing series — leaves a systematic curved pattern in residuals, which appears as autocorrelation even if the underlying errors aren't. **True dynamics** are a third source: if the true model should include lagged Y on the right-hand side (because yesterday's outcome causes today's), omitting those lags forces the dynamic into the error term.

Understanding the **lag structure** matters because not all autocorrelation is AR(1). MA(1) errors (where this period's error depends on last period's shock but not last period's error) have a different pattern: significant autocorrelation at lag 1 only. Seasonal data can show autocorrelation at lag 12 (monthly) or lag 4 (quarterly). The autocorrelation function (ACF) and partial autocorrelation function (PACF) plots reveal these patterns — a slow decay in the ACF is diagnostic of AR structure, while a sharp cutoff points to MA structure. Before applying any correction (GLS, Newey-West standard errors, adding lags), diagnose the pattern carefully: the right fix depends on the right diagnosis.

