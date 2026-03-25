---
id: general-equilibrium-existence
title: 'Existence of General Equilibrium: Fixed-Point Theorems'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: walrasian-equilibrium
  type: hard
- id: fixed-point-iteration
  type: soft
- id: compact-sets
  type: hard
- id: topological-spaces-definition
  type: hard
- id: compact-sets-definition
  type: soft
- id: contract-curve
  type: soft
- id: core-of-an-economy
  type: soft
tags:
- general-equilibrium
- mathematical-economics
stage: expert
status: validated
---
# Existence of General Equilibrium: Fixed-Point Theorems

## Core Idea
General equilibrium existence is non-trivial and requires proof. Under convexity of preferences, continuous utility functions, and no free disposal, Brouwer and Kakutani fixed-point theorems establish that at least one Walrasian equilibrium exists. The proof models excess demand as a mapping from the price simplex to itself and applies fixed-point theory to find equilibrium prices.

## Questions

```yaml
- question: "The existence proof for general equilibrium applies Brouwer's fixed-point theorem by constructing a mapping from the price simplex to itself. At a fixed point of this mapping, what economic condition holds?"
  type: multiple-choice
  options:
    - "Every consumer is spending exactly their endowment income — budget constraints are binding"
    - "Prices are not adjusting under the price-update rule, which means excess demands are zero and all markets clear simultaneously"
    - "The excess demand vector sums to zero, confirming Walras' law"
    - "Utility is maximized for all consumers simultaneously at the given price vector"
  answer: 1
  explanation: "The proof constructs a price-adjustment mapping T(p) that raises prices of goods in excess demand and lowers prices of goods in excess supply. A fixed point p* satisfies T(p*) = p* — prices do not change under the adjustment rule. Prices stop adjusting only when there is no pressure to adjust, which means no good has excess demand or supply: all markets clear. This is precisely a Walrasian equilibrium. Note: Walras' law (option C) is always true by definition at any price vector, not just at equilibrium — it is a necessary condition for the proof to work, not the conclusion."

- question: "A software company has zero marginal cost after the initial development: the first copy costs $10 million to produce, and each additional copy costs essentially nothing. Why does the standard Arrow-Debreu existence proof fail to guarantee a competitive equilibrium for this market?"
  type: multiple-choice
  options:
    - "The price simplex changes dimensions when marginal cost is zero, violating the compactness assumption needed for Brouwer's theorem"
    - "Walras' law breaks down when marginal cost is zero, so the value of excess demands may not sum to zero"
    - "Non-convex production possibilities create supply correspondences that are not upper hemicontinuous, violating the continuity requirements for fixed-point theorems"
    - "Brouwer's theorem only applies to economies with a finite number of goods, and software products are infinitely divisible"
  answer: 2
  explanation: "The existence proof requires that excess demand varies continuously (or upper hemicontinuously) with prices, which depends on convex preferences and convex production sets. Strong increasing returns (like near-zero marginal cost) produce non-convex production sets: a firm facing zero marginal cost may want to produce zero or essentially unlimited quantities depending on whether price exceeds the average fixed cost, creating a discontinuous supply function. Fixed-point theorems require continuity to guarantee that the mapping from prices to excess demands doesn't 'jump' — without continuity, there may be no price where excess demand is zero."

- question: "Walras' law implies that if all but one market is in equilibrium at a given price vector, the final market must also be in equilibrium."
  type: true-false
  answer: true
  explanation: "Walras' law states that at any price vector p, the total value of excess demands sums to zero: p · z(p) = 0. If all n-1 markets clear (excess demand = 0 in each), then the remaining term in the dot product must also be zero. Since the price of the last good is positive (we're on the interior of the price simplex), its excess demand must be zero. This is why the proof only needs to show n-1 markets clear; the last one follows automatically. It is the budget constraint aggregated across all consumers that produces this result."

- question: "The Arrow-Debreu existence theorem guarantees that a competitive equilibrium, when it exists, is unique and Pareto efficient."
  type: true-false
  answer: false
  explanation: "The existence theorem proves only that at least one equilibrium exists — it says nothing about uniqueness or efficiency. Uniqueness requires additional assumptions (like gross substitutability of goods) that are not part of the standard existence conditions. Multiple equilibria are common in general equilibrium models. Pareto efficiency of equilibria is guaranteed by the First Welfare Theorem, which is a separate result requiring its own assumptions (complete markets, no externalities, price-taking behavior). Existence, uniqueness, and efficiency are three distinct properties requiring three distinct proofs."

- question: "What role does the convexity of consumer preferences play in the existence proof for general equilibrium, and what goes wrong mathematically if preferences are non-convex?"
  type: short-answer
  answer: "Convexity of preferences guarantees that the consumer's demand function (or correspondence) is continuous — small changes in prices produce small changes in demanded quantities. Without convexity, demand can jump discontinuously: a consumer might switch abruptly from consuming only good A to consuming only good B as relative prices change slightly, because with non-convex preferences, mixtures of goods are less preferred than extremes. This discontinuity breaks the continuity condition required by fixed-point theorems. If excess demand z(p) is discontinuous, the price-adjustment mapping T(p) may also be discontinuous, and Brouwer's theorem (which requires continuity) no longer guarantees a fixed point exists. Economically, non-convex preferences correspond to goods that are 'lumpy' or exhibit satiation — and markets for such goods often do fail to have competitive equilibria."
  explanation: "The requirement for convexity explains why general equilibrium theory works well for divisible goods traded in smooth markets but struggles with indivisibilities, increasing returns, and network goods. The mathematical failure is not just a technical inconvenience — it reflects a genuine economic phenomenon: markets for goods with strong non-convexities (software, pharmaceuticals, infrastructure) tend toward monopoly or oligopoly rather than competitive equilibrium, and market prices may not accurately reflect social value. The existence proof thus provides both a positive result (markets can work) and a diagnostic tool (here is precisely when and why they may not)."
```

## Explainer

From Walrasian equilibrium, you know the concept: a price vector at which every consumer maximizes utility subject to their budget constraint and all markets clear simultaneously. But knowing what equilibrium means is very different from knowing whether one actually exists. The economy is a system of potentially millions of interacting agents with diverse preferences and endowments. Why should there be any price vector that simultaneously satisfies everyone's optimization and clears every market? The existence proof answers this question and, in doing so, reveals what assumptions about the economy are truly essential for markets to function.

The proof strategy is elegant in structure. First, normalize prices so they lie on the **price simplex** — the set of all non-negative price vectors that sum to one. (Since only relative prices matter in general equilibrium, this normalization loses nothing.) At each price vector, every consumer solves their optimization problem, generating demands. Subtract total endowments from total demands to get the **excess demand function** *z(p)*, which maps each price vector to a vector of excess demands across all goods. Equilibrium means finding a price vector where *z(p) = 0* — supply equals demand in every market. Walras' law (which you know from general equilibrium theory) guarantees that the value of excess demand is always zero, so if all but one market clears, the last one must clear too. The problem reduces to: does the excess demand function have a zero?

This is where **fixed-point theorems** from topology enter. Rather than searching for a zero of *z(p)* directly, the proof constructs a continuous mapping from the price simplex to itself — essentially a rule that takes any price vector and adjusts it in the direction that excess demand suggests (raising prices of goods in excess demand, lowering prices of goods in excess supply). The price simplex is a **compact, convex set** (this is where your topology prerequisites matter). Brouwer's fixed-point theorem states that any continuous function from a compact convex set to itself must have at least one fixed point — a point that maps to itself. At a fixed point of this price-adjustment mapping, prices are not adjusting, which means excess demand is zero: equilibrium. When demand correspondences are set-valued (as with indifference leading to non-unique optimal bundles), **Kakutani's fixed-point theorem** extends the result to upper hemicontinuous correspondences.

The assumptions doing the heavy lifting are **convexity of preferences** (which ensures demand varies continuously with prices and rules out jumps), **continuity of utility** (which keeps demand well-behaved), and **positive endowments** (every consumer owns some of every good, preventing budget constraints from collapsing). If preferences are non-convex — for instance, if consumers have indivisible goods or increasing returns — the excess demand mapping may not be continuous and fixed-point theorems fail to apply. This is not merely a mathematical curiosity: it explains why markets for goods with strong increasing returns (like software or network platforms) may not reach competitive equilibrium naturally. The existence theorem thus tells us both when we can trust the invisible hand and when we should expect market outcomes to be problematic.
