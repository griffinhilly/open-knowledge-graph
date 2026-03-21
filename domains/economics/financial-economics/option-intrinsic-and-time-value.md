---
id: option-intrinsic-and-time-value
title: Option Intrinsic Value and Time Value
domain: economics
course: financial-economics
prerequisites:
- id: call-and-put-options-mechanics
  type: hard
- id: present-value-and-discounting
  type: soft
builds-toward:
- option-greeks-delta-gamma-vega-theta
tags:
- options
- valuation
- option-pricing
stage: formal-systems
status: draft
---

# Option Intrinsic Value and Time Value

## Core Idea
Option price = intrinsic value + time value. Intrinsic value is immediate exercise payoff (never negative for European options; can be negative for an option to sell if out-of-the-money). Time value erodes as expiration approaches and reflects uncertainty; deep out-of-the-money options are mostly time value.

## How It's Best Learned
Track how option prices behave as underlying price and time-to-expiration change. Observe that time decay accelerates near expiration, especially for out-of-the-money options.

## Questions

```yaml
- question: "A call option with strike price $50 on a stock currently trading at $60 has a market price of $13. What is the time value of this option?"
  type: multiple-choice
  options:
    - "$13 — the entire option premium is time value"
    - "$10 — the intrinsic value equals the stock price minus the strike"
    - "$3 — intrinsic value is $10, so the remaining $3 is time value"
    - "$23 — time value is the strike plus the option premium"
  answer: 2
  explanation: "Intrinsic value = max(S − K, 0) = max(60 − 50, 0) = $10. This is the immediate exercise payoff. The market price is $13, which exceeds intrinsic value by $3. That $3 is time value — the premium for the possibility that the stock climbs further before expiration. Option price = intrinsic value + time value is the fundamental decomposition."

- question: "A company announces unexpectedly large earnings uncertainty ahead. The stock price remains unchanged, but implied volatility on its options doubles. What happens to the time value of its at-the-money call options?"
  type: multiple-choice
  options:
    - "Time value decreases — higher volatility makes the option riskier and therefore less valuable to hold"
    - "Time value increases — greater potential movement raises the value of the right (but not obligation) to buy"
    - "Time value is unchanged — only the stock price affects option value, not volatility"
    - "It depends on whether the option is in-the-money or out-of-the-money"
  answer: 1
  explanation: "Higher volatility always increases time value for both calls and puts. The reason is the asymmetric payoff structure: as an option holder, you benefit from large favorable moves but your downside is capped at the premium paid. If the stock might move ±30% instead of ±10%, the upside scenario is much better while the downside is still capped. This asymmetry means option holders gain from volatility — which is why buying options is often described as 'buying volatility.'"

- question: "An out-of-the-money option has zero intrinsic value but can still have a positive market price."
  type: true-false
  answer: true
  explanation: "Intrinsic value is the immediate exercise payoff. For an out-of-the-money option, exercising right now is worthless (max(S − K, 0) = 0 for a call when S < K). But the option still has time value — the possibility that the underlying price could move favorably before expiration. As long as time remains and any chance exists of expiring in-the-money, traders will pay a positive premium."

- question: "As an option approaches its expiration date, its time value increases because uncertainty about the final outcome grows."
  type: true-false
  answer: false
  explanation: "The opposite is true. Time value erodes as expiration approaches — this is theta decay. With less time remaining, there are fewer chances for the underlying to move favorably. Near expiration, an out-of-the-money option is nearly worthless because there is almost no time left for the stock to recover. Theta decay actually accelerates in the final days before expiration."

- question: "Why does higher volatility in the underlying asset always increase the time value of an option, regardless of whether it is a call or a put?"
  type: short-answer
  answer: "Because of the asymmetric payoff structure. An option holder benefits from large moves in the favorable direction but loses only the fixed premium if the move goes the wrong way. Higher volatility increases the probability of large favorable moves without increasing the maximum loss (still capped at the premium). This asymmetry means option holders always benefit from volatility — more potential upside, same capped downside."
  explanation: "For a call: higher volatility means the stock might rise much more, increasing the call's payoff; if it falls, you just don't exercise. For a put: higher volatility means the stock might fall much more, increasing the put's payoff; if it rises, you don't exercise. In both cases, the holder captures the favorable tail and ignores the unfavorable tail. This is why implied volatility is the central pricing variable in options markets."
```

## Explainer

From your study of call and put mechanics, you know that a call option gives the right to buy an asset at the strike price K, and a put gives the right to sell at K. The premium — what you pay to own that right — seems like a single number, but it's actually two conceptually distinct components with very different origins. **Intrinsic value** is what you'd get if you exercised the option right now. **Time value** is the extra premium you pay for the possibility that the option will become more valuable before it expires.

For a call option with strike K = 50 on a stock trading at S = 60, the intrinsic value is max(S - K, 0) = $10. You could exercise immediately and pocket the $10 profit. If the option trades at $13, the extra $3 is time value — the market is paying for the possibility that the stock climbs further before expiration. For an **out-of-the-money** call (S = 45, K = 50), intrinsic value is zero — immediate exercise is worthless — but the option might still trade at $2 or $3 in time value because there's a chance the stock rises above 50 before expiry. The option is a lottery ticket: you can't lose more than the premium, but you might win.

This connects to your study of present value and discounting: time value is really the discounted value of **optionality**. The key drivers are time to expiration, volatility, and the interest rate. More time means more chances for favorable price movements — time value increases with time to expiry and erodes as expiration approaches. This erosion is called **theta decay**. Near expiration, time value collapses rapidly, especially for out-of-the-money options: with one day left, a call that's $5 out of the money is nearly worthless because there's almost no chance the stock makes up the gap. This acceleration of decay in the final days is why traders say "options are wasting assets."

Volatility deserves special attention. High volatility benefits option holders symmetrically: if the stock might move ±30%, an out-of-the-money call might pay off spectacularly; if it moves down, you only lose the premium. The asymmetry of the payoff (you benefit from upside, you're capped on downside at the premium you paid) means higher volatility always increases time value for both calls and puts. This is why **implied volatility** — the volatility the market prices into options — is the central variable in options markets. When traders say "options are expensive," they mean implied volatility is high; the market is pricing in large potential moves, and you're paying for that uncertainty.
