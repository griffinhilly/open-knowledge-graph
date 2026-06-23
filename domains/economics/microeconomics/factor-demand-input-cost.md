---
id: factor-demand-input-cost
title: Factor Demand and Input Cost Minimization
domain: economics
course: microeconomics
prerequisites:
- id: isoquant-factor-substitution
  type: hard
- id: marginal-product-diminishing-returns
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
status: validated
---

# Factor Demand and Input Cost Minimization

## Core Idea
Firms minimize costs for a given output level by choosing an input combination where the isoquant is tangent to the isocost line (MRTS = w/r, where w and r are input prices). The resulting input quantities form factor demand curves that show how input usage responds to input price changes. Cost minimization underlies the firm's long-run production decisions and determines its cost structure.

## Questions

```yaml
- question: "A firm is producing output Q. At its current input mix, MPL/MPK = 3 and w/r = 2 (wages are twice the rental rate of capital). What should the firm do to minimize the cost of producing Q?"
  type: multiple-choice
  options:
    - "Hire more capital and less labor — capital is currently producing more output per dollar"
    - "Hire more labor and less capital — labor produces more output per dollar at current prices"
    - "Maintain the current input mix — MRTS is above the price ratio, which is optimal"
    - "Increase total spending on both inputs to shift the isocost line outward"
  answer: 1
  explanation: "The cost-minimizing condition is MRTS = w/r, i.e., MPL/MPK = w/r. Here MPL/MPK = 3 > w/r = 2, which means labor's marginal product per dollar (MPL/w) exceeds capital's (MPK/r). The firm can produce the same output more cheaply by substituting labor for capital: hire more labor and reduce capital until the marginal products per dollar equalize. This is the no-arbitrage logic: keep substituting toward the input that delivers more output per dollar until the advantage disappears."

- question: "What does the factor demand curve for labor represent in the cost minimization framework?"
  type: multiple-choice
  options:
    - "The total amount of labor the firm hires as its output level increases over time"
    - "The quantity of labor that minimizes cost for a given output level, as the wage rate varies"
    - "The marginal product of labor as a function of the total amount of labor employed"
    - "The share of total costs attributable to labor at the profit-maximizing output level"
  answer: 1
  explanation: "The factor demand curve traces the cost-minimizing labor quantity at each wage level, holding output constant. As the wage rises, the isocost line steepens and the tangency point shifts along the isoquant toward more capital and less labor — the firm substitutes away from the now-expensive input. Plotting these wage-quantity pairs produces a downward-sloping factor demand curve. It is 'derived demand' because the firm doesn't want labor for its own sake — it demands labor to produce output that consumers demand."

- question: "At the cost-minimizing input combination, no reallocation of a dollar from one input to another can produce more output at the same total cost."
  type: true-false
  answer: true
  explanation: "This is the economic meaning of the tangency condition MRTS = w/r. When MPL/w = MPK/r, the last dollar spent on labor and the last dollar spent on capital both yield the same additional output. If they were unequal, the firm could reallocate spending from the lower-productivity input to the higher-productivity one and produce more output at the same cost — contradicting cost minimization. The tangency is precisely the point where this no-arbitrage condition holds, so no profitable reallocation is possible."

- question: "Cost minimization analysis tells the firm how much output to produce — it determines the profit-maximizing quantity."
  type: true-false
  answer: false
  explanation: "Cost minimization is a constrained optimization at a fixed output level: it finds the cheapest way to produce Q units, not how much Q to produce. The output decision is a separate profit-maximization step (choose Q where MR = MC). Cost minimization runs 'inside' profit maximization: for each candidate output level Q, cost minimization determines the minimum cost of achieving it, generating the cost function C(Q). Profit maximization then selects the Q that maximizes TR(Q) − C(Q). The two steps are conceptually and mathematically distinct."

- question: "Explain why cost minimization and profit maximization are separate decisions, and how they relate to each other in the firm's overall optimization."
  type: short-answer
  answer: "Cost minimization asks: given that I want to produce Q units, what is the cheapest input combination? It produces the cost function C(Q) — the minimum cost at every output level. Profit maximization then asks: which Q maximizes profit? It compares revenue and cost across output levels, using C(Q) from the cost minimization step. Cost minimization is a prerequisite for profit maximization: you cannot choose the best output level without knowing how much each output level costs. The firm runs cost minimization 'everywhere' (for all Q) to build C(Q), then uses C(Q) in the profit calculation."
  explanation: "A firm could produce 100 units inefficiently by overpaying for inputs, or efficiently at minimum cost. Profit maximization only makes sense when you assume efficient production — otherwise you are comparing apples to oranges. The separation into two steps also has analytical value: cost minimization is a purely technological-economic question (how to produce), while profit maximization is a market question (how much to sell). The isoquant-isocost analysis lives entirely in the cost minimization step."
```

## Explainer

From your work with isoquants, you already know that a given output level can be produced by many different combinations of labor and capital. The question now is: which combination is cheapest? To answer this, you need a second geometric object — the **isocost line**. An isocost line connects all input combinations (L, K) that cost the same total amount: wL + rK = C, where w is the wage rate and r is the rental rate of capital. Just like a consumer's budget constraint, an isocost line has slope -w/r: for every extra unit of labor you hire, you must release w/r units of capital to stay at the same cost.

The cost-minimizing input combination is where the isoquant is **tangent** to the lowest possible isocost line. At that tangency, the slopes of the two curves are equal: the **marginal rate of technical substitution** (MRTS = MPL/MPK) equals the input price ratio (w/r). You can read this condition as a no-arbitrage rule: if MPL/MPK > w/r, you can produce the same output more cheaply by substituting labor for capital (labor buys more output per dollar than capital does). You keep substituting until the productivity ratios equal the cost ratios — at which point no further profitable rearrangement is possible.

Now trace what happens when an input price changes. Suppose the wage w rises. The isocost line rotates — it becomes steeper (slope -w/r is now more negative). The tangency point shifts along the isoquant toward more capital and less labor: the firm substitutes away from the now-more-expensive input. This movement traces out the **factor demand curve** for labor: as w rises, quantity of labor demanded falls. The factor demand curve for an input is therefore a derived demand — it reflects not a preference for labor per se, but the demand for the output that labor helps produce.

An important subtlety: cost minimization as studied here is a constrained optimization at a fixed output level. It tells you the cheapest way to produce Q units, not how much to produce. The firm's actual output decision (choosing Q to maximize profit, where MR = MC) is a separate step. But the cost-minimizing input choices at every output level generate the firm's cost function — the foundation for all long-run cost analysis. As output scales up, the cost-minimizing input bundle traces an **expansion path** through input space, which determines how average costs behave as the firm grows.
