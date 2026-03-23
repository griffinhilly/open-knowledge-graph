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
stage: formal-systems
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

## Questions

```yaml
- question: "If the marginal propensity to consume (MPC) is 0.8 and disposable income rises by $500, by how much does consumption increase?"
  type: multiple-choice
  options:
    - "$500 — consumption rises dollar-for-dollar with income"
    - "$400 — consumption rises by MPC times the income change"
    - "$100 — consumption rises by the marginal propensity to save times the income change"
    - "$0 — consumption is determined by autonomous spending, not current income"
  answer: 1
  explanation: "The consumption function C = a + b×Y_d has slope b = MPC. A change in disposable income ΔY_d causes consumption to change by b × ΔY_d = 0.8 × $500 = $400. The remaining $100 is saved (MPS = 1 − MPC = 0.2). Option A reflects the misconception that MPC = 1; option C confuses MPS with MPC; option D misunderstands autonomous consumption as the only driver of spending."

- question: "In the consumption function C = a + b×Y_d, the intercept 'a' is positive even when disposable income is zero. What does this represent?"
  type: multiple-choice
  options:
    - "A mathematical artifact — the intercept has no economic meaning when income is zero"
    - "The amount that government transfers to households when their income falls to zero"
    - "Autonomous consumption — spending on necessities funded by drawing down savings, borrowing, or selling assets even when current income is zero"
    - "The maximum amount households are willing to consume regardless of income level"
  answer: 2
  explanation: "Autonomous consumption (the intercept 'a') is the spending that occurs even when current income is zero — people still need food, housing, and other necessities, funded by drawing down savings, selling assets, or borrowing. It is 'autonomous' because it is independent of current income. This is not a mathematical artifact: households do not cut consumption to zero when income temporarily falls, which is one reason recessions do not produce complete economic collapse."

- question: "A higher marginal propensity to consume means households save more of each additional dollar of income."
  type: true-false
  answer: false
  explanation: "MPC and MPS are complements that always sum to 1 (MPC + MPS = 1). A higher MPC means households *spend* more of each additional dollar, which necessarily means they save *less*. If MPC = 0.9, then MPS = 0.1 — only 10 cents of each additional dollar is saved. Confusing the direction of this relationship is a common error; MPC measures the consumption fraction, and MPS = 1 − MPC."

- question: "The MPC and MPS must always sum to 1 because every dollar of disposable income is either consumed or saved."
  type: true-false
  answer: true
  explanation: "By definition, disposable income (Y_d) is divided entirely between consumption (C) and saving (S): Y_d = C + S. The marginal version of this identity is 1 = MPC + MPS. There is no third category — every additional dollar of disposable income is either spent or set aside as saving. This identity is not an empirical finding but a logical necessity from the definition of disposable income."

- question: "Why does the Keynesian consumption function include an intercept term (autonomous consumption), and what economic behavior does it capture?"
  type: short-answer
  answer: "The intercept captures consumption that occurs independently of current income — people spend on necessities even when income is zero or falls sharply, financed by borrowing, asset sales, or drawing down savings. Without this term, the model would predict zero consumption at zero income, which is empirically false and misses an important stabilizing feature of recessions."
  explanation: "Autonomous consumption explains why recessions don't spiral into complete economic collapse — households maintain some baseline spending regardless of income shocks. It also defines the break-even income level where C = Y_d (saving is zero), and below that point, households are dissaving. Understanding the intercept separates those who grasp the function's economic meaning from those who merely know the algebraic form."
```

## Explainer

From GDP components and the circular flow model, you know that consumption (C) is the largest component of aggregate spending — typically 60–70% of GDP in developed economies. The question the **Keynesian consumption function** answers is: how does that spending respond to income? Keynes' key insight was that consumption rises with income but not dollar for dollar. If you receive an extra dollar of income, you spend some of it and save the rest. The fraction you spend is the **marginal propensity to consume** (MPC).

The consumption function is written C = a + b × Y_d, where Y_d is disposable income (income after taxes). The slope b is the MPC — a number between 0 and 1. If b = 0.8, every additional dollar of disposable income generates 80 cents of consumption and 20 cents of saving. The intercept a is **autonomous consumption**: the amount households spend even when income is zero, financed by drawing down savings, selling assets, or borrowing. Autonomous consumption reflects the reality that people have a floor of necessary expenditure regardless of their current income.

The complement of the consumption function is the savings function: S = Y_d − C = Y_d − (a + b × Y_d) = −a + (1−b) × Y_d. The slope of the savings function, (1−b), is the **marginal propensity to save** (MPS). MPC and MPS must sum to 1 by definition — every dollar of income is either consumed or saved. A higher MPC means a flatter savings function; a lower MPC means households save a larger fraction of each additional dollar. This relationship between MPC and MPS is the foundation of the multiplier: when MPC is high, an initial injection of spending generates more additional rounds of spending, amplifying the total effect on output.

The consumption function is central to Keynesian business cycle analysis. When income falls in a recession, consumption falls by b times the income drop — but not all the way to zero, because the autonomous component provides a floor. This partial insulation is one reason recessions don't spiral into economic collapse. Conversely, fiscal stimulus that raises disposable income (through tax cuts or transfers) generates a multiplied consumption response — the basis for Keynesian stabilization policy. The assumption that b is stable and predictable became controversial as economists discovered that consumption responds to *permanent* income expectations (Friedman's permanent income hypothesis) and liquidity constraints, complicating the simple linear relationship. But as a first-order approximation of aggregate consumption behavior, C = a + b × Y_d remains one of the most useful tools in macroeconomics.
