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
stage: expert
status: validated
---

# First-Price Sealed-Bid Auction

## Core Idea
In a first-price auction, the highest bidder wins and pays their own bid. Bidders shade bids below true valuations: in symmetric equilibrium with N bidders and uniform valuations on [0, v], equilibrium bid is b(v) = ((N-1)/N)v. Revenue increases with N. Unlike second-price auctions, truthful bidding is not dominant.

## Questions

```yaml
- question: "In a first-price sealed-bid auction with 5 symmetric bidders drawing valuations uniformly from [0, $100], a bidder with true valuation $80 submits a bid of $80. Is this optimal?"
  type: multiple-choice
  options:
    - "Yes — bidding true value maximizes win probability, which is the primary goal"
    - "Yes — like a second-price auction, truthful bidding is the dominant strategy in any sealed-bid format"
    - "No — bidding $80 guarantees zero surplus even if she wins; the equilibrium bid is $64, shading by (1/N) to balance win probability against surplus"
    - "No — she should bid above $80 to outcompete rivals with higher valuations"
  answer: 2
  explanation: "In a first-price auction, winners pay their own bid, so bidding true value yields zero profit even when winning. The equilibrium strategy is b(v) = ((N-1)/N)v — with N=5, she should bid (4/5)×$80 = $64. This shading trades a lower win probability for positive surplus when she does win. Option B is the critical misconception: truthful bidding is dominant only in second-price auctions, where the winner pays the second-highest bid regardless of her own bid."

- question: "A seller must choose between a first-price and second-price auction. A consultant argues: 'The second-price format will generate more revenue because bidders reveal their true values instead of shading.' Under standard assumptions (symmetric, independent private values, risk-neutral bidders), is this correct?"
  type: multiple-choice
  options:
    - "Yes — truthful bidding always extracts full valuation surplus for the seller"
    - "No — revenue equivalence holds: both formats yield the same expected seller revenue because equilibrium bid shading in the first-price format exactly offsets the higher nominal bids in the second-price format"
    - "Yes — bid shading in first-price auctions necessarily hurts the seller relative to second-price"
    - "No — first-price always generates more revenue because the winner pays more than the second-highest value"
  answer: 1
  explanation: "Revenue equivalence is the key theorem: under symmetric independent private values with risk-neutral bidders, first-price and second-price auctions generate identical expected seller revenue. In second-price, the winner bids truthfully but pays only the second-highest value. In first-price, the winner shades to (N-1)/N of her value and pays that shaded amount — which turns out to equal the expected second-highest valuation given she has the highest. The expected payments are identical. Revenue equivalence breaks down only when bidders are risk-averse, valuations are asymmetric, or there is a common-value component."

- question: "In a first-price sealed-bid auction, as the number of symmetric bidders increases without limit, equilibrium bids converge toward each bidder's true valuation."
  type: true-false
  answer: true
  explanation: "The equilibrium bid formula b(v) = ((N-1)/N)v approaches v as N → ∞. With many competitors, the expected gap between the highest and second-highest valuation shrinks — you cannot afford to shade aggressively without risking losing to a rival with a nearly identical valuation. In the limit, competition does the seller's work of extracting true valuations, analogously to how perfect competition drives price to marginal cost."

- question: "In a first-price sealed-bid auction, bidding your true valuation is the dominant strategy, just as it is in a second-price (Vickrey) auction."
  type: true-false
  answer: false
  explanation: "In a second-price auction, the winner pays the second-highest bid, so your own bid determines only whether you win, not what you pay — making truthful bidding dominant regardless of others' bids. In a first-price auction, the winner pays their own bid, so winning at your true value yields exactly zero surplus. The optimal strategy is to shade below true value, with b(v) = ((N-1)/N)v in the symmetric uniform-values model. Truthful bidding is never optimal in a first-price auction with positive competition."

- question: "Why does the revenue equivalence theorem hold between first-price and second-price auctions, despite the fact that bidders shade their bids in first-price but bid truthfully in second-price?"
  type: short-answer
  answer: "In a second-price auction, winners bid truthfully but pay only the second-highest bid — retaining surplus equal to (own value − second-highest value). In a first-price auction, winners shade their bids to (N-1)/N of their value and pay that shaded amount. The equilibrium shaded bid turns out to equal the expected value of the second-order statistic from the valuation distribution, given that the bidder has the highest valuation. So in expectation, the winner pays the same amount in both formats, and the seller receives the same expected revenue. What the seller gains from truthful bidding in the second-price format is exactly offset by the shading in the first-price format."
  explanation: "The theorem is counterintuitive because the mechanisms feel so different. The insight is that rational agents adjust their strategies to equalize expected payoffs, and in doing so equate expected payments to the seller. Revenue equivalence breaks down when these equilibrating adjustments cannot fully compensate — for instance, when risk-averse bidders shade less in first-price (because the certain win at a shaded bid is preferred over a risky bet), raising first-price revenue above the second-price benchmark."
```

## Explainer

From auction theory, you know the four standard auction formats and the revenue equivalence theorem. The **first-price sealed-bid auction** is the format that most clearly illustrates strategic bid shading — the central tension between wanting to win and wanting to pay less. Each bidder submits a single sealed bid, the highest bidder wins, and they pay exactly what they bid. Unlike the second-price auction where truthful bidding is dominant, here bidding your true value guarantees zero surplus if you win. The entire strategic problem is figuring out how far below your true value to bid.

Consider the tradeoff facing a bidder who values the item at $80. Bidding $80 guarantees zero profit even if she wins. Bidding $50 yields $30 profit if she wins — but she might lose to someone who bid $60. The optimal bid balances the **probability of winning** (which increases with your bid) against the **surplus if you win** (which decreases with your bid). The expected payoff is (v - b) × Pr(win | b), and the bidder chooses b to maximize this expression. Solving this optimization requires knowing the distribution of competing bids, which depends on the distribution of competing valuations.

In the symmetric **independent private values** model with N bidders whose valuations are drawn uniformly from [0, v̄], the equilibrium bidding strategy has an elegant closed form: **b(v) = ((N-1)/N) × v**. A bidder with valuation v bids a fraction (N-1)/N of her true value. With 2 bidders, you bid half your value; with 10 bidders, you bid 90% of your value. The intuition is direct: more competition means a smaller gap between the highest and second-highest valuations, so you cannot afford to shade as aggressively. As N grows large, bids converge to true values and the auction approaches full surplus extraction — competition does the seller's work.

This equilibrium bidding function reveals why revenue equivalence holds despite the very different feel of first-price and second-price auctions. In a second-price auction, the winner pays the second-highest value and there is no shading. In a first-price auction, the winner pays her own shaded bid, which is lower than her value but higher than the second-highest bid. The expected payment turns out to be identical: in both cases, the expected revenue equals the expected value of the second-highest order statistic of the valuation distribution. Revenue equivalence breaks down when bidders are risk-averse (they shade less in first-price auctions, raising revenue above the second-price benchmark), when valuations are asymmetric (different bidders draw from different distributions), or when valuations have a common-value component (introducing the winner's curse).
