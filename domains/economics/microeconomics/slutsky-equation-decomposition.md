---
id: slutsky-equation-decomposition
title: Slutsky Equation and Price Effect Decomposition
domain: economics
course: microeconomics
prerequisites:
- id: income-and-substitution-effects
  type: hard
- id: hicksian-demand
  type: hard
- id: duality-consumer-preferences
  type: soft
- id: normal-vs-inferior-goods-analysis
  type: soft
builds-toward:
  - demand-system-integrability
tags:
- consumer theory
- price effects
- decomposition
stage: formal-systems
status: validated
---
# Slutsky Equation and Price Effect Decomposition

## Core Idea
The Slutsky equation decomposes the total price effect into a substitution effect (movement along indifference curve) and income effect (shift of budget line). Mathematically: ∂x/∂p = ∂h/∂p − (∂x/∂m)·x, where h is compensated (Hicksian) demand. The substitution effect is always negative, but income effects vary, allowing Giffen goods in rare cases.

## Questions

```yaml
- question: "The price of a good rises. For this good, the substitution effect is −5 units and the income effect is +2 units (the good is inferior). What is the total price effect, and what type of good is this?"
  type: multiple-choice
  options:
    - "Total effect: −3 units; this is a Giffen good because the income effect is positive"
    - "Total effect: −3 units; this is an inferior good with a downward-sloping demand curve"
    - "Total effect: +3 units; the positive income effect dominates, making this a Giffen good"
    - "Total effect: −7 units; the effects add when both are negative"
  answer: 1
  explanation: "The Slutsky equation gives total effect = substitution effect + income effect = −5 + 2 = −3. The demand curve still slopes downward. The income effect being positive (+2) for an inferior good means as you become effectively poorer (price rise reduces real income), you buy MORE of the inferior good. But here it's not large enough to reverse the substitution effect. A Giffen good requires the (positive) income effect to EXCEED the magnitude of the (always negative) substitution effect in absolute terms, giving a positive total effect. Option A is wrong: a positive income effect alone doesn't make something a Giffen good."

- question: "Which component of the Slutsky equation is guaranteed to be non-positive for any good, regardless of whether the good is normal, inferior, or Giffen?"
  type: multiple-choice
  options:
    - "The total price effect ∂x/∂p, because demand curves slope downward"
    - "The income effect x·(∂x/∂m), because income effects always reinforce price effects"
    - "The substitution effect ∂h/∂p, because utility-maximizing consumers always substitute away from relatively more expensive goods"
    - "Both the substitution and income effects, because price increases always reduce demand"
  answer: 2
  explanation: "The substitution effect ∂h/∂p is guaranteed non-positive. This follows from the mathematical properties of utility maximization: the Slutsky matrix is negative semi-definite, which means own-price substitution effects are always ≤ 0. Intuitively: holding utility constant, if a good gets relatively more expensive, you never substitute TOWARD it. The income effect and total effect can be positive (for inferior and Giffen goods). The demand curve's downward slope is the norm but not a guarantee — Giffen goods disprove it."

- question: "For a Giffen good, the substitution effect is positive — the consumer substitutes toward the good when its price rises."
  type: true-false
  answer: false
  explanation: "This is the most important misconception about Giffen goods. The substitution effect is ALWAYS non-positive — for every good, including Giffen goods. What makes a Giffen good special is not its substitution effect (which is negative, like everything else) but its INCOME EFFECT. When a Giffen good's price rises, the consumer is effectively much poorer (the good constitutes a large share of the budget), causing them to cut back on higher-quality substitutes and buy MORE of the cheap Giffen good. The income effect is positive and large enough in magnitude to outweigh the negative substitution effect."

- question: "The Slutsky equation predicts that demand for a normal good must slope downward, because both the substitution and income effects work in the same direction."
  type: true-false
  answer: true
  explanation: "For a normal good, ∂x/∂m > 0 — as income rises, you buy more. When price rises, you become effectively poorer, so the income effect reduces demand (the term −x·(∂x/∂m) is negative). The substitution effect is also always non-positive. So for a normal good, both effects point in the same direction — demand unambiguously falls when price rises. This confirms the law of demand for all normal goods. Only for inferior goods (∂x/∂m < 0) does the income effect fight the substitution effect, and only for Giffen goods is it strong enough to reverse the total effect."

- question: "Why is the substitution effect always non-positive, and why does this hold even for Giffen goods?"
  type: short-answer
  answer: "The substitution effect measures how demand changes when price rises but income is simultaneously adjusted to keep utility constant (moving along the same indifference curve). Since the consumer remains at the same utility level, they are optimizing over a new budget constraint that makes the good relatively more expensive. Utility maximization guarantees they will never choose to buy more of a now-relatively-expensive good when compensated demand keeps them at the same utility — this follows from the negative semi-definiteness of the Slutsky matrix. Giffen goods have a large positive income effect (they are strongly inferior), but their substitution effect is negative like everything else."
  explanation: "The key is the definition of the substitution effect: it holds utility constant, asking 'if you were fully compensated for the price increase, would you still shift away from this good?' The answer is always yes or neutral — you move along an indifference curve to a tangency with a steeper budget line, always reducing or holding constant the quantity of the now-relatively-expensive good. This is a mathematical necessity, not an empirical regularity. What Giffen goods prove is that the income effect can dominate the substitution effect — but the substitution effect itself is always pulling demand downward."
```

## Explainer

You already know from income and substitution effects that a price change does two things simultaneously: it makes a good relatively more expensive compared to substitutes (the **substitution effect**), and it changes your real purchasing power (the **income effect**). The Slutsky equation gives the algebraic tool to separate these effects precisely — instead of reasoning through indifference curve diagrams each time, you have a formula that holds for any demand function.

The equation is: ∂x/∂p = ∂h/∂p − x · (∂x/∂m). The left side is the **total price effect** — how observed Marshallian demand changes when price p changes. The first right-hand term is the **substitution effect**: ∂h/∂p, the Hicksian (compensated) demand derivative, which holds utility constant by adjusting income as price changes. This is the term your prerequisite on Hicksian demand prepared you for. The second term is the **income effect**: x (current quantity consumed) times how demand responds to income. The minus sign converts the real income loss from a price rise into its demand consequence.

The critical result is that the substitution effect is *always* non-positive. When a price rises and you adjust income to keep utility constant, you will always substitute away — this follows from the mathematical properties of utility maximization (the negative semi-definiteness of the Slutsky matrix). The income effect can go either way: positive for normal goods (which reinforces the downward slope) or negative for inferior goods (which fights it).

For most goods, both effects point downward: price rises, you substitute away *and* you're effectively poorer. But for a **Giffen good** — an inferior good that consumes a huge share of the budget — the income effect is large enough in magnitude to overcome the substitution effect. A price increase makes you so much poorer that you can't afford the higher-quality substitute, so you buy *more* of the cheap good. The Slutsky equation makes this theoretically possible, though empirically extremely rare. More broadly, the equation underpins welfare analysis (compensating variation, equivalent variation), index number theory, and all of modern demand system estimation — the substitution matrix it implies is a central object in advanced microeconomics.
