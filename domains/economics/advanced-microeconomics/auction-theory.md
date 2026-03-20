---
id: auction-theory
title: Auction Theory
domain: economics
course: advanced-microeconomics
prerequisites:
- id: mechanism-design-intro
  type: hard
- id: probability-spaces-measure-theoretic
  type: soft
- id: game-theory-basics-microeconomics
  type: hard
- id: expected-value-theory
  type: hard
- id: optimization-multivariable-basics
  type: soft
builds-toward:
- first-price-auction
- second-price-auction
tags:
- auctions
- mechanism-design
- bidding
stage: advanced
status: draft
---

# Auction Theory

## Core Idea
Auction theory analyzes mechanisms for selling goods to bidders with private valuations. Key results include the revenue equivalence theorem (many auctions yield same expected revenue under symmetry) and the optimal auction design (Myerson auction). Auctions are canonical applications of mechanism design with incomplete information.

## Explainer

An auction is a game where a seller allocates a good to one of several buyers, each of whom privately knows how much the good is worth to them. From your study of game theory, you know how to analyze strategic interaction; from mechanism design, you know the seller can shape the rules to influence outcomes. Auction theory applies both toolkits to a specific, economically important setting: how should goods be sold when the seller does not know buyers' valuations?

The four classic auction formats illustrate how different rules create different strategic incentives. In an **English (ascending) auction**, the price rises until only one bidder remains — it is weakly dominant to stay in until the price hits your valuation. In a **Dutch (descending) auction**, the price falls from a high starting point and the first bidder to claim the item wins at that price — you must decide when to jump in, trading off the chance of a lower price against the risk of losing. In a **second-price sealed-bid auction**, each bidder submits one bid; the highest bidder wins but pays the second-highest bid — truthful bidding is a dominant strategy, since your bid only affects whether you win, not what you pay. In a **first-price sealed-bid auction**, the highest bidder wins and pays their own bid — so bidders shade their bids below their true values to earn positive surplus, and finding the equilibrium bidding strategy requires solving a differential equation using expected value calculations from your probability background.

The most striking result in auction theory is the **revenue equivalence theorem**: under symmetric independent private values, risk-neutral bidders, and a common prior distribution, all four standard auction formats generate the same expected revenue for the seller. This is surprising because the strategic reasoning feels so different across formats. The key insight is that any auction satisfying these conditions must give each bidder type the same expected surplus — and since the total surplus is fixed by the allocation, the seller's revenue must also be the same. Revenue equivalence tells you that if auctions differ in revenue, it must be because one of the assumptions is violated: bidders are risk-averse, valuations are correlated, bidders are asymmetric, or the reserve price differs.

When the seller wants to maximize revenue, the **Myerson optimal auction** provides the answer. The seller should allocate the good to the bidder with the highest **virtual valuation** — a transformation of the true valuation that accounts for the information rent bidders earn from having private information. Virtual valuation equals the true value minus a markup that depends on the distribution of types. This often means setting a reserve price that excludes low-value bidders entirely, even though selling to them would be efficient. The gap between efficiency and revenue maximization is a central theme: auctions that maximize social surplus (allocate to whoever values the good most) generally differ from auctions that maximize the seller's revenue, because extracting surplus from informed bidders requires distorting the allocation.
