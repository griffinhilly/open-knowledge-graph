---
id: option-greeks-delta-gamma-vega-theta
title: 'Option Greeks: Delta, Gamma, Vega, and Theta'
domain: economics
course: financial-economics
prerequisites:
- id: black-scholes-model
  type: hard
tags:
- options
- risk-sensitivity
- hedging
stage: formal-systems
status: draft
---

# Option Greeks: Delta, Gamma, Vega, and Theta

## Core Idea
Delta (∂C/∂S) measures price sensitivity to stock changes; gamma (∂²C/∂S²) measures delta's sensitivity; vega (∂C/∂σ) measures volatility exposure; theta (∂C/∂t) measures time decay. Traders use Greeks to monitor and hedge portfolio risks.

## How It's Best Learned
Calculate Greeks for an option using Black-Scholes. Construct a delta-hedged portfolio and verify that it is insensitive to small stock price moves. Observe gamma and theta tradeoffs: short gamma (negative gamma) profits from low realized volatility but loses on large moves.
