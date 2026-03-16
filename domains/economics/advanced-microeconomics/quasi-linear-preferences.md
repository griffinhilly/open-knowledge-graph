---
id: quasi-linear-preferences
title: Quasi-Linear Preferences and Their Properties
domain: economics
course: advanced-microeconomics
prerequisites:
- id: consumer-theory-utility
  type: hard
- id: indifference-curves
  type: soft
builds-toward:
- mechanism-design-and-vickrey-clarke-groves
tags:
- preferences
- utility
- applied-microeconomics
stage: advanced
status: draft
---

# Quasi-Linear Preferences and Their Properties

## Core Idea
Quasi-linear preferences have the form u(x, y) = v(x) + y, where x is a divisible good and y is numeraire (money). Income effects vanish for good x: the marginal rate of substitution depends only on x, not income. This makes quasi-linear preferences analytically tractable and natural for auction and mechanism design, as the planner can use cash transfers to manipulate welfare without distorting the allocation of x.

## Explainer

From your study of consumer theory and indifference curves, you know that a consumer's demand for a good generally depends on both its price and the consumer's income. When your income rises, you typically buy more of most goods — this is the **income effect**. But in many economic models, especially in mechanism design and public economics, income effects create enormous analytical complications. **Quasi-linear preferences** are a special utility structure that eliminates income effects for one good, dramatically simplifying the analysis while still capturing the essential economic tradeoffs.

The utility function takes the form u(x, y) = v(x) + y, where x is the good you are analyzing and y is a **numeraire** — think of it as "money" or "everything else." The function v(x) is concave (diminishing marginal value), and the key feature is that y enters linearly. This linearity means the marginal utility of money is constant: an extra dollar is always worth exactly one util, regardless of how much money you already have. As a result, the consumer's willingness to pay for good x — their marginal rate of substitution between x and y — depends only on how much x they have, not on their income or wealth. Draw the indifference curves: they are vertical translates of each other, all with the same shape, just shifted up or down. This means the demand for x is independent of income.

Why does this matter so much in practice? Consider an auction designer deciding how to allocate an object. With general preferences, giving a bidder more money might change how much they value the object, tangling the allocation and transfer problems together. With quasi-linear preferences, valuation for the object is a fixed number v(x) that does not shift when the designer adjusts monetary transfers. This **separability** between the allocation decision (who gets x?) and the transfer decision (who pays or receives money?) is what makes quasi-linear preferences the workhorse assumption in mechanism design and auction theory. The designer can optimize the allocation of x to maximize total surplus v₁(x₁) + v₂(x₂) + ... and then use transfers to redistribute surplus however needed — without worrying that the transfers will distort the allocation.

The assumption has clear limitations. It requires that agents have enough money to pay any required transfer — the analysis breaks down if wealth constraints bind, because then the linearity in y no longer applies. And in contexts where income effects are economically important (housing, healthcare, labor supply), quasi-linearity is a poor approximation. But for analyzing auctions for discrete goods, public goods provision, or regulatory mechanisms where the monetary stakes are small relative to participants' wealth, the assumption is both realistic enough and analytically indispensable. It allows clean characterization of efficient mechanisms, clean separation of efficiency from distribution, and clean expressions for information rents — making it the natural starting point for nearly all formal mechanism design.
