---
id: calvo-pricing-model
title: Calvo Pricing Model
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: nominal-rigidities-sticky-prices
  type: hard
builds-toward:
- new-keynesian-model-baseline
tags:
- price-stickiness
- random-adjustment
- monetary-policy-transmission
stage: advanced
status: draft
---

# Calvo Pricing Model

## Core Idea
The Calvo pricing framework models price adjustment as random, with each firm receiving a constant probability of resetting its price each period independent of the size of desired price changes. This generates a realistic distribution of prices across firms and produces substantial monetary policy transmission lags despite firms' ability to adjust prices immediately when allowed. Calvo pricing's mathematical tractability has made it the standard specification in modern DSGE models used by central banks.

## Explainer

From your study of nominal rigidities and sticky prices, you know that prices in the real economy do not adjust continuously — firms leave prices unchanged for weeks or months even when costs change. The challenge for macroeconomic modeling is capturing this stickiness in a way that is both realistic and mathematically tractable. The **Calvo pricing model** solves this with an elegantly simple assumption: in any given period, each firm faces a fixed probability (1 − θ) of being able to reset its price, and a probability θ of being stuck with its current price. This "reset lottery" is independent of how long the firm has been stuck or how badly its price is misaligned.

Think of it like a traffic light that randomly turns green for individual firms. Each period, roughly (1 − θ) of all firms get a green light and can choose any price they want. The remaining θ fraction must keep charging last period's price regardless of what has happened to their costs or demand. If θ = 0.75, then on average a firm waits four quarters between price changes — roughly matching empirical evidence on price adjustment frequency. The randomness means that at any moment, the economy contains a distribution of prices: some were set this period and reflect current conditions perfectly, while others were set several periods ago and are increasingly stale.

The key insight emerges when a firm does get to reset. Because it knows it may be stuck with this price for an uncertain number of periods, it does not simply set the price that is optimal today. Instead, it sets a **forward-looking price** — a weighted average of the prices it would ideally charge in this period, next period, the period after, and so on, with declining weights reflecting the probability it will get to reset again. This forward-looking behavior is what generates the **New Keynesian Phillips Curve**: current inflation depends not just on current economic conditions (the output gap) but also on expected future inflation. Firms that can reset today will set higher prices if they expect inflation to continue, embedding expectations directly into the price level.

Why does this matter for monetary policy? Because Calvo pricing creates a quantifiable delay between monetary shocks and their full effect on prices. When a central bank cuts interest rates, demand rises, but only a fraction of firms can raise prices immediately. The rest are stuck at old prices, so real output increases — monetary policy has real effects. Over subsequent periods, more firms get to reset, prices gradually adjust, and the real effects fade. The parameter θ directly controls the speed of this adjustment: higher θ means more stickiness, longer transmission lags, and more powerful monetary policy. This is why θ is one of the most consequential parameters in central bank models — it determines how much of a rate change shows up as real output versus inflation, and how quickly.
