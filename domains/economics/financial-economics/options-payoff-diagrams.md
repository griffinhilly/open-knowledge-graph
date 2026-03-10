---
id: options-payoff-diagrams
title: Options Strategies and Put-Call Parity
domain: economics
course: financial-economics
prerequisites:
- id: options-basics-financial
  type: hard
- id: present-value-and-discounting
  type: soft
builds-toward:
- black-scholes-model
tags:
- options-strategies
- put-call-parity
- straddle
- spreads
- no-arbitrage
stage: formal-systems
status: draft
---

# Options Strategies and Put-Call Parity

## Core Idea
Options can be combined to create payoff profiles tailored to specific market views. Key strategies include bull spreads (limited upside at lower cost), straddles (profit from large moves in either direction, useful around earnings), and collars (capping both gains and losses). Put-call parity is a fundamental no-arbitrage relationship linking European call and put prices: C − P = S − PV(K), where S is the stock price and PV(K) is the present value of the strike. Any violation creates a riskless arbitrage profit, so the relationship holds tightly in liquid markets and allows put prices to be inferred from call prices (or vice versa).

## How It's Best Learned
Graph the combined payoff and profit of each strategy at expiration and identify what market view each strategy reflects. Derive put-call parity from a no-arbitrage replication argument and verify numerically with real option chains. Understand how the straddle's payoff depends on realized volatility, not price direction.

## Common Misconceptions
- Put-call parity holds exactly only for European options; American options (exercisable any time) satisfy an inequality rather than an equality due to the early exercise premium.
- Strategies with attractive payoff diagrams can still lose money if the premium paid makes the break-even stock move too large to achieve.
