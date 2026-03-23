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
stage: expert
status: draft
---

# Calvo Pricing Model

## Core Idea
The Calvo pricing framework models price adjustment as random, with each firm receiving a constant probability of resetting its price each period independent of the size of desired price changes. This generates a realistic distribution of prices across firms and produces substantial monetary policy transmission lags despite firms' ability to adjust prices immediately when allowed. Calvo pricing's mathematical tractability has made it the standard specification in modern DSGE models used by central banks.

## Questions

```yaml
- question: "In a Calvo pricing economy with θ = 0.75, a central bank unexpectedly cuts interest rates. What happens in the immediate period after the cut?"
  type: multiple-choice
  options:
    - "All prices fall immediately by the same proportion as the interest rate cut"
    - "Only 25% of firms can reset prices; the rest are stuck, so real output temporarily rises as the same nominal demand buys more at sticky prices"
    - "Firms anticipate the cut in advance and adjust prices before it happens, so no real effects occur"
    - "No real effects occur because prices are fully flexible when firms have the option to change them"
  answer: 1
  explanation: "With θ = 0.75, only a fraction (1 − θ) = 25% of firms can reset their prices in any given period. The remaining 75% are stuck at old prices. When the central bank cuts rates and demand rises, sticky prices mean the same nominal demand buys more real output at those unchanged prices. This is the monetary transmission mechanism: real effects occur precisely because not all prices adjust immediately. If all firms could adjust instantly (θ = 0), the price level would fully absorb the demand stimulus and real output would not change."

- question: "When a firm gets a Calvo 'green light' to reset its price, why does it typically set a price above its currently optimal level?"
  type: multiple-choice
  options:
    - "Firms are irrational and always overshoot their target price"
    - "Government regulations require a minimum markup over production costs"
    - "Because it may be stuck with this price for multiple periods, the firm sets a forward-looking price weighted toward future desired prices, which are higher if it expects inflation to continue"
    - "Firms set high prices now to compensate for being forced to keep prices low in past periods"
  answer: 2
  explanation: "A Calvo-resetting firm knows it faces a lottery about when it will get to reset again. It will not simply choose the price that maximizes profit today; it chooses the price that maximizes expected profit over the uncertain number of periods it will be stuck with this price. If the firm expects the aggregate price level to rise (inflation), then future desired prices will be higher than today's desired price, so the optimal reset price is a weighted average tilted above the current optimum. This forward-looking price-setting behavior is exactly what makes the New Keynesian Phillips Curve forward-looking."

- question: "In the Calvo model, a firm that has been unable to reset its price for the past 3 periods is no more likely to reset next period than a firm that just reset."
  type: true-false
  answer: true
  explanation: "This is the defining feature of Calvo pricing: the reset probability (1 − θ) is constant and memoryless — independent of how long the firm has been stuck or how misaligned its price has become. This is sometimes called the 'Calvo lottery.' It is mathematically convenient (it generates a tractable, stationary distribution of price vintages) and is the key assumption that makes DSGE models analytically solvable. The assumption is a simplification — in reality, firms with severely misaligned prices are more likely to update — but it is tractable and empirically reasonable on average."

- question: "The Calvo model predicts that firms adjust prices frequently in small increments, keeping prices nearly always close to their optimal level."
  type: true-false
  answer: false
  explanation: "The Calvo model predicts the opposite: firms adjust prices infrequently (only when they receive a random 'green light') and in large increments when they do adjust, because their prices may have drifted far from optimal during the period of being stuck. The realistic feature of Calvo pricing is that it generates lumpy, infrequent price changes, not continuous small adjustments. This matches empirical evidence showing prices are often unchanged for months before jumping by several percentage points when they do change."

- question: "Explain why the Calvo pricing mechanism implies that current inflation depends on expected future inflation, not just current economic conditions."
  type: short-answer
  answer: "When a firm resets its price, it will be stuck with that price for an uncertain number of future periods. To maximize expected profit over this horizon, it must choose a price that is optimal not just today but on average across all future periods it might be stuck. If the firm expects higher inflation in future periods — meaning the aggregate price level will be higher — then the currently optimal reset price must be set above the current optimum to avoid being underpriced in future periods. Since a fraction of all firms is resetting today and each is forward-looking in this way, aggregate inflation today reflects the collective forward-looking price-setting decisions, which embed expectations about future inflation. This is the mechanism behind the New Keynesian Phillips Curve: πₜ = βEₜπₜ₊₁ + κxₜ."
  explanation: "The key insight is that price stickiness makes today's pricing decisions implicitly about the future. A fully flexible firm would only optimize for today; a Calvo firm must hedge across an uncertain future duration of price freezing, embedding expectations into current inflation."
```

## Explainer

From your study of nominal rigidities and sticky prices, you know that prices in the real economy do not adjust continuously — firms leave prices unchanged for weeks or months even when costs change. The challenge for macroeconomic modeling is capturing this stickiness in a way that is both realistic and mathematically tractable. The **Calvo pricing model** solves this with an elegantly simple assumption: in any given period, each firm faces a fixed probability (1 − θ) of being able to reset its price, and a probability θ of being stuck with its current price. This "reset lottery" is independent of how long the firm has been stuck or how badly its price is misaligned.

Think of it like a traffic light that randomly turns green for individual firms. Each period, roughly (1 − θ) of all firms get a green light and can choose any price they want. The remaining θ fraction must keep charging last period's price regardless of what has happened to their costs or demand. If θ = 0.75, then on average a firm waits four quarters between price changes — roughly matching empirical evidence on price adjustment frequency. The randomness means that at any moment, the economy contains a distribution of prices: some were set this period and reflect current conditions perfectly, while others were set several periods ago and are increasingly stale.

The key insight emerges when a firm does get to reset. Because it knows it may be stuck with this price for an uncertain number of periods, it does not simply set the price that is optimal today. Instead, it sets a **forward-looking price** — a weighted average of the prices it would ideally charge in this period, next period, the period after, and so on, with declining weights reflecting the probability it will get to reset again. This forward-looking behavior is what generates the **New Keynesian Phillips Curve**: current inflation depends not just on current economic conditions (the output gap) but also on expected future inflation. Firms that can reset today will set higher prices if they expect inflation to continue, embedding expectations directly into the price level.

Why does this matter for monetary policy? Because Calvo pricing creates a quantifiable delay between monetary shocks and their full effect on prices. When a central bank cuts interest rates, demand rises, but only a fraction of firms can raise prices immediately. The rest are stuck at old prices, so real output increases — monetary policy has real effects. Over subsequent periods, more firms get to reset, prices gradually adjust, and the real effects fade. The parameter θ directly controls the speed of this adjustment: higher θ means more stickiness, longer transmission lags, and more powerful monetary policy. This is why θ is one of the most consequential parameters in central bank models — it determines how much of a rate change shows up as real output versus inflation, and how quickly.
