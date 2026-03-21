---
id: price-consumption-curve-demand-derivation
title: Price Consumption Curve and Derivation of Demand
domain: economics
course: microeconomics
prerequisites:
- id: demand-curve-individual-consumer
  type: hard
- id: indifference-curves
  type: hard
builds-toward:
- income-and-substitution-effects
tags:
- demand-derivation
- price-change
- consumer-response
stage: formal-systems
status: draft
---

# Price Consumption Curve and Derivation of Demand

## Core Idea
The price consumption curve (or price expansion path) shows how a consumer's optimal bundle changes as the price of one good varies, holding income and the other good's price constant. By plotting the optimal quantity at each price, we derive the demand curve. This shows that demand curves come from utility maximization under constraints.

## How It's Best Learned
Rotate the budget line by changing the price of one good; find new optimum each time; plot the resulting price-quantity points to see the demand curve emerge.

## Questions

```yaml
- question: "As the price of coffee falls step by step, a consumer's optimal bundle traces the price consumption curve. What does plotting each (coffee price, optimal coffee quantity) pair on a separate graph produce?"
  type: multiple-choice
  options:
    - "The income expansion path for coffee"
    - "The consumer's individual demand curve for coffee"
    - "A single indifference curve for the consumer"
    - "The budget constraint at a fixed coffee price"
  answer: 1
  explanation: "Each point on the PCC tells you the optimal quantity of coffee at a specific price. Translating those (price, quantity) pairs into price-quantity space produces the demand curve. This derivation matters because it shows demand curves are not empirical approximations — they are the logical consequence of utility maximization under a budget constraint."

- question: "A consumer has L-shaped (Leontief) indifference curves — they always buy goods X and Y in a fixed 1:1 ratio. What does this imply about their demand curve for good X?"
  type: multiple-choice
  options:
    - "The demand curve is perfectly elastic — they are infinitely sensitive to price"
    - "The demand curve is perfectly inelastic — quantity demanded does not change with price"
    - "The demand curve slopes upward — lower prices mean they buy less X to maintain the ratio"
    - "The demand curve cannot be derived using the price consumption curve method"
  answer: 1
  explanation: "L-shaped indifference curves mean the consumer always consumes X and Y in a fixed ratio regardless of relative prices. When the price of X falls, the budget line rotates but the optimal ratio doesn't change — only total spending adjusts. The quantity of X consumed stays constant: perfectly inelastic demand. The preference geometry directly determines demand curve shape."

- question: "The shape of a consumer's demand curve reflects the shape of their underlying indifference curves."
  type: true-false
  answer: true
  explanation: "The demand curve is derived directly from the price consumption curve, which traces optimal tangency points as price changes. Preferences determine indifference curve shapes, which determine where budget lines are tangent, which determines the PCC, which determines the demand curve. Elasticity reflects preference structure — perfect complements produce inelastic demand; easy substitutability produces elastic demand."

- question: "The price consumption curve is constructed by shifting the budget line parallel to its original position."
  type: true-false
  answer: false
  explanation: "A price change ROTATES the budget line, it does not shift it. If the price of good X falls, the X-axis intercept moves outward (the consumer can now buy more X with the same income) while the Y-axis intercept stays fixed. A parallel shift would reflect a change in income, not a price change. The PCC traces optimal bundles as the budget line rotates around the Y-axis intercept."

- question: "Why does deriving the demand curve from the price consumption curve reveal more than simply observing that people buy more when prices fall?"
  type: short-answer
  answer: "The PCC derivation shows the demand curve is the logical consequence of utility maximization under a budget constraint — not just an empirical pattern. It reveals WHY demand has the shape it does: the geometry of indifference curves (preference structure) determines elasticity. Perfect complements produce inelastic demand; highly substitutable goods produce elastic demand. The derivation also enables welfare analysis, connecting observed demand behavior to underlying utility, which is required for measuring consumer surplus and evaluating policy."
  explanation: "The theoretical grounding matters for policy. Knowing that demand curves emerge from optimization means you can predict how they change when income changes, when related prices change, or when preferences shift. A purely empirical description can only report past behavior; the utility-based derivation explains behavior and enables prediction across novel circumstances."
```

## Explainer

You already know two things: a consumer's budget line shows all affordable combinations of two goods, and an **indifference curve** shows all combinations that provide equal utility. The consumer's optimum is where the budget line is tangent to the highest reachable indifference curve. The **price consumption curve (PCC)** is what you get when you ask: if the price of one good changes, how does this optimal bundle change?

Start with a concrete setup: a consumer choosing between coffee (good X) and other goods (good Y), with fixed income. Lower the price of coffee. The budget line *rotates outward* on the coffee axis—coffee is cheaper, so the endpoint on the X-axis moves right while the maximum Y stays fixed. This rotation produces a new budget line tangent to a new, higher indifference curve at a new optimal bundle. Reduce the price again, find the new optimum, and again. Each optimal bundle is a point in (X, Y) space. Connecting all these points traces the **price consumption curve**—the path of optimal choices as the price of coffee varies continuously.

Deriving the **demand curve** is a direct translation. Each point on the PCC tells you the price of coffee and the optimal quantity of coffee at that price. Plot these (price, quantity) pairs on a separate graph with price on the vertical axis and quantity on the horizontal. The resulting curve *is* the demand curve. This derivation matters because it reveals that demand curves are not arbitrary—they are the observable consequence of utility maximization under a budget constraint. The shape of the demand curve reflects the shape of the underlying indifference curves.

The PCC also reveals how preference structure drives demand elasticity. If indifference curves are L-shaped (perfect complements, like left and right shoes), the consumer always buys the goods in fixed proportions regardless of price—the demand curve is inelastic. If the consumer readily substitutes coffee for other goods when its price rises (indifference curves with high curvature), the demand curve will be more elastic. The connection between the geometry of preferences and the slope of the demand curve is one of the deeper insights this construction provides.
