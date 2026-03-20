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

## Explainer

You already know from supply and demand that the demand curve slopes downward — higher prices reduce quantity demanded. **Price elasticity of demand (PED)** answers the quantitative question that the demand curve leaves open: by *how much* does quantity fall when price rises? The formula is PED = (% change in Qd) / (% change in P), and the result is almost always negative because price and quantity move in opposite directions. Economists usually work with the absolute value |PED|, classifying demand as **elastic** when |PED| > 1 (consumers are highly responsive) and **inelastic** when |PED| < 1 (consumers are relatively unresponsive).

The elastic/inelastic boundary has an immediate implication for revenue. If demand is elastic, a price increase drives away so many customers that total revenue falls — the lost volume outweighs the higher price per unit. If demand is inelastic, buyers largely stick around, so the price increase raises total revenue. This is the **total revenue test**: for elastic demand, price and revenue move in opposite directions; for inelastic demand, they move together. Airlines exploit this by charging business travelers (inelastic: no good substitute, employer pays) far more than leisure travelers (elastic: flexible timing, price-sensitive). The same product, two elasticities.

What determines elasticity? Four classic factors: (1) **availability of substitutes** — more substitutes mean more elastic demand, because buyers can easily switch; (2) **necessity versus luxury** — insulin is inelastic, vacations are elastic; (3) **budget share** — goods that consume a tiny fraction of income (salt, matches) are inelastic because price changes barely register; (4) **time horizon** — demand is more elastic in the long run, when consumers have time to adjust their habits and capital (switching cars, moving closer to work), than in the short run when they're locked into existing arrangements.

The persistent misconception is equating elasticity with slope. Slope is ΔQ/ΔP — a constant ratio along a linear demand curve. Elasticity is (ΔQ/Q)/(ΔP/P) — a ratio that changes at every point because Q and P themselves change. At the top of a linear demand curve (high price, low quantity), a given absolute price change is a small percentage of a large price, but the resulting quantity change is a large percentage of a small quantity — demand is elastic. At the bottom, the reverse holds — demand is inelastic. The midpoint has unit elasticity. A demand curve is therefore not "elastic" or "inelastic" as a whole: those labels only make sense at a specific price point.
