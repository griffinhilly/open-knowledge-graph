---
id: american-option-exercise-decisions
title: Optimal Exercise Decisions for American Options
domain: economics
course: financial-economics
prerequisites:
- id: american-vs-european-options
  type: hard
- id: option-intrinsic-and-time-value
  type: soft
builds-toward:
- options-greeks-trading-applications
tags:
- options
- exercise
- optimization
- american
stage: formal-systems
status: validated
---

# Optimal Exercise Decisions for American Options

## Core Idea
American options' early exercise feature has value when receiving the intrinsic value immediately dominates holding the option. For calls on non-dividend-paying stocks, early exercise is never optimal (time value exceeds intrinsic value). For puts, deep in-the-money puts may warrant early exercise. Dividend-paying stocks complicate decisions: large upcoming dividends can make early call exercise optimal.

## How It's Best Learned
Use binomial trees to solve the optimal exercise boundary and compare American and European option values under different scenarios.

## Questions

```yaml
- question: "An American call on a non-dividend-paying stock is deep in-the-money with one month to expiration. An investor exercises it immediately to 'lock in profits.' Was this decision optimal?"
  type: multiple-choice
  options:
    - "Yes — exercising eliminates downside risk from a stock price reversal"
    - "Yes — deep in-the-money options have negligible time value so little is lost"
    - "No — the option could have been sold for intrinsic value plus positive time value, which is always more"
    - "It depends on how deep in-the-money the option is"
  answer: 2
  explanation: "Early exercise of an American call on a non-dividend-paying stock is never optimal. The option's market price equals intrinsic value plus time value, and time value is always positive before expiration. Exercising captures only intrinsic value, permanently destroying the time value. Selling the option always dominates exercising — it yields intrinsic plus time value. Option B is the seductive misconception: even 'negligible' time value is better than zero."

- question: "When might early exercise of an American put be optimal?"
  type: multiple-choice
  options:
    - "Never — puts, like calls, should always be held to expiration"
    - "When the put is deep in-the-money and the interest earned on the intrinsic value exceeds the remaining time value"
    - "When implied volatility is high, making the option more valuable alive"
    - "Only when the underlying stock pays dividends"
  answer: 1
  explanation: "For a deep in-the-money put (e.g., the right to sell at $50 when the stock is at $2), exercising now yields ~$48 that can earn interest. If that interest exceeds the remaining time value of keeping the put alive, early exercise is rational. This is the key asymmetry: puts face an interest-opportunity cost that can dominate their time value; calls don't, because exercising a call means paying the strike price and forgoing interest on those funds."

- question: "An American call on a non-dividend-paying stock is always worth more than an otherwise identical European call because of the early exercise right."
  type: true-false
  answer: false
  explanation: "Because early exercise is never optimal for calls on non-dividend-paying stocks, the early exercise right has zero practical value. The American and European call are worth exactly the same in this case. The pricing premium for American options over European options only materializes for puts (where early exercise can be optimal) or for calls on dividend-paying stocks."

- question: "Early exercise of an American call can become optimal when a large dividend is about to be paid."
  type: true-false
  answer: true
  explanation: "When a stock goes ex-dividend, its price falls by approximately the dividend amount, shrinking the call's intrinsic value. Exercising just before the ex-dividend date captures the pre-dividend stock price. If the dividend exceeds the forgone time value from surrendering the option, early exercise is optimal. This is why American call options on high-dividend stocks trade above their European counterparts."

- question: "Why is early exercise of an American call on a non-dividend-paying stock never optimal?"
  type: short-answer
  answer: "At any point before expiration, the option's market price equals intrinsic value plus positive time value. Exercising captures only intrinsic value — time value is permanently destroyed. Since the option can always be sold in the market for at least intrinsic value plus some time value, selling always strictly dominates exercising. The early exercise right is valuable in principle but should never actually be used on non-dividend-paying stocks."
  explanation: "The intuition 'lock in profits by exercising' is wrong because the option itself already locks in those profits — it can be sold at any time. Exercising is irreversible and wasteful: you receive the stock (worth S) by paying the strike (K), getting S − K. But selling the option yields at least S − K plus the time premium. Early exercise is only rational when a specific cash flow (a dividend) makes holding the option cost more than exercising it."
```

## Explainer

Your prerequisite on American versus European options introduced the key asymmetry: an American option grants the right to exercise at any point up to expiration, not just at maturity. Your study of intrinsic and time value established that an option's total market value equals intrinsic value plus time value, where time value is always non-negative because optionality has value. These two facts together produce a surprisingly elegant result for calls — and a more nuanced story for puts.

Start with a call option on a **non-dividend-paying stock**. At any moment before expiration, the option trades at its intrinsic value plus some positive time value. If you exercise early, you receive only the intrinsic value — you permanently give up the remaining time value. Since you can always sell the option in the market for at least intrinsic value (and typically more), early exercise destroys value compared to selling. Therefore, **early exercise of an American call on a non-dividend-paying stock is never optimal**. The American and European call are worth exactly the same in this case. The early exercise right is valuable in principle, but you should never actually use it.

**Puts are different.** For a deep in-the-money put — say, the right to sell a stock at $50 when it currently trades near $2 — the intrinsic value is $48 and the maximum possible future payoff is capped at $50 (since the stock cannot fall below zero). Holding the option now means waiting to eventually receive something close to $48–$50 anyway. Meanwhile, you forgo the interest you could earn on $48 if you exercised today and invested the proceeds. When the interest forgone exceeds the remaining time value of keeping the put alive, early exercise is optimal. Deep in-the-money American puts can therefore trade above their European counterparts — the early exercise right has positive value.

**Dividends** complicate the call analysis. When a stock goes ex-dividend, its price drops by approximately the dividend amount, shrinking the call's intrinsic value. Exercising the call just before the ex-dividend date captures the pre-dividend stock price. The trade-off: early exercise forgoes the remaining time value but avoids the drop. The decision rule is that early exercise is worthwhile if the dividend exceeds the forgone time value from surrendering the option early. This is why American call options on high-dividend stocks trade above their European counterparts.

The **optimal exercise boundary** formalizes these comparisons as a function of time to expiration and, for dividend-paying stocks, the dividend schedule. Binomial trees compute this boundary numerically by **backward induction**: at each terminal node, the payoff is max(S − K, 0). At each earlier node, you compare the immediate exercise value (intrinsic value) to the **continuation value** (the discounted expected value of keeping the option alive). The optimal decision is always to take the higher of the two. This backward sweep — comparing exercise versus continuation at every node — is the fundamental algorithm underlying American option valuation.
