---
id: first-price-second-price-auctions
title: 'Auction Design: First-Price and Second-Price Sealed-Bid Auctions'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: mechanism-design-basics
  type: hard
tags:
- auction-theory
- mechanism-design
stage: expert
status: validated
---

# Auction Design: First-Price and Second-Price Sealed-Bid Auctions

## Core Idea
In second-price (Vickrey) auctions, the winner pays the second-highest bid and truth-telling is dominant. In first-price auctions, the winner pays their own bid, inducing bid-shading below true value. The Revenue Equivalence Theorem shows these formats generate the same expected revenue under independent private values. Strategic incentives differ fundamentally between formats.

## Questions

```yaml
- question: "Your true value for an item is $400. In a second-price sealed-bid auction, what bid maximizes your expected payoff?"
  type: multiple-choice
  options:
    - "$400 — bidding your true value is the dominant strategy regardless of how many bidders there are"
    - "Less than $400 — you should shade your bid to reduce what you pay if you win"
    - "More than $400 — overbidding increases your chance of winning without changing what you pay"
    - "It depends on the number of other bidders and your beliefs about their values"
  answer: 0
  explanation: "In a second-price auction, the winner pays the second-highest bid, not their own. This decouples your bid (which determines whether you win) from what you pay (determined by others). Bidding above $400 risks winning at a price above your value — a loss. Bidding below $400 risks losing to someone who bid $350 when you could have won with positive surplus. Bidding exactly $400 is the only bid that cannot hurt you. This is true regardless of competition — it is a dominant strategy, not a best response to particular beliefs about others."

- question: "In a first-price sealed-bid auction with two bidders drawing values independently from a uniform distribution on [0, 1], the symmetric equilibrium strategy is:"
  type: multiple-choice
  options:
    - "Bid your true value — underbidding only risks losing to a close competitor"
    - "Bid half your true value — the equilibrium formula is (n-1)/n times your value, with n=2"
    - "Bid zero — in a one-shot game, credible commitment is impossible"
    - "Bid your value minus a constant depending on the number of bidders"
  answer: 1
  explanation: "In a first-price auction with n bidders and values uniform on [0,1], the symmetric Bayesian Nash equilibrium bid is (n-1)/n times your value. With n=2, each bidder bids half their value. Bidding your true value guarantees zero surplus if you win, which is irrational when you could shade down and earn positive surplus. The formula shows that bid-shading decreases as competition increases: with 10 bidders you bid 90% of your value, because the risk of losing to a close rival outweighs the benefit of shading further."

- question: "In a first-price auction, bidding your true value maximizes your chance of winning and is therefore the dominant strategy."
  type: true-false
  answer: false
  explanation: "Bidding your true value in a first-price auction maximizes your probability of winning but yields zero surplus if you win — you pay exactly what the item is worth to you. The rational strategy is bid-shading: bidding below your true value to preserve positive surplus upon winning. Truth-telling is the dominant strategy in second-price auctions, where your bid determines only whether you win, not what you pay. In first-price auctions, your bid determines both, making bid-shading the equilibrium response."

- question: "The Revenue Equivalence Theorem states that under independent private values with risk-neutral bidders, a seller's expected revenue is the same in first-price and second-price auctions."
  type: true-false
  answer: true
  explanation: "This is the theorem's central claim. In second-price auctions, winners bid their true values but pay less (the second-highest value). In first-price auctions, winners shade their bids but pay their own (shaded) bid. These effects exactly offset under independent private values with risk-neutral bidders, yielding identical expected revenue. The theorem breaks down with risk aversion (first-price generates more revenue because bidders shade less), correlated values, or asymmetric bidders — which is why real auction design requires attention to the specific environment."

- question: "Why is truth-telling a dominant strategy in a second-price auction but not in a first-price auction? Explain the key difference in how each payment rule affects bidding incentives."
  type: short-answer
  answer: "In a second-price auction, your bid determines only whether you win — not what you pay if you win. Payment equals the second-highest bid, which is independent of your own bid. This decoupling means shading your bid can only hurt you (by sometimes losing when you could have won), while overbidding cannot help (you still pay the second-highest bid). Bidding your true value is safe in all cases — a dominant strategy. In a first-price auction, your bid determines both whether you win and exactly what you pay. Bidding your true value guarantees zero surplus upon winning, so every rational bidder shades their bid below their value to trade a lower win probability for positive surplus when they do win."
  explanation: "The distinction hinges on whether the bid is pivotal for winning only or for both winning and paying. Second-price auctions decouple these, creating a dominant strategy. First-price auctions couple them, requiring strategic calculation about competitors' values and producing a Bayesian Nash equilibrium rather than a dominant strategy."
```

## Explainer

Consider selling a painting through a sealed-bid auction. Each bidder privately writes down a number and submits it. The highest bidder wins. The question is: how much does the winner pay? This single design choice — the payment rule — fundamentally changes how rational bidders behave, even though the information structure and allocation rule (highest bid wins) are identical.

In a **second-price sealed-bid auction** (also called a Vickrey auction), the winner pays the *second-highest* bid, not their own. This creates a remarkable strategic property: **truth-telling is a dominant strategy**. To see why, suppose your true value for the painting is $500. If you bid $500 and win, you pay whatever the second-highest bidder submitted — say $350 — and pocket $150 in surplus. Could you do better by bidding $600? You win in exactly the same cases (your bid only matters for whether you win, not what you pay), so overbidding gains nothing. Could you do better by bidding $400? You might lose to someone who bid $450, forfeiting a deal that would have given you $50 in surplus. Underbidding can only hurt you. The dominant strategy is to bid exactly your value, regardless of what others do. This is why the Vickrey auction is central to mechanism design — it achieves efficient allocation (the highest-value bidder always wins) through a simple incentive structure.

In a **first-price sealed-bid auction**, the winner pays their own bid. Now truth-telling is disastrous: if you bid your true value and win, your surplus is zero. Every rational bidder **shades their bid** below their true value, trading a lower probability of winning for positive surplus when they do win. The optimal amount of shading depends on your beliefs about competitors' values. With *n* bidders whose values are independently drawn from a uniform distribution on [0, 1], the symmetric equilibrium strategy is to bid (n−1)/n times your true value. With 2 bidders, you bid half your value; with 10, you bid nine-tenths. More competition means less shading, because the risk of losing to a close rival outweighs the benefit of a larger surplus.

The **Revenue Equivalence Theorem** delivers a surprising punchline: under independent private values with risk-neutral bidders, the seller's expected revenue is the same in both formats. In the second-price auction, winners pay less (the second-highest value), but they bid their true values. In the first-price auction, winners pay more (their own bid), but they shade below their true values. These effects offset exactly. The theorem extends far beyond these two formats — it applies to any auction that allocates the good to the highest-value bidder and gives zero surplus to a bidder with the lowest possible value. Revenue equivalence does break down with risk aversion (first-price generates more revenue because bidders shade less to avoid losing), correlated values, or asymmetric bidders, which is why auction design in practice — from spectrum licenses to online advertising — requires careful attention to the specific environment.
