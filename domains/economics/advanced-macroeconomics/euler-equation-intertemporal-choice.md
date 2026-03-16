---
id: euler-equation-intertemporal-choice
title: Euler Equation and Intertemporal Consumption Choice
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: bellman-equation-dynamic-programming
  type: hard
- id: consumer-theory-utility
  type: hard
- id: partial-derivatives
  type: soft
- id: chain-rule
  type: soft
builds-toward:
- solow-growth-model
- consumption-smoothing-intertemporal
tags:
- intertemporal-choice
- consumption
- first-order-conditions
stage: advanced
status: draft
---

# Euler Equation and Intertemporal Consumption Choice

## Core Idea
The Euler equation characterizes optimal consumption growth: u'(c_t) = βE_t[u'(c_{t+1})(1+r_{t+1})]. It equates current marginal utility to discounted expected future marginal utility, showing consumption growth depends on the real interest rate and the elasticity of intertemporal substitution.

## Explainer

From consumer theory, you know that an optimizing agent equates marginal utility per dollar across goods. The Euler equation applies this same logic across time rather than across goods. Instead of asking "should I spend another dollar on apples or oranges?", the consumer asks "should I spend another dollar today or save it and spend (1+r) dollars tomorrow?" At the optimum, the consumer must be indifferent between these two options—otherwise, shifting consumption between periods would increase total utility.

The **Euler equation** formalizes this indifference condition. The left side, u'(c_t), is the marginal utility gained from consuming one more unit today. The right side, βE_t[u'(c_{t+1})(1+r_{t+1})], is the expected marginal utility of saving that unit instead: it earns a gross return (1+r) and is consumed next period, but future utility is discounted by the factor **β** (which captures the consumer's impatience—how much less they value future satisfaction relative to present satisfaction). If u'(c_t) exceeded the right side, the consumer would be better off consuming more today and saving less; if it fell short, saving more would be preferable. At the optimum, the two sides are equal.

From your work with the Bellman equation, you can derive the Euler equation directly. In the dynamic programming formulation, the consumer maximizes the value function by choosing current consumption, and the first-order condition with respect to consumption yields exactly the Euler equation via the envelope theorem. The power of this result is that it replaces the entire infinite-horizon optimization problem with a simple period-by-period condition. You do not need to solve for the complete consumption path—the Euler equation, combined with a budget constraint and a transversality condition, fully characterizes optimal behavior.

The equation's implications become concrete with a standard utility function. Using CRRA (constant relative risk aversion) utility, u(c) = c^(1-σ)/(1-σ), the Euler equation implies that consumption growth, c_{t+1}/c_t, is an increasing function of the real interest rate and a decreasing function of the risk aversion parameter σ. The reciprocal 1/σ is called the **elasticity of intertemporal substitution (EIS)**—it measures how willing the consumer is to shift consumption across time in response to interest rate changes. A high EIS means consumption growth responds strongly to interest rates; a low EIS means the consumer cares mostly about smoothing consumption and is relatively insensitive to returns. This single parameter governs consumption dynamics, asset pricing, and the effectiveness of interest rate policy in virtually every modern macroeconomic model.
