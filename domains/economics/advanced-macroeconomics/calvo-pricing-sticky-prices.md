---
id: calvo-pricing-sticky-prices
title: Calvo Pricing and Sticky Prices
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: new-keynesian-framework
  type: hard
- id: price-discrimination
  type: soft
builds-toward:
- phillips-curve-new-keynesian
tags:
- pricing
- sticky-prices
- nominal-rigidities
stage: advanced
status: draft
---

# Calvo Pricing and Sticky Prices

## Core Idea
Calvo pricing assumes firms can adjust prices only randomly (with constant probability each period), creating a realistic form of price rigidity. Unlike menu-cost models, Calvo pricing leads to tractable equilibria and is widely used in DSGE models. The key insight is that firms optimally reset prices but must sometimes sell at stale prices, creating nominal inertia. This staggered pricing structure causes monetary shocks to have real effects on output and employment in the short run.

## Explainer

From the New Keynesian framework, you know that nominal rigidities — the failure of prices and wages to adjust instantly — are what give monetary policy its real effects. The question is how to model this rigidity in a way that is both realistic and analytically tractable. Guillermo Calvo's 1983 pricing model provides the standard answer used in modern macroeconomics. The core assumption is elegantly simple: in each period, every firm faces a fixed probability (1 − θ) of being able to reset its price, and a probability θ of being stuck with its current price. This probability is independent of how long the firm has been stuck — a memoryless process, like a coin flip each period.

Think of it as a lottery. Each period, a fraction (1 − θ) of firms "win" the right to change their price, while the remaining fraction θ must continue selling at whatever price they last set. If θ = 0.75, then on average a firm goes four periods between price adjustments. The firms that get to reset their price do so optimally: they look forward, anticipating that they may be stuck at this new price for several periods, and set a price that is optimal on average over the expected duration. This **forward-looking price-setting** is critical — firms do not just set today's ideal price, they set a price that accounts for expected future inflation and demand conditions, because they know they may not get another chance to adjust soon.

The power of the Calvo setup is what it implies in aggregate. At any moment, the economy contains a mix of firms: some just reset their prices (reflecting current conditions), while others are stuck at prices set one, two, or many periods ago (reflecting past conditions). The **aggregate price level** is therefore a weighted average of current optimal prices and stale historical prices. When the central bank increases the money supply, firms that are stuck at old prices cannot raise their prices immediately. Their goods become temporarily cheap in real terms, boosting demand for their output and increasing real economic activity. This is how monetary shocks generate real effects — not because firms are irrational, but because the staggered structure of price adjustment creates unavoidable nominal inertia.

Aggregating the Calvo pricing decisions across all firms yields the **New Keynesian Phillips Curve** (NKPC): current inflation depends on expected future inflation and a measure of real marginal cost (often proxied by the output gap). This equation is one of the three core building blocks of the standard New Keynesian model, alongside the IS curve and a monetary policy rule. The Calvo parameter θ governs how flat or steep the Phillips curve is — higher θ (stickier prices) means inflation responds more sluggishly to changes in economic conditions, giving monetary policy more traction over real output. The elegance of Calvo pricing is that a single parameter captures the degree of nominal rigidity in the entire economy, making it the workhorse specification for policy analysis at central banks worldwide.
