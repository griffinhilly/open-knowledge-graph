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
- id: partial-derivatives
  type: soft
- id: differential-equations-intro-separable
  type: soft
- id: normal-distribution
  type: soft
- id: differential-equations-intro
  type: soft
- id: normal-distribution-theory
  type: hard
- id: fundamental-theorem-of-calculus-part-1
  type: hard
tags:
- black-scholes
- options-pricing
- implied-volatility
- greeks
- derivatives
stage: formal-systems
status: validated
---

# Black-Scholes Options Pricing Model

## Core Idea
The Black-Scholes model (1973) provides a closed-form formula for European option prices by constructing a continuously rebalanced, riskless hedge between the option and the underlying asset. The call price is C = S·N(d₁) − K·e^(−rT)·N(d₂), where N(·) is the standard normal CDF and d₁, d₂ depend on S, K, r, T, and the asset's volatility σ. The remarkable insight is that under continuous hedging, the expected return of the underlying is irrelevant — only its volatility drives option value. Implied volatility, backed out from observed market prices, reveals the market's consensus expectation of future volatility and is a key market indicator.

## How It's Best Learned
Understand each term of the formula intuitively: S·N(d₁) is the expected receipt conditional on exercise and K·e^(−rT)·N(d₂) is the expected payment. Use an options calculator to vary each input and observe the Greeks (delta, gamma, vega, theta). Study the volatility smile to see where the constant-volatility assumption breaks down.

## Common Misconceptions
- Black-Scholes is a theoretical benchmark, not the market's actual pricing mechanism — practitioners adjust for the volatility smile, dividends, and other departures from model assumptions.
- Implied volatility is not the same as realized (historical) volatility — implied volatility reflects option market pricing and includes a variance risk premium.

## Questions

```yaml
- question: "In the Black-Scholes formula C = S·N(d₁) − K·e^(−rT)·N(d₂), what does the term K·e^(−rT)·N(d₂) represent?"
  type: multiple-choice
  options:
    - "The current stock price weighted by the probability of exercise"
    - "The present value of the strike price weighted by the risk-neutral probability the option expires in the money"
    - "The implied volatility premium embedded in the option price"
    - "The delta of the option times the stock price"
  answer: 1
  explanation: "K·e^(−rT) is the present value of the strike payment discounted at the risk-free rate, and N(d₂) is the risk-neutral probability that the option expires in the money (S_T > K). So this term is the expected present-value outflow if exercise occurs. The full formula is the expected receipt (S·N(d₁)) minus the expected payment — a form of 'expected value of owning the asset upon exercise minus expected cost of exercising.'"

- question: "Implied volatility derived from Black-Scholes equals the realized (historical) volatility of the underlying asset."
  type: true-false
  answer: false
  explanation: "Implied volatility is backed out from observed market option prices and reflects the market's forward-looking expectation of future volatility, plus a variance risk premium. Realized volatility measures actual past price fluctuations. The two diverge systematically — implied volatility tends to exceed realized volatility on average, a gap called the variance risk premium, because investors pay extra to hedge against volatility uncertainty."

- question: "Why is the expected return of the underlying stock not an input in the Black-Scholes formula, even though a higher expected return seems like it would increase the value of a call option?"
  type: short-answer
  answer: "Black-Scholes constructs a continuously rebalanced delta hedge that makes the combined portfolio of the option and a short stock position instantaneously riskless. In a riskless portfolio, the expected return is irrelevant — it must earn the risk-free rate by no-arbitrage. The hedge eliminates all dependence on the stock's drift, leaving only volatility (the random component) as the driver of option value."
  explanation: "This is the model's central insight. Intuition says 'higher expected stock return → higher call value,' but that intuition is wrong because you could also buy the stock directly to benefit from that return. What the option provides that the stock does not is asymmetric exposure to volatility. The risk-neutral pricing framework captures this: we price as if the stock grows at the risk-free rate (eliminating the expected return from the problem) and discount at the risk-free rate."
```

## Explainer

To understand Black-Scholes, start with what an option is: a call option gives you the right — but not the obligation — to buy an asset at a fixed price K (the strike) by expiration T. Its value at expiration is max(S_T − K, 0). The puzzle that Black and Scholes solved in 1973 is: what is this right *worth today*, before we know S_T?

The brilliant insight is a **delta hedge**. For every call option you sell, you can buy Δ shares of the underlying stock such that the combined position (short call, long Δ shares) is instantaneously riskless — small moves in the stock price cancel out. Because the hedge is riskless, it must earn exactly the risk-free rate (otherwise there would be an arbitrage). This no-arbitrage condition, applied continuously as Δ changes with the stock price, produces a partial differential equation (the Black-Scholes PDE) whose solution is the famous formula. The critical consequence: the stock's expected return drops entirely out of the equation. Risk and return cancel in the hedge, leaving only volatility.

The formula C = S·N(d₁) − K·e^(−rT)·N(d₂) has a clean interpretation. Think of it as: (expected value of receiving the stock upon exercise) minus (expected present value of paying the strike). S·N(d₁) is the stock price weighted by a modified probability of exercise, capturing the expected upside. K·e^(−rT)·N(d₂) is the discounted strike payment weighted by N(d₂), the risk-neutral probability that the option ends in the money. Both d₁ and d₂ are functions of S/K (how far in or out of the money), r, T, and σ — the volatility of the stock's log returns.

**Implied volatility** is the model's most important practical output. You can observe option prices in the market, and you know S, K, r, and T. The only unknown in the formula is σ. Running the formula in reverse — finding the σ that makes the model price match the market price — gives you implied volatility. It is the market's consensus forecast of future volatility. Crucially, implied volatility is not the same as realized (historical) volatility: it reflects both expected future variance and the risk premium investors demand for bearing volatility uncertainty.

The model's assumptions are its biggest limitations: constant volatility, no dividends, continuous trading, and log-normal returns. In practice, the volatility smile — implied volatility varying systematically across strike prices — proves that the market assigns higher probability to large moves than a log-normal distribution predicts. Practitioners use Black-Scholes as a quoting convention (expressing prices in volatility terms) and then model the smile separately. Understanding where the model breaks down is as important as knowing the formula itself.


