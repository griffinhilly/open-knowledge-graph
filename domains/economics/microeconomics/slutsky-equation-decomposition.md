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
builds-toward:
- demand-system-integrability
- normal-vs-inferior-goods-analysis
tags:
- consumer theory
- price effects
- decomposition
stage: abstract-reasoning
status: draft
---

# Slutsky Equation and Price Effect Decomposition

## Core Idea
The Slutsky equation decomposes the total price effect into a substitution effect (movement along indifference curve) and income effect (shift of budget line). Mathematically: ∂x/∂p = ∂h/∂p − (∂x/∂m)·x, where h is compensated (Hicksian) demand. The substitution effect is always negative, but income effects vary, allowing Giffen goods in rare cases.

## Explainer

You already know from income and substitution effects that a price change does two things simultaneously: it makes a good relatively more expensive compared to substitutes (the **substitution effect**), and it changes your real purchasing power (the **income effect**). The Slutsky equation gives the algebraic tool to separate these effects precisely — instead of reasoning through indifference curve diagrams each time, you have a formula that holds for any demand function.

The equation is: ∂x/∂p = ∂h/∂p − x · (∂x/∂m). The left side is the **total price effect** — how observed Marshallian demand changes when price p changes. The first right-hand term is the **substitution effect**: ∂h/∂p, the Hicksian (compensated) demand derivative, which holds utility constant by adjusting income as price changes. This is the term your prerequisite on Hicksian demand prepared you for. The second term is the **income effect**: x (current quantity consumed) times how demand responds to income. The minus sign converts the real income loss from a price rise into its demand consequence.

The critical result is that the substitution effect is *always* non-positive. When a price rises and you adjust income to keep utility constant, you will always substitute away — this follows from the mathematical properties of utility maximization (the negative semi-definiteness of the Slutsky matrix). The income effect can go either way: positive for normal goods (which reinforces the downward slope) or negative for inferior goods (which fights it).

For most goods, both effects point downward: price rises, you substitute away *and* you're effectively poorer. But for a **Giffen good** — an inferior good that consumes a huge share of the budget — the income effect is large enough in magnitude to overcome the substitution effect. A price increase makes you so much poorer that you can't afford the higher-quality substitute, so you buy *more* of the cheap good. The Slutsky equation makes this theoretically possible, though empirically extremely rare. More broadly, the equation underpins welfare analysis (compensating variation, equivalent variation), index number theory, and all of modern demand system estimation — the substitution matrix it implies is a central object in advanced microeconomics.
