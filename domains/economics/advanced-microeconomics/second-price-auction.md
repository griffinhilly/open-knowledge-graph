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
stage: expert
status: validated
---

# Second-Price Sealed-Bid Auction (Vickrey Auction)

## Core Idea
In a Vickrey auction, the highest bidder wins but pays the second-highest bid. Truthful bidding is a weakly dominant strategy: bid true valuation regardless of others' bids. This simplicity makes Vickrey auctions attractive for online advertising and spectrum sales, though they differ slightly from pure Vickrey in practice.

## How It's Best Learned
Analyze bidder payoffs graphically. Show that truthful bid maximizes utility for any bid distribution. Compare revenue with first-price auctions.

## Questions

```yaml
- question: "You value a painting at $600. In a Vickrey auction, you bid $800. The highest competing bid turns out to be $750. What is your payoff?"
  type: multiple-choice
  options:
    - "+$600, because you won the item you wanted"
    - "-$150, because you pay $750 for something worth $600 to you"
    - "+$50, because your surplus is $800 minus $750"
    - "$0, because overbidding in a Vickrey auction is always a dominant strategy"
  answer: 1
  explanation: "You win and pay the second-highest bid ($750), but the item is only worth $600 to you—a loss of $150. This is precisely the risk of overbidding: you occasionally win at a price above your true value, which is never worth it. A truthful bid of $600 would have lost this auction (to the $750 bidder), but that outcome is correct—winning at $750 when your value is $600 destroys $150 of surplus."

- question: "Why does truthful bidding eliminate the strategic complexity that bidders face in first-price auctions?"
  type: multiple-choice
  options:
    - "In second-price auctions, all bidders observe each other's valuations before submitting bids"
    - "Your optimal bid depends only on your own valuation, not on competitors' distributions or strategies"
    - "The auctioneer enforces truthful revelation through binding contracts before the auction starts"
    - "Second-price auctions have fewer participants, so strategic calculation is unnecessary"
  answer: 1
  explanation: "In a first-price auction, optimal bidding requires shading your bid below your value—and how much to shade depends on beliefs about competitors' valuations and strategies. In a second-price auction, truthful bidding is dominant regardless of what others do. Your payoff-maximizing bid is simply your own value. The payment rule renders competitors' information irrelevant to your bidding decision."

- question: "In a Vickrey auction, a bidder who knows their valuation exactly has no incentive to deviate from bidding that valuation, regardless of what other bidders do."
  type: true-false
  answer: true
  explanation: "This is what 'weakly dominant strategy' means: truth-telling is at least as good as any other bid for every possible configuration of competing bids. No information about competitors—whether you have it or not—can make a non-truthful bid better. This property is exceptional; most auction formats require you to form beliefs about competitors to bid optimally."

- question: "Under standard assumptions, a seller earns higher expected revenue from a Vickrey auction than from a first-price sealed-bid auction, because bidders in first-price auctions shade their bids downward."
  type: true-false
  answer: false
  explanation: "The revenue equivalence theorem shows that both auction formats yield identical expected revenue under standard assumptions (risk-neutral bidders, independent private values, symmetric equilibrium). In first-price auctions, bidders shade their bids but pay what they bid; in Vickrey auctions, bidders bid truthfully but pay the second-highest bid. These effects exactly cancel in expectation."

- question: "Why is bidding below your true valuation also a mistake in a Vickrey auction, even though it seems to protect you from overpaying?"
  type: short-answer
  answer: "Bidding below your value risks losing auctions you should win. If a competing bid falls between your true value and your understated bid, you lose even though winning would have been profitable—since you would have paid the competitor's lower bid. The Vickrey payment rule already protects you from overpaying: you always pay someone else's bid, not your own, so there is nothing to gain by understating your value and much to lose by missing profitable wins."
  explanation: "The dominant strategy proof covers both directions: bidding above value introduces the risk of winning at a loss, while bidding below value introduces the risk of missing a profitable win. Only truthful bidding avoids both failure modes simultaneously, for every possible realization of competing bids."
```

## Explainer

From your study of auction theory, you know that auction design is about setting rules that determine who wins and what they pay. In a **second-price sealed-bid auction** (also called a **Vickrey auction**), each bidder submits a single sealed bid without seeing others' bids. The highest bidder wins the item, but — and this is the crucial twist — they pay the *second*-highest bid, not their own. This payment rule, which seems counterintuitive at first, produces a remarkably clean strategic result.

The key insight is that **bidding your true valuation is a weakly dominant strategy**. To see why, suppose you value a painting at $500. If you bid $500 (truthfully), there are two cases. If the highest competing bid is below $500 — say $350 — you win and pay $350, netting $150 in surplus. If the highest competing bid is above $500 — say $600 — you lose, but that is fine because winning would have meant paying more than the item is worth to you. Now consider deviating. If you bid above your value — say $550 — you might win when the second-highest bid is $520, but then you pay $520 for something worth only $500 to you, losing $20. If you bid below your value — say $400 — you might lose when the second-highest bid is $450, missing a deal that would have given you $50 of surplus. Truthful bidding avoids both pitfalls: it wins exactly when winning is profitable and loses exactly when winning would be unprofitable.

This logic holds regardless of how many bidders participate, what their valuations are, or what strategies they use. Your optimal bid depends only on your own valuation — you never need to guess what others will do. This **dominant strategy** property makes the Vickrey auction especially attractive in practice because bidders face no strategic complexity. Contrast this with the first-price auction, where the winner pays their own bid: there, optimal bidding requires shading your bid below your true value (to capture surplus), which in turn requires estimating the distribution of competing bids. The first-price auction demands sophisticated strategic reasoning; the second-price auction demands only self-knowledge.

A natural question is whether the auctioneer sacrifices revenue by using this generous payment rule. The **revenue equivalence theorem** shows that under standard assumptions (risk-neutral bidders, independent private values), the expected revenue is identical across first-price and second-price auctions. In the first-price auction, bidders shade their bids down but pay what they bid; in the second-price auction, bidders bid truthfully but pay less than their bid. These effects exactly offset. The Vickrey auction is the single-item case of the more general VCG mechanism — the same "pay your externality" logic that makes truth-telling dominant in broader mechanism design problems. In practice, second-price auctions form the backbone of online advertising markets (Google's ad auctions use a variant), precisely because the dominant-strategy property means bidders can participate without needing complex bidding algorithms.
