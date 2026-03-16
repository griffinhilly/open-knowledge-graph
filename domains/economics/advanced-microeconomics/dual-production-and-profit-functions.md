---
id: dual-production-and-profit-functions
title: 'Duality in Production: Profit Function and Hotelling''s Lemma'
domain: economics
course: advanced-microeconomics
prerequisites:
- id: profit-maximization-microeconomics
  type: hard
- id: cost-minimization-and-factor-demand
  type: hard
tags:
- producer-theory
- profit
- duality
stage: advanced
status: draft
---

# Duality in Production: Profit Function and Hotelling's Lemma

## Core Idea
The profit function π(p, w) gives maximum profit as a function of prices and is homogeneous of degree 1 and convex in (p, w). Hotelling's lemma states that the derivative of profit with respect to a price gives the optimal supply (or factor demand with negative sign): ∂π/∂p = output supply, ∂π/∂w = -factor demand. The profit function unifies output and input decisions, embodying the duality principle.

## Explainer

From profit maximization, you know that a firm chooses output and inputs to maximize revenue minus costs, given its production technology. From cost minimization, you know that the cost function encodes the cheapest way to produce any given output level. The **dual approach** to producer theory takes this one step further: instead of starting with the production function and solving an optimization problem every time prices change, you encode all the firm's optimal behavior directly into a single object — the **profit function** π(p, w), where p is the output price and w is the vector of input prices.

The profit function is defined as π(p, w) = max over (y, x) of {p·y − w·x} subject to the technology constraint. Think of it as the "best the firm can do" at any given set of prices. This function has elegant mathematical properties that follow purely from the fact that it represents an optimum. It is **homogeneous of degree one** in (p, w): if all prices double, the firm's optimal choices remain the same but profits exactly double (no money illusion). It is **convex** in prices: this means that the firm benefits from price variability — if the output price fluctuates, average profits exceed the profit at the average price, because the firm can adjust its production plan to exploit high-price periods.

The deepest insight is **Hotelling's lemma**, which states that you can recover the firm's optimal supply and factor demands simply by differentiating the profit function. Specifically, ∂π/∂p = y*(p, w) gives the profit-maximizing output level, and ∂π/∂wᵢ = −xᵢ*(p, w) gives the negative of the optimal demand for input i. This is extraordinarily powerful: rather than re-solving the firm's optimization problem for each price configuration, you differentiate once. The negative sign on factor demand is intuitive — higher input prices reduce profit, and the rate of reduction equals how much of that input the firm uses.

The practical payoff of duality is that it makes **comparative statics** almost effortless. Because π is convex in prices, the matrix of second derivatives (the Hessian) is positive semidefinite. This immediately tells you that ∂y*/∂p ≥ 0 (supply curves slope upward) and ∂xᵢ*/∂wᵢ ≤ 0 (own-price factor demand slopes downward) — results that require considerable effort to prove using the primal production function approach. Duality also provides a clean framework for empirical work: estimate a flexible functional form for π(p, w) from price and profit data, then differentiate to recover supply and demand functions that are automatically consistent with profit-maximizing behavior. The profit function, cost function, and production function each contain the same information about technology — duality theory shows they are three equivalent representations of the same firm.
