---
id: option-greeks-delta-gamma-vega-theta
title: 'Option Greeks: Delta, Gamma, Vega, and Theta'
domain: economics
course: financial-economics
prerequisites:
- id: black-scholes-model
  type: hard
- id: partial-derivatives
  type: soft
- id: partial-derivatives-definition
  type: hard
- id: higher-order-partials
  type: soft
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

## Explainer

The Black-Scholes model gives you a formula for option prices — but once you have that formula, you can differentiate it with respect to any of its inputs. The **Greeks** are exactly those partial derivatives. Each Greek answers a specific "what if" question: what happens to the option's value if the stock price moves a little? If time passes? If volatility changes? Because options are nonlinear instruments, monitoring these sensitivities is essential for understanding and managing the risk in any portfolio that contains them.

**Delta** (∂C/∂S) is the most fundamental Greek. For a call option, delta ranges from 0 to 1: a delta of 0.6 means the option price increases by approximately $0.60 for each $1 rise in the underlying stock. You can think of delta as the probability-weighted equivalent stock position — holding one call with delta 0.6 has roughly the same instantaneous price exposure as holding 0.6 shares. Delta-hedging means holding −delta shares per option to make the portfolio value insensitive to small stock moves. The key word is "small": delta itself changes as the stock price moves, which brings in gamma. **Gamma** (∂²C/∂S²) measures how quickly delta changes with the stock price. High gamma means your delta-hedge will be stale after even modest price moves and needs frequent rebalancing. Options near the money and near expiration have the highest gamma — their delta is most sensitive to small stock moves around the strike.

**Vega** (∂C/∂σ) measures sensitivity to changes in **implied volatility**. This is arguably the most important Greek for options traders, because much of an option's value is volatility premium. A vega of 0.25 means that if implied volatility rises by 1 percentage point, the option value increases by $0.25. Options are inherently long vega — higher volatility makes the option more valuable because it increases the chance of a large favorable move. Buying options means buying volatility; selling options means selling volatility. This reframing reveals why sophisticated options markets are often described as markets for volatility rather than markets for directional bets.

**Theta** (∂C/∂t) captures **time decay** — the loss in option value as expiration approaches, holding everything else equal. Theta is typically negative for option holders: each passing day erodes the time value of the option. Near expiration, theta accelerates sharply, especially for at-the-money options. The gamma-theta tradeoff is the central tension in options trading: being long gamma (buying options, profiting from large moves) requires paying theta (losing value as time passes). A delta-neutral portfolio that is long gamma profits when realized volatility exceeds what was priced in (implied volatility) but bleeds theta daily. Short gamma positions collect theta but are vulnerable to large moves. Managing this tradeoff — monitoring your P&L as a function of how much the stock actually moves versus how much volatility you paid for — is the core skill of options market-making.
