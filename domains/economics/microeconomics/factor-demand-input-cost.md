---
id: factor-demand-input-cost
title: Factor Demand and Input Cost Minimization
domain: economics
course: microeconomics
prerequisites:
- id: isoquant-factor-substitution
  type: hard
builds-toward:
- short-run-cost-fixed-variable
- long-run-average-cost
tags:
- factor-demand
- input-costs
- cost-minimization
- isocost
stage: formal-systems
status: draft
---

# Factor Demand and Input Cost Minimization

## Core Idea
Firms minimize costs for a given output level by choosing an input combination where the isoquant is tangent to the isocost line (MRTS = w/r, where w and r are input prices). The resulting input quantities form factor demand curves that show how input usage responds to input price changes. Cost minimization underlies the firm's long-run production decisions and determines its cost structure.

## Explainer

From your work with isoquants, you already know that a given output level can be produced by many different combinations of labor and capital. The question now is: which combination is cheapest? To answer this, you need a second geometric object — the **isocost line**. An isocost line connects all input combinations (L, K) that cost the same total amount: wL + rK = C, where w is the wage rate and r is the rental rate of capital. Just like a consumer's budget constraint, an isocost line has slope -w/r: for every extra unit of labor you hire, you must release w/r units of capital to stay at the same cost.

The cost-minimizing input combination is where the isoquant is **tangent** to the lowest possible isocost line. At that tangency, the slopes of the two curves are equal: the **marginal rate of technical substitution** (MRTS = MPL/MPK) equals the input price ratio (w/r). You can read this condition as a no-arbitrage rule: if MPL/MPK > w/r, you can produce the same output more cheaply by substituting labor for capital (labor buys more output per dollar than capital does). You keep substituting until the productivity ratios equal the cost ratios — at which point no further profitable rearrangement is possible.

Now trace what happens when an input price changes. Suppose the wage w rises. The isocost line rotates — it becomes steeper (slope -w/r is now more negative). The tangency point shifts along the isoquant toward more capital and less labor: the firm substitutes away from the now-more-expensive input. This movement traces out the **factor demand curve** for labor: as w rises, quantity of labor demanded falls. The factor demand curve for an input is therefore a derived demand — it reflects not a preference for labor per se, but the demand for the output that labor helps produce.

An important subtlety: cost minimization as studied here is a constrained optimization at a fixed output level. It tells you the cheapest way to produce Q units, not how much to produce. The firm's actual output decision (choosing Q to maximize profit, where MR = MC) is a separate step. But the cost-minimizing input choices at every output level generate the firm's cost function — the foundation for all long-run cost analysis. As output scales up, the cost-minimizing input bundle traces an **expansion path** through input space, which determines how average costs behave as the firm grows.
