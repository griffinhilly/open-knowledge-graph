---
id: auction-theory
title: Auction Theory
domain: economics
course: advanced-microeconomics
prerequisites:
- id: mechanism-design-basics
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
stage: expert
status: validated
---

# Auction Theory

## Core Idea
Auction theory analyzes mechanisms for selling goods to bidders with private valuations. Key results include the revenue equivalence theorem (many auctions yield same expected revenue under symmetry) and the optimal auction design (Myerson auction). Auctions are canonical applications of mechanism design with incomplete information.

## Questions

```yaml
- question: "A seller holds an English ascending auction and earns $500 in expected revenue. They consider switching to a first-price sealed-bid auction with identical bidders and valuations. Under standard assumptions, what should the seller expect?"
  type: multiple-choice
  options:
    - "Higher revenue — in first-price auctions bidders cannot observe rivals' bids, so they bid closer to their true values"
    - "Lower revenue — bidders shade their bids below true values in first-price auctions, reducing what the seller receives"
    - "The same expected revenue — both formats are covered by the revenue equivalence theorem under symmetric IPV and risk-neutral bidders"
    - "Revenue depends entirely on the number of bidders, not the auction format"
  answer: 2
  explanation: "The revenue equivalence theorem states that under symmetric independent private values, risk-neutral bidders, and a common prior distribution, all standard auction formats generate the same expected revenue. Although bidders shade their bids in a first-price auction (bidding below their true value to earn positive surplus), they bid more aggressively than they would in a second-price auction, and these effects exactly cancel. If revenues differ across formats in practice, it signals a violation of the assumptions — e.g., risk-averse bidders (who overbid in first-price to reduce uncertainty) or correlated valuations."

- question: "In a Myerson optimal auction, the seller refuses to sell to a bidder who values the item at $30 even when no other bidder is present. Why might this be revenue-maximizing?"
  type: multiple-choice
  options:
    - "The Myerson auction prioritizes fairness and requires multiple bidders to function"
    - "Setting a reserve price above $30 means the seller is simply irrational — selling always beats not selling"
    - "If the bidder's virtual valuation is negative (due to the information rent markup), allocating to them would cost the seller more in expected information rents than it gains"
    - "The seller is legally required to set a minimum price equal to production cost"
  answer: 2
  explanation: "Virtual valuation = true value − (information rent markup based on the type distribution). For bidders with low valuations and a distribution that places significant probability mass below their value, the virtual valuation can be negative. Selling to such bidders is inefficient for the seller: the information rent they must be given (to prevent high-type bidders from mimicking low types) exceeds their contribution. A reserve price that excludes them raises expected revenue despite sometimes resulting in no sale. This is the central tension: the allocation that maximizes revenue differs from the allocation that maximizes social surplus."

- question: "In a second-price sealed-bid auction, truthful bidding (submitting your true valuation) is a dominant strategy — optimal regardless of what other bidders do."
  type: true-false
  answer: true
  explanation: "In a second-price auction, you pay the second-highest bid, not your own. If you bid your true value v: if you win (your bid is highest), you pay the second-highest bid, which is less than v, earning positive surplus. If you lose, you pay nothing. Bidding above v risks winning when the second price exceeds v (negative surplus). Bidding below v risks losing to a bid between your reduced bid and v, when you would have profited by winning. Neither deviation improves your expected outcome — truthful bidding weakly dominates all alternatives, and this holds regardless of what others bid."

- question: "The revenue equivalence theorem implies that sellers should be indifferent among all auction formats regardless of bidders' risk preferences and the correlation structure of their valuations."
  type: true-false
  answer: false
  explanation: "Revenue equivalence holds only under specific assumptions: symmetric bidders, independent private values, risk-neutral bidders, and common prior distribution. If bidders are risk-averse, first-price auctions tend to generate higher revenue (risk-averse bidders overbid to reduce the uncertainty of losing). If valuations are correlated (a common scenario when bidders have overlapping information), ascending auctions tend to generate more revenue than sealed-bid formats. Revenue equivalence tells you the conditions under which format doesn't matter; it also tells you exactly which violations will make it matter."

- question: "Why does maximizing revenue in an auction sometimes require allocating the good inefficiently — and what insight does this reveal about mechanism design?"
  type: short-answer
  answer: "Revenue maximization requires allocating to the bidder with the highest virtual valuation, not the highest true valuation. Virtual valuation subtracts an information rent markup reflecting the seller's uncertainty about the bidder's type. For low-valuation bidders, this markup can exceed their true value, making their virtual valuation negative — so the seller earns more by withholding the good than by selling to them. The efficient allocation (give it to whoever values it most) ignores this rent; the revenue-maximizing allocation accounts for it. The gap between the two reveals that extracting information from privately-informed buyers is not free — it requires distorting the allocation."
  explanation: "This is a microcosm of the broader mechanism design lesson: when agents have private information, any mechanism that elicits truthful reporting must grant them information rents (surplus from revealing their type). Mechanisms that extract more rent from high-value types must compensate low-value types — or exclude them. The revenue-optimal mechanism optimally trades off these information costs against the gains from trade, and the result is a reserve price that excludes some potential buyers even when trade would be mutually beneficial."
```

## Explainer

An auction is a game where a seller allocates a good to one of several buyers, each of whom privately knows how much the good is worth to them. From your study of game theory, you know how to analyze strategic interaction; from mechanism design, you know the seller can shape the rules to influence outcomes. Auction theory applies both toolkits to a specific, economically important setting: how should goods be sold when the seller does not know buyers' valuations?

The four classic auction formats illustrate how different rules create different strategic incentives. In an **English (ascending) auction**, the price rises until only one bidder remains — it is weakly dominant to stay in until the price hits your valuation. In a **Dutch (descending) auction**, the price falls from a high starting point and the first bidder to claim the item wins at that price — you must decide when to jump in, trading off the chance of a lower price against the risk of losing. In a **second-price sealed-bid auction**, each bidder submits one bid; the highest bidder wins but pays the second-highest bid — truthful bidding is a dominant strategy, since your bid only affects whether you win, not what you pay. In a **first-price sealed-bid auction**, the highest bidder wins and pays their own bid — so bidders shade their bids below their true values to earn positive surplus, and finding the equilibrium bidding strategy requires solving a differential equation using expected value calculations from your probability background.

The most striking result in auction theory is the **revenue equivalence theorem**: under symmetric independent private values, risk-neutral bidders, and a common prior distribution, all four standard auction formats generate the same expected revenue for the seller. This is surprising because the strategic reasoning feels so different across formats. The key insight is that any auction satisfying these conditions must give each bidder type the same expected surplus — and since the total surplus is fixed by the allocation, the seller's revenue must also be the same. Revenue equivalence tells you that if auctions differ in revenue, it must be because one of the assumptions is violated: bidders are risk-averse, valuations are correlated, bidders are asymmetric, or the reserve price differs.

When the seller wants to maximize revenue, the **Myerson optimal auction** provides the answer. The seller should allocate the good to the bidder with the highest **virtual valuation** — a transformation of the true valuation that accounts for the information rent bidders earn from having private information. Virtual valuation equals the true value minus a markup that depends on the distribution of types. This often means setting a reserve price that excludes low-value bidders entirely, even though selling to them would be efficient. The gap between efficiency and revenue maximization is a central theme: auctions that maximize social surplus (allocate to whoever values the good most) generally differ from auctions that maximize the seller's revenue, because extracting surplus from informed bidders requires distorting the allocation.
