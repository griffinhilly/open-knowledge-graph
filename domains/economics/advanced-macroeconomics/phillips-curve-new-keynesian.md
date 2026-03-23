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
stage: expert
status: draft
---

# Phillips Curve Derivation in New Keynesian Models

## Core Idea
The New Keynesian Phillips curve shows that inflation depends on expected future inflation, the output gap, and marginal costs. Unlike the traditional Phillips curve (which posits a stable unemployment-inflation tradeoff), the NKPC is forward-looking and depends on real variables. This microfounded derivation from Calvo pricing explains why monetary policy affects inflation through demand pressure on costs, not backward-looking wage adjustment, and why supply shocks can cause stagflation.

## Questions

```yaml
- question: "A central bank credibly announces it will pursue a strict low-inflation policy starting next year. Under the New Keynesian Phillips Curve (NKPC), what effect does this announcement have on *current* inflation?"
  type: multiple-choice
  options:
    - "None — announcements only affect inflation when implemented through actual interest rate changes"
    - "A potentially large immediate reduction — firms resetting prices today choose lower prices in anticipation of lower future inflation, reducing current inflation before policy takes effect"
    - "A rise in current inflation — lower expected future inflation raises real interest rates, boosting current demand and costs"
    - "The same effect as under adaptive expectations — both frameworks respond identically to policy announcements"
  answer: 1
  explanation: "The NKPC is forward-looking: π_t = βE_t[π_{t+1}] + κx_t. Firms resetting prices today set them optimally over the expected duration of the price lock-in, weighting expected future marginal costs and inflation. If the central bank credibly commits to lower future inflation, E_t[π_{t+1}] falls, and firms resetting prices now choose lower prices, reducing current inflation. This is the fundamental difference from adaptive-expectations models, where inflation has inertia because past inflation shapes expectations — and is why credibility and communication are first-class policy tools in the New Keynesian framework."

- question: "An oil supply shock sharply raises input costs (marginal costs) while simultaneously reducing potential output. Under the NKPC, the expected outcome is:"
  type: multiple-choice
  options:
    - "Falling inflation, because the output gap turns negative and dominates the equation"
    - "No change in inflation, because supply shocks do not enter the NKPC"
    - "Both rising inflation and falling output simultaneously — stagflation — because the NKPC links inflation directly to real marginal cost, not only to the output gap"
    - "Rising unemployment and falling inflation, as the traditional Phillips curve predicts for all shocks"
  answer: 2
  explanation: "The NKPC links inflation to real marginal cost (proxied by the output gap). A supply shock raises marginal costs directly, pushing inflation up through the κx_t term, even as output falls below potential. This is the NKPC's key advantage over the traditional Phillips curve: it naturally accommodates cost-push inflation that produces stagflation — rising prices alongside rising unemployment — which the demand-focused traditional curve could not explain. The two terms (expectations and marginal cost) can push in opposite or reinforcing directions."

- question: "In the New Keynesian Phillips Curve (π_t = βE_t[π_{t+1}] + κx_t), today's inflation is driven primarily by past inflation through adaptive expectations and backward-looking adjustment."
  type: true-false
  answer: false
  explanation: "This describes the *traditional* (adaptive expectations) Phillips curve, not the NKPC. In the NKPC, current inflation is driven by *expected future* inflation (E_t[π_{t+1}]) and the current output gap. The forward-looking nature arises from firms' optimization: a firm resetting its price today knows it may be locked in for several periods, so it sets a price that accounts for expected future costs and inflation. Past inflation does not enter directly; if expectations were re-anchored to zero, current inflation could fall immediately."

- question: "Central bank credibility matters more in the New Keynesian framework than in traditional models because inflation expectations of future policy feed directly into current pricing decisions."
  type: true-false
  answer: true
  explanation: "In adaptive-expectations models, inflation has inertia because people expect tomorrow to look like yesterday — credibility is helpful but its effect is gradual, working through slowly updating expectations. In the NKPC, because current inflation depends on E_t[π_{t+1}], a credible commitment to lower future inflation reduces current inflation immediately through current pricing decisions. A central bank that lacks credibility will find that firms set higher prices today in anticipation of high future inflation — making the inflation problem self-fulfilling. Credibility is not just helpful; it is a direct input to the inflation equation."

- question: "What does it mean for the NKPC to be 'forward-looking,' and why does this make central bank communication a genuine policy instrument?"
  type: short-answer
  answer: "The NKPC is forward-looking because current inflation depends on expected *future* inflation (E_t[π_{t+1}]) rather than past inflation. This arises from Calvo pricing: firms that get to reset their price today know they may be stuck with it for several periods, so they set a price that is optimal on average over expected future conditions, weighting expected future marginal costs and price levels. When aggregated across all firms, the economy's current inflation depends on what firms expect the future price level will be. If the central bank credibly commits to low future inflation, firms resetting prices today choose lower prices in anticipation — reducing current inflation without waiting for demand-side effects to work through the system. This makes communication and commitment a first-class policy tool: managing expectations of future policy directly shapes today's pricing behavior."
  explanation: "The contrast with adaptive expectations is sharp. In adaptive models, you can only reduce inflation by engineering a recession (shifting the output gap) and waiting for expectations to slowly update from experience. In the NKPC, credible announcements have immediate effects through the expectations term — a 'costless disinflation' is theoretically possible if credibility is perfect. In practice, credibility is imperfect and disinflation has real costs, but the framework explains why central banks invest heavily in communication."
```

## Explainer

From the traditional Phillips curve, you know the empirical observation that inflation and unemployment tend to move inversely — tight labor markets push wages and prices up. From Calvo pricing, you know that firms do not adjust prices continuously; instead, each period only a random fraction of firms get the opportunity to reset their prices, while the rest are stuck with their existing prices. The **New Keynesian Phillips Curve** (NKPC) derives the inflation-output relationship from these microfoundations, producing a relationship that is fundamentally forward-looking rather than backward-looking.

The derivation begins with a firm that gets the chance to reset its price. Because it knows it may be stuck with this price for several periods (the Calvo lottery may not select it again soon), it does not simply set price equal to current marginal cost. Instead, it sets a price that is optimal *on average* over the expected duration it will be locked in — a weighted average of current and expected future marginal costs. When you aggregate across all firms (some resetting, most stuck at old prices), the overall price level evolves as a blend of newly set prices and inherited prices. The resulting equation for inflation takes a remarkably clean form: **π_t = βE_t[π_{t+1}] + κx_t**, where π_t is current inflation, E_t[π_{t+1}] is expected future inflation, x_t is the output gap (or equivalently, real marginal cost), β is the discount factor, and κ is a slope parameter that depends on how frequently firms reset prices and how sensitive marginal costs are to output.

The forward-looking nature of this equation is its most important feature and its sharpest departure from the traditional Phillips curve. In the old framework, inflation was driven by past inflation through adaptive expectations — inflation had inertia because people expected tomorrow's inflation to look like yesterday's. In the NKPC, inflation today depends on what firms expect inflation to be *tomorrow*. If a central bank credibly commits to lowering future inflation, firms that reset prices today will choose lower prices in anticipation, and current inflation falls — even before the policy has fully taken effect. This is why central bank credibility and communication matter enormously in the New Keynesian framework: expectations of future policy feed directly into today's pricing decisions.

The NKPC also clarifies why **supply shocks** cause stagflation — the simultaneous appearance of rising inflation and falling output that the traditional Phillips curve could not accommodate. An adverse supply shock (like an oil price spike) raises marginal costs directly, pushing inflation up through the κx_t term. But because the shock also reduces potential output, the output gap may turn negative even as inflation rises. The traditional Phillips curve, which linked inflation only to the unemployment gap, could not separate demand-driven from cost-driven inflation. The NKPC, by grounding inflation in real marginal costs, naturally accounts for both channels. This microfounded structure is what makes the NKPC the inflation equation at the heart of modern DSGE models used by central banks worldwide.
