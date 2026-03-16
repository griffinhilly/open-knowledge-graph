---
id: volatility-garch-modeling
title: Modeling Time-Varying Volatility with GARCH
domain: economics
course: financial-economics
prerequisites:
- id: expected-return-and-variance-of-assets
  type: hard
- id: autoregressive-ar-models
  type: soft
- id: expected-value-and-variance-of-assets
  type: soft
builds-toward:
- options-implied-volatility-extraction
tags:
- volatility
- garch
- forecasting
- modeling
stage: formal-systems
status: draft
---

# Modeling Time-Varying Volatility with GARCH

## Core Idea
GARCH models capture volatility clustering—the tendency for large price changes to be followed by more volatility. A GARCH(1,1) model expresses conditional variance as a weighted average of lagged squared returns and past variance: σ²_t = ω + αε²_{t-1} + βσ²_{t-1}. This is superior to constant volatility for option pricing, risk management, and portfolio construction.

## How It's Best Learned
Estimate GARCH parameters using actual return data and compare one-step-ahead volatility forecasts to realized volatility measures.

## Explainer

From your work on asset returns, you know that variance (σ²) is the standard measure of risk, and that portfolio optimization requires estimates of expected return and variance for each asset. The implicit assumption in the basic framework is that variance is constant over time. Empirically, this is wrong in a very structured way: financial return series exhibit **volatility clustering**, meaning large price moves (positive or negative) tend to cluster together, followed by calmer periods. A plot of daily stock returns makes this obvious — the series looks like alternating stretches of high-amplitude and low-amplitude fluctuations. A constant-variance model misses this pattern entirely.

**GARCH** (Generalized Autoregressive Conditional Heteroskedasticity) models volatility as a time-varying process with memory. The GARCH(1,1) model specifies the conditional variance as:
σ²ₜ = ω + αε²ₜ₋₁ + βσ²ₜ₋₁

Each term has an intuition. The constant ω sets a floor — it ensures variance doesn't collapse to zero. The term αε²ₜ₋₁ is the **news** component: if yesterday's return was surprisingly large (ε² is large), today's variance estimate gets updated upward. This is the autoregressive part applied to squared residuals — just as an AR model says today's value depends on yesterday's, GARCH says today's variance depends on yesterday's shock. The term βσ²ₜ₋₁ is the **persistence** component: it carries forward the previous variance estimate, capturing the fact that volatility regimes (high-volatility or low-volatility periods) tend to last for days or weeks, not just one period.

The parameter sum α+β controls how quickly volatility reverts to its long-run average ω/(1−α−β). If α+β is close to 1 (typical for equity markets, often 0.98–0.99), volatility is highly persistent — a shock to volatility today will still be felt weeks later. If α+β < 1, the process is stationary and volatility eventually mean-reverts. If α+β = 1, you have an **IGARCH** model (integrated GARCH), where shocks are permanent. In practice, equity index volatility is estimated with α ≈ 0.05–0.10 and β ≈ 0.85–0.90: large persistence, but with a meaningful news component. The connection to AR models from your time series prerequisite is exact: just as ARMA models capture autocorrelation in the first moment (the level) of a series, GARCH captures autocorrelation in the second moment (the variance). You can verify this by running an AR(1) on the squared returns from a GARCH process — the autocorrelation will be detectable.

GARCH-based volatility forecasts are used in option pricing (replacing the constant σ in Black-Scholes with a time-varying conditional variance), value-at-risk calculations (dynamic VaR uses today's GARCH estimate instead of a fixed historical window), and portfolio rebalancing (downweight assets when their conditional volatility spikes). Extensions like **EGARCH** and **GJR-GARCH** capture the **leverage effect** — the empirical finding that negative return shocks increase volatility more than positive shocks of the same magnitude — which the symmetric GARCH(1,1) misses.
