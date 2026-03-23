---
id: mechanism-design-optimal-mechanisms
title: Optimal Mechanism Design and Revenue Extraction
domain: economics
course: advanced-microeconomics
prerequisites:
- id: mechanism-design-and-vickrey-clarke-groves
  type: hard
- id: bayesian-games-and-incomplete-information
  type: soft
- id: lagrange-multipliers
  type: hard
- id: constrained-optimization
  type: hard
- id: constrained-optimization-lagrange
  type: soft
tags:
- mechanism-design
- auction-theory
stage: expert
status: draft
---

# Optimal Mechanism Design and Revenue Extraction

## Core Idea
The revelation principle shows that the mechanism designer can focus on direct revelation mechanisms where truth-telling is incentive-compatible. Myerson's auction theorem characterizes optimal auction design: price each bidder's virtual value (value minus information rents). This may involve excluding low-value bidders or reducing quantities sold to increase revenue. Optimal mechanisms balance efficiency and revenue extraction.

## Questions

```yaml
- question: "In an optimal auction, bidder A has an actual value of 80 and bidder B has an actual value of 70, but their virtual values are 50 and 65, respectively. Who wins the good in Myerson's optimal auction?"
  type: multiple-choice
  options:
    - "Bidder A, because their actual value is highest"
    - "Bidder B, because their virtual value is highest"
    - "Neither bidder, because the virtual values are too close to determine a winner"
    - "The good is not sold because neither virtual value is negative"
  answer: 1
  explanation: "Myerson's optimal auction allocates to the bidder with the highest *virtual* value, not actual value. Bidder B has the higher virtual value (65 > 50), so B wins despite having the lower actual value. This is the central insight: the information rents that must be paid to high-actual-value bidders make it optimal to reallocate toward those with higher virtual values. Option A represents the naive efficiency approach (maximize total value), which a revenue-maximizing seller should not use."

- question: "Why does the optimal auction sometimes withhold the good from the highest-value bidder, even when that bidder values it more than the seller's cost?"
  type: multiple-choice
  options:
    - "Because the seller cannot identify who has the highest value under incomplete information"
    - "Because withholding raises the price for future auction rounds"
    - "Because the information rents paid to that bidder would exceed the revenue gain, making exclusion more profitable"
    - "Because the revelation principle requires some probability of non-sale"
  answer: 2
  explanation: "Incentive compatibility forces sellers to leave information rents to high-value bidders — they must be paid enough not to misreport. Excluding low-value bidders reduces the information rents paid to higher-value ones, since there are fewer types to 'envy.' When a bidder's virtual value is negative (actual value is low but information rents are high), selling to them destroys more in informational costs than it gains in revenue. The reserve price is set where virtual value equals zero, not where actual value equals cost — a crucial distinction."

- question: "The revelation principle states that any equilibrium outcome of a complex multi-round auction can be replicated by a simpler direct mechanism where participants truthfully report their private values."
  type: true-false
  answer: true
  explanation: "The revelation principle is the foundational simplification result in mechanism design. No matter how complicated the mechanism (extensive-form bargaining, signaling games, dynamic auctions), if agents play an equilibrium, there exists an equivalent direct revelation mechanism where truth-telling is incentive-compatible and produces the same outcomes. This dramatically narrows the design problem: instead of searching over all possible mechanisms, designers can restrict to direct truth-telling mechanisms without loss of generality."

- question: "The optimal auction always allocates the good to the bidder with the highest actual value, since this maximizes total surplus."
  type: true-false
  answer: false
  explanation: "This is false — it is the naive efficiency approach, not revenue maximization. Myerson's optimal auction allocates to the bidder with the highest *virtual* value, which deducts information rents from actual values. High-actual-value bidders command high information rents (otherwise they could mimic lower types profitably), so their virtual values may be lower than those of competitors. Furthermore, if the highest virtual value is negative, the good is not sold at all — which would never happen under pure efficiency maximization. Revenue maximization and efficiency maximization are distinct objectives with different solutions."

- question: "What are information rents in mechanism design, and why do they force a revenue-maximizing seller to use virtual values rather than actual values?"
  type: short-answer
  answer: "Information rents are the surplus that high-value bidders retain because incentive compatibility requires they receive enough utility to prefer truthful reporting over mimicking a lower type. Virtual value = v − (1−F(v))/f(v) subtracts this informational cost from each bidder's actual value. Allocating to the highest virtual value maximizes expected revenue net of information rents — the actual surplus the seller keeps after compensating bidders for truthful disclosure."
  explanation: "The rent extraction problem is fundamental: you cannot extract the full surplus because doing so would make high-value bidders prefer to report a lower type. The optimal mechanism balances how much surplus it extracts against how much it must leave as a rent to ensure truthful reporting. Virtual values encode exactly this tradeoff in a single number per bidder."
```

## Explainer

From the VCG mechanism, you know how to design mechanisms that achieve efficient allocations while maintaining truthful reporting. But efficiency is not always the designer's goal — a seller running an auction typically wants to maximize **revenue**, not total surplus. Optimal mechanism design asks: given incentive compatibility and participation constraints, what mechanism extracts the most revenue (or achieves whatever objective the designer has)? The answer, provided by Roger Myerson's foundational 1981 result, transforms mechanism design from art to science.

The starting point is the **revelation principle**, which dramatically simplifies the design problem. It says: for any mechanism (no matter how complex — multi-round auctions, bargaining protocols, signaling games) where agents play an equilibrium, there exists an equivalent **direct revelation mechanism** that achieves the same outcome by simply asking agents to report their types truthfully. This means the designer never needs to consider exotic mechanisms — they can restrict attention to direct mechanisms where truth-telling is incentive-compatible, without any loss of generality. The design problem reduces to choosing an allocation rule and a payment rule subject to IC and individual rationality (IR) constraints, then optimizing over this tractable set.

Myerson's key insight is the concept of **virtual value**. In a standard auction, you might think the seller should allocate the good to the highest-value bidder. But incentive compatibility forces the seller to leave information rents to high-value bidders — a bidder with value 80 must be paid enough that they would not pretend to have value 60. The virtual value adjusts each bidder's actual value downward by the cost of these information rents: virtual value = v - (1 - F(v))/f(v), where F is the distribution of values and f is its density. The **optimal auction** allocates to the bidder with the highest virtual value (not actual value), provided that virtual value exceeds zero — otherwise the good is not sold at all. This is why reserve prices exist: excluding low-value bidders reduces the information rents paid to higher-value ones, increasing expected revenue.

When the value distribution satisfies a **regularity condition** (virtual value is increasing in actual value), the optimal auction takes a remarkably simple form. For symmetric bidders, it is equivalent to a standard first-price or second-price auction with an optimally chosen reserve price — Myerson's revenue equivalence result shows these formats generate identical expected revenue. The reserve price is set where virtual value equals zero, not where actual value equals the seller's cost. This means the seller sometimes inefficiently withholds the good (the seller values it less than the highest bidder, but still does not sell) because the revenue gain from reduced information rents outweighs the efficiency loss. With asymmetric bidders or irregular distributions, optimal mechanisms become more complex — potentially involving randomized allocation or bidder-specific reserve prices — and the tension between efficiency and revenue extraction becomes the central design challenge. This framework extends far beyond auctions to procurement, regulation, and any setting where a principal designs rules for privately-informed agents using constrained optimization.
