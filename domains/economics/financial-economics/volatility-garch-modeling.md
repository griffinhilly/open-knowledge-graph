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
builds-toward: []
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

## Questions

```yaml
- question: "Following a major market crash, a GARCH(1,1) model estimates today's conditional volatility as very high. With α = 0.09 and β = 0.90, how will volatility behave over the following weeks?"
  type: multiple-choice
  options:
    - "Volatility will immediately return to the long-run average since markets are efficient"
    - "Volatility will remain elevated for weeks, decaying gradually, because α + β = 0.99 indicates very high persistence"
    - "Volatility will continue rising indefinitely as past shocks compound"
    - "The model cannot forecast future volatility — GARCH only describes current variance"
  answer: 1
  explanation: "The parameter sum α + β = 0.99 controls how quickly conditional variance reverts to its long-run mean ω/(1 − α − β). With the sum close to 1, shocks decay very slowly — each period retains 99% of the previous period's elevated variance. This captures the empirical reality of volatility clustering: after a major shock, elevated volatility persists for days or weeks, not just one period. Markets can be informationally efficient and still exhibit this second-moment persistence."

- question: "In the GARCH(1,1) equation σ²ₜ = ω + αε²ₜ₋₁ + βσ²ₜ₋₁, what does the term αε²ₜ₋₁ represent?"
  type: multiple-choice
  options:
    - "The long-run average variance level that the process mean-reverts toward"
    - "The persistence of yesterday's variance estimate carried into today's forecast"
    - "The impact of yesterday's unexpected return shock on today's conditional variance"
    - "The leverage effect from negative returns exceeding positive returns of the same size"
  answer: 2
  explanation: "ε²ₜ₋₁ is the squared residual from yesterday — the unexpected return, large when there was a surprise move (positive or negative). The α coefficient scales how much this 'news' updates the current variance estimate. A large shock yesterday (ε² large) pushes today's estimated variance upward. This is the 'news impact' or ARCH component. The β term separately captures persistence — carrying forward the previous variance estimate regardless of what new shock arrived."

- question: "In a GARCH(1,1) model, volatility is assumed constant across time, with shocks causing only temporary, single-period deviations before immediately reverting."
  type: true-false
  answer: false
  explanation: "GARCH is explicitly designed to model time-varying volatility. The β term (typically 0.85–0.90 in equity markets) ensures shocks persist across multiple periods: a large ε²ₜ today raises σ²ₜ₊₁, which carries over into σ²ₜ₊₂, and so on. A constant-variance model (ARCH(0)) would assume all shocks die after one period. GARCH's improvement over constant variance is precisely capturing this multi-period clustering of volatility."

- question: "The closer α + β is to 1 in a GARCH(1,1) model, the more persistent volatility is and the slower it reverts to its long-run average."
  type: true-false
  answer: true
  explanation: "The long-run variance is ω/(1 − α − β), and the speed of reversion toward it after a shock is governed by (α + β). When α + β = 1 (IGARCH), shocks are permanent — volatility never mean-reverts. When α + β = 0.99 (typical for equity indices), reversion is extremely slow. When α + β = 0.80, reversion is much faster. This parameter sum is therefore the key indicator of how long-lived volatility episodes will be."

- question: "What is volatility clustering, and why does it make the constant-variance assumption inadequate for modeling financial returns?"
  type: short-answer
  answer: "Volatility clustering is the empirical pattern where large price changes tend to be followed by more large price changes, and calm periods by more calm periods — regardless of sign. A constant-variance model assigns the same σ² to every time period, which is contradicted by this autocorrelation in the magnitude of returns. In calm periods it overestimates risk; in turbulent periods it underestimates it. GARCH addresses this by making σ²ₜ a function of past shocks and past variance, allowing the model to track changing risk levels dynamically."
  explanation: "The practical consequence of ignoring volatility clustering is severe: risk management models (VaR) become unreliable, option prices are mispriced (constant-σ Black-Scholes prices are wrong during high-volatility regimes), and portfolio allocations based on a fixed σ are stale. GARCH's time-varying conditional variance gives a day-specific risk estimate, which is why it became standard in financial risk management."
```

## Explainer

From your work on asset returns, you know that variance (σ²) is the standard measure of risk, and that portfolio optimization requires estimates of expected return and variance for each asset. The implicit assumption in the basic framework is that variance is constant over time. Empirically, this is wrong in a very structured way: financial return series exhibit **volatility clustering**, meaning large price moves (positive or negative) tend to cluster together, followed by calmer periods. A plot of daily stock returns makes this obvious — the series looks like alternating stretches of high-amplitude and low-amplitude fluctuations. A constant-variance model misses this pattern entirely.

**GARCH** (Generalized Autoregressive Conditional Heteroskedasticity) models volatility as a time-varying process with memory. The GARCH(1,1) model specifies the conditional variance as:
σ²ₜ = ω + αε²ₜ₋₁ + βσ²ₜ₋₁

Each term has an intuition. The constant ω sets a floor — it ensures variance doesn't collapse to zero. The term αε²ₜ₋₁ is the **news** component: if yesterday's return was surprisingly large (ε² is large), today's variance estimate gets updated upward. This is the autoregressive part applied to squared residuals — just as an AR model says today's value depends on yesterday's, GARCH says today's variance depends on yesterday's shock. The term βσ²ₜ₋₁ is the **persistence** component: it carries forward the previous variance estimate, capturing the fact that volatility regimes (high-volatility or low-volatility periods) tend to last for days or weeks, not just one period.

The parameter sum α+β controls how quickly volatility reverts to its long-run average ω/(1−α−β). If α+β is close to 1 (typical for equity markets, often 0.98–0.99), volatility is highly persistent — a shock to volatility today will still be felt weeks later. If α+β < 1, the process is stationary and volatility eventually mean-reverts. If α+β = 1, you have an **IGARCH** model (integrated GARCH), where shocks are permanent. In practice, equity index volatility is estimated with α ≈ 0.05–0.10 and β ≈ 0.85–0.90: large persistence, but with a meaningful news component. The connection to AR models from your time series prerequisite is exact: just as ARMA models capture autocorrelation in the first moment (the level) of a series, GARCH captures autocorrelation in the second moment (the variance). You can verify this by running an AR(1) on the squared returns from a GARCH process — the autocorrelation will be detectable.

GARCH-based volatility forecasts are used in option pricing (replacing the constant σ in Black-Scholes with a time-varying conditional variance), value-at-risk calculations (dynamic VaR uses today's GARCH estimate instead of a fixed historical window), and portfolio rebalancing (downweight assets when their conditional volatility spikes). Extensions like **EGARCH** and **GJR-GARCH** capture the **leverage effect** — the empirical finding that negative return shocks increase volatility more than positive shocks of the same magnitude — which the symmetric GARCH(1,1) misses.
