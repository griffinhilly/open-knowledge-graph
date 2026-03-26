---
id: income-consumption-path-engel
title: Income Consumption Path and Engel Curves
domain: economics
course: microeconomics
prerequisites:
- id: marginal-utility-diminishing-marginal
  type: hard
- id: indifference-curves
  type: hard
builds-toward:
- income-elasticity-normal-inferior
tags:
- consumer-choice
- income
- consumption-path
stage: formal-systems
status: validated
---

# Income Consumption Path and Engel Curves

## Core Idea
The income consumption path (or income expansion path) traces how a consumer's optimal bundle changes as income rises, with prices held constant. An Engel curve graphs the relationship between income and quantity demanded for a specific good. The shape of the Engel curve—upward (normal good) or downward (inferior good)—reveals how tastes change with income.

## How It's Best Learned
Draw budget lines at increasing income levels, find optimum at each, and trace the path. Separately graph income vs. quantity for one good to see the Engel curve.

## Common Misconceptions
- Income and demand always move together (they do for normal goods, but move opposite for inferior goods).
- Engel curves are the same for all goods (they differ by good type and consumer preferences).

## Questions

```yaml
- question: "As a consumer's income rises from $30,000 to $80,000/year, they take fewer bus rides per month. What does this tell us about bus rides for this consumer?"
  type: multiple-choice
  options:
    - "Bus rides are a luxury good — consumers want proportionally more of them at higher incomes"
    - "Bus rides are a normal good — any reduction in quantity must reflect a price increase, not an income effect"
    - "Bus rides are an inferior good — demand falls in absolute terms as income rises past the threshold where alternatives become affordable"
    - "The consumer's preferences for bus rides have changed, which shifts the Engel curve"
  answer: 2
  explanation: "An inferior good is defined as one for which quantity demanded *falls* as income rises, with prices held constant. Bus rides fit the classic pattern: at low income they're the best available option; at higher income, the consumer can afford a car or ride-sharing and substitutes away. Option B is the common misconception — income changes cause shifts in the demand curve (or movement along the Engel curve), not movements along the demand curve. Prices haven't changed here."

- question: "An Engel curve for ramen noodles has a positive slope below $25,000 annual income and a negative slope above $25,000. What does this mean?"
  type: multiple-choice
  options:
    - "Ramen is always a normal good but becomes a smaller share of spending at high income"
    - "Ramen is a normal good at low incomes (demand rises with income) but becomes an inferior good above $25,000 (demand falls as income rises further)"
    - "The Engel curve must be drawn incorrectly — slopes cannot change direction"
    - "The price of ramen rises as consumers become wealthier, explaining the slope reversal"
  answer: 1
  explanation: "Good type is not fixed — it depends on income level. Below $25,000, ramen is normal: higher income lets the consumer buy more of it. Above $25,000, ramen becomes inferior: higher income makes restaurant meals or better food newly affordable, and the consumer substitutes away from ramen absolutely (fewer units, not just a smaller share). Engel curves routinely have inflection points. The slope change reveals a change in relative marginal utility between ramen and its substitutes at that income threshold."

- question: "The income consumption path holds prices constant and traces how the consumer's optimal bundle changes as income varies."
  type: true-false
  answer: true
  explanation: "This is the defining feature: prices are fixed, and only income varies. Each income level produces a parallel budget line (same slope, farther from origin), and the tangency between that budget line and the highest reachable indifference curve gives the optimal bundle at that income. Connecting those optimal bundles traces the income consumption path. If prices changed, the budget line would rotate rather than shift, producing a different kind of path (the price consumption path)."

- question: "A good classified as inferior will have a downward-sloping Engel curve at most income levels."
  type: true-false
  answer: false
  explanation: "A good is normal at some income levels and inferior at others. 'Inferior' is not an inherent property of a good but a description of how demand responds to income changes in a particular range. A cheap food staple may be normal at low income (consumers want more as they can afford it) and inferior at higher income (consumers substitute away once better alternatives are affordable). The Engel curve's slope can change from positive to negative at the income threshold where substitution kicks in."

- question: "Explain the microeconomic logic for why a consumer might buy less of a good when their income rises. What is happening to marginal utility?"
  type: short-answer
  answer: "As income rises, the consumer's opportunity set expands — goods that were previously unaffordable become options. If a higher-quality substitute (e.g., restaurants vs. ramen, a car vs. bus rides) now lies within reach, the consumer compares the marginal utility per dollar of the cheap staple against the newly affordable substitute. Because of diminishing marginal utility, consuming more of the staple yields decreasing satisfaction per unit, while the substitute offers higher marginal utility at the margin. Once income passes the threshold, the consumer maximizes utility by reallocating spending toward the substitute — and absolute quantity of the inferior good falls."
  explanation: "The key is that 'inferior' does not mean the good became worse or less satisfying. At low income, the staple was the best option available. At high income, better options become feasible, and diminishing marginal utility from the staple means the substitute now wins the marginal utility comparison. The consumer rationally shifts spending, reducing demand for the former staple in absolute terms."
```

## Explainer

You already know how a consumer finds their optimal bundle using indifference curves: the optimal choice sits at the tangency between the budget line and the highest reachable indifference curve. The price of each good and the consumer's income determine where the budget line sits. The **income consumption path** answers a simple question: what happens to that optimal bundle as income rises, holding both prices fixed? Each income level produces a parallel budget line shifted outward, and each budget line has its own tangency point. Connecting all those tangency points traces the income consumption path through the indifference map.

The shape of the path depends entirely on how preferences are structured. If the consumer always allocates a constant share of income to each good — as with Cobb-Douglas preferences — the path is a straight ray through the origin, meaning both goods scale proportionally with income. More interesting cases arise when the ratio shifts. If the path veers toward good X as income rises, the consumer is buying proportionally more X — X is a **normal good**. If the path bends away from good X (the consumer actually buys less of X at higher income), X is an **inferior good**. Ramen noodles and bus rides are the classic examples: as income rises past a threshold, people switch to more expensive substitutes, and demand for the inferior good falls absolutely, not just proportionally.

The **Engel curve** takes information from the income consumption path and projects it onto a simpler two-dimensional graph: income on the vertical axis, quantity of one specific good on the horizontal axis. Each point on the Engel curve corresponds to one income level and the optimal quantity of that good at that income. A positively sloped Engel curve confirms a normal good; a negatively sloped portion reveals an inferior good at that income range. Note that a good can switch from normal to inferior as income passes through different ranges — **luxury goods** show an Engel curve that slopes even more steeply than income (budget share rises), while **necessities** have a flatter slope (budget share falls as income rises).

The connection to your prerequisite on diminishing marginal utility is this: as you accumulate income and consume more of any good, the marginal utility from additional units declines. At some income level, you may stop wanting more of a cheap staple — not because it made you worse off before, but because the marginal utility of alternatives has overtaken it. This is the microeconomic foundation for inferior goods. The Engel curve also lays the groundwork for income elasticity of demand, which you will study next: it measures the percentage change in quantity demanded per percentage change in income, and its sign directly reflects whether the good is normal or inferior.
