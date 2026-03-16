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

## Explainer

From your study of call and put mechanics, you know that a call option gives the right to buy an asset at the strike price K, and a put gives the right to sell at K. The premium — what you pay to own that right — seems like a single number, but it's actually two conceptually distinct components with very different origins. **Intrinsic value** is what you'd get if you exercised the option right now. **Time value** is the extra premium you pay for the possibility that the option will become more valuable before it expires.

For a call option with strike K = 50 on a stock trading at S = 60, the intrinsic value is max(S - K, 0) = $10. You could exercise immediately and pocket the $10 profit. If the option trades at $13, the extra $3 is time value — the market is paying for the possibility that the stock climbs further before expiration. For an **out-of-the-money** call (S = 45, K = 50), intrinsic value is zero — immediate exercise is worthless — but the option might still trade at $2 or $3 in time value because there's a chance the stock rises above 50 before expiry. The option is a lottery ticket: you can't lose more than the premium, but you might win.

This connects to your study of present value and discounting: time value is really the discounted value of **optionality**. The key drivers are time to expiration, volatility, and the interest rate. More time means more chances for favorable price movements — time value increases with time to expiry and erodes as expiration approaches. This erosion is called **theta decay**. Near expiration, time value collapses rapidly, especially for out-of-the-money options: with one day left, a call that's $5 out of the money is nearly worthless because there's almost no chance the stock makes up the gap. This acceleration of decay in the final days is why traders say "options are wasting assets."

Volatility deserves special attention. High volatility benefits option holders symmetrically: if the stock might move ±30%, an out-of-the-money call might pay off spectacularly; if it moves down, you only lose the premium. The asymmetry of the payoff (you benefit from upside, you're capped on downside at the premium you paid) means higher volatility always increases time value for both calls and puts. This is why **implied volatility** — the volatility the market prices into options — is the central variable in options markets. When traders say "options are expensive," they mean implied volatility is high; the market is pricing in large potential moves, and you're paying for that uncertainty.
