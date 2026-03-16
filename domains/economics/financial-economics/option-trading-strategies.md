---
id: option-trading-strategies
title: Option Trading Strategies
domain: economics
course: financial-economics
prerequisites:
- id: put-call-parity
  type: hard
- id: options-payoff-diagrams
  type: hard
builds-toward:
- hedging-with-derivatives
tags:
- options
- strategies
- spreads
stage: formal-systems
status: draft
---

# Option Trading Strategies

## Core Idea
Multi-option strategies (spreads, straddles, strangles, collars, butterflies) combine calls and puts with different strikes and maturities to create customized payoff profiles. Each strategy expresses a specific directional or volatility view with controlled risk and cost. Strategies can reduce premium costs, limit losses, or isolate specific risk exposures.

## Explainer

You already know how to draw a single call or put payoff diagram and how put-call parity connects their prices. Option strategies are simply additions and subtractions of those basic diagrams — you stack the payoffs of multiple options to create a combined profile that expresses a precise market view. The key insight is that by combining options, you can sculpt almost any payoff shape you want, trading off premium cost, maximum profit, and maximum loss.

The simplest multi-option structure is a **spread**: buying one option and selling another of the same type (both calls or both puts) at different strike prices. A **bull call spread** — buy a call at a lower strike, sell a call at a higher strike — profits when the underlying rises moderately, while the premium received from selling the upper call reduces your net cost. You give up unlimited upside above the upper strike in exchange for paying less premium upfront. A **bear put spread** works symmetrically for a bearish view. Spreads are the core "I have a directional view but want to reduce cost" tool.

**Straddles** and **strangles** express a volatility view rather than a directional view. A **straddle** buys a call and a put at the same strike. You profit if the underlying moves a lot in either direction — you don't care which way, just that it moves enough to cover the combined premium. A **strangle** is cheaper: buy an out-of-the-money call and an out-of-the-money put. You need a larger move to profit, but you pay less premium. Both strategies reflect a bet that realized volatility will exceed the implied volatility priced into the options. If the underlying barely moves, both positions lose their premium.

A **collar** is an equity holder's tool: own the stock, buy a protective put (floor on losses), and sell a call (cap on gains). The put premium is funded partly by the call premium sold. Collars are popular for hedging large equity positions at low net cost. A **butterfly spread** — buy a call at a low strike, sell two calls at a middle strike, buy a call at a high strike — creates a narrow profit zone around the middle strike, profiting if the underlying stays near the current price. It is a bet on low volatility with a defined, limited cost. The central theme across all these structures is that you are always buying or selling volatility, direction, or both, and the strategy's shape on a payoff diagram reveals exactly what you are paying for and what risk you are accepting.
