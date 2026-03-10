---
id: black-scholes-model
title: Black-Scholes Options Pricing Model
domain: economics
course: financial-economics
prerequisites:
- id: options-payoff-diagrams
  type: hard
- id: normal-distribution-intro
  type: hard
- id: natural-logarithm-and-e
  type: soft
tags:
- black-scholes
- options-pricing
- implied-volatility
- greeks
- derivatives
stage: formal-systems
status: draft
---

# Black-Scholes Options Pricing Model

## Core Idea
The Black-Scholes model (1973) provides a closed-form formula for European option prices by constructing a continuously rebalanced, riskless hedge between the option and the underlying asset. The call price is C = S·N(d₁) − K·e^(−rT)·N(d₂), where N(·) is the standard normal CDF and d₁, d₂ depend on S, K, r, T, and the asset's volatility σ. The remarkable insight is that under continuous hedging, the expected return of the underlying is irrelevant — only its volatility drives option value. Implied volatility, backed out from observed market prices, reveals the market's consensus expectation of future volatility and is a key market indicator.

## How It's Best Learned
Understand each term of the formula intuitively: S·N(d₁) is the expected receipt conditional on exercise and K·e^(−rT)·N(d₂) is the expected payment. Use an options calculator to vary each input and observe the Greeks (delta, gamma, vega, theta). Study the volatility smile to see where the constant-volatility assumption breaks down.

## Common Misconceptions
- Black-Scholes is a theoretical benchmark, not the market's actual pricing mechanism — practitioners adjust for the volatility smile, dividends, and other departures from model assumptions.
- Implied volatility is not the same as realized (historical) volatility — implied volatility reflects option market pricing and includes a variance risk premium.
