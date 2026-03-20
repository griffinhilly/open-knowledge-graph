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

## Questions

```yaml
- question: "A household earns $50,000 per year and receives an unexpected $2,000 tax rebate. They spend $1,600 of it and save $400. What is their MPC?"
  type: multiple-choice
  options:
    - "0.032 — calculated as $1,600 divided by total annual income of $50,000"
    - "0.80 — calculated as $1,600 spent divided by the $2,000 income change"
    - "0.20 — calculated as the $400 saved divided by the $2,000 income change"
    - "Cannot be determined without knowing their total annual consumption"
  answer: 1
  explanation: "MPC = ΔC / ΔY_d = 1,600 / 2,000 = 0.80. The MPC is always calculated from the *change* in income and the resulting *change* in consumption — not from totals. Option A is the classic confusion with the average propensity to consume (APC), which uses total income in the denominator. Option C gives the marginal propensity to save (MPS = 0.20), which is the complement: MPC + MPS = 1."

- question: "If the MPC is 0.8, a $100 increase in government spending leads to what total increase in GDP through the multiplier process?"
  type: multiple-choice
  options:
    - "$80 — the direct consumption share of the initial spending"
    - "$100 — the initial dollar of government spending only"
    - "$500 — calculated as 1 / (1 − MPC) = 1 / 0.2 = 5, times the initial $100"
    - "$180 — the initial dollar plus one round of re-spending (100 × 0.8)"
  answer: 2
  explanation: "The fiscal multiplier is 1 / (1 − MPC) = 1 / (1 − 0.8) = 1 / 0.2 = 5. The initial $100 becomes income for someone who spends $80, which becomes income for someone who spends $64, and so on. The total is the geometric series 1 + 0.8 + 0.64 + … = 1 / (1 − 0.8) = 5. Option D captures only the first round of re-spending and misses the cascading effect that defines the multiplier."

- question: "Because every dollar of disposable income must be either consumed or saved, MPC and MPS must sum to exactly 1 by definition."
  type: true-false
  answer: true
  explanation: "MPC + MPS = 1 is a definitional identity, not an empirical claim. If a household receives an extra dollar and spends 80 cents, it must save the remaining 20 cents — there is no third category. This means MPS = 1 − MPC, and knowing one immediately gives you the other. It also means MPC must be between 0 and 1 (exclusive): it cannot be negative (you can't un-consume) or greater than 1 (you can't spend more than you receive, on the margin, in this framework)."

- question: "The average propensity to consume (APC) and the marginal propensity to consume (MPC) measure the same household behavior — APC is just the MPC calculated at a specific income level."
  type: true-false
  answer: false
  explanation: "APC (= C / Y_d) measures the fraction of *total* income spent on consumption. MPC (= ΔC / ΔY_d) measures the fraction of an *additional dollar* of income that is consumed. For the consumption function C = a + b·Y_d, MPC is the constant slope b, while APC = a/Y_d + b — a value that changes as income rises. A high-income household may have a lower APC than a low-income household even if their MPC is identical, because autonomous consumption a is a smaller fraction of their larger income."

- question: "Why do lower-income households tend to have a higher MPC than higher-income households, and what are the macroeconomic implications for fiscal stimulus targeted at different income groups?"
  type: short-answer
  answer: "Lower-income households are typically liquidity-constrained — they spend essentially all of each additional dollar because they have unmet consumption needs and little savings cushion. Higher-income households can afford to save a larger fraction of additional income. This means fiscal stimulus (tax cuts or transfers) targeted at lower-income households generates a larger multiplier effect: more of each dollar cycles back into consumption and GDP. The same total stimulus will have a larger aggregate demand impact if concentrated at the bottom of the income distribution than if distributed uniformly or toward higher earners."
  explanation: "This has direct policy implications: a $500 tax rebate to a lower-income household with MPC ≈ 0.95 generates roughly $10,000 in total GDP impact via the multiplier (1 / 0.05 = 20). The same rebate to a high-income household with MPC ≈ 0.50 generates only $1,000 (1 / 0.5 = 2). Economists debating stimulus design must account for the distribution of MPC across the income spectrum, not just the aggregate MPC."
```

## Explainer

From your consumption function work, you know that Keynesian consumption takes the form C = a + b·Yd, where a is autonomous consumption and b is a coefficient on disposable income. The **marginal propensity to consume** is exactly that coefficient b — the slope of the consumption function. But understanding the MPC as more than a parameter means building intuition about what it measures, where it comes from behaviorally, and why its magnitude matters so much for macroeconomic policy.

The MPC answers the question: if a household receives one more dollar of disposable income, how much of it gets spent? If a household earning $60,000 per year receives a $1,000 tax rebate and spends $800 of it on goods and services, their MPC is 0.8. The remaining $0.20 is saved, giving a marginal propensity to save (MPS) of 0.2. Because every dollar of income is either consumed or saved, MPC + MPS = 1 by definition. Empirically, MPC in developed economies tends to cluster between 0.75 and 0.90 on average, though it varies substantially by income group: lower-income households, who are often liquidity-constrained, typically have MPC close to 1 (they spend essentially all additional income), while wealthier households save a larger fraction.

The **average propensity to consume (APC)**, which is C/Yd, is a different and often confused concept. The APC is the share of total income spent on consumption, while the MPC is the share of an *additional* dollar spent. For the linear consumption function C = a + b·Yd, APC = a/Yd + b. As income rises, the autonomous component a becomes a smaller fraction of total spending, so APC falls even though MPC (the slope b) is constant. This explains why higher-income households save a larger fraction of their total income even when the marginal spending rate is the same — the constant autonomous consumption a is a larger share of income for poorer households.

The MPC's most important downstream application is the **fiscal multiplier**. When the government spends an additional dollar, that dollar becomes income for someone, who spends MPC of it, which becomes income for someone else, who spends MPC of that, and so on. The total increase in GDP from the initial spending is the sum of this geometric series: 1 + MPC + MPC² + MPC³ + … = 1/(1 − MPC). With MPC = 0.8, the multiplier is 5: each dollar of government spending raises total output by $5 through the chain of re-spending. This is why the MPC is not just a microeconomic behavioral parameter — it is the key variable connecting individual household spending decisions to the aggregate macroeconomic effects of fiscal policy.
