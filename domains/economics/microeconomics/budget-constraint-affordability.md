---
id: budget-constraint-affordability
title: Budget Constraint and Purchasing Power
domain: economics
course: microeconomics
prerequisites: []
builds-toward:
- consumer-equilibrium-optimality
- effects-income-substitution-price-change
tags:
- budget-constraint
- income
- prices
- affordability
stage: formal-systems
status: validated
---

# Budget Constraint and Purchasing Power

## Core Idea
The budget constraint represents all consumption bundles a consumer can afford given their income and the prices of goods. Expressed as I = P₁Q₁ + P₂Q₂ (for two goods), it defines the feasible set of purchases. Changes in income shift the budget line outward or inward, while price changes rotate it. The budget constraint limits the consumer's choices and forces trade-offs between goods.

## How It's Best Learned
Graph budget constraints for different income and price scenarios. Use the intercepts (maximum quantity of each good if all income is spent on that good) to understand the budget line's position.

## Common Misconceptions
- Thinking the budget constraint is always binding—consumers need not spend all their income.
- Assuming price and income changes have symmetric effects—a price increase rotates the budget line differently than an income increase.

## Questions

```yaml
- question: "The price of coffee (good 1) rises while the price of tea (good 2) and consumer income remain unchanged. What happens to the budget constraint?"
  type: multiple-choice
  options:
    - "The line rotates inward — the coffee-axis intercept falls, but the tea-axis intercept is unchanged"
    - "The line shifts inward in parallel — all bundles of coffee and tea become less affordable"
    - "The line rotates outward — consumers substitute toward tea, expanding the feasible set"
    - "The slope becomes shallower — coffee is now relatively more expensive than tea"
  answer: 0
  explanation: "A price change for one good rotates the budget line around the intercept of the unchanged good. If P₁ (coffee) rises, the maximum coffee affordable (I/P₁) falls, so that intercept moves inward. But since P₂ and I are unchanged, the tea intercept (I/P₂) stays fixed — the line pivots. A parallel inward shift (option B) would require income to fall or both prices to rise proportionally. This geometric distinction between rotation and parallel shift is the key insight of this topic. Note also that option D gets the direction wrong: if coffee becomes more expensive, the slope −P₁/P₂ becomes steeper in magnitude, not shallower."

- question: "Consumer income doubles while all prices remain unchanged. What is the effect on the budget constraint?"
  type: multiple-choice
  options:
    - "The line shifts outward parallel to its original position — the slope is unchanged because relative prices have not changed"
    - "The line rotates outward — higher income raises purchasing power of good 1 more than good 2"
    - "The slope steepens — doubling income changes the relative price ratio"
    - "Both intercepts double but the slope also changes to reflect higher purchasing power"
  answer: 0
  explanation: "Income affects both intercepts equally: if I doubles, both I/P₁ and I/P₂ double, shifting both intercepts out by the same factor. The slope (−P₁/P₂) is unchanged because neither price changed — only income. The result is a parallel outward shift. The slope encodes only relative prices; income determines how far out along the slope you can reach, not the slope itself. Options B–D incorrectly suggest that income changes the slope."

- question: "An increase in the price of good 1 and a decrease in income have the same effect on the budget constraint — both shift the line inward in parallel."
  type: true-false
  answer: false
  explanation: "This is the key asymmetry the topic is designed to teach. An income decrease shifts the line inward in parallel — both intercepts fall by the same proportion, so the slope is unchanged. A price increase for good 1 rotates the line inward around the good 2 intercept — only the good 1 intercept changes, so the slope changes. They both reduce affordability, but in geometrically distinct ways with different implications: income changes affect the feasible set uniformly, while price changes alter relative trade-offs."

- question: "The slope of the budget line represents the opportunity cost of good 1 in terms of good 2 — how many units of good 2 must be given up to buy one more unit of good 1."
  type: true-false
  answer: true
  explanation: "The slope is −P₁/P₂, the relative price ratio. If good 1 costs $4 and good 2 costs $2, the slope is −2: buying one more unit of good 1 requires forgoing 2 units of good 2. This is exactly the opportunity cost of good 1 expressed in units of good 2. The slope thus encodes the market's forced trade-off independently of income — which is why a price change alters the slope and an income change does not."

- question: "Explain why a price increase for one good rotates the budget line rather than shifting it in parallel. What does this rotation convey that a parallel shift would not?"
  type: short-answer
  answer: "When only P₁ rises, the maximum quantity of good 1 affordable (I/P₁) falls, but the maximum of good 2 (I/P₂) is unchanged — so only one intercept moves, producing a rotation around the good 2 intercept. A parallel shift would move both intercepts equally, which happens when income changes. The rotation conveys that relative prices have changed: good 1 is now more expensive relative to good 2. The slope steepens, meaning the opportunity cost of good 1 in terms of good 2 has increased. A parallel shift preserves relative prices; a rotation does not."
  explanation: "The geometric distinction between rotation and parallel shift encodes an economically meaningful difference. After a parallel shift from an income change, the consumer faces the same relative trade-offs at a different scale. After a rotation from a price change, the trade-offs themselves have changed — the consumer must give up more of good 2 per unit of good 1. This difference matters for consumer behavior: pure income changes produce income effects; price changes produce both income and substitution effects."
```

## Explainer

The budget constraint maps the space of what a consumer can actually afford. With income I and two goods at prices P₁ and P₂, the equation I = P₁Q₁ + P₂Q₂ describes a line in quantity space — the **budget line**. Every point on the line exhausts the budget exactly; points inside are affordable but leave money unspent; points outside are unaffordable. The intercepts give you a useful anchor: if you spend everything on good 1, you can buy I/P₁ units; if you spend everything on good 2, you can buy I/P₂ units. The **slope** of the budget line is −P₁/P₂ — the **relative price ratio** — telling you how many units of good 2 you must give up to afford one more unit of good 1.

Two things can change the budget line, and they do so in distinct ways. A change in income shifts the line parallel: higher income shifts it outward (you can afford more of everything), lower income shifts it inward. The slope doesn't change because the relative prices haven't. A change in the price of one good **rotates** the line around the intercept of the unchanged good. If P₁ rises, the good 1 intercept falls (you can afford fewer units of good 1 with all your income), but the good 2 intercept is unchanged. This rotation is fundamentally different from a parallel shift — the geometry captures the asymmetry that the common misconception denies.

The budget constraint is the "can" side of consumer theory. It tells you what's feasible, not what the consumer will choose. You need preferences (the indifference curve framework) to answer the "will" question — that's where this topic leads. But before you can find the optimal bundle, you need to characterize the feasible set. Think of it like a monthly budget: knowing you have $2,000 available doesn't tell you how you'll split it between rent and food, but it does set a hard outer boundary on what combinations are even possible.

One important nuance: the budget constraint is not always binding. A consumer who spends less than their income chooses a point inside the budget set, not on the boundary. In standard consumer theory, we assume non-satiation — more is always preferred to less — which means consumers spend all their income and the constraint binds. This assumption is worth knowing explicitly because it's what drives the result that the optimal bundle lies on the budget line rather than in the interior of the budget set.
