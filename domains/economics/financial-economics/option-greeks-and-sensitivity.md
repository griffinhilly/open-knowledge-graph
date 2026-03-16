---
id: option-greeks-and-sensitivity
title: Option Greeks and Sensitivity Analysis
domain: economics
course: financial-economics
prerequisites:
- id: black-scholes-model
  type: hard
- id: put-call-parity
  type: soft
- id: partial-derivatives
  type: soft
- id: chain-rule
  type: hard
builds-toward:
- option-trading-strategies
- hedging-with-derivatives
tags:
- options
- greeks
- sensitivity
stage: formal-systems
status: draft
---

# Option Greeks and Sensitivity Analysis

## Core Idea
The Greeks (delta, gamma, vega, theta, rho) measure how option prices respond to changes in underlying factors. Delta measures stock price sensitivity, gamma measures delta sensitivity (convexity), vega measures volatility sensitivity, theta measures time decay, and rho measures interest rate sensitivity. Traders use Greeks to manage portfolio risk and hedge exposures.

## Explainer

From your study of Black-Scholes and partial derivatives, you have all the tools to understand the Greeks: they are literally the partial derivatives of the Black-Scholes option pricing formula with respect to each of its inputs. Black-Scholes takes the stock price S, strike K, time to expiration T, risk-free rate r, and volatility σ as inputs and outputs an option price C. Each Greek answers the question: if I change one input by a small amount while holding everything else fixed, how much does C change?

**Delta** (∂C/∂S) is the most important Greek. For a call option, delta ranges from 0 to 1 — when the option is deep out-of-the-money, a $1 move in the stock barely affects the option price (delta ≈ 0); when the option is deep in-the-money, the option moves nearly dollar-for-dollar with the stock (delta ≈ 1). At-the-money options have delta ≈ 0.5. Delta has a practical interpretation: it tells you how many shares of stock you need to short to create a **delta-neutral hedge** that is momentarily insensitive to small stock-price moves. If you own a call with delta 0.5, you short 0.5 shares per option to hedge. This is the basis of dynamic hedging.

But delta only provides a linear approximation, and that's where **gamma** (∂²C/∂S²) comes in — it's the rate of change of delta. Using your chain rule knowledge: as the stock price moves, delta itself shifts, and gamma tells you how fast. A high-gamma option changes character rapidly as the underlying moves. Practically, a long option position has positive gamma: as the stock rises, your delta increases and you're synthetically getting longer; as it falls, your delta decreases and you're getting shorter. This **convexity** is valuable — it means the option benefits from volatility in both directions. You pay for this benefit through **theta** (∂C/∂T), the rate of time decay. All else equal, options lose value as expiration approaches because there is less time for the stock to move into profitability. Theta is typically negative for long options — you're paying for optionality that erodes daily.

**Vega** (∂C/∂σ) measures sensitivity to implied volatility. Options become more valuable when volatility is high because there's a greater chance the underlying makes a large move. Vega is always positive for long options (calls and puts alike) because more volatility unambiguously helps option holders. When markets become fearful, implied volatility spikes — the VIX (which measures implied volatility on S&P options) is sometimes called the "fear gauge" for exactly this reason. Traders who are long vega profit when volatility rises, regardless of direction. Together, delta, gamma, theta, and vega give you a complete first-order description of your option position's risk profile: directional exposure (delta), convexity benefit (gamma), time decay cost (theta), and volatility exposure (vega). Managing a complex options book means balancing these exposures against each other to express the views you want while hedging the risks you don't.
