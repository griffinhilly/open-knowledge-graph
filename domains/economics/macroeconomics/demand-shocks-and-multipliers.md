---
id: demand-shocks-and-multipliers
title: Demand Shocks and the Multiplier Mechanism
domain: economics
course: macroeconomics
prerequisites:
- id: as-ad-model
  type: hard
- id: fiscal-multiplier
  type: hard
builds-toward:
- aggregate-demand
- supply-shocks-aggregate-disruptions
tags:
- demand-shocks
- multiplier
- dynamics
stage: advanced
status: draft
---

# Demand Shocks and the Multiplier Mechanism

## Core Idea
When demand increases (e.g., from higher government spending), output initially rises more than the initial shock due to the multiplier effect: additional income from the initial increase generates further consumption and investment. The size of the multiplier depends on the marginal propensity to consume, tax rates, and the openness of the economy. Multipliers are typically 1.5 to 2 in developed economies, but can vary with the state of the business cycle and interest rate response.

## Explainer

From the AS-AD model, you know that a positive demand shock shifts the AD curve rightward, raising output and the price level in the short run. From the fiscal multiplier, you know the formula: government spending multiplier = 1/(1 − MPC), which for MPC = 0.8 gives a multiplier of 5. But why does one dollar of government spending become five dollars of output? The multiplier mechanism is the propagation story — how an initial demand injection ripples through the economy in successive rounds of spending and income.

The mechanism is a feedback loop between income and consumption. Suppose the government spends $100 million on road construction. Workers and suppliers receive $100 million in income. With **marginal propensity to consume (MPC)** = 0.8, they spend $80 million of it on consumer goods — groceries, clothing, restaurant meals. Those sellers now have $80 million in additional income; they spend 80% of that, or $64 million. The next round generates $51.2 million in spending, and so on. The total is a geometric series: 100 + 80 + 64 + 51.2 + ⋯ = 100 × [1/(1 − 0.8)] = $500 million. The $100 million injection produced $500 million in total output — a multiplier of 5. The intuition is simple: every dollar spent becomes someone else's income, which drives further spending.

The simple multiplier of 1/(1 − MPC) overstates real-world effects because it ignores **leakages** — income that exits the spending loop. **Taxes** reduce the disposable income available for consumption: with a proportional tax rate t, the after-tax MPC is MPC × (1 − t), reducing the multiplier. **Imports** divert spending abroad: a dollar spent on an imported good becomes income for a foreign worker, not a domestic one, and generates no further domestic multiplier effect. In an open economy, the multiplier is 1/(1 − MPC(1−t) + m), where m is the marginal propensity to import — substantially smaller than the closed-economy version. **Crowding out** provides another dampener: if the government borrows to finance spending, higher interest rates reduce private investment, partially offsetting the demand stimulus.

The multiplier is not a constant of nature — it varies with economic conditions. During a recession with substantial **output gap** (actual output below potential), firms hold idle capacity and unemployed workers exist; additional demand is met by real output increases, not price increases, and the multiplier is larger. At or near **full employment**, the same demand shock runs into supply constraints and mainly raises prices — the multiplier in real terms shrinks. The central bank's response matters too: if the bank raises interest rates to combat inflationary pressure from the demand shock, crowding out increases and the effective multiplier falls further. Empirical estimates of fiscal multipliers range from below 1 in booms with active monetary policy to above 2 in severe recessions with a binding zero lower bound on interest rates.

Negative demand shocks work symmetrically, and this symmetry explains why recessions tend to be self-reinforcing. A collapse in investment demand — firms cutting capital expenditure, households cutting consumption after a wealth shock — generates successive rounds of income reduction and further spending cuts. Each dollar of lost demand propagates into further lost income and additional spending cuts, amplifying the initial shock rather than absorbing it. This is the macroeconomic case for countercyclical fiscal policy: a government that cuts spending during a recession amplifies the negative multiplier, while one that expands spending can offset the private-sector contraction through the same propagation mechanism working in reverse.
