---
id: cost-minimization-and-factor-demand
title: Cost Minimization and Conditional Factor Demand
domain: economics
course: advanced-microeconomics
prerequisites:
- id: production-function-microeconomics
  type: hard
- id: long-run-costs-economies-of-scale
  type: soft
- id: lagrange-multipliers
  type: hard
- id: partial-derivatives
  type: soft
builds-toward:
- dual-production-and-profit-functions
tags:
- producer-theory
- costs
- optimization
stage: advanced
status: draft
---

# Cost Minimization and Conditional Factor Demand

## Core Idea
Firms minimize cost for any target output by equating the marginal rate of technical substitution to the input price ratio. Conditional factor demands depend on output and input prices and are derived from the cost function using Shephard's lemma: ∂C/∂w_i = conditional demand for input i. This mirrors the consumer duality problem and is essential for understanding production technology.

## Explainer

You already know from production theory that a firm transforms inputs into output according to a production function f(x₁, x₂). From your work with Lagrange multipliers, you know how to optimize a function subject to a constraint. Cost minimization brings these together: given input prices w₁ and w₂ and a target output level q, the firm chooses input quantities to minimize total cost w₁x₁ + w₂x₂ subject to f(x₁, x₂) = q. This is the producer's analog of the consumer's expenditure minimization problem.

The optimality condition has an intuitive interpretation. Setting up the Lagrangian and taking first-order conditions yields the rule that the **marginal rate of technical substitution** (MRTS) — the rate at which the firm can substitute one input for another while maintaining output — must equal the input price ratio w₁/w₂. Graphically, this is the point where an **isoquant** (constant-output curve) is tangent to an **isocost line** (constant-cost line). If the MRTS exceeds the price ratio, the firm is using too much of input 2 relative to input 1: it could maintain the same output at lower cost by substituting toward the cheaper input. The tangency condition ensures no further cost-saving substitution is possible.

Solving the cost minimization problem for all output levels produces two key objects. The **conditional factor demands** x_i*(w₁, w₂, q) tell you how much of each input the firm uses as a function of input prices and target output — they are "conditional" because output is held fixed rather than being chosen optimally. The **cost function** C(w₁, w₂, q) = w₁x₁* + w₂x₂* gives the minimized cost as a function of prices and output. This cost function encodes everything about the firm's technology in a compact, tractable form.

The connection between the cost function and factor demands is captured by **Shephard's lemma**: ∂C/∂w_i = x_i*. Differentiating the cost function with respect to an input price directly recovers the conditional demand for that input. This result, which parallels the envelope theorem from your optimization background, is powerful because it means you can derive factor demands from the cost function without re-solving the optimization problem. The entire framework mirrors consumer duality — expenditure function maps to cost function, Hicksian demands map to conditional factor demands, and Shephard's lemma works identically on both sides. Recognizing this parallel deepens your understanding of both producer and consumer theory.
