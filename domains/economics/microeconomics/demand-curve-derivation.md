---
id: demand-curve-derivation
title: Deriving the Demand Curve
domain: economics
course: microeconomics
prerequisites:
- id: consumer-optimum
  type: hard
- id: income-and-substitution-effects
  type: soft
builds-toward: []
tags:
- demand derivation
- price-consumption curve
- individual demand
- market demand
stage: formal-systems
status: validated
---
# Deriving the Demand Curve

## Core Idea
An individual's demand curve is derived by tracing out the consumer's optimum as the price of one good varies while income and other prices are held constant. As price varies, the budget line rotates and the optimal bundle changes, tracing a price-consumption curve; projecting these optima onto a price-quantity diagram yields the demand curve. Market demand is the horizontal summation of all individual demand curves. This derivation connects the deep theory of consumer choice to the observable demand curves used in market analysis.

## How It's Best Learned
Derive the demand curve step-by-step using a specific utility function (e.g., Cobb-Douglas), varying price numerically and plotting the resulting optima. This makes the derivation concrete before the graphical exposition.

## Common Misconceptions
- Market demand aggregation is horizontal (summing quantities at each price), not vertical.
- Students sometimes mix up shifts of the demand curve (income or other-price changes) with movements along it (own-price changes) when applying this derivation.

## Questions

```yaml
- question: "A consumer's price-consumption curve for good X shows the optimal bundles as the price of X falls from $10 to $5 to $2. How is the individual demand curve for X constructed from this information?"
  type: multiple-choice
  options:
    - "By averaging the quantities consumed across all three price levels to find a representative demand"
    - "By plotting each (price, optimal quantity of X) pair from the price-consumption curve on a separate price-quantity graph"
    - "By connecting the endpoints of the budget lines at each price level"
    - "By computing the slope of the indifference curves at each optimal bundle"
  answer: 1
  explanation: "The demand curve is constructed by projecting the price-consumption curve into price-quantity space: for each price level, you read off the optimal quantity of X from the tangency point and plot (price, quantity) on a new graph. This is the formal derivation — the demand curve is not assumed or estimated; it is generated directly from the consumer's preferences (indifference map) and income. Each point on the demand curve corresponds to one tangency on the indifference map."

- question: "At a price of $8, Consumer A demands 3 units and Consumer B demands 5 units. What is market demand at $8?"
  type: multiple-choice
  options:
    - "4 units — market demand is the average of individual demands"
    - "8 units — market demand is the sum of all individual demands at that price"
    - "3 units — market demand equals the minimum individual demand to reflect scarcity constraints"
    - "5 units — market demand equals the median consumer's demand"
  answer: 1
  explanation: "Market demand is the horizontal summation of individual demand curves: at each price, you add up the quantities demanded by all consumers. Here, 3 + 5 = 8 units. This is horizontal (summing quantities at a given price), not vertical (averaging prices for a given quantity). The averaging misconception is very common but wrong — it would undercount total market demand and misrepresent the aggregate willingness to purchase."

- question: "Market demand at any given price is found by averaging individual consumers' demanded quantities at that price."
  type: true-false
  answer: false
  explanation: "Market demand is the horizontal *sum* of individual demands, not the average. At any price p, market demand equals the total quantity all consumers want to buy: Q_market = Q_1 + Q_2 + ... + Q_n. Averaging would give the 'typical consumer's' demand, not the market total. This distinction matters enormously in practice — a market with 1,000 consumers each demanding 2 units has a market demand of 2,000, not 2."

- question: "A rise in consumer income shifts the demand curve for a normal good rightward because it changes the optimal budget-line tangency at every price, not just one."
  type: true-false
  answer: true
  explanation: "This is exactly right, and it connects the graphical rule (income shifts the curve) to the underlying mechanics. An income increase expands the budget line outward at every price level. For each price, the new budget line generates a new tangency point, yielding a higher optimal quantity of X. When you project all these new optima into price-quantity space, every point on the demand curve shifts to the right. This is why income is a curve-shifter rather than a movement along the existing curve — it changes the price-consumption path itself."

- question: "Why is the market demand curve typically flatter (more price-elastic) than an individual consumer's demand curve?"
  type: short-answer
  answer: "Because market demand aggregates consumers with widely differing reservation prices. As price falls slightly, some consumers who were just barely priced out now enter the market — each small price reduction brings in many marginal buyers who were near their reservation price. Individual demand curves reflect one person's preferences; the market curve pools all those heterogeneous preferences. The more diverse the consumer population, the more buyers are waiting just below any price threshold, making the aggregate response to price changes larger."
  explanation: "This is why horizontal summation matters conceptually, not just mechanically. The market demand curve is flatter partly because it includes more consumers at lower prices (extensive margin) and partly because existing consumers buy more (intensive margin). In empirical work, market-level price elasticities are often larger in absolute value than individual-level elasticities, which has direct implications for pricing policy and welfare calculations."
```

## Explainer

You already know from the consumer optimum that a rational consumer picks the bundle where a **budget line** is tangent to an **indifference curve** — the point where the marginal rate of substitution equals the price ratio. Deriving the demand curve is simply asking: what happens to that optimal choice as the price of one good changes, holding income and the other price fixed?

When the price of good X falls, the budget line rotates outward along the X-axis (you can now afford more X than before). Each new price generates a new budget line, a new tangency point, and a new optimal quantity of X. Connect those optimal points in the budget-line space and you trace the **price-consumption curve** — a path through consumption space showing how the bundle evolves as price changes. Now take each price and its corresponding optimal X quantity and plot them on a separate diagram with price on the vertical axis and quantity on the horizontal. The result is the individual **demand curve** for good X.

This construction reveals something important: the demand curve is not a freestanding behavioral rule — it is a derived object, entirely determined by the consumer's preferences (indifference map) and income. Changing income or the price of Y does not move you along this demand curve; it shifts it, because the entire price-consumption curve shifts. This is why the distinction between "change in quantity demanded" (movement along the curve as X's price changes) and "change in demand" (shift of the curve as income or other prices change) maps directly onto the indifference-curve mechanics.

**Market demand** aggregates these individual curves horizontally. At any given price, each consumer has a desired quantity; market demand at that price is the sum of all those quantities. If Consumer A demands 4 units and Consumer B demands 6 units at a price of $5, market demand at $5 is 10 units — not the average, not the vertical sum, but the horizontal sum at every price. As new consumers enter the market, the demand curve shifts rightward; as consumers exit, it shifts left. This horizontal aggregation is why market demand curves tend to be flatter (more elastic) than individual curves: the market can draw on many consumers whose reservation prices differ, so a small price reduction brings in many marginal buyers spread across the population.
