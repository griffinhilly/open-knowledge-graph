---
id: first-price-second-price-auctions
title: 'Auction Design: First-Price and Second-Price Sealed-Bid Auctions'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: mechanism-design-and-vickrey-clarke-groves
  type: hard
tags:
- auction-theory
- mechanism-design
stage: advanced
status: draft
---

# Auction Design: First-Price and Second-Price Sealed-Bid Auctions

## Core Idea
In second-price (Vickrey) auctions, the winner pays the second-highest bid and truth-telling is dominant. In first-price auctions, the winner pays their own bid, inducing bid-shading below true value. The Revenue Equivalence Theorem shows these formats generate the same expected revenue under independent private values. Strategic incentives differ fundamentally between formats.

## Explainer

Consider selling a painting through a sealed-bid auction. Each bidder privately writes down a number and submits it. The highest bidder wins. The question is: how much does the winner pay? This single design choice — the payment rule — fundamentally changes how rational bidders behave, even though the information structure and allocation rule (highest bid wins) are identical.

In a **second-price sealed-bid auction** (also called a Vickrey auction), the winner pays the *second-highest* bid, not their own. This creates a remarkable strategic property: **truth-telling is a dominant strategy**. To see why, suppose your true value for the painting is $500. If you bid $500 and win, you pay whatever the second-highest bidder submitted — say $350 — and pocket $150 in surplus. Could you do better by bidding $600? You win in exactly the same cases (your bid only matters for whether you win, not what you pay), so overbidding gains nothing. Could you do better by bidding $400? You might lose to someone who bid $450, forfeiting a deal that would have given you $50 in surplus. Underbidding can only hurt you. The dominant strategy is to bid exactly your value, regardless of what others do. This is why the Vickrey auction is central to mechanism design — it achieves efficient allocation (the highest-value bidder always wins) through a simple incentive structure.

In a **first-price sealed-bid auction**, the winner pays their own bid. Now truth-telling is disastrous: if you bid your true value and win, your surplus is zero. Every rational bidder **shades their bid** below their true value, trading a lower probability of winning for positive surplus when they do win. The optimal amount of shading depends on your beliefs about competitors' values. With *n* bidders whose values are independently drawn from a uniform distribution on [0, 1], the symmetric equilibrium strategy is to bid (n−1)/n times your true value. With 2 bidders, you bid half your value; with 10, you bid nine-tenths. More competition means less shading, because the risk of losing to a close rival outweighs the benefit of a larger surplus.

The **Revenue Equivalence Theorem** delivers a surprising punchline: under independent private values with risk-neutral bidders, the seller's expected revenue is the same in both formats. In the second-price auction, winners pay less (the second-highest value), but they bid their true values. In the first-price auction, winners pay more (their own bid), but they shade below their true values. These effects offset exactly. The theorem extends far beyond these two formats — it applies to any auction that allocates the good to the highest-value bidder and gives zero surplus to a bidder with the lowest possible value. Revenue equivalence does break down with risk aversion (first-price generates more revenue because bidders shade less to avoid losing), correlated values, or asymmetric bidders, which is why auction design in practice — from spectrum licenses to online advertising — requires careful attention to the specific environment.
