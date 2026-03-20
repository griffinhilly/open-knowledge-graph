---
id: income-and-substitution-effects
title: Income and Substitution Effects
domain: economics
course: microeconomics
prerequisites:
- id: consumer-optimum
  type: hard
- id: income-and-cross-price-elasticity
  type: soft
builds-toward:
- demand-curve-derivation
tags:
- income effect
- substitution effect
- Slutsky decomposition
- Giffen goods
stage: formal-systems
status: validated
---

# Income and Substitution Effects

## Core Idea
When a good's price changes, the total effect on demand decomposes into two parts. The substitution effect is always negative (goods become relatively cheaper → consumers substitute toward them), reflecting movement along an indifference curve. The income effect reflects the change in real purchasing power; it is negative for normal goods and positive for inferior goods. For a Giffen good, the income effect is so strongly positive that the demand curve slopes upward — a theoretical curiosity that rarely occurs in practice.

## How It's Best Learned
Use the Slutsky decomposition graphically: draw the original optimum, the compensated budget line (rotated to new price ratio, shifted back to original indifference curve), and the final optimum. Distinguish the two steps clearly before moving to algebra.

## Common Misconceptions
- Students often forget that the substitution effect is always negative for a price increase; the sign of the total effect depends on the income effect.
- Giffen goods are real but extremely rare — the logic requires a strongly inferior good that consumes a large share of budget.

## Questions

```yaml
- question: "A very poor household spends most of its income on a staple food (potatoes). The price of potatoes falls significantly. According to the income and substitution effects framework, which outcome is theoretically possible?"
  type: multiple-choice
  options:
    - "The household definitely buys more potatoes — the substitution effect always dominates"
    - "The household buys less potatoes — the real income gain allows them to afford better food, and the income effect outweighs the substitution effect"
    - "The household buys exactly the same amount — the two effects always cancel for staple foods"
    - "The income effect cannot apply to goods that take up a large budget share"
  answer: 1
  explanation: "This is the Giffen good scenario. When a staple consumes a large share of income, a price drop generates a substantial real income gain. For an inferior good (one consumers buy less of as they grow richer), this income gain causes them to shift toward preferred foods. If the income effect is large enough to outweigh the substitution effect (which always points toward buying more), quantity demanded of potatoes actually falls. This gives an upward-sloping demand curve — unusual but logically coherent once you decompose the effects."

- question: "The substitution effect of a price decrease is:"
  type: multiple-choice
  options:
    - "Always positive (more quantity demanded), regardless of whether the good is normal or inferior"
    - "Positive for normal goods, negative for inferior goods"
    - "Zero for inferior goods — substitution only applies to normal goods"
    - "Determined by the direction of the income effect for that good"
  answer: 0
  explanation: "The substitution effect is always unambiguous in sign: when price falls, the good is relatively cheaper than alternatives, so consumers substitute toward it — regardless of whether it is normal or inferior. The substitution effect measures movement along a single indifference curve (holding utility constant), reflecting pure relative price changes. It is the income effect whose sign varies: positive for normal goods (more consumption as real income rises), negative for inferior goods (less consumption as real income rises)."

- question: "The substitution effect always causes quantity demanded to move in the opposite direction of a price change — when price rises, the substitution effect alone reduces quantity demanded."
  type: true-false
  answer: true
  explanation: "The substitution effect captures the pure relative price response: when a good becomes relatively more expensive than alternatives, consumers substitute away from it, holding utility constant. This is always negative for a price increase, always positive for a price decrease. There are no exceptions. The total effect on quantity demanded may be ambiguous (for inferior goods) because the income effect can work in the opposite direction, but the substitution effect itself never changes sign."

- question: "For an inferior good whose price rises, both the income effect and the substitution effect cause quantity demanded to fall."
  type: true-false
  answer: false
  explanation: "When the price of an inferior good rises, the substitution effect causes quantity demanded to fall (the good is relatively more expensive). But the income effect works in the opposite direction: the price increase reduces real income, and for an inferior good, lower real income means consumers buy *more* of it (they substitute toward it when they're poorer). The two effects work against each other. If the income effect is strong enough, it can dominate — producing a Giffen good with an upward-sloping demand curve."

- question: "Explain, in your own words, why a Giffen good has an upward-sloping demand curve. What must be true about the income and substitution effects for this to occur?"
  type: short-answer
  answer: "A Giffen good has an upward-sloping demand curve because when its price falls, the income effect (which is positive for this inferior good — real income rises, so less of the inferior good is consumed) outweighs the substitution effect (which always pushes toward more consumption when price falls). The net effect is less quantity demanded at a lower price. For this to occur, the good must be inferior and must constitute a large enough share of the consumer's budget that a price change produces a substantial real income effect."
  explanation: "The Slutsky decomposition reveals that every price change has two components operating simultaneously. The substitution effect always obeys the law of demand. The income effect depends on whether the good is normal or inferior. For a Giffen good, the income effect is so large and negative (inferior good + large budget share) that it reverses the law of demand. The upward slope is not a violation of rationality — it is the correct prediction of the model when the two effects are decomposed correctly."
```

## Explainer

When the price of a good falls, two distinct forces pull on your demand simultaneously, and they can reinforce each other or work against each other. Understanding why requires decomposing the total price effect into two conceptually separate pieces — each driven by different economic logic.

The first piece is the **substitution effect**. Imagine you are compensated after the price falls — just enough income removed so that you end up exactly as well-off as before. You're on the same indifference curve from your consumer optimum work, but facing new relative prices. Because good 1 is now relatively cheaper, you substitute toward it even at the same utility level. This effect is always unambiguous in sign: a price decrease always increases quantity demanded via the substitution effect, a price increase always decreases it. The substitution effect follows the law of demand by construction, reflecting movement along a single indifference curve.

The second piece is the **income effect**. When the price of a good you buy falls, your real purchasing power rises — you can afford bundles that were previously out of reach. This is equivalent to receiving a bonus income increase. For a **normal good**, higher real income means you want more of it, so the income effect reinforces the substitution effect. For an **inferior good**, higher real income causes you to buy less — you shift away from it as you become richer in real terms. The income effect now works against the substitution effect.

The **Slutsky decomposition** is the graphical technique that separates these effects precisely. Start at the original optimum A. Rotate the budget line to the new price ratio and simultaneously adjust income so you can just barely afford your original bundle — this creates the compensated budget line. Its intersection with the original indifference curve is point B. The move from A to B is purely the substitution effect. Now restore the consumer's actual (uncompensated) new budget line — they're richer in real terms — and find the final optimum C. The move from B to C is the income effect. Total effect = substitution + income.

For most goods, both effects point the same direction and you get a normal downward-sloping demand curve. The rare **Giffen good** is the exception: an inferior good where the income effect is so large and negative that it completely swamps the substitution effect. The canonical example is a staple food consuming a large fraction of a poor household's budget — when its price falls, the real income gain is so large that the household shifts consumption toward preferred foods and actually buys less of the staple. The demand curve slopes upward, not as a theoretical curiosity but as a logical consequence of decomposing the effects correctly.
