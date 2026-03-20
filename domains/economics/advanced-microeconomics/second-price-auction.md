---
id: second-price-auction
title: Second-Price Sealed-Bid Auction (Vickrey Auction)
domain: economics
course: advanced-microeconomics
prerequisites:
- id: auction-theory
  type: hard
tags:
- auctions
- bidding
- truthful-revelation
stage: advanced
status: draft
---

# Second-Price Sealed-Bid Auction (Vickrey Auction)

## Core Idea
In a Vickrey auction, the highest bidder wins but pays the second-highest bid. Truthful bidding is a weakly dominant strategy: bid true valuation regardless of others' bids. This simplicity makes Vickrey auctions attractive for online advertising and spectrum sales, though they differ slightly from pure Vickrey in practice.

## How It's Best Learned
Analyze bidder payoffs graphically. Show that truthful bid maximizes utility for any bid distribution. Compare revenue with first-price auctions.

## Explainer

From your study of auction theory, you know that auction design is about setting rules that determine who wins and what they pay. In a **second-price sealed-bid auction** (also called a **Vickrey auction**), each bidder submits a single sealed bid without seeing others' bids. The highest bidder wins the item, but — and this is the crucial twist — they pay the *second*-highest bid, not their own. This payment rule, which seems counterintuitive at first, produces a remarkably clean strategic result.

The key insight is that **bidding your true valuation is a weakly dominant strategy**. To see why, suppose you value a painting at $500. If you bid $500 (truthfully), there are two cases. If the highest competing bid is below $500 — say $350 — you win and pay $350, netting $150 in surplus. If the highest competing bid is above $500 — say $600 — you lose, but that is fine because winning would have meant paying more than the item is worth to you. Now consider deviating. If you bid above your value — say $550 — you might win when the second-highest bid is $520, but then you pay $520 for something worth only $500 to you, losing $20. If you bid below your value — say $400 — you might lose when the second-highest bid is $450, missing a deal that would have given you $50 of surplus. Truthful bidding avoids both pitfalls: it wins exactly when winning is profitable and loses exactly when winning would be unprofitable.

This logic holds regardless of how many bidders participate, what their valuations are, or what strategies they use. Your optimal bid depends only on your own valuation — you never need to guess what others will do. This **dominant strategy** property makes the Vickrey auction especially attractive in practice because bidders face no strategic complexity. Contrast this with the first-price auction, where the winner pays their own bid: there, optimal bidding requires shading your bid below your true value (to capture surplus), which in turn requires estimating the distribution of competing bids. The first-price auction demands sophisticated strategic reasoning; the second-price auction demands only self-knowledge.

A natural question is whether the auctioneer sacrifices revenue by using this generous payment rule. The **revenue equivalence theorem** shows that under standard assumptions (risk-neutral bidders, independent private values), the expected revenue is identical across first-price and second-price auctions. In the first-price auction, bidders shade their bids down but pay what they bid; in the second-price auction, bidders bid truthfully but pay less than their bid. These effects exactly offset. The Vickrey auction is the single-item case of the more general VCG mechanism — the same "pay your externality" logic that makes truth-telling dominant in broader mechanism design problems. In practice, second-price auctions form the backbone of online advertising markets (Google's ad auctions use a variant), precisely because the dominant-strategy property means bidders can participate without needing complex bidding algorithms.
