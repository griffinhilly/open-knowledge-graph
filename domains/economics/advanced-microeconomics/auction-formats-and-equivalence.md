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
stage: expert
status: draft
---

# Auction Formats and Revenue Equivalence

## Core Idea
Standard auction formats include English (ascending price), Dutch (descending price), sealed-bid first-price, and sealed-bid second-price. Under symmetric bidder assumptions, these formats generate equal expected revenue (revenue equivalence theorem). Different formats induce different bidding behavior and have different strategic implications.

## Questions

```yaml
- question: "A bidder values an item at $100. In which auction format is bidding exactly $100 a weakly dominant strategy — meaning it is never worse than any other bid, regardless of what others do?"
  type: multiple-choice
  options:
    - "Sealed-bid first-price auction, because winning with a lower bid wastes surplus"
    - "Dutch auction, because claiming the item early avoids the risk of losing"
    - "Sealed-bid second-price (Vickrey) auction, because winning means you pay the second-highest bid, not your own"
    - "English auction only when fewer than three competitors are present"
  answer: 2
  explanation: "In a Vickrey (second-price) auction, truthful bidding is a weakly dominant strategy: if you win, you pay someone else's bid, not yours, so bidding your true value cannot hurt you. Bidding above your value risks winning and overpaying; bidding below risks losing when you could have won profitably. In first-price and Dutch auctions, you pay your own bid, so the optimal strategy is bid shading — bidding below true value — making truthful bidding suboptimal there."

- question: "A seller knows her bidders are strongly risk-averse (they dislike uncertainty about whether they will win). Compared to a second-price auction, a first-price auction will generate:"
  type: multiple-choice
  options:
    - "The same revenue, because the revenue equivalence theorem holds regardless of bidder risk preferences"
    - "Lower revenue, because risk-averse bidders shade their bids further below value to avoid overpaying"
    - "Higher revenue, because risk-averse bidders shade their bids less (they bid more aggressively to reduce the chance of losing)"
    - "Revenue that depends only on the number of bidders, not on their risk attitudes"
  answer: 2
  explanation: "Revenue equivalence breaks down when bidders are risk-averse. In a first-price auction, where losing means getting nothing, risk-averse bidders shade their bids *less* aggressively than risk-neutral bidders would — they accept a smaller surplus to increase their probability of winning. This higher bidding translates into higher expected revenue for the seller. Second-price auctions do not produce this effect because the winner's payment is independent of their own bid."

- question: "A Dutch auction (descending-price) and a sealed-bid first-price auction are strategically equivalent: the optimal bidding strategy and the distribution of outcomes are identical in both."
  type: true-false
  answer: true
  explanation: "In both formats, a bidder must commit to a price before knowing others' bids, and the winner pays exactly their own bid. The strategic problem is identical: how much to shade below your true value, trading off a higher probability of winning (bid high) against a larger surplus if you do win (bid low). Because the information structure and payoff structure are the same, both formats induce the same equilibrium bids and the same expected outcomes."

- question: "The revenue equivalence theorem implies that bidders behave the same way across all four standard auction formats."
  type: true-false
  answer: false
  explanation: "Revenue equivalence says expected *revenues* are equal under its assumptions — not that bidding behavior is identical. In fact, bidding behavior is strikingly different: in English and Vickrey auctions, truthful bidding is dominant; in Dutch and first-price auctions, the equilibrium involves bid shading below true value. The theorem's insight is that these very different strategies happen to produce the same expected revenue for the seller. Behavior diverges; outcomes (in expectation) do not."

- question: "Explain the core logic of the revenue equivalence theorem: why should four auction formats with such different rules produce the same expected revenue?"
  type: short-answer
  answer: "Under the theorem's assumptions (risk-neutral, symmetric bidders; highest-value bidder wins; bidder with lowest value pays zero), what ultimately determines revenue is the underlying distribution of bidder values and the number of bidders. Strategic differences across formats (truthful bidding vs. shading) exactly offset each other: in formats where bidders shade down, they win at lower prices but more often in the right situations, leaving the seller's expected take unchanged. The information rents captured by each bidder are the same in all formats because the winner's expected payment is pinned down by the second-highest value — regardless of how that payment is realized."
  explanation: "The deep intuition is that a seller cannot extract more than the 'information rent' a bidder has by virtue of having a higher value than competitors. Any format that awards the item to the highest-value bidder and leaves the lowest-value bidder with zero surplus must generate the same expected revenue — the format's rules determine how revenue is distributed across outcomes, but the expectation is invariant. Revenue equivalence fails when one of these conditions breaks down: asymmetric bidders have different information rents; correlated values (winner's curse) change incentives; risk aversion changes the bid-shading calculus."
```

## Explainer

From Nash equilibrium, you know how to find stable strategy profiles where no player wants to deviate. Auctions are a natural and high-stakes application: each bidder must decide how much to bid, knowing that others are making the same calculation. The four standard **auction formats** each create a different strategic environment, yet under certain conditions they produce surprisingly similar outcomes.

In an **English auction** (ascending price), the auctioneer starts low and raises the price until only one bidder remains. Your dominant strategy is simple: stay in until the price exceeds your valuation, then drop out. You never need to guess what others will bid — you just react to the rising price. The winner is the bidder with the highest valuation, and they pay approximately the second-highest valuation (the price at which the last competitor dropped out). A **sealed-bid second-price auction** (also called a Vickrey auction) reaches the same outcome through a different mechanism: each bidder submits one sealed bid, the highest bid wins, but the winner pays the *second*-highest bid. Here, bidding your true valuation is a weakly dominant strategy — you cannot do better by shading your bid up or down. These two formats are **strategically equivalent**: both lead to truthful revelation and payment equal to the second-highest value.

The **Dutch auction** (descending price) starts high and drops until someone claims the item. This is strategically identical to a **sealed-bid first-price auction**: in both cases, you must commit to a price without knowing others' bids, and if you win, you pay exactly what you bid. The optimal strategy involves **bid shading** — bidding below your true valuation to capture some surplus, balanced against the risk of losing to a slightly higher bid. How much you shade depends on the number of competitors and what you believe about the distribution of their valuations. More competitors means less shading, because the risk of being outbid rises.

The **revenue equivalence theorem** is the unifying result. It states that under four conditions — bidders are risk-neutral, symmetric (values drawn from the same distribution), the bidder with the highest value wins, and the bidder with the lowest possible value pays nothing — all four auction formats generate the same **expected revenue** for the seller. This is remarkable because the formats look so different: some involve truthful bidding, others strategic shading; some are dynamic, others static. The theorem shows that these surface differences wash out in expectation. The intuition is that what determines revenue is the underlying distribution of values and the number of bidders, not the specific rules of the game. Revenue equivalence breaks down when its assumptions fail — when bidders are risk-averse (favoring first-price auctions, which generate more revenue), when values are correlated (the "winner's curse" becomes relevant), or when bidders are asymmetric. These violations are precisely why auction design matters in practice and why governments and firms invest heavily in choosing the right format for spectrum sales, procurement, and online advertising.
