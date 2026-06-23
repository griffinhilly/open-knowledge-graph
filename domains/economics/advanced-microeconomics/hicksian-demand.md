---
id: hicksian-demand
title: Hicksian Demand (Compensated Demand)
domain: economics
course: advanced-microeconomics
prerequisites:
- id: expenditure-function-microeconomics
  type: hard
- id: consumer-duality-and-expenditure-function
  type: hard
builds-toward:
- slutsky-equation
tags:
- consumer-theory
- demand
- price-effect
stage: formal-systems
status: validated
---

# Hicksian Demand (Compensated Demand)

## Core Idea
Hicksian demand h(p, u) is the quantity demanded that minimizes expenditure for a given utility level. Unlike Marshallian demand, Hicksian demand eliminates the income effect: it shows only the substitution effect of price changes. By Shephard's lemma, h(p, u) = ∇_p e(p, u), directly recovering demand from the expenditure function.

## How It's Best Learned
Start with graphical representation showing constant utility. Derive Hicksian demands for specific utility functions. Compare slopes of Hicksian vs. Marshallian demands to understand income effects.

## Common Misconceptions
Mixing up Hicksian and Marshallian demand. Thinking Hicksian demand is always downward-sloping (it is, but Marshallian may not be). Not seeing why income is held constant in Hicksian demand.

## Questions

```yaml
- question: "When the price of a good rises, its Hicksian demand decreases. Yet for a Giffen good, Marshallian demand *increases* when price rises. How can both statements be true simultaneously?"
  type: multiple-choice
  options:
    - "Giffen goods violate Shephard's lemma, so Hicksian demand analysis does not apply to them"
    - "Hicksian demand isolates only the substitution effect (always negative), while Marshallian demand also includes the income effect, which for a strongly inferior good can be large enough to dominate and reverse the direction"
    - "Both Hicksian and Marshallian demand slope downward for Giffen goods; the difference is only in the magnitude of the response"
    - "The Giffen paradox only affects demand measured in nominal terms; in real terms both demands slope downward"
  answer: 1
  explanation: "Hicksian demand holds utility constant, so it captures only the pure substitution effect: as a good becomes more expensive, the consumer substitutes away from it along the same indifference curve. This substitution effect is always negative (less of the good at higher prices), making Hicksian demand always downward-sloping. Marshallian demand also includes the income effect — rising prices reduce real purchasing power. For a strongly inferior good (a Giffen good), this income effect is positive and large enough to overwhelm the negative substitution effect, producing upward-sloping Marshallian demand. The Slutsky equation formalizes this decomposition."

- question: "A consumer minimizes expenditure subject to achieving utility ū at prices p. Shephard's lemma states that the Hicksian demand for good i equals:"
  type: multiple-choice
  options:
    - "∂x_i/∂p_i — the change in Marshallian demand when price i changes"
    - "∂e(p, ū)/∂p_i — the partial derivative of the expenditure function with respect to price i"
    - "∂e(p, ū)/∂ū — the marginal cost of raising the utility target"
    - "The slope of the income-consumption path at prices p"
  answer: 1
  explanation: "Shephard's lemma is the key technical result connecting Hicksian demand to the expenditure function: h_i(p, ū) = ∂e(p, ū)/∂p_i. It follows from the envelope theorem — at the expenditure-minimizing bundle, a small increase in p_i raises minimum expenditure by exactly the quantity of good i being consumed, because the consumer is already optimizing and adjusts only at the margin. This gives a powerful computational shortcut: derive the expenditure function once, and differentiate with respect to prices to recover all Hicksian demands."

- question: "Hicksian demand curves always slope downward, regardless of whether the good is normal, inferior, or Giffen."
  type: true-false
  answer: true
  explanation: "Hicksian demand is derived from expenditure minimization holding utility constant, so it captures only the substitution effect. The substitution effect is always negative (by the concavity of the expenditure function in prices): as a good becomes more expensive relative to alternatives, a utility-maximizing consumer always substitutes away from it along the same indifference curve. There is no income effect to potentially reverse this. This is in contrast to Marshallian demand, which can slope upward for Giffen goods because it includes both substitution and income effects."

- question: "Hicksian demand holds income constant while Marshallian demand holds utility constant."
  type: true-false
  answer: false
  explanation: "This is reversed. Marshallian (uncompensated) demand x(p, m) holds *income* m fixed — it is the standard demand function derived from utility maximization subject to a budget constraint. Hicksian (compensated) demand h(p, ū) holds *utility* ū fixed — it is derived from expenditure minimization subject to achieving a given utility level. The term 'compensated' refers to the fact that when prices change, Hicksian demand imagines the consumer's income being adjusted to keep them on the same indifference curve, isolating the pure substitution effect."

- question: "Explain why Hicksian demand is called 'compensated' demand and what it means for the consumer's income to be 'adjusted' as prices change."
  type: short-answer
  answer: "Hicksian demand is 'compensated' because it imagines compensating the consumer for price changes — adjusting their income just enough to keep them at the same utility level as prices shift. If a price rises and real purchasing power falls, the consumer is hypothetically given extra income to restore their original utility. This compensation removes the income effect from the price response, leaving only the pure substitution effect: the change in the bundle that results from relative prices shifting while the standard of living stays constant. The resulting demand function traces movement along a single indifference curve."
  explanation: "The compensation is hypothetical — it is an analytical device to decompose the total price effect rather than a policy being implemented. In practice, when prices change, income is not literally adjusted. But by imagining this compensation, Hicksian demand isolates the part of demand behavior that is purely about substitution between goods at different relative prices, without the confounding effect of price changes on purchasing power. This isolation is what makes Hicksian demand the right tool for welfare analysis and the Slutsky decomposition."
```

## Explainer

From your study of the expenditure function, you know that e(p, u) gives the minimum cost of achieving utility level u at prices p. **Hicksian demand** — also called compensated demand — is the demand function that falls out of that same minimization problem. It answers: if a consumer must achieve exactly utility u at prices p, what bundle does she choose? The quantities h(p, u) that solve the expenditure minimization problem are the Hicksian demands.

The connection to the expenditure function is made precise by **Shephard's lemma**: h_i(p, u) = ∂e(p, u)/∂p_i. Differentiating the expenditure function with respect to the price of good i recovers the Hicksian demand for good i. This is an application of the envelope theorem — at the optimum, the effect of a small price increase on minimized expenditure equals the quantity of that good being consumed, because the consumer is already optimizing and adjusts her bundle only at the margin.

The key difference between Hicksian and Marshallian demand is what is held constant. **Marshallian demand** x(p, m) holds income m fixed and lets utility adjust when prices change. **Hicksian demand** h(p, u) holds utility u fixed and lets the required expenditure adjust. This distinction isolates the pure **substitution effect**: when a price rises, the consumer substitutes away from the more expensive good, holding her standard of living constant. Hicksian demand curves always slope downward because the substitution effect always works against a price increase — this follows from the concavity of the expenditure function in prices. Marshallian demand can occasionally slope upward (Giffen goods) because it bundles together the substitution effect with the income effect, and a sufficiently large negative income effect on an inferior good can dominate.

Understanding this decomposition is essential for what comes next. The **Slutsky equation** formalizes the relationship: ∂x_i/∂p_j = ∂h_i/∂p_j − x_j · ∂x_i/∂m. The total effect of a price change on Marshallian demand equals the substitution effect (captured by Hicksian demand) minus the income effect. Hicksian demand provides the clean, utility-constant benchmark that makes this decomposition possible. Without it, you cannot separate the two channels through which price changes affect consumption, and you cannot determine whether observed demand responses reflect genuine substitution patterns or merely the mechanical effect of price changes on purchasing power.
