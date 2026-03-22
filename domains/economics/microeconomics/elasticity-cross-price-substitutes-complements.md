---
id: elasticity-cross-price-substitutes-complements
title: Cross-Price Elasticity of Demand
domain: economics
course: microeconomics
prerequisites:
- id: price-elasticity-demand-microeconomics
  type: hard
builds-toward:
- substitutes-complements-cross-elasticity
tags:
- elasticity
- cross-price
- substitutes
- complements
stage: formal-systems
status: draft
---

# Cross-Price Elasticity of Demand

## Core Idea
Cross-price elasticity measures how the quantity demanded of one good responds to a price change in another good. Positive cross-elasticity indicates substitutes (e.g., coffee and tea), while negative cross-elasticity indicates complements (e.g., hot dogs and buns). This metric is crucial for firms deciding on pricing strategies when products are interrelated.

## How It's Best Learned
Classify pairs of goods as substitutes or complements first by intuition, then calculate cross-elasticity to verify. Compare cross-elasticities across different good pairs to understand the strength of substitution relationships.

## Common Misconceptions
- Thinking all complements must have the same sign and magnitude of elasticity.
- Confusing the direction of causation—cross-elasticity shows the relationship, not which good 'causes' demand for the other.

## Questions

```yaml
- question: "The price of coffee rises by 20% and, as a result, demand for tea increases by 10%. What is the cross-price elasticity of demand for tea with respect to coffee price, and what does the sign tell you?"
  type: multiple-choice
  options:
    - "+0.5; coffee and tea are substitutes — people switch to tea when coffee becomes more expensive"
    - "−0.5; coffee and tea are complements — rising coffee prices reduce tea demand"
    - "+0.5; coffee and tea are complements — the positive sign indicates they go together"
    - "+2.0; coffee and tea are independent goods with no systematic relationship"
  answer: 0
  explanation: "Cross-price elasticity = (% change in quantity demanded of tea) / (% change in price of coffee) = 10% / 20% = +0.5. The positive sign indicates substitutes: when coffee gets more expensive, consumers switch to tea, raising tea demand. Complements have negative cross-price elasticity (rising price of one reduces demand for the other). The most common error is reversing the sign interpretation — positive always means substitutes."

- question: "Gasoline prices rise sharply. A car manufacturer observes a significant drop in demand for large SUVs. What does the cross-price elasticity of demand between gasoline and SUVs reveal about their relationship?"
  type: multiple-choice
  options:
    - "They are substitutes — consumers switch from SUVs to gasoline when gas is cheaper"
    - "They are complements — rising gasoline prices reduce the value of SUV ownership, lowering demand for SUVs"
    - "They are independent goods — gasoline price changes should not systematically affect SUV demand"
    - "They are perfect substitutes — consumers can directly replace one with the other"
  answer: 1
  explanation: "The negative cross-price elasticity (higher gasoline price → lower SUV demand) signals complements. Gasoline and SUVs are consumed together — you need gas to run an SUV. When gasoline becomes more expensive, owning and operating a large SUV becomes costlier overall, reducing demand for them. This is the classic complement relationship: goods that are used jointly such that rising cost of one reduces demand for the other."

- question: "A cross-price elasticity of −1.5 between printer ink cartridges and printers indicates that when printer prices rise, demand for ink cartridges falls — confirming that printers and ink are complements."
  type: true-false
  answer: true
  explanation: "The negative sign is the signature of complements: when the price of one good rises, demand for the other falls. Printers and ink cartridges are consumed jointly — fewer printer purchases means fewer cartridges needed. The magnitude of −1.5 indicates a fairly strong complementary relationship: a 10% rise in printer prices leads to a 15% drop in ink cartridge demand."

- question: "If the cross-price elasticity of demand between two goods is positive, the goods are complements — a price increase in one raises demand for the other."
  type: true-false
  answer: false
  explanation: "This reverses the sign interpretation. A positive cross-price elasticity indicates substitutes: when the price of good B rises, consumers switch to good A, raising demand for A. Complements have negative cross-price elasticity: rising price of B reduces demand for A because they are consumed jointly. Confusing the signs is the most common error in applying cross-price elasticity."

- question: "Explain why cross-price elasticity is strategically important for a business. Give an example of how the sign and magnitude would inform a pricing decision."
  type: short-answer
  answer: "Cross-price elasticity quantifies how a firm's demand responds to competitors' or complements' price changes. A positive cross-elasticity with a rival's product reveals a competitive threat: if the rival raises prices, customers will switch to the firm. The magnitude tells the firm how aggressively to respond — high positive elasticity means many customers are ready to switch, so the firm might hold prices to capture the inflow. A negative cross-elasticity with a complementary product signals that the firm's fortunes are tied to that product's price — e.g., a printer manufacturer should worry when ink prices rise."
  explanation: "The power of cross-price elasticity is turning intuitive guesses ('are these related?') into measurable, actionable numbers. A coffee shop facing rising tea prices (positive cross-elasticity with coffee) might hold its own prices stable to attract switching customers. A car manufacturer facing rising gasoline prices (negative cross-elasticity with SUVs) might pivot marketing toward fuel-efficient vehicles. Without the number, these are hunches; with it, they are data-driven decisions."
```

## Explainer

You already know that own-price elasticity measures how sensitive quantity demanded is to the good's own price. **Cross-price elasticity of demand** extends that logic to ask: how sensitive is demand for good A to a change in the price of good B? The formula is the same structure — percentage change in quantity demanded of A divided by percentage change in price of B — but now the price doing the changing belongs to a different good.

The **sign** of cross-price elasticity is what makes it powerful. If the cross-price elasticity between coffee and tea is positive, it means that when the price of tea rises, demand for coffee goes up — people substitute coffee for the now-pricier tea. Goods with positive cross-price elasticity are **substitutes**. If the cross-price elasticity between hot dogs and buns is negative, it means that when the price of hot dogs rises, demand for buns falls — fewer people buying hot dogs means fewer buns needed. Goods with negative cross-price elasticity are **complements**. The sign encodes the economic relationship in a single number.

The **magnitude** measures the strength of the relationship. A cross-price elasticity of +0.1 between beef and chicken means they are weak substitutes — a 10% rise in beef prices only raises chicken demand by 1%. A cross-price elasticity of +2.0 would indicate very close substitutes, like two brands of identical gasoline. Near-zero cross-elasticity means the goods are essentially unrelated, like salt and bicycles. This allows firms to map their competitive landscape quantitatively: a high positive cross-elasticity with a rival's product signals a direct competitive threat.

The practical applications follow directly. A coffee chain facing a surge in tea prices knows demand for coffee will rise — it might hold prices steady to capture the inflow of switching customers. A car manufacturer seeing rising gasoline prices faces the complement effect: fewer car trips means potentially lower demand for new vehicles. Cross-price elasticity is the tool that turns an intuitive guess ("are these goods related?") into a measurable, actionable input for pricing and strategy decisions.
