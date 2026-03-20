---
id: first-price-auction
title: First-Price Sealed-Bid Auction
domain: economics
course: advanced-microeconomics
prerequisites:
- id: auction-theory
  type: hard
tags:
- auctions
- bidding
- sealed-bid
stage: advanced
status: draft
---

# First-Price Sealed-Bid Auction

## Core Idea
In a first-price auction, the highest bidder wins and pays their own bid. Bidders shade bids below true valuations: in symmetric equilibrium with N bidders and uniform valuations on [0, v], equilibrium bid is b(v) = ((N-1)/N)v. Revenue increases with N. Unlike second-price auctions, truthful bidding is not dominant.

## Explainer

From auction theory, you know the four standard auction formats and the revenue equivalence theorem. The **first-price sealed-bid auction** is the format that most clearly illustrates strategic bid shading — the central tension between wanting to win and wanting to pay less. Each bidder submits a single sealed bid, the highest bidder wins, and they pay exactly what they bid. Unlike the second-price auction where truthful bidding is dominant, here bidding your true value guarantees zero surplus if you win. The entire strategic problem is figuring out how far below your true value to bid.

Consider the tradeoff facing a bidder who values the item at $80. Bidding $80 guarantees zero profit even if she wins. Bidding $50 yields $30 profit if she wins — but she might lose to someone who bid $60. The optimal bid balances the **probability of winning** (which increases with your bid) against the **surplus if you win** (which decreases with your bid). The expected payoff is (v - b) × Pr(win | b), and the bidder chooses b to maximize this expression. Solving this optimization requires knowing the distribution of competing bids, which depends on the distribution of competing valuations.

In the symmetric **independent private values** model with N bidders whose valuations are drawn uniformly from [0, v̄], the equilibrium bidding strategy has an elegant closed form: **b(v) = ((N-1)/N) × v**. A bidder with valuation v bids a fraction (N-1)/N of her true value. With 2 bidders, you bid half your value; with 10 bidders, you bid 90% of your value. The intuition is direct: more competition means a smaller gap between the highest and second-highest valuations, so you cannot afford to shade as aggressively. As N grows large, bids converge to true values and the auction approaches full surplus extraction — competition does the seller's work.

This equilibrium bidding function reveals why revenue equivalence holds despite the very different feel of first-price and second-price auctions. In a second-price auction, the winner pays the second-highest value and there is no shading. In a first-price auction, the winner pays her own shaded bid, which is lower than her value but higher than the second-highest bid. The expected payment turns out to be identical: in both cases, the expected revenue equals the expected value of the second-highest order statistic of the valuation distribution. Revenue equivalence breaks down when bidders are risk-averse (they shade less in first-price auctions, raising revenue above the second-price benchmark), when valuations are asymmetric (different bidders draw from different distributions), or when valuations have a common-value component (introducing the winner's curse).
