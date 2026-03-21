---
id: budget-constraint
title: Budget Constraint
domain: economics
course: microeconomics
prerequisites:
- id: consumer-theory-utility
  type: hard
- id: graphing-linear-equations
  type: soft
- id: slope-intercept-form
  type: soft
- id: marginal-utility-and-consumer-choice
  type: soft
builds-toward:
- consumer-optimum
- income-and-substitution-effects
tags:
- budget constraint
- budget line
- affordable set
- relative prices
stage: formal-systems
status: validated
---
# Budget Constraint

## Core Idea
The budget constraint defines the set of consumption bundles a consumer can afford given income (I) and prices (P_x, P_y): P_x·X + P_y·Y ≤ I. Graphically it is a straight line with slope −P_x/P_y, representing the relative price of the two goods. A change in income shifts the budget line parallel to itself; a change in one price rotates the budget line around one intercept. The budget line embodies both the purchasing power constraint and the market tradeoffs facing the consumer.

## How It's Best Learned
Draw budget lines for various income and price combinations, labeling intercepts and slope. Explore how each of income, price of good X, and price of good Y changes the line independently.

## Common Misconceptions
- Students often confuse a parallel shift (income change) with a rotation (price change).
- The slope of the budget line reflects relative prices — not the absolute price of either good.

## Questions

```yaml
- question: "A consumer's income doubles while prices remain unchanged. How does this affect the budget line?"
  type: multiple-choice
  options:
    - "The budget line rotates outward around the horizontal intercept, since more X can be purchased"
    - "The budget line shifts outward in a parallel fashion, with both intercepts doubling and the slope unchanged"
    - "The slope of the budget line steepens, reflecting the increased purchasing power"
    - "The budget line rotates around the origin, since the consumer can afford more of both goods proportionally"
  answer: 1
  explanation: "An income change shifts the budget line parallel to itself. Both intercepts (I/P_x and I/P_y) are proportional to income I, so when income doubles, both intercepts double — the line shifts out uniformly. The slope is −P_x/P_y, which depends only on prices. Since prices didn't change, the slope is unchanged. Rotation only occurs when one price changes (moving one intercept while holding the other fixed)."

- question: "The price of good X falls while income and the price of good Y remain unchanged. What happens to the budget line?"
  type: multiple-choice
  options:
    - "The budget line shifts outward in parallel — the consumer can afford more of everything at the same rate"
    - "The budget line rotates outward around the vertical intercept — the horizontal intercept increases while the vertical intercept stays the same"
    - "The budget line rotates inward around the horizontal intercept — cheaper X means the consumer doesn't need as much income"
    - "The slope becomes more negative, rotating around the midpoint of the original line"
  answer: 1
  explanation: "A price change for one good rotates the budget line around the opposite intercept. The vertical intercept I/P_y doesn't change (income and P_y are unchanged). The horizontal intercept I/P_x increases (P_x fell, so you can afford more X if you spend everything on it). The line fans outward from the vertical intercept. The new slope −P_x/P_y is less steep (less negative) since P_x is now smaller relative to P_y."

- question: "The slope of the budget line represents the absolute price of good X."
  type: true-false
  answer: false
  explanation: "The slope is −P_x/P_y — the ratio of the two prices, i.e., the relative price of X in terms of Y. It tells you how many units of Y you must give up to get one more unit of X. The absolute level of prices does not determine the slope — only their ratio does. If both prices doubled (with income also doubling), the budget line would be identical, with the same slope, because relative prices are unchanged."

- question: "A consumer faces P_x = $4 and P_y = $2 with income I = $40. If P_x rises to $8 while income and P_y stay the same, the budget line rotates inward around the vertical intercept."
  type: true-false
  answer: true
  explanation: "The vertical intercept is I/P_y = 40/2 = 20 and does not change (income and P_y are unchanged). The horizontal intercept falls from I/P_x = 40/4 = 10 to 40/8 = 5. The line rotates inward around the vertical intercept, becoming steeper — the slope goes from −P_x/P_y = −4/2 = −2 to −8/2 = −4, reflecting that X is now more expensive relative to Y."

- question: "Explain why the slope of the budget line is economically meaningful as a 'relative price,' and how it differs from the absolute price of either good."
  type: short-answer
  answer: "The slope −P_x/P_y tells you the rate at which the market exchanges Y for X: to buy one more unit of X, you must give up P_x/P_y units of Y. This is the opportunity cost of X expressed in units of Y — what you actually sacrifice. Absolute prices P_x and P_y only become meaningful in relation to income; their ratio matters independently of income because it governs tradeoffs. If both prices doubled with income doubled, the budget set and all consumption tradeoffs would be identical — only relative prices determine the slope and shape of the constraint."
  explanation: "This is why price changes rotate the budget line rather than shift it: a price change on one good changes the relative price (slope) but leaves the opposite intercept fixed. The slope is the market's exchange rate between goods, and the optimal consumption point equates this market rate to the consumer's personal marginal rate of substitution."
```

## Explainer

The **budget constraint** translates your income and the prices you face into a picture of what's possible. If you have income I and face prices P_x and P_y for two goods X and Y, the constraint is P_x·X + P_y·Y = I. Think of it as a checkbook equation: the total you spend on X plus the total you spend on Y can't exceed what you have. The boundary — the budget line — maps out every combination that exactly exhausts your income. Everything below it is affordable; everything above is not.

The intercepts of the budget line have a clean interpretation. If you spent your entire income on good X, you could afford I/P_x units — that's the horizontal intercept. If you spent everything on Y, you'd get I/P_y units — the vertical intercept. The **slope** of the line connecting these two points is −P_x/P_y, which is the **relative price** of X in terms of Y. It tells you the market rate of substitution: how many units of Y you must give up to get one more unit of X. This is what makes the slope economically meaningful — it's not about the absolute price of either good, but about what one costs in terms of the other.

Now connect this to your prerequisite: **marginal utility**. A utility-maximizing consumer wants the bundle on the budget line that reaches the highest possible indifference curve. The optimal point is where the slope of the indifference curve (the marginal rate of substitution, MRS) equals the slope of the budget line (−P_x/P_y). If MRS > P_x/P_y, you value X more than the market charges for it in terms of Y, so you should buy more X. The budget line tells you what the market requires; the indifference curve tells you what you prefer; the optimal bundle is where they agree.

Understanding what shifts the budget line versus what rotates it is the most important skill here. A change in **income** shifts the entire line outward (higher I) or inward (lower I), keeping the slope the same — both intercepts change proportionally. A change in the **price of one good** rotates the line around the opposite intercept: if P_x falls, the horizontal intercept I/P_x moves farther out while the vertical intercept stays fixed, making the line flatter. This distinction — parallel shift for income changes, rotation for price changes — directly governs how consumer behavior responds to economic shocks and is the foundation for income and substitution effect analysis.
