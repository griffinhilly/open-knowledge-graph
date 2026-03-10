---
id: beta-and-systematic-risk
title: Beta and Systematic Risk
domain: economics
course: financial-economics
prerequisites:
- id: portfolio-diversification
  type: hard
- id: bivariate-regression
  type: soft
- id: correlation-coefficient
  type: soft
builds-toward:
- capital-asset-pricing-model
tags:
- beta
- systematic-risk
- market-risk
- covariance
- capm
stage: formal-systems
status: draft
---

# Beta and Systematic Risk

## Core Idea
Beta (β) measures an asset's sensitivity to market-wide movements — its systematic (non-diversifiable) risk. Formally, β = Cov(rᵢ, rₘ) / Var(rₘ), estimated by regressing historical asset returns on market returns. A beta of 1 means the asset moves in lockstep with the market; beta > 1 amplifies market swings (cyclical or technology stocks); beta < 1 dampens them (utilities, consumer staples); negative beta means the asset tends to move against the market. Because idiosyncratic risk can be freely diversified away, only beta — not total volatility — determines the risk premium in equilibrium.

## How It's Best Learned
Estimate beta by regressing monthly stock returns on index returns over a 5-year window and interpret the slope coefficient. Compare betas across cyclical (high beta) and defensive (low beta) sectors. Understand the Hamada equation relating levered and unlevered beta to see how financial leverage raises beta.

## Common Misconceptions
- A highly volatile stock with low correlation to the market can have low beta — volatility and systematic risk are distinct concepts.
- Beta estimated from historical data is unstable and sensitive to the chosen time window and market proxy, making forward-looking beta a source of significant estimation error.
