---
id: edgeworth-box-exchange
title: Edgeworth Box Analysis
domain: economics
course: advanced-microeconomics
prerequisites:
- id: walrasian-equilibrium
  type: soft
- id: indifference-curves
  type: hard
builds-toward:
- core-of-an-economy
tags:
- general-equilibrium
- exchange
- visualization
stage: advanced
status: draft
---

# Edgeworth Box Analysis

## Core Idea
The Edgeworth box is a geometric tool for analyzing two-person, two-good exchange economies. The contract curve traces all mutually beneficial allocations where indifference curves are tangent; competitive equilibrium lies on this curve. The box illustrates how trade expands the feasible set from autarky and demonstrates Pareto efficiency of equilibrium.

## Explainer

You already know how to read a single consumer's indifference map — curves showing bundles of two goods that yield equal satisfaction, with higher curves representing greater utility. The **Edgeworth box** takes two consumers' indifference maps and overlays them in a single diagram, creating a powerful visual tool for analyzing exchange.

The construction is elegant. Imagine Consumer A's origin in the bottom-left corner, with good X on the horizontal axis and good Y on the vertical axis, just like a standard indifference curve diagram. Now take Consumer B's diagram, rotate it 180 degrees, and place B's origin in the top-right corner. The width of the box equals the total endowment of good X in the economy; the height equals the total endowment of good Y. Every point inside the box represents a complete allocation — how much of each good goes to each consumer — because what A does not have, B has. The initial endowment (what each consumer starts with before any trade) is a single point in the box.

From the endowment point, draw both consumers' indifference curves passing through it. These curves divide the box into regions. The **lens-shaped area** between the two indifference curves contains all allocations that make both consumers better off than the endowment — the set of mutually beneficial trades. Any move from the endowment into this lens is a Pareto improvement. Rational, voluntary trade will push the economy somewhere into this region. But where exactly? The consumers will keep trading as long as further mutually beneficial trades exist — that is, as long as their indifference curves at the current allocation are not tangent.

Trade stops when the indifference curves become **tangent**, meaning the consumers' marginal rates of substitution are equal. At tangency, there is no further reallocation that can benefit one consumer without harming the other — the allocation is Pareto efficient. The locus of all such tangency points across the entire box forms the **contract curve**, which traces every efficient allocation from A-gets-everything to B-gets-everything. The competitive equilibrium — found by introducing prices and letting both consumers optimize on their budget constraints — lands on the contract curve, confirming visually that competitive markets achieve efficiency.

The Edgeworth box makes several abstract ideas concrete and visible. You can *see* that the initial endowment matters: it determines which segment of the contract curve is reachable through voluntary trade. You can *see* that efficiency and equity are distinct: every point on the contract curve is efficient, but they range from extremely favorable to A to extremely favorable to B. And you can *see* why prices work: the budget line through the endowment, at equilibrium prices, is tangent to both consumers' indifference curves simultaneously, coordinating their demands so that markets clear. This geometric intuition carries forward into general equilibrium theory with many consumers and goods, where the algebra replaces the picture but the logic is the same.
