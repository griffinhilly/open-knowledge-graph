---
id: contract-curve
title: The Contract Curve
domain: economics
course: advanced-microeconomics
prerequisites:
- id: edgeworth-box
  type: hard
- id: pareto-efficiency-microeconomics
  type: hard
tags:
- general-equilibrium
- efficiency
- trade
stage: formal-systems
status: draft
---

# The Contract Curve

## Core Idea
The contract curve is the locus of Pareto efficient allocations in an Edgeworth box—points where the indifference curves of the two consumers are tangent. Trade moves the economy along the contract curve. The set of allocations in the contract curve that both agents prefer to the initial endowment is the core, the set of outcomes that cannot be blocked by coalitions.

## Questions

```yaml
- question: "Two traders start at an allocation in the interior of an Edgeworth box that is NOT on the contract curve. What can we definitively conclude?"
  type: multiple-choice
  options:
    - "Both traders are worse off than they would be at their initial endowment"
    - "There exist other allocations that make at least one trader better off without making the other worse off"
    - "The two traders' marginal rates of substitution are equal at this allocation"
    - "The allocation is unfair, and redistribution is required to achieve justice"
  answer: 1
  explanation: "A point off the contract curve is Pareto inefficient by definition: the indifference curves cross rather than being tangent, which means there is a 'lens' of allocations that both traders prefer. Moving into that lens makes at least one trader better off without harming the other — i.e., a Pareto improvement is available. Note that option C gets it exactly backwards: equal MRS is the condition FOR being on the contract curve, not off it. And option D is wrong because the contract curve concerns efficiency, not fairness."

- question: "At every point on the contract curve, what condition holds for the two consumers?"
  type: multiple-choice
  options:
    - "Their incomes are equal, ensuring a fair distribution of resources"
    - "Their marginal utilities are equal for every good consumed"
    - "Their marginal rates of substitution are equal — both value the tradeoff between goods identically at the margin"
    - "Their indifference curves are parallel, indicating compatible preferences"
  answer: 2
  explanation: "The geometric condition for being on the contract curve is that the two consumers' indifference curves are tangent — touching at exactly one point. Tangency means their slopes are equal. The slope of an indifference curve is the marginal rate of substitution (MRS), so equal MRS is the condition. This matters because if MRS values differ, there is room for a beneficial trade: the consumer who values good X more can trade with the one who values it less, and both gain. Only when MRS values equalize have all gains from trade been exhausted."

- question: "Every point on the contract curve is equally desirable from a social welfare perspective, since all points are Pareto efficient."
  type: true-false
  answer: false
  explanation: "Pareto efficiency is a condition about the impossibility of further Pareto improvements — it says nothing about distribution or fairness. The contract curve extends from one corner of the Edgeworth box (where one agent has almost everything) to the opposite corner (where the other agent has almost everything). These extreme points are just as 'efficient' as the middle, but the distributions are radically different. The choice among contract-curve points is a distributional question that efficiency alone cannot answer — it requires a social welfare function, an ethical criterion, or a bargaining outcome."

- question: "A competitive equilibrium allocation in an Edgeworth box economy must lie on the contract curve."
  type: true-false
  answer: true
  explanation: "This is the First Welfare Theorem applied to the exchange economy: competitive equilibria are Pareto efficient. In the Edgeworth box, Pareto efficiency is equivalent to being on the contract curve (MRS equality). A competitive equilibrium requires that both consumers optimize at the same prices, which implies they reach the same MRS (since each sets MRS equal to the price ratio). Hence their MRS values are equal at equilibrium, which is the condition for being on the contract curve. The equilibrium is also in the core — both agents prefer it to their endowment, or they would not voluntarily trade."

- question: "Why does equal MRS between two consumers imply Pareto efficiency in an exchange economy? Explain the economic logic."
  type: short-answer
  answer: "If two consumers have different MRS values, they disagree about how much of good Y they are willing to give up for one unit of good X. The consumer with the higher MRS values X more highly in terms of Y. This creates a mutually beneficial trade: the high-MRS consumer can offer the low-MRS consumer some Y in exchange for X, and both gain utility. Trades like this are possible whenever MRS values differ. When MRS values are equal, both consumers value the marginal tradeoff identically — no further exchange can make one better off without making the other worse off. Pareto efficiency is exactly this condition: no further improvements possible."
  explanation: "The MRS equality condition is not just a geometric curiosity — it directly encodes the exhaustion of gains from trade. As long as consumers disagree about marginal valuations (unequal MRS), a mutually beneficial transaction exists. Trade continues until the disagreement is eliminated. This is also why the competitive equilibrium is efficient: market prices force all consumers to the same MRS, automatically coordinating what would otherwise require direct negotiation."
```

## Explainer

From the Edgeworth box, you know how to represent all possible allocations of two goods between two people in a single diagram, and from Pareto efficiency you know that an allocation is efficient when you cannot make one person better off without making the other worse off. The **contract curve** connects these two ideas: it is the line through the Edgeworth box that traces out every Pareto efficient allocation.

Geometrically, a point is on the contract curve when the two consumers' indifference curves are **tangent** to each other at that point. Tangency means their **marginal rates of substitution (MRS) are equal** — both consumers value the tradeoff between the two goods identically at the margin. Why does equal MRS imply efficiency? If the MRS values differ, there is room for a mutually beneficial trade. Suppose Alice values an extra unit of good X at 3 units of good Y, while Bob values it at only 1 unit of Y. Then Alice could give Bob 2 units of Y for 1 unit of X, and both would be happier. Only when their marginal valuations coincide have all gains from trade been exhausted — and that is exactly where the indifference curves are tangent.

The contract curve typically runs from one corner of the Edgeworth box to the opposite corner, passing through the interior. Its exact shape depends on the consumers' preferences. With identical homothetic preferences, the contract curve is the diagonal of the box. With very different preferences, it may bow strongly toward one side. Every point on the contract curve is efficient, but they differ dramatically in how the gains are distributed — at one end, Alice has nearly everything; at the other, Bob does. Efficiency alone says nothing about fairness.

Not every point on the contract curve is a plausible outcome of voluntary trade. Given an initial endowment (the starting allocation before trade), both consumers will only agree to move to allocations that make each of them at least as well off as they were initially. The subset of the contract curve where both consumers are on or above their initial indifference curves is called the **core** of the economy. The core narrows the efficient allocations to those that are individually rational — neither party would agree to a trade that leaves them worse off than their endowment. Competitive equilibrium, as you would expect from the First Welfare Theorem, lies within this core.

The contract curve is more than a geometric curiosity — it crystallizes the fundamental distinction between **efficiency** and **distribution** that runs through all of welfare economics. Choosing a point on the contract curve determines how the surplus is split between the two agents. Markets select one particular point (the competitive equilibrium); negotiation, bargaining power, or social choice mechanisms select others. The contract curve shows the full menu of efficient outcomes and makes visible the tradeoffs that any allocation mechanism must navigate.
