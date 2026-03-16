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
stage: advanced
status: draft
---

# Optimal Mechanism Design and Revenue Extraction

## Core Idea
The revelation principle shows that the mechanism designer can focus on direct revelation mechanisms where truth-telling is incentive-compatible. Myerson's auction theorem characterizes optimal auction design: price each bidder's virtual value (value minus information rents). This may involve excluding low-value bidders or reducing quantities sold to increase revenue. Optimal mechanisms balance efficiency and revenue extraction.

## Explainer

From the VCG mechanism, you know how to design mechanisms that achieve efficient allocations while maintaining truthful reporting. But efficiency is not always the designer's goal — a seller running an auction typically wants to maximize **revenue**, not total surplus. Optimal mechanism design asks: given incentive compatibility and participation constraints, what mechanism extracts the most revenue (or achieves whatever objective the designer has)? The answer, provided by Roger Myerson's foundational 1981 result, transforms mechanism design from art to science.

The starting point is the **revelation principle**, which dramatically simplifies the design problem. It says: for any mechanism (no matter how complex — multi-round auctions, bargaining protocols, signaling games) where agents play an equilibrium, there exists an equivalent **direct revelation mechanism** that achieves the same outcome by simply asking agents to report their types truthfully. This means the designer never needs to consider exotic mechanisms — they can restrict attention to direct mechanisms where truth-telling is incentive-compatible, without any loss of generality. The design problem reduces to choosing an allocation rule and a payment rule subject to IC and individual rationality (IR) constraints, then optimizing over this tractable set.

Myerson's key insight is the concept of **virtual value**. In a standard auction, you might think the seller should allocate the good to the highest-value bidder. But incentive compatibility forces the seller to leave information rents to high-value bidders — a bidder with value 80 must be paid enough that they would not pretend to have value 60. The virtual value adjusts each bidder's actual value downward by the cost of these information rents: virtual value = v - (1 - F(v))/f(v), where F is the distribution of values and f is its density. The **optimal auction** allocates to the bidder with the highest virtual value (not actual value), provided that virtual value exceeds zero — otherwise the good is not sold at all. This is why reserve prices exist: excluding low-value bidders reduces the information rents paid to higher-value ones, increasing expected revenue.

When the value distribution satisfies a **regularity condition** (virtual value is increasing in actual value), the optimal auction takes a remarkably simple form. For symmetric bidders, it is equivalent to a standard first-price or second-price auction with an optimally chosen reserve price — Myerson's revenue equivalence result shows these formats generate identical expected revenue. The reserve price is set where virtual value equals zero, not where actual value equals the seller's cost. This means the seller sometimes inefficiently withholds the good (the seller values it less than the highest bidder, but still does not sell) because the revenue gain from reduced information rents outweighs the efficiency loss. With asymmetric bidders or irregular distributions, optimal mechanisms become more complex — potentially involving randomized allocation or bidder-specific reserve prices — and the tension between efficiency and revenue extraction becomes the central design challenge. This framework extends far beyond auctions to procurement, regulation, and any setting where a principal designs rules for privately-informed agents using constrained optimization.
