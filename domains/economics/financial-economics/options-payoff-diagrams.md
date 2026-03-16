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
status: validated
---

# Options Strategies and Put-Call Parity

## Core Idea
Options can be combined to create payoff profiles tailored to specific market views. Key strategies include bull spreads (limited upside at lower cost), straddles (profit from large moves in either direction, useful around earnings), and collars (capping both gains and losses). Put-call parity is a fundamental no-arbitrage relationship linking European call and put prices: C − P = S − PV(K), where S is the stock price and PV(K) is the present value of the strike. Any violation creates a riskless arbitrage profit, so the relationship holds tightly in liquid markets and allows put prices to be inferred from call prices (or vice versa).

## How It's Best Learned
Graph the combined payoff and profit of each strategy at expiration and identify what market view each strategy reflects. Derive put-call parity from a no-arbitrage replication argument and verify numerically with real option chains. Understand how the straddle's payoff depends on realized volatility, not price direction.

## Common Misconceptions
- Put-call parity holds exactly only for European options; American options (exercisable any time) satisfy an inequality rather than an equality due to the early exercise premium.
- Strategies with attractive payoff diagrams can still lose money if the premium paid makes the break-even stock move too large to achieve.

## Explainer

From your study of options basics, you know the building blocks: a call gives the right to buy at strike K, a long call pays max(S_T − K, 0) at expiration, and a put pays max(K − S_T, 0). Options become strategically powerful when you combine them. The key insight is that any payoff profile you want — bounded upside, protection against downside, profit from large moves in either direction — can be engineered by mixing calls, puts, and the underlying stock. Learning to read and construct **payoff diagrams** (the shape of profit/loss at expiration as a function of the terminal stock price S_T) is the entry point to options strategy.

The most instructive strategies are built from two or three legs. A **bull spread** buys a call at a lower strike K₁ and sells a call at a higher strike K₂ > K₁. The sold call brings in premium, reducing cost, but caps your upside at K₂. Your payoff diagram shows flat losses below K₁, linear gains between K₁ and K₂, and flat profits above K₂. This strategy reflects a moderate bullish view: you expect the stock to rise but are willing to surrender gains above K₂ in exchange for a cheaper position. A **straddle** buys both a call and a put at the same strike. The payoff is V-shaped: losses if the stock barely moves (you paid two premiums) and gains if it moves far in either direction. Straddles are popular before earnings announcements — you don't know which direction the stock will move, but you believe the move will be large enough to exceed the total premium paid.

**Put-call parity** is the fundamental no-arbitrage relationship that ties all of these pieces together: C − P = S − PV(K), where C is the European call price, P is the European put price, S is the current stock price, and PV(K) is the present value of the strike (discounted at the risk-free rate over the option's life). The derivation is a replication argument: a portfolio of long call plus short put replicates a forward contract on the stock (obligation to buy at K), which today costs S − PV(K). If C − P ≠ S − PV(K), you can construct a riskless arbitrage by taking offsetting positions in both portfolios, locking in a profit with no risk or capital required. The fact that such opportunities are immediately exploited in liquid markets is why put-call parity holds as a near-exact constraint on European option prices.

The practical import of put-call parity is that it links the pricing of calls and puts. Once you know the call price, you can infer the put price (or vice versa) without independently modeling the put. This is why market makers focus on calls in many markets and back out put prices from parity, and it's why any apparent discrepancy between call and put prices is a signal of either illiquidity or imminent arbitrage. Building toward Black-Scholes, put-call parity is one of the few pricing relationships that holds without any model assumptions about return distributions — it follows from no-arbitrage alone, making it more robust than model-dependent pricing formulas.
