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

## Questions

```yaml
- question: "A European call costs $8 and the corresponding European put costs $3. The stock price is $100, the strike is $98, and PV(K) = $95. Does put-call parity hold?"
  type: multiple-choice
  options:
    - "No — C − P = $5 but S − PV(K) = $3, so there is an arbitrage opportunity"
    - "No — C − P = $5 but S − PV(K) = $7, so the call is overpriced"
    - "Yes — C − P = $5 and S − PV(K) = $5, so parity holds exactly"
    - "Yes — parity always holds by definition for European options regardless of prices"
  answer: 2
  explanation: "C − P = $8 − $3 = $5, and S − PV(K) = $100 − $95 = $5. Both sides equal $5, so put-call parity holds exactly and no arbitrage opportunity exists. If they differed — say, C − P = $6 but S − PV(K) = $5 — then a riskless profit would be available by selling the overpriced side (call+short put) and buying the underpriced side (long forward)."

- question: "An investor buys a straddle (buys a call and a put at the same strike K) for a total premium of $8. For what range of stock prices at expiration does the investor profit?"
  type: multiple-choice
  options:
    - "Only if the stock rises above the strike by more than $8"
    - "If the stock finishes exactly at the strike — both options are at-the-money and earn the premium back"
    - "If the stock finishes more than $8 above or more than $8 below the strike"
    - "Only if the stock falls below the strike by more than $8"
  answer: 2
  explanation: "A straddle has a V-shaped payoff: the combined payoff is |S_T − K| — the absolute distance from the strike. After paying $8 in total premium, the investor profits if |S_T − K| > $8, i.e., the stock finishes more than $8 away from the strike in either direction. This is why straddles are used before earnings: the direction of the move is unknown, but if the move is large enough to exceed the total premium paid, the straddle profits regardless of direction."

- question: "Put-call parity holds for both European and American options traded on the same underlying stock."
  type: true-false
  answer: false
  explanation: "Put-call parity holds exactly only for European options (exercisable only at expiration). American options carry an early exercise premium — the holder may exercise before expiration when advantageous — which breaks the exact replication argument. For American options, the relationship satisfies an inequality: S − K ≤ C − P ≤ S − PV(K), rather than an equality."

- question: "A bull spread with strikes K₁ = $50 and K₂ = $60 and a net premium of $3 will always profit if the stock finishes above $60 at expiration."
  type: true-false
  answer: true
  explanation: "A bull spread buys a call at K₁ = $50 and sells a call at K₂ = $60. Above K₂, both options are in-the-money: the long call pays S_T − 50 and the short call costs S_T − 60, for a net payoff of $10 regardless of how far above $60 the stock finishes. After paying the $3 net premium, the profit is a fixed $7. The payoff is capped and flat above K₂, and the break-even is at K₁ + premium = $53."

- question: "Explain why put-call parity must hold for European options in liquid markets, using the concept of no-arbitrage."
  type: short-answer
  answer: "If C − P ≠ S − PV(K), you can construct a riskless profit with no capital at risk. A portfolio of long call plus short put has the same payoff at expiration as a long forward (obligation to buy at K): both pay S_T − K regardless of whether S_T is above or below K. A long forward today costs S − PV(K). If C − P > S − PV(K), sell the call+short-put portfolio and buy the forward, locking in an immediate profit with zero net risk. Competition among arbitrageurs eliminates any such gap, enforcing parity."
  explanation: "The replication argument is the backbone of no-arbitrage pricing: two portfolios with identical payoffs in every future state must have identical prices today. The long call plus short put replicates a forward, whose current value is S − PV(K). Any wedge between C − P and S − PV(K) is immediately exploitable by buying cheap and selling expensive. In liquid markets, arbitrageurs eliminate these gaps almost instantly — which is why put-call parity is an empirical near-equality rather than just a theoretical result, and why it holds without any model assumptions about return distributions."
```

## Explainer

From your study of options basics, you know the building blocks: a call gives the right to buy at strike K, a long call pays max(S_T − K, 0) at expiration, and a put pays max(K − S_T, 0). Options become strategically powerful when you combine them. The key insight is that any payoff profile you want — bounded upside, protection against downside, profit from large moves in either direction — can be engineered by mixing calls, puts, and the underlying stock. Learning to read and construct **payoff diagrams** (the shape of profit/loss at expiration as a function of the terminal stock price S_T) is the entry point to options strategy.

The most instructive strategies are built from two or three legs. A **bull spread** buys a call at a lower strike K₁ and sells a call at a higher strike K₂ > K₁. The sold call brings in premium, reducing cost, but caps your upside at K₂. Your payoff diagram shows flat losses below K₁, linear gains between K₁ and K₂, and flat profits above K₂. This strategy reflects a moderate bullish view: you expect the stock to rise but are willing to surrender gains above K₂ in exchange for a cheaper position. A **straddle** buys both a call and a put at the same strike. The payoff is V-shaped: losses if the stock barely moves (you paid two premiums) and gains if it moves far in either direction. Straddles are popular before earnings announcements — you don't know which direction the stock will move, but you believe the move will be large enough to exceed the total premium paid.

**Put-call parity** is the fundamental no-arbitrage relationship that ties all of these pieces together: C − P = S − PV(K), where C is the European call price, P is the European put price, S is the current stock price, and PV(K) is the present value of the strike (discounted at the risk-free rate over the option's life). The derivation is a replication argument: a portfolio of long call plus short put replicates a forward contract on the stock (obligation to buy at K), which today costs S − PV(K). If C − P ≠ S − PV(K), you can construct a riskless arbitrage by taking offsetting positions in both portfolios, locking in a profit with no risk or capital required. The fact that such opportunities are immediately exploited in liquid markets is why put-call parity holds as a near-exact constraint on European option prices.

The practical import of put-call parity is that it links the pricing of calls and puts. Once you know the call price, you can infer the put price (or vice versa) without independently modeling the put. This is why market makers focus on calls in many markets and back out put prices from parity, and it's why any apparent discrepancy between call and put prices is a signal of either illiquidity or imminent arbitrage. Building toward Black-Scholes, put-call parity is one of the few pricing relationships that holds without any model assumptions about return distributions — it follows from no-arbitrage alone, making it more robust than model-dependent pricing formulas.
