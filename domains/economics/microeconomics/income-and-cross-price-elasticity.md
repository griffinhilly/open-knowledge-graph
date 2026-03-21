---
id: income-and-cross-price-elasticity
title: Income and Cross-Price Elasticity
domain: economics
course: microeconomics
prerequisites:
- id: price-elasticity-of-demand
  type: hard
builds-toward:
- consumer-theory-utility
- comparative-statics
tags:
- income elasticity
- cross-price elasticity
- normal goods
- inferior goods
- substitutes
- complements
stage: formal-systems
status: validated
---

# Income and Cross-Price Elasticity

## Core Idea
Income elasticity of demand measures how quantity demanded changes with consumer income; positive values indicate normal goods and negative values indicate inferior goods, with luxury goods having income elasticity greater than one. Cross-price elasticity of demand measures the responsiveness of demand for one good to a price change in another: positive values indicate substitutes, negative values indicate complements. These elasticities help classify goods and predict how market demand shifts when economic conditions change.

## How It's Best Learned
Classify a list of real goods (bus rides, organic food, gasoline) as normal/inferior/luxury using income elasticity. Then identify substitute and complement pairs using cross-price elasticity examples before solving numerical problems.

## Common Misconceptions
- Students confuse the sign conventions: for income elasticity, the sign distinguishes good type; for cross-price, the sign distinguishes the relationship between goods.
- Inferior goods are not 'low-quality' by definition — they are goods whose demand falls as income rises, regardless of quality.

## Questions

```yaml
- question: "As incomes rise in a city, ridership on public buses falls significantly. What does this tell us about bus rides?"
  type: multiple-choice
  options:
    - "Bus rides are a luxury good — demand grows faster than income"
    - "Bus rides are an inferior good — demand falls as income rises"
    - "Bus rides are a complement to cars — their prices are linked"
    - "The income elasticity of bus rides is between 0 and 1"
  answer: 1
  explanation: "An inferior good is one with a negative income elasticity of demand (E_I < 0): as income rises, consumers substitute away from it toward preferred alternatives. Bus rides often fit this pattern in cities — as people earn more, they shift to cars, rideshares, or other modes. 'Inferior' is a technical term describing the income-demand relationship, not a quality judgment. Many inferior goods (generic staples, inexpensive fast food) are perfectly serviceable — they're inferior only in the economic sense."

- question: "The cross-price elasticity of demand for butter with respect to the price of margarine is +0.8. This tells you that butter and margarine are:"
  type: multiple-choice
  options:
    - "Complements — they are often consumed together and the elasticity is positive"
    - "Substitutes — when margarine gets more expensive, consumers switch to butter"
    - "Unrelated goods — a cross-price elasticity below 1.0 indicates no relationship"
    - "Normal goods — the positive sign confirms both are normal goods"
  answer: 1
  explanation: "A positive cross-price elasticity means the goods are substitutes: when the price of margarine rises, quantity demanded of butter increases as consumers switch. A negative cross-price elasticity would indicate complements — goods consumed together, so that a price rise in one reduces demand for both. The magnitude (0.8) tells you how close the substitutes are; the sign tells you the relationship. The positive/negative sign is the key diagnostic, not the magnitude relative to 1."

- question: "An inferior good is defined as a good of low quality or low social status that consumers prefer less."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about inferior goods. 'Inferior' in economics refers strictly to the income-demand relationship: a good is inferior if its income elasticity is negative — that is, if demand for it falls as consumer income rises. The good need not be low quality. Bus rides, instant noodles, and generic store brands may be perfectly fine products; they are 'inferior' only because higher-income consumers tend to substitute away from them. A Giffen good — theoretically possible but rare — is even more extreme: demand rises as its own price rises."

- question: "A positive cross-price elasticity between goods X and Y means that when the price of Y rises, quantity demanded of X increases."
  type: true-false
  answer: true
  explanation: "This is the definition of substitutes via cross-price elasticity. E_XY = (%ΔQ_X) / (%ΔP_Y) > 0 means these variables move in the same direction: when P_Y rises, Q_X rises. Consumers facing a pricier Y switch to X as an alternative. The reverse relationship also holds: if the price of X rises, demand for Y increases. Complements have negative cross-price elasticity — when P_Y rises, consumers buy less of Y and therefore also less of X."

- question: "Why does the sign of income elasticity matter more than the magnitude when classifying a good, and give an example of an inferior good that is not obviously 'cheap' or low-quality?"
  type: short-answer
  answer: "The sign determines the category: positive = normal good, negative = inferior good. Magnitude then subdivides within categories (E_I > 1 = luxury; 0 < E_I < 1 = necessity). An example of a surprising inferior good: margarine itself in some contexts (as incomes rise, consumers switch to butter); public transit in car-owning societies; or rice as a staple in rapidly developing countries where wealthier households shift to more diverse diets."
  explanation: "Sign first, magnitude second is the right classification order because the sign is a categorical fact about consumer preferences — it tells you which direction demand moves with income. Once you know the good is normal (E_I > 0), the magnitude separates luxuries from necessities. For inferior goods, magnitude tells you how steeply demand falls with income. The surprising examples (public transit, generic staples) reinforce that inferiority is about behavior, not quality."
```

## Explainer

You already know that **price elasticity of demand** measures how sensitive quantity demanded is to a change in the good's own price. Income and cross-price elasticities extend this logic to two other forces that shift demand: changes in consumer income and changes in the price of a *related* good. The formulas are parallel: each is a percentage change in quantity demanded divided by a percentage change in something else.

**Income elasticity of demand** (E_I) = % change in Q_d / % change in income. The sign tells you the good's type. If E_I > 0, quantity demanded rises when income rises — the good is a **normal good** (most goods fall here). If E_I < 0, quantity demanded falls when income rises — the good is an **inferior good**. Think of instant ramen or bus rides in cities with good alternatives: as income rises, consumers shift away from these toward restaurant meals or cars. Within normal goods, a further distinction matters: if E_I > 1, demand grows faster than income — these are **luxury goods** (fine dining, international vacations, jewelry). If 0 < E_I < 1, demand grows but slower than income — these are **necessities** (basic food, utilities). This classification matters enormously for business strategy: luxury goods are disproportionately sensitive to recessions, while necessities are relatively stable.

**Cross-price elasticity of demand** (E_XY) = % change in Q_X / % change in price of Y. Here the sign reveals the relationship between the two goods. If E_XY > 0, good X and good Y are **substitutes**: when the price of Y rises, consumers switch to X, raising Q_X. Think of butter and margarine, or Coke and Pepsi. If E_XY < 0, the goods are **complements**: when the price of Y rises, consumers buy less of Y, and since X is used alongside Y, Q_X falls too. Think of printers and ink cartridges, or cars and gasoline. The magnitude tells you how close the substitutes or complements are — a very large positive E_XY means near-perfect substitutes (generic vs. name-brand aspirin); a small positive value means weak substitutes.

These elasticities explain the difference between *movement along a demand curve* and *shifts of the demand curve* — which you mastered in supply-and-demand. When income or a related good's price changes, the entire demand curve shifts. How far it shifts depends on these elasticities. A firm selling a luxury good (high E_I) should expect demand to swing dramatically with the business cycle. A retailer who cuts prices on printers should expect ink sales to rise — the cross-price complement relationship works in reverse too. Connecting the sign and magnitude of these elasticities to real strategic decisions is how they become more than formula exercises.
