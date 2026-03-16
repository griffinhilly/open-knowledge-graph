---
id: hicksian-demand-functions
title: Hicksian (Compensated) Demand Functions
domain: economics
course: advanced-microeconomics
prerequisites:
- id: consumer-duality-and-expenditure-function
  type: hard
- id: slutsky-equation
  type: soft
- id: partial-derivatives
  type: soft
- id: constrained-optimization
  type: hard
builds-toward:
- welfare-analysis-advanced
tags:
- demand
- consumer-theory
- welfare
stage: advanced
status: draft
---

# Hicksian (Compensated) Demand Functions

## Core Idea
Hicksian demand functions show quantities demanded at different prices while holding utility constant (from the expenditure-minimization problem). Unlike Marshallian demand, Hicksian demand is always downward-sloping because it isolates pure substitution effects without income effects. Hicksian demand is central to welfare analysis: compensating and equivalent variations are computed using Hicksian demand.

## Explainer

You already know from consumer theory that **Marshallian demand functions** come from maximizing utility subject to a budget constraint — they tell you how much a consumer buys at given prices and income. **Hicksian demand functions** come from the dual problem: minimizing expenditure subject to maintaining a fixed utility level. The question is no longer "what can I afford?" but "what is the cheapest way to stay exactly this happy?" The answer gives quantities demanded as functions of prices and a utility target, rather than prices and income.

Why does this distinction matter? When the price of a good rises, Marshallian demand captures two simultaneous effects: the consumer substitutes toward cheaper alternatives (substitution effect), and the consumer is effectively poorer because their budget buys less (income effect). For normal goods these effects reinforce each other, but for inferior goods the income effect pushes the opposite direction — and in the extreme case of a Giffen good, income effects dominate and Marshallian demand actually slopes upward. Hicksian demand eliminates this complication entirely. By holding utility constant, it isolates the **pure substitution effect**: when a good's price rises, the consumer always substitutes away from it, period. This is why Hicksian demand curves are guaranteed to slope downward — a property that Marshallian demand cannot claim in general.

The connection to the expenditure function makes Hicksian demands easy to compute once you have done the duality work. By **Shephard's lemma**, the Hicksian demand for good i is simply the partial derivative of the expenditure function with respect to the price of good i: h_i(p, ū) = ∂e(p, ū)/∂p_i. This is elegant because you do not need to re-solve a constrained optimization — the expenditure function already contains all the information. The Slutsky equation then connects the two types of demand: the Marshallian price response equals the Hicksian (substitution) response minus the income effect, which is the product of the income derivative of Marshallian demand and the quantity consumed.

The real payoff of Hicksian demand is in **welfare analysis**. When you want to measure how much a price change hurts or helps a consumer, Marshallian consumer surplus is only an approximation — it conflates substitution and income effects. Hicksian demand gives exact welfare measures. **Compensating variation** asks: after the price change, how much income must we give (or take from) the consumer to restore their original utility? It is the area to the left of the Hicksian demand curve evaluated at the original utility level. **Equivalent variation** asks the symmetric question from the new utility level. These measures are the theoretically correct way to evaluate the welfare impact of price changes, taxes, and subsidies, which is why Hicksian demand is indispensable in applied welfare economics.
