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

## Questions

```yaml
- question: "An investor buys a straddle (long call + long put at the same strike) on a stock before an earnings announcement. The stock barely moves after the announcement. What happens to the investor's position?"
  type: multiple-choice
  options:
    - "She profits because the call gains value as the put loses value, netting a gain"
    - "She breaks even because gains on one leg always offset losses on the other"
    - "She loses money — both options expire near worthless, and she paid premium for both"
    - "She profits because implied volatility typically rises around earnings announcements"
  answer: 2
  explanation: "A straddle's profit depends on the magnitude of the move, not its direction. If the underlying barely moves, both the call and the put expire near worthless, and the investor loses the combined premium paid. To profit, the stock must move enough in either direction to exceed the total premium cost. This is a bet that realized volatility will exceed the implied volatility priced into the options. A minimal stock move is exactly the scenario where straddles fail."

- question: "How does a bull call spread differ from simply buying a call, and what is the tradeoff?"
  type: multiple-choice
  options:
    - "A spread always has higher profit potential than a single call, with the same premium cost"
    - "A spread buys a call at a lower strike and sells a call at a higher strike — reducing net premium but capping gains above the upper strike"
    - "A spread requires less capital because you sell the put rather than the call at the higher strike"
    - "A spread is directionally neutral, while buying a single call expresses a bullish view"
  answer: 1
  explanation: "A bull call spread buys a call at strike K₁ and sells a call at strike K₂ > K₁. The premium received from the upper call reduces your net cost vs. buying only the lower-strike call. But you give up profits above K₂, since gains on the long call are offset by losses on the short call beyond that point. The tradeoff is explicit: lower net premium in exchange for capped maximum profit. Both the single call and the spread are bullish, but the spread expresses a more precise view — 'the stock will rise moderately, not dramatically above K₂.'"

- question: "Buying a straddle is primarily a directional bet — you profit when the stock rises significantly."
  type: true-false
  answer: false
  explanation: "A straddle profits from large movement in either direction. Buying both a call and a put at the same strike means you gain whether the stock surges upward or crashes downward — as long as the move exceeds the combined premium paid. This makes a straddle a volatility bet: you are betting that realized volatility will exceed what the market (via implied volatility) expects. If you had a directional view, a single call or put would be more efficient — the straddle pays for optionality in both directions."

- question: "In a bull call spread, selling the higher-strike call reduces the net premium paid but limits the maximum profit the strategy can generate."
  type: true-false
  answer: true
  explanation: "This is the fundamental spread tradeoff. The premium received from selling the upper-strike call reduces net cost, lowering the break-even point and capital at risk. But by selling that call, you are obligated to deliver if the stock exceeds the upper strike. Any gain on the long lower-strike call above the upper strike is exactly offset by the loss on the short upper-strike call. Maximum profit is capped at (K₂ − K₁) minus net premium paid."

- question: "Describe the three positions that constitute a collar and explain the economic tradeoff it represents for an equity holder."
  type: short-answer
  answer: "A collar involves: (1) holding the underlying stock, (2) buying a put option below the current price to establish a floor on losses, and (3) selling a call option above the current price, using the premium received to offset the put's cost. The tradeoff is that you give up upside participation above the call strike in exchange for downside protection below the put strike. If strikes are chosen so call premium ≈ put premium, the collar can be structured at near-zero net cost."
  explanation: "Collars are popular for hedging large equity positions (e.g., an executive with concentrated company stock) because they provide meaningful protection at low net cost. The payoff diagram of the combined position shows a horizontal line below the put strike (loss is floored), a rising diagonal between the strikes, and another horizontal line above the call strike (gain is capped). The collar converts unlimited upside and unlimited downside into a bounded range of outcomes."
```

## Explainer

You already know how to draw a single call or put payoff diagram and how put-call parity connects their prices. Option strategies are simply additions and subtractions of those basic diagrams — you stack the payoffs of multiple options to create a combined profile that expresses a precise market view. The key insight is that by combining options, you can sculpt almost any payoff shape you want, trading off premium cost, maximum profit, and maximum loss.

The simplest multi-option structure is a **spread**: buying one option and selling another of the same type (both calls or both puts) at different strike prices. A **bull call spread** — buy a call at a lower strike, sell a call at a higher strike — profits when the underlying rises moderately, while the premium received from selling the upper call reduces your net cost. You give up unlimited upside above the upper strike in exchange for paying less premium upfront. A **bear put spread** works symmetrically for a bearish view. Spreads are the core "I have a directional view but want to reduce cost" tool.

**Straddles** and **strangles** express a volatility view rather than a directional view. A **straddle** buys a call and a put at the same strike. You profit if the underlying moves a lot in either direction — you don't care which way, just that it moves enough to cover the combined premium. A **strangle** is cheaper: buy an out-of-the-money call and an out-of-the-money put. You need a larger move to profit, but you pay less premium. Both strategies reflect a bet that realized volatility will exceed the implied volatility priced into the options. If the underlying barely moves, both positions lose their premium.

A **collar** is an equity holder's tool: own the stock, buy a protective put (floor on losses), and sell a call (cap on gains). The put premium is funded partly by the call premium sold. Collars are popular for hedging large equity positions at low net cost. A **butterfly spread** — buy a call at a low strike, sell two calls at a middle strike, buy a call at a high strike — creates a narrow profit zone around the middle strike, profiting if the underlying stays near the current price. It is a bet on low volatility with a defined, limited cost. The central theme across all these structures is that you are always buying or selling volatility, direction, or both, and the strategy's shape on a payoff diagram reveals exactly what you are paying for and what risk you are accepting.
