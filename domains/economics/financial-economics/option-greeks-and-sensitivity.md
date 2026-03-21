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

## Questions

```yaml
- question: "A trader holds a call option with delta 0.4 and constructs a delta-neutral hedge. Market implied volatility then spikes upward by 10 percentage points. What is the effect on the position?"
  type: multiple-choice
  options:
    - "No effect — the position is delta-neutral, so all market moves are hedged"
    - "The position loses value because delta-neutral positions are inherently short volatility"
    - "Vega causes the option to gain value; the delta-neutral hedge eliminates only directional exposure, not volatility exposure"
    - "The hedge must be incorrect because delta-neutral positions cannot experience vega effects"
  answer: 2
  explanation: "Delta-neutral hedging eliminates only directional risk (first-order sensitivity to the underlying price). It does not eliminate vega exposure. When implied volatility spikes, all long options gain value through vega, regardless of whether they are delta-hedged. This is why professional options traders manage Greeks separately: being delta-neutral says nothing about your vega, gamma, or theta profile. A position can be delta-neutral but carry enormous volatility risk."

- question: "An at-the-money call option has positive gamma. If the underlying stock rises significantly, what happens to the option's delta?"
  type: multiple-choice
  options:
    - "Delta stays near 0.5 because ATM options always have delta 0.5"
    - "Delta increases toward 1.0 as the option moves into-the-money — gamma has caused the position to become more directionally sensitive"
    - "Delta decreases toward 0 because a rising stock price reduces the option's time value"
    - "Gamma and delta are independent; delta does not change when the stock moves"
  answer: 1
  explanation: "Gamma is the rate of change of delta. For a long call starting at-the-money (delta ≈ 0.5), a large upward move takes the option deep in-the-money and delta rises toward 1.0. This convexity is the key value of gamma: as the stock rises you become more long; as it falls you become less long. This self-reinforcing behavior in favorable directions is what you're paying for through negative theta."

- question: "A long call option and a long put option on the same stock with the same strike and expiration have opposite signs of vega."
  type: true-false
  answer: false
  explanation: "Both long calls and long puts have positive vega. This surprises students who assume that since calls and puts move in opposite directions with the stock, their volatility sensitivity must also be opposite. But higher volatility benefits the holder of any long option — more volatility means a greater chance of a large move, which helps a call (if the stock goes up) or a put (if it goes down). Only short option positions have negative vega, regardless of call or put."

- question: "A position that is simultaneously long gamma and long theta is the standard profile of a long option position."
  type: true-false
  answer: false
  explanation: "Long options have positive gamma but negative theta — this is the fundamental tradeoff in options. You pay for convexity through time decay. Gamma and theta are always in opposition for a simple long or short option: positive gamma comes with negative theta; negative gamma comes with positive theta. There is no free lunch — if you want convexity, you pay daily rent through time decay."

- question: "Explain the relationship between gamma and theta for a long option position, and what this reveals about what you're actually paying for when you buy an option."
  type: short-answer
  answer: "Gamma and theta are opposite sides of the same tradeoff. Positive gamma (convexity) means the position benefits from large moves in either direction — as the stock rises, delta increases and you get more long; as it falls, delta decreases and you get less long. This self-adjusting property is valuable. Negative theta means the option loses value every day as expiration approaches. When you buy an option, you are paying for the right to this convexity. Theta represents the daily 'rent' on that optionality — if the stock doesn't move enough to offset the time decay, the option expires worthless."
  explanation: "The gamma-theta tradeoff is the core economic logic of options pricing. The daily theta payment is the fair price for the gamma benefit given current volatility expectations. If realized volatility turns out higher than implied, long gamma positions profit; if lower, they lose. Buying options is essentially a bet that realized volatility will exceed implied volatility."
```

## Explainer

From your study of Black-Scholes and partial derivatives, you have all the tools to understand the Greeks: they are literally the partial derivatives of the Black-Scholes option pricing formula with respect to each of its inputs. Black-Scholes takes the stock price S, strike K, time to expiration T, risk-free rate r, and volatility σ as inputs and outputs an option price C. Each Greek answers the question: if I change one input by a small amount while holding everything else fixed, how much does C change?

**Delta** (∂C/∂S) is the most important Greek. For a call option, delta ranges from 0 to 1 — when the option is deep out-of-the-money, a $1 move in the stock barely affects the option price (delta ≈ 0); when the option is deep in-the-money, the option moves nearly dollar-for-dollar with the stock (delta ≈ 1). At-the-money options have delta ≈ 0.5. Delta has a practical interpretation: it tells you how many shares of stock you need to short to create a **delta-neutral hedge** that is momentarily insensitive to small stock-price moves. If you own a call with delta 0.5, you short 0.5 shares per option to hedge. This is the basis of dynamic hedging.

But delta only provides a linear approximation, and that's where **gamma** (∂²C/∂S²) comes in — it's the rate of change of delta. Using your chain rule knowledge: as the stock price moves, delta itself shifts, and gamma tells you how fast. A high-gamma option changes character rapidly as the underlying moves. Practically, a long option position has positive gamma: as the stock rises, your delta increases and you're synthetically getting longer; as it falls, your delta decreases and you're getting shorter. This **convexity** is valuable — it means the option benefits from volatility in both directions. You pay for this benefit through **theta** (∂C/∂T), the rate of time decay. All else equal, options lose value as expiration approaches because there is less time for the stock to move into profitability. Theta is typically negative for long options — you're paying for optionality that erodes daily.

**Vega** (∂C/∂σ) measures sensitivity to implied volatility. Options become more valuable when volatility is high because there's a greater chance the underlying makes a large move. Vega is always positive for long options (calls and puts alike) because more volatility unambiguously helps option holders. When markets become fearful, implied volatility spikes — the VIX (which measures implied volatility on S&P options) is sometimes called the "fear gauge" for exactly this reason. Traders who are long vega profit when volatility rises, regardless of direction. Together, delta, gamma, theta, and vega give you a complete first-order description of your option position's risk profile: directional exposure (delta), convexity benefit (gamma), time decay cost (theta), and volatility exposure (vega). Managing a complex options book means balancing these exposures against each other to express the views you want while hedging the risks you don't.
