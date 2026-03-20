---
id: edgeworth-box
title: The Edgeworth Box
domain: economics
course: advanced-microeconomics
prerequisites:
- id: indifference-curves
  type: hard
- id: consumer-optimum
  type: hard
builds-toward:
- contract-curve
tags:
- general-equilibrium
- exchange
- visualization
stage: formal-systems
status: draft
---

# The Edgeworth Box

## Core Idea
The Edgeworth box is a graphical tool for analyzing exchange between two consumers and two goods. The box dimensions represent total endowments; points inside show allocations. Each consumer's origin is opposite; indifference curves show preferences. The box visualizes both the feasible set and outcomes of trade.

## How It's Best Learned
Draw boxes for specific utility functions. Mark initial endowments and trace contract curves. Overlay competitive equilibrium prices to show how prices support equilibrium allocation.

## Common Misconceptions
Thinking Edgeworth box only works for two consumers (extends to many). Confusing directions of axes for the two consumers. Not seeing how price line tangency characterizes equilibrium.

## Explainer

You already understand indifference curves — those level sets of a consumer's utility function showing all bundles that yield equal satisfaction — and consumer optimum, where a budget line is tangent to the highest reachable indifference curve. The **Edgeworth box** takes these familiar single-consumer tools and fuses them into a single diagram that captures an entire exchange economy with two consumers and two goods.

Here is the construction. Suppose the economy has a total of 10 units of food and 6 units of clothing. Draw a rectangle that is 10 units wide and 6 units tall. Consumer A reads the diagram normally: A's origin is the bottom-left corner, food increases rightward, clothing increases upward. Consumer B reads the diagram upside-down and backwards: B's origin is the top-right corner, and B's quantities increase as you move left and down. Every single point inside the box simultaneously specifies an allocation for both consumers, and these allocations are **feasible** — the quantities add up to the economy's total endowments. This double-reading trick is the key insight: one diagram, two complete consumer problems.

Now overlay both consumers' indifference curves. At any point in the box, A's indifference curve through that point is the usual convex-toward-A's-origin shape. B's indifference curve through the same point is convex toward B's origin (the top-right corner), so it appears concave from A's perspective. Where two indifference curves cross, there is a lens-shaped region between them representing allocations that make both consumers better off — these are **mutually beneficial trades**. The consumers would naturally trade into this lens. They stop trading only when no such lens exists, which occurs exactly where an A-indifference curve is tangent to a B-indifference curve. At tangency, the **marginal rates of substitution** are equal — both consumers value the tradeoff between the two goods identically, so no further gains from trade exist. The locus of all such tangency points is the **contract curve**, and every point on it is Pareto efficient.

To see how competitive equilibrium fits in, mark the **initial endowment point** — the allocation before any trade. Draw a straight line through this point with a slope equal to the negative price ratio (−p_food/p_clothing). This line acts as both consumers' budget constraint simultaneously, since what A sells is exactly what B buys. The competitive equilibrium occurs where this price line is tangent to both consumers' indifference curves at the same point — that is, where both consumers independently optimize and the market clears. The equilibrium allocation lies on the contract curve, confirming that competitive outcomes are Pareto efficient. The Edgeworth box thus gives you a single visual framework that unifies consumer theory, exchange, efficiency, and equilibrium — making it the foundational diagram of general equilibrium analysis.
