---
id: hicksian-demand
title: Hicksian Demand (Compensated Demand)
domain: economics
course: advanced-microeconomics
prerequisites:
- id: expenditure-function-microeconomics
  type: hard
builds-toward:
- slutsky-equation
tags:
- consumer-theory
- demand
- price-effect
stage: abstract-reasoning
status: draft
---

# Hicksian Demand (Compensated Demand)

## Core Idea
Hicksian demand h(p, u) is the quantity demanded that minimizes expenditure for a given utility level. Unlike Marshallian demand, Hicksian demand eliminates the income effect: it shows only the substitution effect of price changes. By Shephard's lemma, h(p, u) = ∇_p e(p, u), directly recovering demand from the expenditure function.

## How It's Best Learned
Start with graphical representation showing constant utility. Derive Hicksian demands for specific utility functions. Compare slopes of Hicksian vs. Marshallian demands to understand income effects.

## Common Misconceptions
Mixing up Hicksian and Marshallian demand. Thinking Hicksian demand is always downward-sloping (it is, but Marshallian may not be). Not seeing why income is held constant in Hicksian demand.

## Explainer

From your study of the expenditure function, you know that e(p, u) gives the minimum cost of achieving utility level u at prices p. **Hicksian demand** — also called compensated demand — is the demand function that falls out of that same minimization problem. It answers: if a consumer must achieve exactly utility u at prices p, what bundle does she choose? The quantities h(p, u) that solve the expenditure minimization problem are the Hicksian demands.

The connection to the expenditure function is made precise by **Shephard's lemma**: h_i(p, u) = ∂e(p, u)/∂p_i. Differentiating the expenditure function with respect to the price of good i recovers the Hicksian demand for good i. This is an application of the envelope theorem — at the optimum, the effect of a small price increase on minimized expenditure equals the quantity of that good being consumed, because the consumer is already optimizing and adjusts her bundle only at the margin.

The key difference between Hicksian and Marshallian demand is what is held constant. **Marshallian demand** x(p, m) holds income m fixed and lets utility adjust when prices change. **Hicksian demand** h(p, u) holds utility u fixed and lets the required expenditure adjust. This distinction isolates the pure **substitution effect**: when a price rises, the consumer substitutes away from the more expensive good, holding her standard of living constant. Hicksian demand curves always slope downward because the substitution effect always works against a price increase — this follows from the concavity of the expenditure function in prices. Marshallian demand can occasionally slope upward (Giffen goods) because it bundles together the substitution effect with the income effect, and a sufficiently large negative income effect on an inferior good can dominate.

Understanding this decomposition is essential for what comes next. The **Slutsky equation** formalizes the relationship: ∂x_i/∂p_j = ∂h_i/∂p_j − x_j · ∂x_i/∂m. The total effect of a price change on Marshallian demand equals the substitution effect (captured by Hicksian demand) minus the income effect. Hicksian demand provides the clean, utility-constant benchmark that makes this decomposition possible. Without it, you cannot separate the two channels through which price changes affect consumption, and you cannot determine whether observed demand responses reflect genuine substitution patterns or merely the mechanical effect of price changes on purchasing power.
