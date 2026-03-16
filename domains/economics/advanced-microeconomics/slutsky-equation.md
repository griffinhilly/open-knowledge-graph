---
id: slutsky-equation
title: The Slutsky Equation
domain: economics
course: advanced-microeconomics
prerequisites:
- id: income-and-substitution-effects
  type: hard
- id: consumer-theory-utility
  type: hard
- id: partial-derivatives
  type: hard
- id: linear-algebra
  type: soft
- id: partial-derivatives-definition
  type: hard
- id: implicit-differentiation-multivariable
  type: soft
builds-toward:
- compensated-demand-curves
- revealed-preference-axioms
tags:
- consumer-theory
- demand
- decomposition
stage: advanced
status: draft
---

# The Slutsky Equation

## Core Idea
The Slutsky equation decomposes the total change in quantity demanded into a substitution effect (movement along indifference curve at constant utility) and an income effect (adjustment for purchasing power changes). This decomposition is fundamental to understanding how consumers respond to price changes and reveals that demand slopes downward primarily through the substitution effect.

## Explainer

When you studied income and substitution effects, you learned that a price change does two things at once: it changes the relative price of goods (making one cheaper or more expensive compared to alternatives) and it changes the consumer's real purchasing power. The Slutsky equation takes this intuition and gives it precise mathematical form, allowing you to separate these two channels exactly.

The equation is written as ∂xᵢ/∂pⱼ = ∂hᵢ/∂pⱼ − xⱼ · (∂xᵢ/∂m), where xᵢ is the **Marshallian (ordinary) demand** for good i, hᵢ is the **Hicksian (compensated) demand**, and m is income. The first term on the right is the **substitution effect** — how demand changes when the price changes but utility is held constant. Because the compensated demand holds the consumer on the same indifference curve, this term isolates pure relative-price responses. From your work with partial derivatives, you can see that each term is a partial derivative holding different things constant: Marshallian demand holds income constant, while Hicksian demand holds utility constant.

The second term, −xⱼ · (∂xᵢ/∂m), is the **income effect**. When the price of good j rises, a consumer who was buying xⱼ units of it effectively loses xⱼ · Δpⱼ in purchasing power. The factor ∂xᵢ/∂m tells you how demand for good i responds to income changes. The negative sign appears because a price increase reduces real income. For a **normal good** (∂xᵢ/∂m > 0), the income effect reinforces the substitution effect — both push demand down when price rises. For an **inferior good**, the income effect works against the substitution effect, and in the extreme case of a **Giffen good**, the income effect dominates, producing upward-sloping demand.

The substitution effect is always negative for own-price changes (∂hᵢ/∂pᵢ ≤ 0) — this is guaranteed by the concavity of the expenditure function, which you can verify using the second-order conditions from your optimization background. This means the substitution effect always pushes demand in the "intuitive" direction: higher price, less quantity. The law of demand can only be violated when the income effect is large enough and works in the opposite direction, which requires the good to be inferior and to consume a large share of the budget.

The Slutsky equation also has a matrix form — the **Slutsky matrix** S with entries sᵢⱼ = ∂hᵢ/∂pⱼ is symmetric and negative semidefinite. Symmetry means that the compensated cross-price effect of good j on good i equals the effect of good i on good j. These properties come directly from the structure of constrained optimization and connect consumer theory to the mathematical properties you studied in linear algebra. The matrix form becomes essential when you move to revealed preference theory, where you test whether observed demand data is consistent with utility maximization by checking whether the implied Slutsky matrix satisfies these conditions.
