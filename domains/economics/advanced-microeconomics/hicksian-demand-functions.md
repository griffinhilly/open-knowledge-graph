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

## Questions

```yaml
- question: "The price of a good rises. Which statement correctly distinguishes how Hicksian and Marshallian demand respond?"
  type: multiple-choice
  options:
    - "Hicksian demand includes the income effect while Marshallian demand does not"
    - "Both always decrease, but Hicksian demand decreases by more because utility is held constant"
    - "Hicksian demand always decreases because only the substitution effect operates; Marshallian demand may increase if the income effect dominates (e.g., a Giffen good)"
    - "Marshallian demand is always downward-sloping; Hicksian demand can slope upward for inferior goods"
  answer: 2
  explanation: "Hicksian demand isolates the pure substitution effect by holding utility constant at the original level. When a price rises, consumers always substitute away from the more expensive good — so Hicksian demand always falls. Marshallian demand mixes the substitution effect with the income effect (the consumer is now effectively poorer). For normal goods, both effects reinforce each other and Marshallian demand also falls. For inferior Giffen goods, the income effect is so large and in the opposite direction that Marshallian demand actually rises — but Hicksian demand still falls, since that income effect is stripped out."

- question: "A welfare economist wants to measure the exact welfare loss a consumer suffers from a price increase. She should use the area to the left of:"
  type: multiple-choice
  options:
    - "The Marshallian demand curve, because it reflects actual market behavior"
    - "The Hicksian demand curve evaluated at the original utility level, which gives the compensating variation"
    - "The average of the Hicksian and Marshallian demand curves to capture both effects"
    - "Neither; welfare loss must be computed using the indirect utility function directly"
  answer: 1
  explanation: "Marshallian consumer surplus (area under the Marshallian demand curve) is only an approximation of welfare change because it conflates the substitution and income effects. The theoretically exact welfare measure is the compensating variation (CV) — the income adjustment needed to restore original utility after the price change — which equals the area to the left of the Hicksian demand curve at the original utility level. Shephard's lemma provides the connection: Hicksian demand is the derivative of the expenditure function with respect to price, so integrating it gives expenditure changes at constant utility."

- question: "The area to the left of a Hicksian demand curve provides an exact welfare measure of a price change, whereas the corresponding area under a Marshallian demand curve is only an approximation."
  type: true-false
  answer: true
  explanation: "Marshallian consumer surplus mixes the substitution effect with the income effect, making it an approximation of the theoretically correct compensating and equivalent variations. Hicksian demand holds utility constant, so integrating it over a price change gives the exact expenditure change needed to keep the consumer at a fixed utility level — the definition of compensating variation (CV). Equivalent variation uses the Hicksian demand curve at the new utility level. For practical purposes, Marshallian surplus is often used as an approximation when income effects are small."

- question: "Hicksian demand and Marshallian demand coincide whenever the income elasticity of demand is zero (as in quasi-linear utility), but they differ for all normal goods."
  type: true-false
  answer: false
  explanation: "The statement correctly identifies the quasi-linear case but wrongly says they 'differ for all normal goods' as if that were a surprising fact requiring clarification. More precisely: Hicksian and Marshallian demand always differ unless income effects are zero (quasi-linear utility). For normal goods they differ because the income effect reinforces the substitution effect; for inferior goods they can differ dramatically — with Marshallian demand sloping upward (Giffen good) while Hicksian demand still slopes downward. The key insight is that Hicksian demand *never* slopes upward, regardless of the good type."

- question: "Why is Hicksian demand guaranteed to be downward-sloping in own price, even when Marshallian demand need not be?"
  type: short-answer
  answer: "Hicksian demand solves the expenditure minimization problem at a fixed utility level, so any price change is answered purely by substituting away from the now-more-expensive good — there is no income effect to counteract the substitution. The substitution effect is always negative in own price (consumers always substitute toward cheaper alternatives), which is why the Hicksian demand curve always slopes down. Marshallian demand includes both substitution and income effects; for a Giffen inferior good, the income effect is large and positive, can dominate the substitution effect, and produces an upward-sloping demand curve."
  explanation: "This is the central conceptual distinction of the topic. The Slutsky equation makes the decomposition explicit: Marshallian price response = Hicksian (substitution) response − (income effect). The substitution term is always ≤ 0. For normal goods the income term is also negative (income falls → demand falls), reinforcing the downward slope. For inferior goods the income term is positive and large enough, in the Giffen case, to flip the sign of the total Marshallian response — but the Hicksian term is still negative."
```

## Explainer

You already know from consumer theory that **Marshallian demand functions** come from maximizing utility subject to a budget constraint — they tell you how much a consumer buys at given prices and income. **Hicksian demand functions** come from the dual problem: minimizing expenditure subject to maintaining a fixed utility level. The question is no longer "what can I afford?" but "what is the cheapest way to stay exactly this happy?" The answer gives quantities demanded as functions of prices and a utility target, rather than prices and income.

Why does this distinction matter? When the price of a good rises, Marshallian demand captures two simultaneous effects: the consumer substitutes toward cheaper alternatives (substitution effect), and the consumer is effectively poorer because their budget buys less (income effect). For normal goods these effects reinforce each other, but for inferior goods the income effect pushes the opposite direction — and in the extreme case of a Giffen good, income effects dominate and Marshallian demand actually slopes upward. Hicksian demand eliminates this complication entirely. By holding utility constant, it isolates the **pure substitution effect**: when a good's price rises, the consumer always substitutes away from it, period. This is why Hicksian demand curves are guaranteed to slope downward — a property that Marshallian demand cannot claim in general.

The connection to the expenditure function makes Hicksian demands easy to compute once you have done the duality work. By **Shephard's lemma**, the Hicksian demand for good i is simply the partial derivative of the expenditure function with respect to the price of good i: h_i(p, ū) = ∂e(p, ū)/∂p_i. This is elegant because you do not need to re-solve a constrained optimization — the expenditure function already contains all the information. The Slutsky equation then connects the two types of demand: the Marshallian price response equals the Hicksian (substitution) response minus the income effect, which is the product of the income derivative of Marshallian demand and the quantity consumed.

The real payoff of Hicksian demand is in **welfare analysis**. When you want to measure how much a price change hurts or helps a consumer, Marshallian consumer surplus is only an approximation — it conflates substitution and income effects. Hicksian demand gives exact welfare measures. **Compensating variation** asks: after the price change, how much income must we give (or take from) the consumer to restore their original utility? It is the area to the left of the Hicksian demand curve evaluated at the original utility level. **Equivalent variation** asks the symmetric question from the new utility level. These measures are the theoretically correct way to evaluate the welfare impact of price changes, taxes, and subsidies, which is why Hicksian demand is indispensable in applied welfare economics.
