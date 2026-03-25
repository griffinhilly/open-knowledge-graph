---
id: price-elasticity-of-demand
title: Price Elasticity of Demand
domain: economics
course: microeconomics
prerequisites:
- id: supply-and-demand-basics
  type: hard
- id: percent-increase-decrease
  type: soft
- id: derivative-as-slope-of-tangent
  type: soft
- id: comparative-statics
  type: soft
- id: elasticity-supply-responsiveness
  type: soft
- id: elasticity-income-superior-inferior-goods
  type: soft
builds-toward:
- income-and-cross-price-elasticity
- price-discrimination
- price-controls-and-deadweight-loss
- consumer-surplus-microeconomics
tags:
- elasticity
- price sensitivity
- inelastic
- elastic
stage: formal-systems
status: validated
---
# Price Elasticity of Demand

## Core Idea
Price elasticity of demand (PED) measures the responsiveness of quantity demanded to a change in price: PED = (% change in Qd) / (% change in P). Demand is elastic (|PED| > 1) when consumers are highly responsive, inelastic (|PED| < 1) when not. Determinants include availability of substitutes, necessity vs. luxury, budget share, and time horizon. Crucially, along a linear demand curve, elasticity varies — it is not the same as slope.

## How It's Best Learned
Compute elasticity using the midpoint formula on numerical examples before relating it to total revenue. The total-revenue test (elastic demand → price and revenue move oppositely) gives a practical anchor for the concept.

## Common Misconceptions
- Elasticity and slope are not the same thing; a steeper curve is less elastic at any given point, but slope is constant while elasticity changes along a linear demand curve.
- Students often forget the negative sign convention and misidentify elastic vs. inelastic based on sign rather than absolute value.

## Questions

```yaml
- question: "A pharmaceutical company sells insulin, for which demand is highly inelastic. If they raise the price by 20%, what happens to total revenue?"
  type: multiple-choice
  options:
    - "Total revenue falls — the higher price drives away enough customers to reduce overall revenue"
    - "Total revenue rises — inelastic buyers largely continue purchasing, so the price increase outweighs the small quantity decrease"
    - "Total revenue is unchanged — for inelastic goods, price changes never affect revenue"
    - "Total revenue may rise or fall depending on the slope of the demand curve at the current price"
  answer: 1
  explanation: "This is the total revenue test: for inelastic demand (|PED| < 1), price and total revenue move in the same direction. Because buyers are relatively unresponsive to price changes, a price increase causes only a small drop in quantity demanded — not enough to offset the higher revenue per unit. Total revenue rises. Option A describes what happens with elastic demand. Option C is wrong — inelastic demand does not mean revenue is fixed. Option D confuses slope with elasticity; for a given price point, it is elasticity (not slope) that determines the revenue effect."

- question: "As you move from the top of a linear demand curve (high price, low quantity) down to the bottom (low price, high quantity), how does price elasticity of demand change?"
  type: multiple-choice
  options:
    - "It remains constant — a linear curve has constant slope, so elasticity is also constant"
    - "It increases — lower prices make consumers more sensitive to further price changes"
    - "It decreases — demand becomes more inelastic as you move toward lower prices and higher quantities"
    - "It first increases then decreases, reaching a maximum at the midpoint"
  answer: 2
  explanation: "Along a linear demand curve, elasticity decreases as you move from top to bottom (from the high-price, low-quantity end to the low-price, high-quantity end). At the top, a given absolute price change is a small percentage of a large price, while the resulting quantity change is a large percentage of a small quantity — demand is elastic. At the bottom, the same absolute change is a large percentage of a small price, while the quantity change is a small percentage of a large quantity — demand is inelastic. The midpoint has unit elasticity. Slope is constant; elasticity is not. Option A is the most common misconception."

- question: "A steeper demand curve has higher price elasticity of demand than a flatter demand curve at the same price point."
  type: true-false
  answer: false
  explanation: "This is the most persistent misconception in elasticity. A steeper demand curve has LOWER elasticity (more inelastic) than a flatter one at the same price. Slope is ΔQ/ΔP — a ratio of absolute changes. Elasticity is (ΔQ/Q)/(ΔP/P) — a ratio of percentage changes. Steeper slope means less quantity response per unit of price change, which translates to a smaller |PED|. A perfectly vertical demand curve has zero elasticity (perfectly inelastic); a perfectly horizontal curve has infinite elasticity (perfectly elastic). Slope and elasticity move in opposite directions."

- question: "Price elasticity of demand changes at every point along a linear demand curve, even though the slope is constant throughout."
  type: true-false
  answer: true
  explanation: "This is the key insight that distinguishes elasticity from slope. Slope = ΔQ/ΔP is constant along a linear curve by definition. But elasticity = (ΔQ/Q)/(ΔP/P) = (ΔQ/ΔP) × (P/Q). Since P and Q change as you move along the curve, the ratio P/Q changes continuously — and therefore so does elasticity, even though ΔQ/ΔP is fixed. At the top of the curve, P is large and Q is small, so P/Q is large and elasticity is high. At the bottom, P is small and Q is large, so elasticity is low. The midpoint of the curve has unit elasticity."

- question: "Why can't we describe a linear downward-sloping demand curve as simply 'elastic' or 'inelastic,' and what does this imply for how firms should interpret demand data?"
  type: short-answer
  answer: "Because elasticity changes at every point along the curve. At high prices (top of the curve), demand is elastic — a small percentage price decrease brings a large percentage increase in quantity. At low prices (bottom), demand is inelastic — the same price change has a smaller proportional quantity effect. Only at the midpoint is elasticity exactly 1. A firm cannot say 'our demand is inelastic' as a blanket statement; it can only say 'demand is inelastic at prices below X.' This matters for pricing: raising price increases revenue when demand is inelastic at that price point, but decreases revenue when demand is elastic — the same product, different conclusions at different prices."
  explanation: "The practical implication is that firms must estimate elasticity at the specific price point under consideration, not assume it is constant. This is why economists use the midpoint formula for arc elasticity between two specific prices, rather than treating the entire demand curve as uniformly elastic or inelastic. Revenue-maximizing pricing requires finding the price where elasticity equals 1 (unit elastic), which is the peak of the total revenue curve."
```

## Explainer

You already know from supply and demand that the demand curve slopes downward — higher prices reduce quantity demanded. **Price elasticity of demand (PED)** answers the quantitative question that the demand curve leaves open: by *how much* does quantity fall when price rises? The formula is PED = (% change in Qd) / (% change in P), and the result is almost always negative because price and quantity move in opposite directions. Economists usually work with the absolute value |PED|, classifying demand as **elastic** when |PED| > 1 (consumers are highly responsive) and **inelastic** when |PED| < 1 (consumers are relatively unresponsive).

The elastic/inelastic boundary has an immediate implication for revenue. If demand is elastic, a price increase drives away so many customers that total revenue falls — the lost volume outweighs the higher price per unit. If demand is inelastic, buyers largely stick around, so the price increase raises total revenue. This is the **total revenue test**: for elastic demand, price and revenue move in opposite directions; for inelastic demand, they move together. Airlines exploit this by charging business travelers (inelastic: no good substitute, employer pays) far more than leisure travelers (elastic: flexible timing, price-sensitive). The same product, two elasticities.

What determines elasticity? Four classic factors: (1) **availability of substitutes** — more substitutes mean more elastic demand, because buyers can easily switch; (2) **necessity versus luxury** — insulin is inelastic, vacations are elastic; (3) **budget share** — goods that consume a tiny fraction of income (salt, matches) are inelastic because price changes barely register; (4) **time horizon** — demand is more elastic in the long run, when consumers have time to adjust their habits and capital (switching cars, moving closer to work), than in the short run when they're locked into existing arrangements.

The persistent misconception is equating elasticity with slope. Slope is ΔQ/ΔP — a constant ratio along a linear demand curve. Elasticity is (ΔQ/Q)/(ΔP/P) — a ratio that changes at every point because Q and P themselves change. At the top of a linear demand curve (high price, low quantity), a given absolute price change is a small percentage of a large price, but the resulting quantity change is a large percentage of a small quantity — demand is elastic. At the bottom, the reverse holds — demand is inelastic. The midpoint has unit elasticity. A demand curve is therefore not "elastic" or "inelastic" as a whole: those labels only make sense at a specific price point.
