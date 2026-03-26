---
id: price-elasticity-demand-microeconomics
title: Price Elasticity of Demand
domain: economics
course: microeconomics
prerequisites:
- id: supply-and-demand-basics
  type: hard
builds-toward:
- elasticity-cross-price-substitutes-complements
- elasticity-income-superior-inferior-goods
- tax-incidence-and-elasticity
tags:
- elasticity
- demand
- sensitivity
- price-change
stage: formal-systems
status: validated
---

# Price Elasticity of Demand

## Core Idea
Price elasticity of demand measures how responsively quantity demanded changes to a price change, expressed as the percentage change in quantity divided by the percentage change in price. Elastic demand (|ε| > 1) means consumers are very sensitive to price; inelastic demand (|ε| < 1) means quantity changes little when price changes. This concept is fundamental for understanding how firms set prices and how price changes affect total revenue.

## How It's Best Learned
Start with the midpoint formula for calculating elasticity on specific demand curves. Then examine real-world goods (e.g., salt vs. restaurant meals) and predict elasticity before calculating it. Use graphs to visualize why steeper demand curves are more inelastic.

## Common Misconceptions
- Confusing the slope of the demand curve with its elasticity—a flatter curve is not necessarily more elastic.
- Assuming elasticity is constant along an entire demand curve—elasticity varies at each point.
- Forgetting that elasticity is the responsiveness of quantity, not just whether it changes.

## Questions

```yaml
- question: "A pharmaceutical company raises the price of a patented drug by 20%, and its total sales revenue increases. What does this tell you about the price elasticity of demand for this drug?"
  type: multiple-choice
  options:
    - "Demand is elastic — a 20% price increase caused such a large revenue gain that elasticity must exceed 1"
    - "Demand is inelastic — when a price increase raises revenue, quantity fell less than proportionally, so |ε| < 1"
    - "Demand is unit elastic — price and quantity changed by equal percentages, leaving revenue unchanged"
    - "You cannot determine elasticity without knowing the exact percentage change in quantity"
  answer: 1
  explanation: "The relationship between elasticity and total revenue is the key application: if a price increase raises revenue, it means the quantity drop was proportionally smaller than the price increase — |ε| < 1 (inelastic). If demand were elastic, the quantity fall would dominate and revenue would decline. Revenue going up after a price increase is diagnostic of inelastic demand."

- question: "Along a single linear demand curve, a firm sells at a high price with low quantity. As it lowers price and moves to the high-quantity end of the curve, what happens to elasticity?"
  type: multiple-choice
  options:
    - "Elasticity increases — lower prices always mean more elastic demand"
    - "Elasticity decreases — at lower prices and higher quantities, the same absolute price change represents a smaller percentage change, making demand less elastic"
    - "Elasticity stays constant — a linear demand curve has constant elasticity by definition"
    - "Elasticity becomes unit elastic throughout — linear curves always have |ε| = 1"
  answer: 1
  explanation: "Elasticity varies along a linear demand curve because elasticity is a percentage concept while slope is an absolute concept. At the high-price, low-quantity end, a price drop represents a large percentage change — so elasticity is high. At the low-price, high-quantity end, the same absolute price change is a small percentage — making demand inelastic there. The slope is constant; elasticity is not."

- question: "A steeper demand curve is generally less elastic than a flatter demand curve."
  type: true-false
  answer: false
  explanation: "This is the most common misconception in elasticity. Slope and elasticity are related but distinct. While a steeper curve tends toward inelasticity and a flatter curve tends toward elasticity when compared at the same point, elasticity also varies along any given curve. A point on a steep curve at high prices could be more elastic than a point on a flat curve at low prices. You cannot compare elasticities without specifying where on each curve you are measuring."

- question: "If demand for a product is elastic and a firm raises its price, the firm's total revenue will decrease."
  type: true-false
  answer: true
  explanation: "Total revenue = price × quantity. With elastic demand (|ε| > 1), a price increase causes a proportionally larger decrease in quantity demanded. The quantity effect dominates, and revenue falls. This is why airlines use aggressive sales and dynamic pricing in leisure markets — raising price too much causes enough customers to switch alternatives that revenue actually drops."

- question: "Why does elasticity vary along a linear demand curve even though the slope is constant? Explain using the concept of percentage changes."
  type: short-answer
  answer: "Elasticity is calculated as (% change in quantity) / (% change in price). A percentage change depends on the base value: a $1 change in price from $100 is 1%, but the same $1 change from $10 is 10%. On a linear demand curve, the absolute changes in price and quantity are constant (slope is constant), but the percentage changes vary because the base values — the current price and quantity — change at every point. At high prices and low quantities, the same absolute changes represent large percentages, making elasticity high. At low prices and high quantities, those same absolute changes are small percentages, making elasticity low."
  explanation: "This is why the slope-elasticity confusion persists: students see a straight line and assume constant slope means constant elasticity. But elasticity requires percentage thinking, and percentages depend on the base, which changes continuously as you move along the curve."
```

## Explainer

Supply and demand tells you that quantity demanded falls when price rises — but it doesn't tell you by *how much*. **Price elasticity of demand** fills that gap. It measures the percentage change in quantity demanded for a one-percent change in price: ε = (%ΔQ) / (%ΔP). Because price and quantity move in opposite directions along a demand curve, this number is always negative — but economists typically report its absolute value. An elasticity of 2 means a 1% price increase causes a 2% drop in quantity demanded. An elasticity of 0.3 means quantity barely budges.

The key threshold is |ε| = 1. When |ε| > 1, demand is **elastic** — consumers are very responsive, which usually happens for goods with many substitutes, luxury items, or goods that represent a large share of the budget. When |ε| < 1, demand is **inelastic** — consumers are relatively unresponsive, typical of necessities like insulin, gasoline, or salt. The words "elastic" and "inelastic" are not vague descriptions; they have precise meaning in relation to this threshold.

The most important application is the relationship between elasticity and **total revenue** (price × quantity). If demand is elastic, a price increase reduces quantity so sharply that revenue falls — the quantity effect dominates. If demand is inelastic, a price increase causes only a small drop in quantity, so revenue rises — the price effect dominates. This is why drug companies can charge high prices for patented medicines (inelastic demand) but airlines hold sales aggressively (elastic demand in leisure markets). Elasticity translates the abstract demand curve into a practical pricing decision.

Elasticity varies along a linear demand curve, which is the most common student pitfall. At the high-price, low-quantity end of a linear demand curve, the percentage change in quantity for a given absolute change is large, so demand is elastic there. At the low-price, high-quantity end, the same absolute change represents a small percentage shift, so demand is inelastic. The slope of the curve is constant, but the elasticity is not — they are related but distinct measures. Always calculate elasticity at a specific point; don't assume it describes the whole curve. Determinants that make demand more elastic include: availability of substitutes, longer time horizons, higher budget share, and the narrowness with which you define the market.
