---
id: value-at-risk-measurement
title: Value-at-Risk Measurement
domain: economics
course: financial-economics
prerequisites:
- id: portfolio-diversification
  type: hard
- id: variance-of-random-variables
  type: hard
- id: quantiles-and-percentiles
  type: hard
- id: probability-distributions
  type: hard
- id: normal-distribution-theory
  type: soft
tags:
- var
- risk-measurement
- quantitative
stage: formal-systems
status: draft
---

# Value-at-Risk Measurement

## Core Idea
Value at Risk (VaR) quantifies the maximum portfolio loss over a given time horizon at a specified confidence level (e.g., 95% or 99%). VaR can be calculated parametrically (assuming normal returns), historically, or through Monte Carlo simulation. VaR is widely used in regulation and risk management but underestimates tail risk (extreme losses).

## Explainer

You already know how to work with quantiles and probability distributions, and you know that portfolio diversification reduces variance. **Value at Risk (VaR)** puts those tools together into a single risk number: given a portfolio's return distribution, what is the threshold loss that will be exceeded only α% of the time over the next T days? A "one-day 99% VaR of $1 million" means: over the next trading day, there is a 1% probability of losing more than $1 million. Equivalently, the 1st percentile of the one-day loss distribution is $1 million.

The most common calculation method is **parametric VaR**, which assumes portfolio returns are normally distributed. You need three inputs: the portfolio's expected return (often assumed to be zero for short horizons), its standard deviation σ, and the desired confidence level. For a 99% one-tailed VaR, the critical value from the standard normal distribution is z = 2.326. So parametric VaR = −(μ + z × σ) × Portfolio value, where μ is the expected return. For a $10 million portfolio with daily standard deviation of 1%, one-day 99% VaR = 2.326 × 0.01 × $10M = $232,600. The appeal is simplicity: if you can estimate covariance matrices, you can compute VaR for any portfolio.

**Historical simulation VaR** avoids the normality assumption entirely by using actual past returns. Take the last 500 (or 1,000) trading days of portfolio returns, sort them, and find the 1st percentile — that is your 99% VaR. No distributional assumption required. The drawback is that historical VaR is only as good as the historical record: if the tail events in the lookback window were mild, the estimated VaR will be too small. And it weights all historical days equally regardless of how relevant the market conditions were.

**Monte Carlo VaR** generates thousands of simulated portfolio return paths by drawing from assumed distributions for each risk factor (interest rates, equity returns, exchange rates), applying the portfolio's sensitivity to each factor, and building the full simulated loss distribution. The VaR is then the appropriate percentile of this simulated distribution. Monte Carlo handles complex, nonlinear portfolios (with options, structured products) that violate the linearity assumptions underlying parametric VaR, but requires careful specification of correlation structures and tail behavior.

The fundamental limitation of VaR — regardless of method — is that it tells you nothing about what happens beyond the threshold. A 99% VaR of $1 million means that in the worst 1% of days, you lose *more* than $1 million, but it could be $1.1 million or $100 million. Two portfolios can have identical VaR while one has manageable tail losses and the other is catastrophically exposed. This is why risk managers also compute **Expected Shortfall (ES)**, also called Conditional VaR or CVaR: the expected loss given that you are in the worst 1% of outcomes. ES penalizes fat tails properly, and the Basel III/IV regulatory framework shifted from requiring VaR to requiring ES at the 97.5% level precisely for this reason. Despite its limitations, VaR remains the dominant risk reporting metric because its single-number simplicity makes it easy to communicate, aggregate across desks, and set limits.


