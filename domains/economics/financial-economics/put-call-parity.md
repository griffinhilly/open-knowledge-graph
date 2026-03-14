---
id: put-call-parity
title: Put-Call Parity
domain: economics
course: financial-economics
prerequisites:
- id: options-basics-financial
  type: hard
- id: options-payoff-diagrams
  type: hard
builds-toward:
- option-greeks-and-sensitivity
- option-trading-strategies
tags:
- options
- parity
- arbitrage
stage: formal-systems
status: draft
---

# Put-Call Parity

## Core Idea
Put-call parity is the fundamental relationship stating that for European options: C - P = S - PV(K), where C is the call price, P is the put price, S is the stock price, and K is the strike price. This relationship prevents arbitrage and is essential for option pricing, synthetic replication, and understanding the relative values of puts and calls.

## How It's Best Learned
Verify put-call parity with real option quotes on the same underlying and strike, identifying when deviations occur and what arbitrage transactions would exploit them.

## Common Misconceptions
- Put-call parity holds for American options (it only holds exactly for European options; Americans have additional value from early exercise).
- The parity relationship is always perfectly observed (transaction costs, bid-ask spreads, and dividend timing create small deviations).
