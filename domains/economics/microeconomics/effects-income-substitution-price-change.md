---
id: effects-income-substitution-price-change
title: Income and Substitution Effects of Price Changes
domain: economics
course: microeconomics
prerequisites:
- id: consumer-equilibrium-optimality
  type: hard
- id: income-and-substitution-effects
  type: soft
builds-toward:
- demand-curve-derivation
tags:
- price-change
- income-effect
- substitution-effect
- decomposition
stage: formal-systems
status: validated
---

# Income and Substitution Effects of Price Changes

## Core Idea
When a good's price changes, the total effect on quantity demanded can be decomposed into two components: the substitution effect (the change in quantity due to the good becoming relatively more or less expensive, holding utility constant) and the income effect (the change in quantity due to the change in purchasing power). The substitution effect always moves in the opposite direction to the price change, while the income effect's direction depends on whether the good is normal or inferior.

## Questions

```yaml
- question: "When the price of an inferior good falls, which of the following correctly describes the two effects?"
  type: multiple-choice
  options:
    - "Both the substitution and income effects increase quantity demanded"
    - "The substitution effect increases quantity demanded; the income effect decreases it"
    - "The substitution effect decreases quantity demanded; the income effect increases it"
    - "Both the substitution and income effects decrease quantity demanded"
  answer: 1
  explanation: "The substitution effect always moves opposite to the price change — a price fall makes the good relatively cheaper, so consumers substitute toward it, increasing quantity demanded. But a price fall also raises real purchasing power. For an inferior good, feeling richer leads consumers to buy less of it (they prefer something better). So the income effect pulls in the opposite direction from the substitution effect. For a normal good, both effects would reinforce each other."

- question: "A student explains that when coffee's price falls, they buy more because 'holding utility constant, coffee is now relatively cheaper than tea.' This explanation captures:"
  type: multiple-choice
  options:
    - "The total effect of the price change"
    - "Only the income effect"
    - "Only the substitution effect"
    - "Neither effect — relative price changes are not relevant to consumer choice"
  answer: 2
  explanation: "The substitution effect is defined as the change in quantity demanded when real welfare is held constant but the consumer faces the new relative prices. 'Holding utility constant, coffee is now relatively cheaper than tea' describes exactly this: no change in wellbeing, but a rearrangement driven by changed relative prices. The income effect is the separate component that asks: how does behavior change because real purchasing power has changed?"

- question: "The substitution effect can push quantity demanded in either direction depending on whether a good is normal or inferior."
  type: true-false
  answer: false
  explanation: "The substitution effect always moves opposite to the price change, regardless of whether the good is normal or inferior. When price falls, the substitution effect always increases quantity demanded; when price rises, the substitution effect always decreases it. It is the income effect whose direction depends on good type — positive for normal goods, negative for inferior goods."

- question: "A Giffen good is a special case of an inferior good where the income effect is strong enough to overwhelm the substitution effect."
  type: true-false
  answer: true
  explanation: "Correct. For a Giffen good, the price rise reduces real purchasing power (income effect), and because the good is strongly inferior, this causes the consumer to buy more of it — enough to outweigh the always-present substitution effect pushing in the opposite direction. The result is a demand curve that slopes upward: quantity demanded rises when price rises. Giffen goods are theoretically possible but extremely rare in practice."

- question: "Explain why the substitution effect always moves in the opposite direction from a price change, regardless of whether the good is normal or inferior."
  type: short-answer
  answer: "The substitution effect is defined as the behavioral change when real utility is held constant but relative prices shift. When a good's price falls, it becomes cheaper relative to all other goods. Even if you were somehow kept at the same level of well-being, you would rearrange your consumption to buy more of the now-cheaper good and less of relatively more expensive alternatives. This logic holds regardless of income level or good type — it is purely a response to the change in relative prices."
  explanation: "The key is the definition: the substitution effect is isolated by asking 'what would you do if prices changed but your utility level stayed the same?' Relative price changes always create an incentive to substitute toward the cheaper good and away from relatively more expensive goods. The normal/inferior distinction only matters for the income effect — which asks what happens when real purchasing power changes."
```

## Explainer

When a good's price falls, you buy more of it. That much is obvious from the demand curve. But *why* you buy more turns out to matter economically — there are two distinct mechanisms at work, and they can pull in opposite directions. From your study of consumer equilibrium, you know the consumer maximizes utility subject to a budget constraint. A price change rotates the budget line outward (for a price decrease), moving the consumer to a new optimal bundle. The decomposition asks: how much of that move is about changing relative prices, and how much is about the change in real purchasing power?

The **substitution effect** answers: how would your behavior change if you kept your real welfare constant but faced the new relative prices? When coffee's price falls relative to tea, you would substitute toward coffee even if your utility stayed exactly the same. This effect always moves opposite to the price change — when price falls, the substitution effect always increases quantity demanded, without exception. Geometrically, it is the movement along your original indifference curve to the point where the slope (the marginal rate of substitution) matches the new price ratio. It is a pure response to relative price signals, holding real well-being fixed.

The **income effect** captures the remaining piece: the change in behavior due to the change in real purchasing power. When coffee's price falls, your money buys more than before — you are effectively richer. For a **normal good**, this improvement in real income leads you to buy more of it, reinforcing the substitution effect. Both effects push in the same direction, making the law of demand especially robust for normal goods. For an **inferior good** (like instant noodles if you'd prefer something better), feeling richer makes you buy *less* of it — the income effect works against the substitution effect.

The decomposition has real consequences at the extremes. For most goods, the substitution effect dominates and we get the familiar downward-sloping demand. But for strongly inferior goods with large income effects, the two components can nearly cancel. In the theoretical limiting case — a **Giffen good** — the income effect for an inferior good is powerful enough to completely overwhelm the substitution effect, producing a demand curve that slopes upward: quantity demanded rises when price rises. Confirmed Giffen goods are rare in practice, but the income-substitution decomposition explains *why* the law of demand is not an iron law for all goods, and what specific conditions would have to hold for it to fail.
