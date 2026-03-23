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
stage: expert
status: validated
---

# Hicksian (Compensated) Demand

## Core Idea
Compensated (Hicksian) demand curves show the quantity demanded as price varies while holding utility constant, unlike ordinary Marshallian demand which allows income effects. The compensated demand curve is always negatively sloped due to the substitution effect and forms the foundation of duality theory in consumer economics.

## Questions

```yaml
- question: "A good is a Giffen good: when its price rises, quantity demanded actually increases because the positive income effect (consumers feel poorer, so they buy more of this inferior staple) overwhelms the negative substitution effect. What does the Hicksian demand curve for this good look like?"
  type: multiple-choice
  options:
    - "Upward-sloping, because the good is a Giffen good and quantity demanded rises with price"
    - "Downward-sloping, because the Hicksian curve removes the income effect entirely and shows only the substitution effect, which is always negative regardless of good type"
    - "Upward-sloping, because holding utility constant requires the consumer to buy more when price rises to remain on the same indifference curve"
    - "Vertical, because for a Giffen good the substitution and income effects exactly offset, producing zero net response"
  answer: 1
  explanation: "This is the core theoretical point of Hicksian demand. The Marshallian demand curve for a Giffen good slopes upward because the income effect dominates. But the Hicksian curve strips away the income effect and shows only the substitution effect — which is always negative by definition (when price rises, the consumer substitutes away from the relatively more expensive good). The Slutsky matrix has a negative semidefinite substitution effect block, meaning the own-price substitution effect is always ≤ 0. Giffen behavior is an income-effect phenomenon, invisible in Hicksian demand."

- question: "A government imposes a large excise tax on cigarettes, nearly doubling the price. A health economist wants to calculate the exact welfare cost to consumers. She should:"
  type: multiple-choice
  options:
    - "Calculate the area under the Marshallian demand curve between the old and new price — this is the compensating variation by definition"
    - "Integrate under the Hicksian (compensated) demand curve between the old and new price — this gives the compensating variation, the theoretically exact welfare measure"
    - "Use only the expenditure function directly; no demand curve can give an exact welfare measure because they are approximations"
    - "Average the Marshallian consumer surplus loss and the Hicksian compensating variation to eliminate directional bias"
  answer: 1
  explanation: "The area under the Marshallian demand curve gives consumer surplus — which approximates, but does not exactly equal, the welfare change. The approximation error arises because Marshallian demand includes income effects, which distort the willingness-to-pay interpretation. The Hicksian curve, by holding utility constant, gives the exact compensating variation: the lump-sum income adjustment needed to restore the consumer to original utility after the price change. For large price changes on major expenditure categories like cigarettes, the difference between Marshallian surplus and Hicksian compensating variation can be substantial."

- question: "The Hicksian demand curve is always downward-sloping because it captures only the substitution effect, which is always non-positive — the consumer always substitutes away from a good that has become relatively more expensive."
  type: true-false
  answer: true
  explanation: "This follows directly from the theory of consumer choice and the Slutsky equation. The own-price substitution effect, ∂h_i/∂p_i (where h is Hicksian demand), is guaranteed to be non-positive by the second-order conditions of expenditure minimization — equivalently, by the negative semidefiniteness of the Slutsky matrix. Unlike Marshallian demand, which can exhibit Giffen behavior when income effects dominate, Hicksian demand has an unambiguous sign. This is one reason Hicksian demand is a cleaner theoretical object for welfare and comparative statics analysis."

- question: "For a normal good, the Hicksian demand curve is flatter (more elastic) than the Marshallian demand curve, because holding utility constant amplifies the consumer's price response."
  type: true-false
  answer: false
  explanation: "For a normal good, the Hicksian curve is steeper (less elastic) than the Marshallian curve. Here is why: when price falls, the Marshallian consumer gets both a substitution effect (buys more because it's cheaper) and a positive income effect (feels richer, buys even more of the normal good). These two effects reinforce each other, making Marshallian demand more elastic. The Hicksian curve removes the income effect, leaving only the smaller substitution effect — so the quantity response is smaller at each price, making the Hicksian curve steeper. The relationship reverses for inferior goods."

- question: "What is the fundamental difference between Marshallian and Hicksian demand, and why does this make Hicksian demand the theoretically correct tool for welfare analysis?"
  type: short-answer
  answer: "Marshallian demand holds income constant as price varies, so both the substitution effect and the income effect are present. Hicksian demand holds utility constant (compensating the consumer's income at each price to keep them on the same indifference curve), so only the substitution effect remains. For welfare analysis, what matters is how the consumer's utility changes — the income effect contaminates the Marshallian measure by conflating real price-responsiveness with purchasing-power effects. Integrating under the Hicksian curve gives the compensating variation, the exact income adjustment needed to restore original utility, which is the correct welfare metric."
  explanation: "The practical implication: for small price changes on goods that are a small share of the budget, Marshallian consumer surplus and Hicksian compensating variation are nearly identical (the income effect is small). For large price changes on necessities like housing, healthcare, or food — where income effects are large — the two measures diverge significantly. Using Marshallian surplus to evaluate housing subsidy programs, for instance, can substantially overstate consumer welfare gains."
```

## Explainer

From the Slutsky equation, you already know that the total effect of a price change on quantity demanded can be decomposed into a **substitution effect** (holding utility constant) and an **income effect** (the change in purchasing power). The Hicksian, or **compensated demand curve**, isolates just the substitution effect by asking: how does quantity demanded change with price if we simultaneously adjust the consumer's income to keep them on the *same indifference curve*? This "compensation" strips away the income effect and reveals the pure price-responsiveness of demand.

To visualize this, start with an indifference curve map you already know how to read. When the price of good X falls, the budget line pivots outward, and the consumer moves to a new, higher indifference curve. The Marshallian demand curve records this full move — both the substitution toward the now-cheaper good and the real income gain. The Hicksian demand curve instead imagines sliding the budget line back inward (reducing income) just enough to return the consumer to the *original* indifference curve, then reading off the quantity demanded at the new price ratio. The consumer substitutes toward the cheaper good but is no richer. This is equivalent to asking: "How would this price change affect your choices if I simultaneously taxed away your windfall?"

The critical property of the Hicksian demand curve is that it is **always downward-sloping**. This follows directly from the Slutsky equation: the substitution effect is always negative (when price rises, the consumer substitutes away from the good), regardless of whether the good is normal or inferior. The Marshallian demand curve can, in theory, slope upward for a Giffen good — where the income effect for an inferior good is so large that it overwhelms the substitution effect. The Hicksian curve cannot exhibit this behavior because it has removed the income effect entirely. This makes compensated demand a cleaner theoretical object for welfare analysis, since its slope has an unambiguous sign.

The practical importance of Hicksian demand is in measuring welfare. When economists calculate **compensating variation** — the amount of money needed to restore a consumer to their original utility after a price change — they are integrating under the Hicksian demand curve. The area between the old and new price under the Marshallian curve gives consumer surplus, which is only an approximation of true welfare change (because income effects distort it). The Hicksian curve gives the exact welfare measure. For small price changes or goods that are a small share of the budget, the two curves are nearly identical. For large price changes on major expenditure categories — housing, healthcare — the distinction matters and the Hicksian measure is theoretically correct.

Hicksian demand also connects to **duality theory**, which you will explore further. The expenditure function — the minimum spending needed to reach a given utility level at given prices — is the "dual" of the indirect utility function. Hicksian demand curves are the partial derivatives of the expenditure function with respect to prices (by Shephard's lemma). This duality means that everything you can learn from utility maximization, you can equivalently learn from expenditure minimization, and the Hicksian demand curve is the bridge between the two perspectives.
