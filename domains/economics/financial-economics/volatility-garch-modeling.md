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
