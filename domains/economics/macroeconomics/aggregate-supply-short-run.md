---
id: aggregate-supply-short-run
title: Short-Run Aggregate Supply
domain: economics
course: macroeconomics
prerequisites:
- id: supply-and-demand-basics
  type: hard
- id: production-function-microeconomics
  type: soft
- id: short-run-costs
  type: soft
builds-toward:
- aggregate-supply-long-run
- as-ad-model
tags:
- SRAS
- short-run
- price-level
- output
- sticky-wages
stage: formal-systems
status: validated
---

# Short-Run Aggregate Supply

## Core Idea
The short-run aggregate supply (SRAS) curve shows the total quantity of goods and services that producers will supply at each price level, holding input prices and production capacity fixed. SRAS slopes upward because higher output prices allow firms to cover rising marginal costs and earn higher profits with temporarily sticky input costs (wages often set by contracts). SRAS shifts leftward with higher input costs (oil price rises, wage increases) and rightward with improved technology or lower input prices.

## How It's Best Learned
Contrast the microeconomic supply curve (one market, one price) with SRAS (all markets, overall price level). Work through 'stagflation' scenarios where an adverse supply shock shifts SRAS left, raising prices and lowering output simultaneously.

## Common Misconceptions
- SRAS is upward sloping because wages are sticky, not because of the same forces as individual firm supply curves.
- A change in the price level moves along SRAS; only changes in input costs, technology, or expectations shift the curve.
- 'Short run' here means the period in which input prices (especially wages) have not fully adjusted.

## Questions

```yaml
- question: "An oil price shock sharply raises energy costs for producers across the economy. What happens to the SRAS curve, and what is the combined effect on the price level and real output?"
  type: multiple-choice
  options:
    - "SRAS shifts rightward — higher energy prices signal higher demand, so producers supply more"
    - "We move along the existing SRAS curve — oil is an input cost, not a change in the price level"
    - "SRAS shifts leftward — higher input costs reduce the quantity firms supply at every price level, pushing prices up and output down simultaneously"
    - "SRAS shifts rightward — firms respond by finding more fuel-efficient production methods"
  answer: 2
  explanation: "Input cost increases are the primary leftward shifter of SRAS. When oil prices rise, production costs increase for virtually every firm, reducing the profit margin at each output price. Firms cut production, shifting SRAS left. The result is stagflation — the simultaneous rise in the price level and fall in real output. This is why oil shocks of the 1970s produced both high inflation and recession, which the demand-side framework of the time couldn't explain. Moving 'along' SRAS would only occur if the overall price level changed while input costs stayed fixed."

- question: "The overall price level rises by 5%, but workers' nominal wages are fixed by annual contracts for another year. What happens to firms' profit margins, and what does the SRAS mechanism predict about their output decisions?"
  type: multiple-choice
  options:
    - "Profit margins fall because higher prices make all inputs more expensive, reducing firms' incentive to produce"
    - "Profit margins are unchanged because firms raise prices and wages by the same 5%"
    - "Profit margins temporarily rise because output prices increased while wage costs remain fixed, inducing firms to expand production"
    - "Profit margins rise permanently, shifting the economy to a higher long-run output level"
  answer: 2
  explanation: "This is the sticky-wage mechanism that gives SRAS its upward slope. When the price level rises but wages haven't adjusted yet, firms receive higher revenue per unit of output while paying the same labor costs. The gap between output price and input cost widens, making production more profitable at the margin. Firms respond by expanding output. This is temporary: once contracts expire and workers renegotiate wages upward, the profit margin illusion disappears and output returns to potential. The 'short run' in SRAS is exactly this window of sticky wages."

- question: "The SRAS curve slopes upward for the same reason as an individual firm's supply curve: higher output prices attract new firms into the market."
  type: true-false
  answer: false
  explanation: "This is a common confusion between micro and macro supply. An individual firm's supply curve slopes up partly because of entry by new producers when prices rise. SRAS slopes up for a different reason: sticky wages. When the overall price level rises, firms' output prices rise while wage contracts keep labor costs temporarily fixed, expanding profit margins and inducing higher output. No new firms need to enter — existing firms simply expand production. 'New entry' in response to individual market prices is a micro phenomenon that operates on a much longer timescale than the short-run stickiness that drives SRAS dynamics."

- question: "In the SRAS framework, 'short run' refers to the period during which nominal wages and other input prices have not yet fully adjusted to changes in the overall price level."
  type: true-false
  answer: true
  explanation: "This is the defining characteristic of the SRAS short run — it is not a fixed calendar duration but a conceptual period defined by the degree of wage flexibility. During this period, many wages are fixed by contracts, meaning firms' labor costs don't immediately track movements in the price level. Once contracts expire and wages are renegotiated to reflect the new price level, the profit-margin illusion dissolves, output returns to potential, and we are in the long run (vertical LRAS). Whether this takes months or years depends on contract lengths and the wage-setting institutions of the economy."

- question: "Explain the wage stickiness mechanism that causes SRAS to slope upward. Why does this slope disappear in the long run?"
  type: short-answer
  answer: "SRAS slopes upward because many wages are set by contracts that fix nominal pay for a period. When the overall price level rises, firms receive higher revenue per unit of output while their wage costs remain temporarily unchanged. This expands profit margins at the margin, inducing firms to increase production — output rises with the price level, creating the upward slope. The key is the lag between price-level changes and wage adjustments. In the long run, contracts expire and workers bargain for higher nominal wages to restore real purchasing power. Once wages have fully adjusted upward to match the price increase, the profit-margin effect disappears. Firms are no better off than before — higher output prices are matched by higher input costs — so they return to producing the same potential output regardless of the price level. SRAS becomes vertical (LRAS), and the short-run output expansion is undone."
  explanation: "The SRAS slope is fundamentally a disequilibrium phenomenon — it exists because the labor market hasn't cleared yet. When it does clear (wages adjust), the slope vanishes. This is why macroeconomic policy targeting short-run output gaps has different effects than long-run growth policy."
```

## Explainer

You already know from supply-and-demand basics that the supply curve for an individual market slopes upward because higher prices make production more profitable, drawing out more output from existing producers and attracting new ones. The **short-run aggregate supply (SRAS)** curve looks superficially similar — it also slopes upward — but the mechanism is different and understanding that difference is essential. The SRAS curve shows the relationship between the overall **price level** in the economy and the **total quantity of output** that all producers together are willing to supply. The slope has nothing to do with substitution between goods or entry by new firms. It comes from the fact that input prices, especially wages, are **sticky** — they do not adjust instantaneously to changes in the overall price level.

The stickiness story works as follows. Many workers have wage contracts — annual salary agreements, union contracts, multi-year deals — that fix their nominal pay for a period. If the overall price level rises (say, because aggregate demand surges), firms' output prices rise, but their wage costs remain fixed by contract. This means higher prices translate into higher profit margins per unit of output in the short run, which induces firms to expand production and hire more labor. Aggregate output rises with the price level, giving SRAS its upward slope. If prices fall, the reverse occurs: profit margins are squeezed, output contracts. This connection between your microeconomic production function background (from the soft prerequisite) and the aggregate economy is direct — firms are responding to changing profitability at the margin, just as micro theory predicts.

The crucial distinction is what causes movement *along* SRAS versus what *shifts* the curve. A change in the price level moves you along the existing SRAS curve — nothing structural has changed. What shifts SRAS are changes in factors that affect production costs or capacity at any given price level. **Input costs** are the most important shifter: an oil price spike raises production costs for virtually every firm, reducing the quantity they are willing to supply at each price level and shifting SRAS leftward. This is the mechanism behind **stagflation** — a leftward SRAS shift simultaneously pushes prices up and output down, combining inflation with recession. Conversely, technological improvements reduce costs and shift SRAS rightward, enabling more output at lower prices — the economy can grow without inflationary pressure. Changes in expected future prices also shift SRAS: if workers expect higher inflation, they will bargain for higher nominal wages in the next contract round, raising firms' costs and shifting SRAS left.

The "short run" here is defined not by calendar time but by the degree of wage and price flexibility. In the very short run, many wages and prices are fixed by contracts and menu costs. Over time — months to years, depending on the context — contracts expire, wages are renegotiated, and input prices catch up with the overall price level. When wages fully adjust, the economy moves to the long-run aggregate supply (LRAS) curve, which is vertical: output returns to potential regardless of the price level, because no profit-margin illusion persists once wages have fully risen. Understanding SRAS as a transitional, friction-driven relationship is essential to the AS-AD model you will study next, where the short-run dynamics of price stickiness generate the business cycle fluctuations that macroeconomic policy attempts to stabilize.
