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
- id: linear-transformations
  type: soft
- id: partial-derivatives
  type: hard
- id: implicit-differentiation-multivariable
  type: soft
- id: hicksian-demand
  type: hard
builds-toward:
- compensated-demand-curves
- revealed-preference-axioms
tags:
- consumer-theory
- demand
- decomposition
stage: expert
status: validated
---

# The Slutsky Equation

## Core Idea
The Slutsky equation decomposes the total change in quantity demanded into a substitution effect (movement along indifference curve at constant utility) and an income effect (adjustment for purchasing power changes). This decomposition is fundamental to understanding how consumers respond to price changes and reveals that demand slopes downward primarily through the substitution effect.

## Questions

```yaml
- question: "The price of bread rises sharply. A very poor family spends 60% of its budget on bread. Bread is an inferior good for this family. Using the Slutsky decomposition, what happens to their bread consumption?"
  type: multiple-choice
  options:
    - "Both the substitution and income effects push consumption down, so demand clearly falls"
    - "The substitution effect pushes consumption down, but the income effect pushes it up — if the income effect dominates, this is a Giffen good and consumption rises"
    - "The substitution effect pushes consumption up while the income effect pushes it down"
    - "The income effect is zero for inferior goods, so only the substitution effect matters"
  answer: 1
  explanation: "For any own-price change, the substitution effect (∂hᵢ/∂pᵢ) is always non-positive — holding utility constant, a higher price always reduces compensated demand. The income effect is −xⱼ·(∂xᵢ/∂m). For an inferior good, ∂xᵢ/∂m < 0, and since a price increase effectively reduces real income, the income effect pushes consumption *up*. If the family spends a large fraction of income on bread, xⱼ is large and the income effect can dominate — producing a Giffen good. Option A describes a normal good. Option C reverses the directions."

- question: "The Slutsky equation tells us that the substitution effect for an own-price change (∂hᵢ/∂pᵢ) is always non-positive. What mathematical property guarantees this?"
  type: multiple-choice
  options:
    - "Diminishing marginal utility, which implies consumers always prefer variety"
    - "The concavity of the expenditure function, which makes the Slutsky matrix negative semidefinite"
    - "The strict convexity of indifference curves, which guarantees interior solutions"
    - "The symmetry of the Slutsky matrix, combined with the assumption that goods are substitutes"
  answer: 1
  explanation: "The expenditure function e(p, u) is concave in prices — its Hessian (the Slutsky matrix S with entries ∂²e/∂pᵢ∂pⱼ = ∂hᵢ/∂pⱼ) is negative semidefinite. A negative semidefinite matrix has non-positive diagonal entries, so ∂hᵢ/∂pᵢ ≤ 0 always. This is a mathematical consequence of constrained expenditure minimization, not an assumption about preferences per se. Diminishing marginal utility (option A) is neither necessary nor sufficient for this result."

- question: "For a normal good, the substitution and income effects work in opposite directions when its own price rises — the substitution effect reduces demand while the income effect increases it."
  type: true-false
  answer: false
  explanation: "For a *normal* good, both effects push in the same direction. The substitution effect (always non-positive) reduces compensated demand when own-price rises. The income effect: a price rise reduces real income, and for a normal good (∂xᵢ/∂m > 0), lower income reduces demand further. So both channels reduce quantity demanded — this is why normal goods reliably obey the law of demand. It is *inferior* goods where the effects oppose each other."

- question: "The substitution effect in the Slutsky equation is always non-positive for own-price changes, regardless of whether the good is normal, inferior, or Giffen."
  type: true-false
  answer: true
  explanation: "This is exactly right. The sign of the substitution effect (∂hᵢ/∂pᵢ) is determined by the negative semidefiniteness of the Slutsky matrix — a property of the expenditure function's mathematical structure. It holds for all goods regardless of income effects. What distinguishes normal, inferior, and Giffen goods is the *income* effect. A Giffen good's demand slopes upward not because the substitution effect flips, but because a large, positive income effect (inferior good with large budget share) overwhelms the always-negative substitution effect."

- question: "Explain why a Giffen good's demand curve slopes upward, using the substitution and income effects from the Slutsky decomposition."
  type: short-answer
  answer: "For a Giffen good, the income effect dominates and works in the opposite direction from the substitution effect. When price rises: the substitution effect (always negative) reduces compensated demand. But because the good is inferior (∂xᵢ/∂m < 0) and consumes a large share of the budget, the effective income loss is large — and for an inferior good, lower real income *increases* consumption. If this income effect exceeds the substitution effect in magnitude, total demand rises with price. A Giffen good requires two conditions: it must be inferior, and the consumer must spend enough on it that the real-income effect is large."
  explanation: "The Slutsky equation makes this precise: ∂xᵢ/∂pᵢ = ∂hᵢ/∂pᵢ − xᵢ·(∂xᵢ/∂m). For a Giffen good, the second term is positive (inferior good: ∂xᵢ/∂m < 0, so the negative of a negative times xᵢ > 0 is positive), and it exceeds the magnitude of the first term (which is always ≤ 0). Classic examples include staple foods like bread or potatoes for very poor consumers."
```

## Explainer

When you studied income and substitution effects, you learned that a price change does two things at once: it changes the relative price of goods (making one cheaper or more expensive compared to alternatives) and it changes the consumer's real purchasing power. The Slutsky equation takes this intuition and gives it precise mathematical form, allowing you to separate these two channels exactly.

The equation is written as ∂xᵢ/∂pⱼ = ∂hᵢ/∂pⱼ − xⱼ · (∂xᵢ/∂m), where xᵢ is the **Marshallian (ordinary) demand** for good i, hᵢ is the **Hicksian (compensated) demand**, and m is income. The first term on the right is the **substitution effect** — how demand changes when the price changes but utility is held constant. Because the compensated demand holds the consumer on the same indifference curve, this term isolates pure relative-price responses. From your work with partial derivatives, you can see that each term is a partial derivative holding different things constant: Marshallian demand holds income constant, while Hicksian demand holds utility constant.

The second term, −xⱼ · (∂xᵢ/∂m), is the **income effect**. When the price of good j rises, a consumer who was buying xⱼ units of it effectively loses xⱼ · Δpⱼ in purchasing power. The factor ∂xᵢ/∂m tells you how demand for good i responds to income changes. The negative sign appears because a price increase reduces real income. For a **normal good** (∂xᵢ/∂m > 0), the income effect reinforces the substitution effect — both push demand down when price rises. For an **inferior good**, the income effect works against the substitution effect, and in the extreme case of a **Giffen good**, the income effect dominates, producing upward-sloping demand.

The substitution effect is always negative for own-price changes (∂hᵢ/∂pᵢ ≤ 0) — this is guaranteed by the concavity of the expenditure function, which you can verify using the second-order conditions from your optimization background. This means the substitution effect always pushes demand in the "intuitive" direction: higher price, less quantity. The law of demand can only be violated when the income effect is large enough and works in the opposite direction, which requires the good to be inferior and to consume a large share of the budget.

The Slutsky equation also has a matrix form — the **Slutsky matrix** S with entries sᵢⱼ = ∂hᵢ/∂pⱼ is symmetric and negative semidefinite. Symmetry means that the compensated cross-price effect of good j on good i equals the effect of good i on good j. These properties come directly from the structure of constrained optimization and connect consumer theory to the mathematical properties you studied in linear algebra. The matrix form becomes essential when you move to revealed preference theory, where you test whether observed demand data is consistent with utility maximization by checking whether the implied Slutsky matrix satisfies these conditions.
