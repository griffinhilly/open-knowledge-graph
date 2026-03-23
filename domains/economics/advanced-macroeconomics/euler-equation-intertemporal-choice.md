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
stage: expert
status: validated
---

# Euler Equation and Intertemporal Consumption Choice

## Core Idea
The Euler equation characterizes optimal consumption growth: u'(c_t) = βE_t[u'(c_{t+1})(1+r_{t+1})]. It equates current marginal utility to discounted expected future marginal utility, showing consumption growth depends on the real interest rate and the elasticity of intertemporal substitution.

## Questions

```yaml
- question: "Under the Euler equation with CRRA utility, the real interest rate rises above the consumer's discount rate. What must be true about the optimal consumption path?"
  type: multiple-choice
  options:
    - "Consumption must fall today, since saving is now more attractive"
    - "Consumption must rise today, since higher returns increase lifetime wealth"
    - "Consumption must grow over time — the path tilts upward, but today's level is not pinned by the Euler equation alone"
    - "Consumption must remain flat — the Euler equation enforces consumption smoothing regardless of interest rates"
  answer: 2
  explanation: "The Euler equation with CRRA utility implies c_{t+1}/c_t = [β(1+r)]^{1/σ}. When r > ρ (the discount rate), this ratio exceeds one — consumption grows over time. But the Euler equation is a first-order condition, not a solution: it tells you the shape of the optimal path, not its level. The level is pinned by the budget constraint. Option A is the common error: students conflate 'saving is more attractive' with 'consume less today,' ignoring that a higher interest rate also raises lifetime wealth."

- question: "What does the elasticity of intertemporal substitution (EIS) measure in the context of the Euler equation?"
  type: multiple-choice
  options:
    - "How much a consumer discounts future utility relative to present utility"
    - "How sensitive consumption growth is to changes in the real interest rate"
    - "The probability that a consumer saves rather than consumes in any given period"
    - "How strongly a consumer prefers certain outcomes to risky ones"
  answer: 1
  explanation: "The EIS (equal to 1/σ in CRRA utility) captures how willing consumers are to shift consumption across time in response to interest rate changes. A high EIS means consumption growth responds strongly to r; a low EIS means the consumer prioritizes smooth consumption regardless of returns. Option A describes the discount factor β — a different parameter. Option D describes risk aversion, which σ also governs in CRRA utility, but the EIS specifically concerns intertemporal substitution, not risk."

- question: "The Euler equation directly gives the optimal consumption level for each period, solving the intertemporal optimization problem."
  type: true-false
  answer: false
  explanation: "The Euler equation is a necessary first-order condition — it characterizes what any optimal path must look like, but it does not uniquely determine consumption levels. It tells you how consumption must grow (the ratio c_{t+1}/c_t), but two different budget constraints could generate two different consumption paths that both satisfy the Euler equation. To fully solve the problem, you also need the budget constraint and a transversality condition."

- question: "A consumer with a very low elasticity of intertemporal substitution will maintain nearly flat consumption even when the real interest rate changes substantially."
  type: true-false
  answer: true
  explanation: "Low EIS (high σ) means the consumer has a strong preference for smooth consumption. With CRRA utility, consumption growth = [β(1+r)]^{1/σ} — when σ is large, 1/σ is small, and the exponent barely changes even with large swings in r. Such consumers resist shifting consumption across periods no matter how attractive or unattractive saving becomes. This is why empirically estimating EIS is important for assessing the effectiveness of interest rate policy."

- question: "Explain why the Euler equation can be understood as an indifference condition between consuming today and saving for tomorrow."
  type: short-answer
  answer: "At the optimum, the consumer must be indifferent between spending one more unit of income today (gaining u'(c_t) utility) and saving that unit, earning gross return (1+r), and consuming it next period (gaining β·u'(c_{t+1})·(1+r)). If either side were larger, the consumer would reallocate to exploit the gain. The Euler equation u'(c_t) = β·E_t[u'(c_{t+1})(1+r_{t+1})] says these two must be equal — it is the intertemporal analog of equating marginal utility per dollar across goods in static consumer theory."
  explanation: "This indifference logic mirrors static consumer theory (marginal utility per dollar equalized across goods), just applied across time. The key is that the Euler equation holds as a condition at the optimum — not because the consumer is indifferent everywhere, but because at the chosen point, no marginal reallocation can improve utility."
```

## Explainer

From consumer theory, you know that an optimizing agent equates marginal utility per dollar across goods. The Euler equation applies this same logic across time rather than across goods. Instead of asking "should I spend another dollar on apples or oranges?", the consumer asks "should I spend another dollar today or save it and spend (1+r) dollars tomorrow?" At the optimum, the consumer must be indifferent between these two options—otherwise, shifting consumption between periods would increase total utility.

The **Euler equation** formalizes this indifference condition. The left side, u'(c_t), is the marginal utility gained from consuming one more unit today. The right side, βE_t[u'(c_{t+1})(1+r_{t+1})], is the expected marginal utility of saving that unit instead: it earns a gross return (1+r) and is consumed next period, but future utility is discounted by the factor **β** (which captures the consumer's impatience—how much less they value future satisfaction relative to present satisfaction). If u'(c_t) exceeded the right side, the consumer would be better off consuming more today and saving less; if it fell short, saving more would be preferable. At the optimum, the two sides are equal.

From your work with the Bellman equation, you can derive the Euler equation directly. In the dynamic programming formulation, the consumer maximizes the value function by choosing current consumption, and the first-order condition with respect to consumption yields exactly the Euler equation via the envelope theorem. The power of this result is that it replaces the entire infinite-horizon optimization problem with a simple period-by-period condition. You do not need to solve for the complete consumption path—the Euler equation, combined with a budget constraint and a transversality condition, fully characterizes optimal behavior.

The equation's implications become concrete with a standard utility function. Using CRRA (constant relative risk aversion) utility, u(c) = c^(1-σ)/(1-σ), the Euler equation implies that consumption growth, c_{t+1}/c_t, is an increasing function of the real interest rate and a decreasing function of the risk aversion parameter σ. The reciprocal 1/σ is called the **elasticity of intertemporal substitution (EIS)**—it measures how willing the consumer is to shift consumption across time in response to interest rate changes. A high EIS means consumption growth responds strongly to interest rates; a low EIS means the consumer cares mostly about smoothing consumption and is relatively insensitive to returns. This single parameter governs consumption dynamics, asset pricing, and the effectiveness of interest rate policy in virtually every modern macroeconomic model.
