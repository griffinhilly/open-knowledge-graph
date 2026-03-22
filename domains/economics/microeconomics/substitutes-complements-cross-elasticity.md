---
id: substitutes-complements-cross-elasticity
title: 'Substitutes and Complements: Cross-Price Elasticity'
domain: economics
course: microeconomics
prerequisites:
- id: demand-curve-individual-consumer
  type: hard
builds-toward:
- income-and-cross-price-elasticity
tags:
- elasticity
- related-goods
- demand-shift
stage: formal-systems
status: draft
---

# Substitutes and Complements: Cross-Price Elasticity

## Core Idea
Goods are substitutes if an increase in the price of one raises demand for the other (coffee and tea); they are complements if an increase in price of one reduces demand for the other (hot dogs and buns). Cross-price elasticity measures this relationship quantitatively. Understanding these relationships is crucial for firms' pricing strategies and market analysis.

## Questions

```yaml
- question: "The price of gasoline rises 20%, and you observe that sales of large SUVs fall substantially. What does this tell you about the cross-price elasticity of SUVs with respect to gasoline?"
  type: multiple-choice
  options:
    - "It is positive — gasoline and SUVs are substitutes"
    - "It is negative — gasoline and SUVs are complements"
    - "It is zero — the relationship is coincidental, not causal"
    - "It is positive — higher gasoline prices increase demand for any vehicle"
  answer: 1
  explanation: "When the price of gasoline rises, demand for SUVs falls. Cross-price elasticity ε_XY = (% ΔQ_SUV) / (% ΔP_gas) is negative here (price up, quantity down). A negative cross-price elasticity means the goods are complements — they are used together, so a price increase in one reduces demand for both. This makes intuitive sense: owning and driving an SUV requires gasoline, so when gas gets more expensive, SUVs become more expensive to operate and demand for them falls."

- question: "If the cross-price elasticity of demand for tea with respect to the price of coffee is +1.8, what would you predict when the price of coffee rises significantly?"
  type: multiple-choice
  options:
    - "Demand for tea will fall, since coffee and tea are used together"
    - "Demand for tea will rise, since consumers shift away from expensive coffee toward tea"
    - "Demand for tea is unaffected — tea drinkers and coffee drinkers are entirely separate consumer groups"
    - "Demand for tea will fall slightly, as tea and coffee are weak substitutes"
  answer: 1
  explanation: "A positive cross-price elasticity (+1.8) means coffee and tea are substitutes. When coffee's price rises, consumers shift toward tea — the quantity demanded of tea increases. The magnitude (+1.8) indicates close substitutability: consumers are fairly responsive to price differences between the two goods, and a significant price increase in coffee would produce a substantial increase in tea demand."

- question: "If the cross-price elasticity of demand between two goods is negative, it means they are substitutes."
  type: true-false
  answer: false
  explanation: "This reverses the rule. A POSITIVE cross-price elasticity means substitutes: when the price of Y rises, demand for X rises (consumers switch to X). A NEGATIVE cross-price elasticity means complements: when the price of Y rises, demand for X falls (because Y and X are used together, less Y means less X). Remember: positive = substitutes (they go in opposite directions — one up, consumers switch to the other); negative = complements (they move together — one more expensive, both demanded less)."

- question: "A cross-price elasticity of +0.1 indicates weaker substitutability than a cross-price elasticity of +1.5 — meaning consumers would switch less readily between the goods when one's price changes."
  type: true-false
  answer: true
  explanation: "The magnitude of cross-price elasticity measures the intensity of the relationship. A value of +0.1 means a 10% price increase in good Y causes only a 1% increase in demand for X — consumers barely respond by switching. A value of +1.5 means the same 10% price increase causes a 15% increase in demand for X — consumers switch readily. Both are positive (substitutes), but +1.5 describes much closer substitutes. Airlines, for example, track high cross-price elasticities between competing routes because even small price differences cause large passenger shifts."

- question: "A grocery store discounts chips by 30% and notices that salsa sales increase significantly. What does this reveal about the cross-price elasticity between chips and salsa, and what does it imply about the relationship between these goods?"
  type: short-answer
  answer: "When the price of chips falls, demand for salsa rises — this means the cross-price elasticity of salsa with respect to chip prices is negative (price of chips down → quantity of salsa up). A negative cross-price elasticity means the goods are complements: they are consumed together, so making one cheaper increases demand for both. The observation implies that chips and salsa are strong enough complements that chip promotions reliably drive salsa revenue. Grocery chains exploit this by discounting one good in a complementary pair to boost total basket value."
  explanation: "This connects the quantitative concept to real pricing strategy. The same logic explains why printers are sold cheaply (or at a loss) while ink cartridges are priced high — the negative cross-price elasticity between printers and ink means the two must be considered jointly. Understanding complementarity allows firms to optimize across product lines rather than pricing each item in isolation."
```

## Explainer

From your study of the individual demand curve, you know that the demand for a good depends not only on its own price but on a set of non-price determinants — including the prices of related goods. That observation was qualitative. Cross-price elasticity makes it quantitative: **cross-price elasticity of demand** (ε_XY) measures the percentage change in quantity demanded of good X in response to a one-percent change in the price of good Y. Formally, ε_XY = (% ΔQ_X) / (% ΔP_Y).

The sign of this elasticity tells you the relationship between the goods. When ε_XY > 0, the goods are **substitutes**: a rise in the price of Y makes X relatively cheaper, so consumers shift toward X — quantity demanded of X rises. Coffee and tea are the textbook example, but the category is broad: butter and margarine, Coke and Pepsi, natural gas and heating oil. When ε_XY < 0, the goods are **complements**: a rise in the price of Y reduces the consumption of Y itself, and since X and Y are used together, quantity demanded of X falls too. Hot dogs and buns, cars and gasoline, printers and ink cartridges — in each case, the goods are jointly consumed, so a price increase in one reduces demand for both. When ε_XY ≈ 0, the goods are independent, with no meaningful demand relationship.

The magnitude matters as much as the sign. A cross-price elasticity of +0.1 suggests weak substitutability — perhaps two goods that occasionally compete. A value of +2.0 suggests close substitutes — consumers will readily shift between them in response to small price changes. Firms use these numbers strategically. Airlines closely monitor cross-price elasticities between their routes and competitors' routes. Grocery chains use them to design promotions: if chips and salsa are strong complements (large negative ε), discounting chips will boost salsa sales. Merger authorities use them to define the relevant market — if two goods have high cross-price elasticity, they are in the same market and the merger may harm competition.

There is also a connection to consumer theory. In the framework you've studied, whether two goods are substitutes or complements depends partly on how you handle the income effect. Goods can be **gross substitutes** (ε_XY > 0 using ordinary demand curves, including both substitution and income effects) or **net substitutes** (using Hicksian compensated demand, holding utility constant). For most practical purposes, gross substitutability is what matters, but recognizing the conceptual distinction prepares you for the deeper analysis in income and cross-price elasticity work ahead.
