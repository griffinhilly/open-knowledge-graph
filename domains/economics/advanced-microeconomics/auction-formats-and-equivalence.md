---
id: auction-formats-and-equivalence
title: Auction Formats and Revenue Equivalence
domain: economics
course: advanced-microeconomics
prerequisites:
- id: nash-equilibrium-microeconomics
  type: hard
- id: vcg-auction-mechanism
  type: soft
tags:
- auctions
- mechanism-design
- bidding
stage: advanced
status: draft
---

# Auction Formats and Revenue Equivalence

## Core Idea
Standard auction formats include English (ascending price), Dutch (descending price), sealed-bid first-price, and sealed-bid second-price. Under symmetric bidder assumptions, these formats generate equal expected revenue (revenue equivalence theorem). Different formats induce different bidding behavior and have different strategic implications.

## Explainer

From Nash equilibrium, you know how to find stable strategy profiles where no player wants to deviate. Auctions are a natural and high-stakes application: each bidder must decide how much to bid, knowing that others are making the same calculation. The four standard **auction formats** each create a different strategic environment, yet under certain conditions they produce surprisingly similar outcomes.

In an **English auction** (ascending price), the auctioneer starts low and raises the price until only one bidder remains. Your dominant strategy is simple: stay in until the price exceeds your valuation, then drop out. You never need to guess what others will bid — you just react to the rising price. The winner is the bidder with the highest valuation, and they pay approximately the second-highest valuation (the price at which the last competitor dropped out). A **sealed-bid second-price auction** (also called a Vickrey auction) reaches the same outcome through a different mechanism: each bidder submits one sealed bid, the highest bid wins, but the winner pays the *second*-highest bid. Here, bidding your true valuation is a weakly dominant strategy — you cannot do better by shading your bid up or down. These two formats are **strategically equivalent**: both lead to truthful revelation and payment equal to the second-highest value.

The **Dutch auction** (descending price) starts high and drops until someone claims the item. This is strategically identical to a **sealed-bid first-price auction**: in both cases, you must commit to a price without knowing others' bids, and if you win, you pay exactly what you bid. The optimal strategy involves **bid shading** — bidding below your true valuation to capture some surplus, balanced against the risk of losing to a slightly higher bid. How much you shade depends on the number of competitors and what you believe about the distribution of their valuations. More competitors means less shading, because the risk of being outbid rises.

The **revenue equivalence theorem** is the unifying result. It states that under four conditions — bidders are risk-neutral, symmetric (values drawn from the same distribution), the bidder with the highest value wins, and the bidder with the lowest possible value pays nothing — all four auction formats generate the same **expected revenue** for the seller. This is remarkable because the formats look so different: some involve truthful bidding, others strategic shading; some are dynamic, others static. The theorem shows that these surface differences wash out in expectation. The intuition is that what determines revenue is the underlying distribution of values and the number of bidders, not the specific rules of the game. Revenue equivalence breaks down when its assumptions fail — when bidders are risk-averse (favoring first-price auctions, which generate more revenue), when values are correlated (the "winner's curse" becomes relevant), or when bidders are asymmetric. These violations are precisely why auction design matters in practice and why governments and firms invest heavily in choosing the right format for spectrum sales, procurement, and online advertising.
