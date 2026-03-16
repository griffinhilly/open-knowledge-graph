---
id: two-asset-portfolio-optimization
title: Two-Asset Portfolio Optimization
domain: economics
course: financial-economics
prerequisites:
- id: mean-variance-optimization
  type: hard
- id: correlation-covariance-assets
  type: hard
builds-toward:
- efficient-frontier-construction
tags:
- portfolio-theory
- optimization
- diversification
stage: formal-systems
status: draft
---

# Two-Asset Portfolio Optimization

## Core Idea
For two assets, the minimum-variance portfolio weight allocation depends on their variances and correlation. Frontier portfolios are parameterized by expected return; as correlation decreases, diversification benefits increase, pulling the frontier inward.

## How It's Best Learned
Compute the minimum-variance portfolio for two stocks with different correlations. Plot efficient frontiers for high, zero, and negative correlation to visualize diversification benefits.

## Explainer

From mean-variance optimization, you know that a rational investor cares only about the expected return and variance of their portfolio, and from your study of correlation and covariance between assets, you know that combining assets with imperfect correlation reduces total portfolio variance even when each asset individually is risky. The two-asset case makes these ideas fully concrete before extending to the full efficient frontier.

Suppose you have two assets with expected returns μ₁ and μ₂, standard deviations σ₁ and σ₂, and correlation ρ. You invest weight w in asset 1 and (1−w) in asset 2. The portfolio's expected return is simply the weighted average: μₚ = wμ₁ + (1−w)μ₂. But the portfolio's variance is not the weighted average of the individual variances — it is: σₚ² = w²σ₁² + (1−w)²σ₂² + 2w(1−w)σ₁σ₂ρ. The last term — the covariance contribution — is the engine of diversification. When ρ < 1, this cross-term is smaller than it would be if returns were perfectly correlated, so σₚ² is less than the weighted average of the individual variances.

The **minimum-variance portfolio** is the weight allocation w* that minimizes σₚ². Taking the derivative of σₚ² with respect to w and setting it to zero yields: w* = (σ₂² − σ₁σ₂ρ) / (σ₁² + σ₂² − 2σ₁σ₂ρ). This formula rewards assets whose returns are dissimilar from the other asset — the lower the correlation, the higher the weight placed on the asset with lower absolute variance. As ρ approaches −1 (perfect negative correlation), it becomes possible to construct a portfolio with zero variance — a risk-free combination from two risky assets. As ρ approaches +1, the assets move in lockstep and no diversification is possible; the "frontier" collapses to a straight line between the two assets in expected-return/standard-deviation space.

Plotting the full set of achievable portfolios as w varies from 0 to 1 traces out the **portfolio frontier** — a curve in mean-standard-deviation space that bows leftward, toward lower volatility, when ρ < 1. The leftward bow is the visual representation of diversification: the portfolio frontier offers more return per unit of risk than any individual asset. The minimum-variance portfolio is the leftmost point of this curve. Portfolios on the upper portion of the curve (above the minimum-variance point) are **efficient** — they offer the maximum expected return for a given level of risk. Portfolios below that point are dominated: you could get the same return with less risk, or more return with the same risk, by holding a different combination. This geometry — and the intuition that correlation drives the shape of the frontier — is the foundation you will need to construct the full efficient frontier with N assets.
