---
id: phillips-curve-new-keynesian
title: Phillips Curve Derivation in New Keynesian Models
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: calvo-pricing-sticky-prices
  type: hard
- id: phillips-curve
  type: hard
builds-toward:
- dsge-models
- monetary-policy-transmission
tags:
- phillips-curve
- inflation
- new-keynesian
stage: advanced
status: draft
---

# Phillips Curve Derivation in New Keynesian Models

## Core Idea
The New Keynesian Phillips curve shows that inflation depends on expected future inflation, the output gap, and marginal costs. Unlike the traditional Phillips curve (which posits a stable unemployment-inflation tradeoff), the NKPC is forward-looking and depends on real variables. This microfounded derivation from Calvo pricing explains why monetary policy affects inflation through demand pressure on costs, not backward-looking wage adjustment, and why supply shocks can cause stagflation.

## Explainer

From the traditional Phillips curve, you know the empirical observation that inflation and unemployment tend to move inversely — tight labor markets push wages and prices up. From Calvo pricing, you know that firms do not adjust prices continuously; instead, each period only a random fraction of firms get the opportunity to reset their prices, while the rest are stuck with their existing prices. The **New Keynesian Phillips Curve** (NKPC) derives the inflation-output relationship from these microfoundations, producing a relationship that is fundamentally forward-looking rather than backward-looking.

The derivation begins with a firm that gets the chance to reset its price. Because it knows it may be stuck with this price for several periods (the Calvo lottery may not select it again soon), it does not simply set price equal to current marginal cost. Instead, it sets a price that is optimal *on average* over the expected duration it will be locked in — a weighted average of current and expected future marginal costs. When you aggregate across all firms (some resetting, most stuck at old prices), the overall price level evolves as a blend of newly set prices and inherited prices. The resulting equation for inflation takes a remarkably clean form: **π_t = βE_t[π_{t+1}] + κx_t**, where π_t is current inflation, E_t[π_{t+1}] is expected future inflation, x_t is the output gap (or equivalently, real marginal cost), β is the discount factor, and κ is a slope parameter that depends on how frequently firms reset prices and how sensitive marginal costs are to output.

The forward-looking nature of this equation is its most important feature and its sharpest departure from the traditional Phillips curve. In the old framework, inflation was driven by past inflation through adaptive expectations — inflation had inertia because people expected tomorrow's inflation to look like yesterday's. In the NKPC, inflation today depends on what firms expect inflation to be *tomorrow*. If a central bank credibly commits to lowering future inflation, firms that reset prices today will choose lower prices in anticipation, and current inflation falls — even before the policy has fully taken effect. This is why central bank credibility and communication matter enormously in the New Keynesian framework: expectations of future policy feed directly into today's pricing decisions.

The NKPC also clarifies why **supply shocks** cause stagflation — the simultaneous appearance of rising inflation and falling output that the traditional Phillips curve could not accommodate. An adverse supply shock (like an oil price spike) raises marginal costs directly, pushing inflation up through the κx_t term. But because the shock also reduces potential output, the output gap may turn negative even as inflation rises. The traditional Phillips curve, which linked inflation only to the unemployment gap, could not separate demand-driven from cost-driven inflation. The NKPC, by grounding inflation in real marginal costs, naturally accounts for both channels. This microfounded structure is what makes the NKPC the inflation equation at the heart of modern DSGE models used by central banks worldwide.
