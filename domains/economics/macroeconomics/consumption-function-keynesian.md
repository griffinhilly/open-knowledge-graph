---
id: consumption-function-keynesian
title: The Keynesian Consumption Function
domain: economics
course: macroeconomics
prerequisites:
- id: gdp-components
  type: soft
- id: circular-flow-model
  type: soft
builds-toward:
- marginal-propensity-to-consume-mpc
- aggregate-demand-expenditure-approach
tags:
- consumption
- income
- spending
- keynes
stage: abstract-reasoning
status: draft
---

# The Keynesian Consumption Function

## Core Idea
The Keynesian consumption function specifies a linear relationship between aggregate consumption spending and disposable income: C = a + b*Y_d, where b is the marginal propensity to consume. This captures the empirical observation that consumption increases with income but less than dollar-for-dollar.

## How It's Best Learned
Start with numerical examples and calculate consumption at different income levels. Graph the consumption function and relate slope to MPC. Then trace through a business cycle to show consumption changes with income.

## Common Misconceptions
- Assuming MPC equals 1.
- Confusing consumption with savings function.
- Treating intercept as always positive.

## Explainer

From GDP components and the circular flow model, you know that consumption (C) is the largest component of aggregate spending — typically 60–70% of GDP in developed economies. The question the **Keynesian consumption function** answers is: how does that spending respond to income? Keynes' key insight was that consumption rises with income but not dollar for dollar. If you receive an extra dollar of income, you spend some of it and save the rest. The fraction you spend is the **marginal propensity to consume** (MPC).

The consumption function is written C = a + b × Y_d, where Y_d is disposable income (income after taxes). The slope b is the MPC — a number between 0 and 1. If b = 0.8, every additional dollar of disposable income generates 80 cents of consumption and 20 cents of saving. The intercept a is **autonomous consumption**: the amount households spend even when income is zero, financed by drawing down savings, selling assets, or borrowing. Autonomous consumption reflects the reality that people have a floor of necessary expenditure regardless of their current income.

The complement of the consumption function is the savings function: S = Y_d − C = Y_d − (a + b × Y_d) = −a + (1−b) × Y_d. The slope of the savings function, (1−b), is the **marginal propensity to save** (MPS). MPC and MPS must sum to 1 by definition — every dollar of income is either consumed or saved. A higher MPC means a flatter savings function; a lower MPC means households save a larger fraction of each additional dollar. This relationship between MPC and MPS is the foundation of the multiplier: when MPC is high, an initial injection of spending generates more additional rounds of spending, amplifying the total effect on output.

The consumption function is central to Keynesian business cycle analysis. When income falls in a recession, consumption falls by b times the income drop — but not all the way to zero, because the autonomous component provides a floor. This partial insulation is one reason recessions don't spiral into economic collapse. Conversely, fiscal stimulus that raises disposable income (through tax cuts or transfers) generates a multiplied consumption response — the basis for Keynesian stabilization policy. The assumption that b is stable and predictable became controversial as economists discovered that consumption responds to *permanent* income expectations (Friedman's permanent income hypothesis) and liquidity constraints, complicating the simple linear relationship. But as a first-order approximation of aggregate consumption behavior, C = a + b × Y_d remains one of the most useful tools in macroeconomics.
