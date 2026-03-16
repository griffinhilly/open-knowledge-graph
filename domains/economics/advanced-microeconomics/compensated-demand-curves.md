---
id: compensated-demand-curves
title: Hicksian (Compensated) Demand
domain: economics
course: advanced-microeconomics
prerequisites:
- id: slutsky-equation
  type: hard
- id: indifference-curves
  type: hard
builds-toward:
- expenditure-function-duality
tags:
- consumer-theory
- demand
- utility
stage: advanced
status: draft
---

# Hicksian (Compensated) Demand

## Core Idea
Compensated (Hicksian) demand curves show the quantity demanded as price varies while holding utility constant, unlike ordinary Marshallian demand which allows income effects. The compensated demand curve is always negatively sloped due to the substitution effect and forms the foundation of duality theory in consumer economics.

## Explainer

From the Slutsky equation, you already know that the total effect of a price change on quantity demanded can be decomposed into a **substitution effect** (holding utility constant) and an **income effect** (the change in purchasing power). The Hicksian, or **compensated demand curve**, isolates just the substitution effect by asking: how does quantity demanded change with price if we simultaneously adjust the consumer's income to keep them on the *same indifference curve*? This "compensation" strips away the income effect and reveals the pure price-responsiveness of demand.

To visualize this, start with an indifference curve map you already know how to read. When the price of good X falls, the budget line pivots outward, and the consumer moves to a new, higher indifference curve. The Marshallian demand curve records this full move — both the substitution toward the now-cheaper good and the real income gain. The Hicksian demand curve instead imagines sliding the budget line back inward (reducing income) just enough to return the consumer to the *original* indifference curve, then reading off the quantity demanded at the new price ratio. The consumer substitutes toward the cheaper good but is no richer. This is equivalent to asking: "How would this price change affect your choices if I simultaneously taxed away your windfall?"

The critical property of the Hicksian demand curve is that it is **always downward-sloping**. This follows directly from the Slutsky equation: the substitution effect is always negative (when price rises, the consumer substitutes away from the good), regardless of whether the good is normal or inferior. The Marshallian demand curve can, in theory, slope upward for a Giffen good — where the income effect for an inferior good is so large that it overwhelms the substitution effect. The Hicksian curve cannot exhibit this behavior because it has removed the income effect entirely. This makes compensated demand a cleaner theoretical object for welfare analysis, since its slope has an unambiguous sign.

The practical importance of Hicksian demand is in measuring welfare. When economists calculate **compensating variation** — the amount of money needed to restore a consumer to their original utility after a price change — they are integrating under the Hicksian demand curve. The area between the old and new price under the Marshallian curve gives consumer surplus, which is only an approximation of true welfare change (because income effects distort it). The Hicksian curve gives the exact welfare measure. For small price changes or goods that are a small share of the budget, the two curves are nearly identical. For large price changes on major expenditure categories — housing, healthcare — the distinction matters and the Hicksian measure is theoretically correct.

Hicksian demand also connects to **duality theory**, which you will explore further. The expenditure function — the minimum spending needed to reach a given utility level at given prices — is the "dual" of the indirect utility function. Hicksian demand curves are the partial derivatives of the expenditure function with respect to prices (by Shephard's lemma). This duality means that everything you can learn from utility maximization, you can equivalently learn from expenditure minimization, and the Hicksian demand curve is the bridge between the two perspectives.
