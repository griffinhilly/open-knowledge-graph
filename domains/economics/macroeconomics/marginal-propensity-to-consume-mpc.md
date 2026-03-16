---
id: marginal-propensity-to-consume-mpc
title: The Marginal Propensity to Consume
domain: economics
course: macroeconomics
prerequisites:
- id: consumption-function-keynesian
  type: hard
builds-toward:
- marginal-propensity-to-save-mps
- fiscal-multiplier
- aggregate-demand-expenditure-approach
tags:
- mpc
- consumption
- marginal
- income
stage: abstract-reasoning
status: draft
---

# The Marginal Propensity to Consume

## Core Idea
The marginal propensity to consume (MPC) is the fraction of an additional dollar of disposable income that households spend (0 < MPC < 1). Typically 0.75–0.95 in developed economies.

## How It's Best Learned
Calculate MPC as slope: MPC = ΔC / ΔY_d. Use real income change scenarios and connect to fiscal multiplier effects.

## Common Misconceptions
- Confusing MPC with average propensity to consume.
- Assuming MPC is constant across income levels.
- Treating MPC as equivalent to elasticity.

## Explainer

From your consumption function work, you know that Keynesian consumption takes the form C = a + b·Yd, where a is autonomous consumption and b is a coefficient on disposable income. The **marginal propensity to consume** is exactly that coefficient b — the slope of the consumption function. But understanding the MPC as more than a parameter means building intuition about what it measures, where it comes from behaviorally, and why its magnitude matters so much for macroeconomic policy.

The MPC answers the question: if a household receives one more dollar of disposable income, how much of it gets spent? If a household earning $60,000 per year receives a $1,000 tax rebate and spends $800 of it on goods and services, their MPC is 0.8. The remaining $0.20 is saved, giving a marginal propensity to save (MPS) of 0.2. Because every dollar of income is either consumed or saved, MPC + MPS = 1 by definition. Empirically, MPC in developed economies tends to cluster between 0.75 and 0.90 on average, though it varies substantially by income group: lower-income households, who are often liquidity-constrained, typically have MPC close to 1 (they spend essentially all additional income), while wealthier households save a larger fraction.

The **average propensity to consume (APC)**, which is C/Yd, is a different and often confused concept. The APC is the share of total income spent on consumption, while the MPC is the share of an *additional* dollar spent. For the linear consumption function C = a + b·Yd, APC = a/Yd + b. As income rises, the autonomous component a becomes a smaller fraction of total spending, so APC falls even though MPC (the slope b) is constant. This explains why higher-income households save a larger fraction of their total income even when the marginal spending rate is the same — the constant autonomous consumption a is a larger share of income for poorer households.

The MPC's most important downstream application is the **fiscal multiplier**. When the government spends an additional dollar, that dollar becomes income for someone, who spends MPC of it, which becomes income for someone else, who spends MPC of that, and so on. The total increase in GDP from the initial spending is the sum of this geometric series: 1 + MPC + MPC² + MPC³ + … = 1/(1 − MPC). With MPC = 0.8, the multiplier is 5: each dollar of government spending raises total output by $5 through the chain of re-spending. This is why the MPC is not just a microeconomic behavioral parameter — it is the key variable connecting individual household spending decisions to the aggregate macroeconomic effects of fiscal policy.
