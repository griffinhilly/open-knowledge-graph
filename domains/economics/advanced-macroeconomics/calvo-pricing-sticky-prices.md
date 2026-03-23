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
stage: expert
status: draft
---

# Calvo Pricing and Sticky Prices

## Core Idea
Calvo pricing assumes firms can adjust prices only randomly (with constant probability each period), creating a realistic form of price rigidity. Unlike menu-cost models, Calvo pricing leads to tractable equilibria and is widely used in DSGE models. The key insight is that firms optimally reset prices but must sometimes sell at stale prices, creating nominal inertia. This staggered pricing structure causes monetary shocks to have real effects on output and employment in the short run.

## Questions

```yaml
- question: "In a Calvo pricing economy with θ = 0.75, the central bank unexpectedly increases the money supply. In the short run, real output rises. Why?"
  type: multiple-choice
  options:
    - "Firms are irrational and don't realize the money supply has increased, so they mistakenly expand production"
    - "The fraction of firms stuck at old prices (75%) cannot immediately raise them, so their goods become temporarily cheap in real terms, boosting demand for their output"
    - "All firms instantly raise their prices to absorb the extra money supply, leaving real output unchanged"
    - "Workers immediately renegotiate wages, reducing firms' costs and encouraging them to expand output"
  answer: 1
  explanation: "In the Calvo model, firms are fully rational — those that can reset their prices do so optimally, looking forward. The key is that most firms (fraction θ = 0.75) are stuck at stale prices and cannot adjust. When the money supply rises, the price level rises for adjusting firms but not for stuck firms — their nominal price is unchanged while the money supply increases. Their goods are now cheaper in real terms, demand for their output rises, and they produce more. Monetary policy has real effects not because of irrationality but because the staggered structure of price adjustment creates unavoidable nominal inertia."

- question: "When a firm 'wins the Calvo lottery' and is allowed to reset its price, it sets a price higher than today's optimal price. Why?"
  type: multiple-choice
  options:
    - "It exploits its temporary pricing power to extract monopoly rents before competitors catch up"
    - "It anticipates being stuck at this price for multiple future periods, so it sets a price optimal on average across expected future conditions including inflation"
    - "CIP priority rules require it to match the highest competitor price in the market"
    - "Regulatory constraints prevent it from setting exactly the current optimal price"
  answer: 1
  explanation: "The forward-looking nature of Calvo price-setting is critical. The firm knows it may not get another chance to adjust for several periods — on average, 1/(1-θ) periods. If inflation is positive and demand is growing, today's optimal price will be below the optimal price next period. A firm that sets only today's ideal price will be underpricing in future periods when it's stuck. So it rationally sets a higher price now, averaging across the distribution of future periods it may be stuck. This forward-looking behavior is what generates the expectations term in the New Keynesian Phillips Curve."

- question: "In the Calvo pricing model, the aggregate price level at any given time reflects a weighted average of prices set across many different past periods, not just the current period's optimal price."
  type: true-false
  answer: true
  explanation: "This is the mechanism that creates nominal inertia. At any moment, the economy contains firms that reset their prices this period (setting prices that reflect current conditions), firms that last adjusted one period ago, two periods ago, and so on. The aggregate price level averages over all of these stale and fresh prices, weighted by the fraction of firms at each vintage. Because old prices from past periods are embedded in the current price level, the price level adjusts sluggishly to monetary shocks — even though each firm that can adjust does so optimally and forward-lookingly."

- question: "In the Calvo model, a firm that has been stuck at its current price for many consecutive periods faces a higher probability of being allowed to reset its price in the next period."
  type: true-false
  answer: false
  explanation: "This is the 'memoryless' property — the defining feature of the Calvo assumption. The probability (1 − θ) of receiving permission to adjust is constant each period, regardless of how long the firm has been stuck. Like a fair coin flip, the past does not affect the future probability. This is what makes the Calvo model analytically tractable: the distribution of price vintages in the economy reaches a stationary structure. In contrast, menu-cost models have state-dependent adjustment (firms adjust when the gap between current and optimal price exceeds a threshold), which is more realistic but far harder to aggregate."

- question: "How does the Calvo pricing mechanism allow monetary shocks to have real effects on output, even when all firms are setting prices rationally?"
  type: short-answer
  answer: "In each period, a fraction θ of firms cannot reset their prices regardless of what the central bank does — they are stuck at prices set in previous periods. When the money supply rises, firms that can adjust raise their prices, but stuck firms cannot. The overall price level rises less than the money supply, so real money balances increase. The stuck firms' goods are now cheaper in real terms relative to the new price level — demand for their output rises, and they produce more to meet it. Real output rises even though every firm is behaving rationally. The real effect comes not from confusion but from the structural constraint that not all prices can adjust simultaneously. As contracts expire and more firms adjust, prices catch up and the real effect fades — giving monetary policy a temporary but real impact."
  explanation: "The contrast with a world of fully flexible prices is instructive: if all firms could instantly reset, the money supply increase would immediately raise all prices proportionally, leaving real variables unchanged. Nominal inertia — built into the staggered adjustment structure, not into irrationality — is what creates the non-neutrality of money in the short run."
```

## Explainer

From the New Keynesian framework, you know that nominal rigidities — the failure of prices and wages to adjust instantly — are what give monetary policy its real effects. The question is how to model this rigidity in a way that is both realistic and analytically tractable. Guillermo Calvo's 1983 pricing model provides the standard answer used in modern macroeconomics. The core assumption is elegantly simple: in each period, every firm faces a fixed probability (1 − θ) of being able to reset its price, and a probability θ of being stuck with its current price. This probability is independent of how long the firm has been stuck — a memoryless process, like a coin flip each period.

Think of it as a lottery. Each period, a fraction (1 − θ) of firms "win" the right to change their price, while the remaining fraction θ must continue selling at whatever price they last set. If θ = 0.75, then on average a firm goes four periods between price adjustments. The firms that get to reset their price do so optimally: they look forward, anticipating that they may be stuck at this new price for several periods, and set a price that is optimal on average over the expected duration. This **forward-looking price-setting** is critical — firms do not just set today's ideal price, they set a price that accounts for expected future inflation and demand conditions, because they know they may not get another chance to adjust soon.

The power of the Calvo setup is what it implies in aggregate. At any moment, the economy contains a mix of firms: some just reset their prices (reflecting current conditions), while others are stuck at prices set one, two, or many periods ago (reflecting past conditions). The **aggregate price level** is therefore a weighted average of current optimal prices and stale historical prices. When the central bank increases the money supply, firms that are stuck at old prices cannot raise their prices immediately. Their goods become temporarily cheap in real terms, boosting demand for their output and increasing real economic activity. This is how monetary shocks generate real effects — not because firms are irrational, but because the staggered structure of price adjustment creates unavoidable nominal inertia.

Aggregating the Calvo pricing decisions across all firms yields the **New Keynesian Phillips Curve** (NKPC): current inflation depends on expected future inflation and a measure of real marginal cost (often proxied by the output gap). This equation is one of the three core building blocks of the standard New Keynesian model, alongside the IS curve and a monetary policy rule. The Calvo parameter θ governs how flat or steep the Phillips curve is — higher θ (stickier prices) means inflation responds more sluggishly to changes in economic conditions, giving monetary policy more traction over real output. The elegance of Calvo pricing is that a single parameter captures the degree of nominal rigidity in the entire economy, making it the workhorse specification for policy analysis at central banks worldwide.
