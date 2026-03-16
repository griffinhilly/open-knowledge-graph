---
id: cost-minimization-input-demand
title: Cost Minimization and Conditional Input Demand
domain: economics
course: microeconomics
prerequisites:
- id: production-technology-and-isoquants
  type: hard
- id: lagrange-multipliers
  type: soft
builds-toward:
- returns-to-scale-analysis
- long-run-cost-structure
tags:
- producer theory
- costs
- optimization
- factor demand
stage: abstract-reasoning
status: draft
---

# Cost Minimization and Conditional Input Demand

## Core Idea
Firms minimize the cost of producing a target output by choosing input quantities where the price ratio equals the marginal rate of technical substitution (w/r = MRTS). Conditional input demands x*(w,r,y) show how many inputs to use at given prices and output. The cost function c(w,r,y) gives minimum cost for each output level; its properties (homogeneity, concavity) derive from technology.

## Explainer

From your study of isoquants, you know that an isoquant is a curve showing all input combinations — say, labor L and capital K — that produce the same quantity of output. The slope of an isoquant at any point is the **marginal rate of technical substitution** (MRTS), the rate at which you can substitute one input for another while holding output constant. MRTS equals the ratio of the marginal products: MRTS = MP_L / MP_K. Cost minimization is about finding the right point on an isoquant — the one that costs the least.

The cost of an input bundle (L, K) at wage w and rental rate r is simply wL + rK. If you set this equal to a fixed budget, you get an **isocost line**: L = C/w − (r/w)K. The slope of the isocost line is −r/w (or −w/r when expressed in the conventional orientation). The cost-minimizing input bundle is where an isocost line is tangent to the target isoquant. At this tangency point, the slopes are equal: MRTS = w/r. This tangency condition has an intuitive interpretation: at the optimum, the last dollar spent on labor buys as much output as the last dollar spent on capital — if it didn't, you could reallocate spending between inputs and produce the same output more cheaply.

This optimality condition defines the **conditional input demands** — the functions L*(w, r, y) and K*(w, r, y) that tell the firm how much of each input to hire to produce output y at minimum cost, given prices w and r. They are "conditional" because they depend on the output target y, not on the profit motive directly. Plugging these back into the cost expression gives the **cost function** c(w, r, y) = wL* + rK*, which summarizes everything about the firm's production technology. The cost function is homogeneous of degree one in input prices — doubling both w and r doubles costs without changing optimal input ratios — and it is concave in input prices, reflecting the firm's ability to substitute toward cheaper inputs when prices change.

If you have studied Lagrange multipliers, you can derive the same result formally: minimize wL + rK subject to the constraint f(L, K) = y. The first-order conditions yield w = λ · MP_L and r = λ · MP_K, where λ is the Lagrange multiplier (here, the **marginal cost** of output). Dividing one condition by the other gives MP_L / MP_K = w/r, confirming the tangency condition. The Lagrange multiplier λ plays a central role in producer theory: it is the shadow price of relaxing the output constraint by one unit — that is, the marginal cost of production. Shephard's lemma then tells us that the derivative of the cost function with respect to an input price equals the conditional demand for that input: ∂c/∂w = L*(w, r, y). This powerful result means you can recover input demands from the cost function without solving the optimization problem again.
