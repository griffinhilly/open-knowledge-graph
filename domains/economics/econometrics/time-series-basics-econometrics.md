---
id: time-series-basics-econometrics
title: 'Time Series Data: Structure and Concepts'
domain: economics
course: econometrics
prerequisites:
- id: econometrics-intro
  type: hard
- id: gdp-and-national-income
  type: soft
- id: business-cycles
  type: soft
- id: sequences-and-series-review
  type: soft
- id: probability-theory
  type: hard
- id: sequences-and-series
  type: soft
builds-toward:
- stationarity-and-unit-roots
- serial-correlation
tags:
- time-series
- autocorrelation
- trend
- seasonality
stage: formal-systems
status: validated
---

# Time Series Data: Structure and Concepts

## Core Idea
Time series data records observations on a single unit at sequential, equally spaced time points — GDP, unemployment, or stock prices over quarters or years. Unlike cross-sectional data, time series observations are ordered and typically autocorrelated: past values predict future values. Standard OLS assumptions break down because errors are serially correlated and many economic variables have stochastic trends. Time series analysis requires specialized tools to account for the time dependence structure, distinguish short-run dynamics from long-run relationships, and handle non-stationary processes.

## How It's Best Learned
Plot GDP and the federal funds rate over several decades, visually identifying trends, recessions (business cycles), and co-movement — this builds intuition before formalizing with AR models and cointegration.

## Common Misconceptions
- A 'spurious regression' can show high R² and significant t-statistics between two trending but unrelated series — non-stationarity inflates test statistics.
- 'Seasonal adjustment' is a data preprocessing step, not a modeling technique; always clarify whether a series is seasonally adjusted before modeling.

## Questions

```yaml
- question: "Two trending variables — global average temperature and the number of pirates worldwide since 1800 — show a high R² and a statistically significant coefficient when regressed on each other. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "Pirates causally affect climate through ocean disruption"
    - "The regression suffers from omitted variable bias"
    - "Both variables share a time trend, producing a spurious regression"
    - "The OLS estimator is consistent when applied to time series"
  answer: 2
  explanation: "This is a classic spurious regression: two unrelated non-stationary series that both trend over time will appear strongly correlated because their shared trend dominates. High R² and significant t-statistics do not indicate a real relationship — they reflect the shared trend. Standard OLS inference is invalid for non-stationary series."

- question: "A time series with a stochastic trend is stationary after first-differencing."
  type: true-false
  answer: true
  explanation: "A random walk (the canonical stochastic trend) has the form Yₜ = Yₜ₋₁ + εₜ. First-differencing yields ΔYₜ = εₜ, which is white noise — stationary with constant mean and variance. This is why differencing is a standard preprocessing step before applying OLS to time series data. A series that becomes stationary after one difference is called 'integrated of order 1' or I(1)."

- question: "Why does autocorrelation in the error term cause problems for standard OLS inference, even if OLS coefficient estimates remain unbiased?"
  type: short-answer
  answer: "OLS standard errors are derived under the assumption that errors are uncorrelated. When errors are autocorrelated, the OLS formula for standard errors underestimates the true sampling variability, making t-statistics too large and p-values too small — leading to false positives."
  explanation: "Autocorrelation violates the Gauss-Markov assumption of uncorrelated errors. While the OLS coefficient estimator remains unbiased (errors average out), the estimated variance of those coefficients is biased downward because the standard OLS formula ignores the covariance between error terms across time. The result is overconfident inference — rejecting null hypotheses too often."
```

## Explainer

In cross-sectional data, each observation is an independent draw: one observation on household 47 tells you nothing about household 48. Time series data breaks this assumption. GDP in Q3 is strongly predicted by GDP in Q2, which was predicted by Q1. This temporal dependence — autocorrelation — is not a nuisance; it is the defining feature of time series data and must be modeled explicitly rather than ignored.

Most macroeconomic time series have a trend: they tend to grow over time (GDP, price levels) or fluctuate around a persistent level (interest rates, unemployment). This creates non-stationarity — the statistical properties of the series (mean, variance) change over time. A stationary series has a constant mean and variance that it returns to after any shock. A non-stationary series, by contrast, wanders without reversion. The difference matters enormously for what statistical tools are valid.

The most dangerous pitfall is spurious regression. If you regress two non-stationary series on each other — even if they are completely unrelated — you will typically find high R² and statistically significant coefficients. Both series share a common time trend, and OLS interprets that shared drift as evidence of a relationship. Before running any regression with time series data, you must test whether the series are stationary; if not, you need to either difference the data or use cointegration methods.

Trends can be deterministic (a fixed formula like t or t²) or stochastic (a random walk, where shocks permanently accumulate). The distinction matters for how you remove the trend. For a deterministic trend, you can include a time trend variable in the regression. For a stochastic trend (unit root), you need to first-difference the data. Misdiagnosing the type of trend leads to incorrect detrending and invalid inference.

Time series also exhibit seasonality — regular patterns at fixed intervals (retail sales peak in December, agricultural output peaks at harvest). Seasonality is typically handled by seasonal differencing or adding seasonal dummy variables, or by working with seasonally adjusted data published by statistical agencies. Understanding whether a series is "raw" or "seasonally adjusted" is one of the first things to check before modeling.
