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

## Explainer

You already know that OLS assumes the errors are uncorrelated with each other — that's one of the core OLS assumptions. In cross-sectional data, this is often plausible: the measurement error on one person's wage has nothing to do with another's. But in time-series data, this assumption is routinely violated. If GDP was above trend last quarter, it tends to be above trend this quarter too. That persistence in the outcome bleeds into the residuals if your model doesn't fully explain it, creating **autocorrelation** — each error is correlated with its own past.

The most common pattern is **AR(1) autocorrelation**, where the error today is a scaled version of yesterday's error plus a new shock: uₜ = ρuₜ₋₁ + εₜ. The parameter ρ (rho) measures how persistent the correlation is. If ρ = 0.8, today's error is strongly predicted by yesterday's. If ρ = 0, errors are independent and you're fine. When autocorrelation exists, OLS still finds the same coefficient estimates — it remains unbiased — but the formula it uses to compute standard errors assumes independent errors, so those standard errors are wrong. Typically they are too small, making t-statistics too large and inference too confident.

The sources of autocorrelation give you a diagnostic roadmap. **Omitted variables** that are themselves persistent will inject their dynamics into your residuals — if you're modeling consumption but omit consumer sentiment (which drifts slowly), the omitted variable's autocorrelation becomes your residuals' autocorrelation. **Model misspecification** — for instance, fitting a linear trend to an exponentially growing series — leaves a systematic curved pattern in residuals, which appears as autocorrelation even if the underlying errors aren't. **True dynamics** are a third source: if the true model should include lagged Y on the right-hand side (because yesterday's outcome causes today's), omitting those lags forces the dynamic into the error term.

Understanding the **lag structure** matters because not all autocorrelation is AR(1). MA(1) errors (where this period's error depends on last period's shock but not last period's error) have a different pattern: significant autocorrelation at lag 1 only. Seasonal data can show autocorrelation at lag 12 (monthly) or lag 4 (quarterly). The autocorrelation function (ACF) and partial autocorrelation function (PACF) plots reveal these patterns — a slow decay in the ACF is diagnostic of AR structure, while a sharp cutoff points to MA structure. Before applying any correction (GLS, Newey-West standard errors, adding lags), diagnose the pattern carefully: the right fix depends on the right diagnosis.

