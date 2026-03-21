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

## Questions

```yaml
- question: "A trader holds 100 call options with delta = 0.4 and hedges by selling 40 shares (delta-neutral). The stock then rises $5. Is the portfolio still delta-neutral?"
  type: multiple-choice
  options:
    - "Yes — delta-hedging permanently eliminates all price exposure"
    - "No — as the stock rose, the option's delta increased (due to gamma), so the original hedge is now stale"
    - "No — the hedge should have used put options rather than short shares"
    - "Yes — delta-hedging is exact for moves of any size"
  answer: 1
  explanation: "Delta-hedging is only instantaneously correct for infinitesimally small moves. Gamma measures how quickly delta changes with stock price — for a call, as the stock rises toward and past the strike, delta increases toward 1. After a $5 rise, the option's delta might be 0.55, meaning the hedge (still 40 shares) is now too small to neutralize the exposure. To remain delta-neutral, the trader must buy more shares. This continuous rebalancing requirement is the cost of being short gamma."

- question: "An options trader says: 'I'm selling volatility.' Which position does this most accurately describe?"
  type: multiple-choice
  options:
    - "Buying call options on a stock expected to have high realized volatility"
    - "Selling a straddle (a call and a put at the same strike) to collect premium while expecting the stock to stay near its current price"
    - "Buying put options as a hedge against a market decline"
    - "Shorting shares to profit from an expected price drop"
  answer: 1
  explanation: "Selling volatility means taking positions that profit from low realized volatility — typically selling options and collecting premium (short vega). A straddle sale profits if the stock stays near the strike; both the call and put expire worthless and the seller keeps the premium. The key reframe is that options markets are volatility markets: buying options goes long vega and long gamma; selling options goes short vega and short gamma. Options A, C, and D are directional price bets, not volatility positions."

- question: "An option holder benefits from time passing — theta is positive for long option positions because expiration reduces uncertainty."
  type: true-false
  answer: false
  explanation: "Theta is almost always negative for option holders. As expiration approaches with no change in stock price or volatility, the option loses time value — the probability of a large favorable move decreases, so the time premium erodes. This decay accelerates sharply near expiration for at-the-money options. Option sellers (short positions) have positive theta, collecting that daily decay. The holder paid for time value; it erodes against them each day."

- question: "A delta-neutral portfolio has zero exposure to stock price changes, regardless of how large those changes are."
  type: true-false
  answer: false
  explanation: "Delta-neutrality holds only instantaneously, for infinitesimally small price changes. For any finite move, gamma matters — the portfolio's delta changes as the stock moves, so directional exposure develops. To hedge against larger moves, a trader would need to be gamma-neutral as well (typically achieved by holding options with offsetting gammas). Even then, even higher-order Greeks become relevant for very large moves. Delta-hedging is a first-order, local approximation that requires continuous rebalancing to remain accurate."

- question: "Explain the gamma-theta tradeoff in options trading. Why can't a trader simultaneously be long gamma and collect positive theta?"
  type: short-answer
  answer: "Gamma and theta are intrinsically linked: being long gamma means owning options, which means paying time premium — negative theta. Each day, the option's time value erodes (theta drain). Conversely, selling options gives positive theta (collecting daily decay) but leaves you short gamma and vulnerable to large moves. The tradeoff is: you pay daily (theta) for the right to profit from large moves (gamma), or you collect daily (theta) by accepting the risk of large moves. You cannot have both."
  explanation: "This tradeoff is the central risk-reward tension in options trading. A long gamma position profits when realized volatility exceeds implied volatility — when the stock actually moves more than the market priced in. A short gamma position profits from calm markets. The daily theta paid or collected is the market's 'fair' price for the gamma exposure. Managing this — judging whether actual volatility will beat or underperform implied volatility — is the core skill of options market-making and is why options are fundamentally instruments for trading volatility, not just direction."
```

## Explainer

The Black-Scholes model gives you a formula for option prices — but once you have that formula, you can differentiate it with respect to any of its inputs. The **Greeks** are exactly those partial derivatives. Each Greek answers a specific "what if" question: what happens to the option's value if the stock price moves a little? If time passes? If volatility changes? Because options are nonlinear instruments, monitoring these sensitivities is essential for understanding and managing the risk in any portfolio that contains them.

**Delta** (∂C/∂S) is the most fundamental Greek. For a call option, delta ranges from 0 to 1: a delta of 0.6 means the option price increases by approximately $0.60 for each $1 rise in the underlying stock. You can think of delta as the probability-weighted equivalent stock position — holding one call with delta 0.6 has roughly the same instantaneous price exposure as holding 0.6 shares. Delta-hedging means holding −delta shares per option to make the portfolio value insensitive to small stock moves. The key word is "small": delta itself changes as the stock price moves, which brings in gamma. **Gamma** (∂²C/∂S²) measures how quickly delta changes with the stock price. High gamma means your delta-hedge will be stale after even modest price moves and needs frequent rebalancing. Options near the money and near expiration have the highest gamma — their delta is most sensitive to small stock moves around the strike.

**Vega** (∂C/∂σ) measures sensitivity to changes in **implied volatility**. This is arguably the most important Greek for options traders, because much of an option's value is volatility premium. A vega of 0.25 means that if implied volatility rises by 1 percentage point, the option value increases by $0.25. Options are inherently long vega — higher volatility makes the option more valuable because it increases the chance of a large favorable move. Buying options means buying volatility; selling options means selling volatility. This reframing reveals why sophisticated options markets are often described as markets for volatility rather than markets for directional bets.

**Theta** (∂C/∂t) captures **time decay** — the loss in option value as expiration approaches, holding everything else equal. Theta is typically negative for option holders: each passing day erodes the time value of the option. Near expiration, theta accelerates sharply, especially for at-the-money options. The gamma-theta tradeoff is the central tension in options trading: being long gamma (buying options, profiting from large moves) requires paying theta (losing value as time passes). A delta-neutral portfolio that is long gamma profits when realized volatility exceeds what was priced in (implied volatility) but bleeds theta daily. Short gamma positions collect theta but are vulnerable to large moves. Managing this tradeoff — monitoring your P&L as a function of how much the stock actually moves versus how much volatility you paid for — is the core skill of options market-making.
