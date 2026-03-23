---
id: consumption-function-and-income-dependency
title: The Consumption Function
domain: economics
course: macroeconomics
prerequisites:
- id: circular-flow-model
  type: hard
- id: budget-constraint
  type: soft
- id: consumer-theory-utility
  type: soft
builds-toward:
- marginal-propensity-to-consume-mpc
- fiscal-multiplier
tags:
- consumption
- income
- aggregate-demand
stage: formal-systems
status: validated
---

# The Consumption Function

## Core Idea
The consumption function describes how aggregate household consumption depends primarily on disposable income (current and expected future), along with wealth, interest rates, and confidence. Keynes posited that the marginal propensity to consume (the share of additional income spent) is less than one and stable over time, making consumption a predictable component of aggregate demand.

## Questions

```yaml
- question: "The government announces two fiscal policies: Policy A is a one-time $500 tax rebate; Policy B is a permanent $500/year tax cut. According to the permanent income hypothesis, which policy produces a larger increase in consumption in the year it takes effect?"
  type: multiple-choice
  options:
    - "Policy A, because lump-sum payments are immediately available to spend"
    - "They produce identical consumption increases because the dollar amounts are the same"
    - "Policy B, because households recognize the permanent income increase and raise their consumption accordingly"
    - "Neither policy affects consumption — only wage income enters the consumption function"
  answer: 2
  explanation: "The permanent income hypothesis holds that households smooth consumption over their lifetime, responding primarily to changes in *permanent* income, not transitory windfalls. A one-time rebate (Policy A) raises lifetime wealth by only $500; a permanent tax cut raises lifetime wealth by $500 × remaining years. Households save most of the one-time rebate and spread it across their lifetime, so its immediate consumption effect is small. The permanent cut raises perceived lifetime income substantially, inducing a much larger immediate consumption increase. This distinction has major policy implications: temporary fiscal stimulus is less powerful than models assuming the simple Keynesian MPC would predict."

- question: "If the marginal propensity to consume is 0.75 and a household receives a $200 increase in disposable income, what is the change in consumption predicted by Keynes's simple consumption function?"
  type: multiple-choice
  options:
    - "$200, because all additional income is eventually consumed"
    - "$150, because MPC = 0.75 means 75 cents of each dollar is spent"
    - "$266, because the multiplier effect amplifies the initial income increase"
    - "$50, because MPS = 0.25 determines what is consumed above the autonomous level"
  answer: 1
  explanation: "In Keynes's consumption function C = a + b·Y_d, the MPC (b = 0.75) is applied directly to the income change: ΔC = MPC × ΔY = 0.75 × $200 = $150. The household saves the remaining $50 (MPS = 0.25). Note that option C confuses the household's consumption response with the economy-wide multiplier effect — the multiplier describes what happens to *aggregate income* after a spending injection circulates through the economy, which is a separate (though related) concept."

- question: "A higher marginal propensity to consume implies a larger fiscal multiplier, because less income leaks out of the circular flow as savings at each round of spending."
  type: true-false
  answer: true
  explanation: "The fiscal multiplier is 1/(1 − MPC) in the simplest Keynesian model. When MPC = 0.8, the multiplier is 1/0.2 = 5; when MPC = 0.6, it is 1/0.4 = 2.5. The intuition: each round of spending generates income, which generates further spending — but each round also 'leaks' some income as savings (MPS = 1 − MPC). A higher MPC means less leakage per round and more total spending generated. Conversely, the multiplier would be infinite if MPC = 1 (no savings), which is why MPC < 1 is essential to keeping the model finite."

- question: "According to Keynes's simple consumption function C = a + b·Y_d, a household with zero disposable income will have zero consumption."
  type: true-false
  answer: false
  explanation: "The constant term *a* is autonomous consumption — spending that occurs even at zero income, funded by dis-saving (drawing down assets) or borrowing. Keynes included this term precisely to capture the empirical reality that households do not reduce consumption to zero when income falls to zero. Even unemployed households consume basic necessities by spending savings or taking on debt. Setting Y_d = 0 gives C = a > 0, not C = 0. Only a function with no intercept (pure proportional consumption) would predict zero consumption at zero income."

- question: "Why does the fiscal multiplier exceed 1, and what role does the MPC play in determining its magnitude?"
  type: short-answer
  answer: "The multiplier exceeds 1 because an initial spending injection circulates through the economy in successive rounds. When the government spends $1, that $1 becomes income for its recipients, who spend MPC of it (say $0.80), which becomes income for a second group, who spend MPC × MPC = $0.64, and so on. The total addition to output is 1 + MPC + MPC² + ... = 1/(1 − MPC). The MPC determines both how much circulates in each round and how quickly the series converges: a higher MPC means larger subsequent rounds and a larger total multiplier. The gap (1 − MPC = MPS) is the 'leakage' that prevents infinite amplification — each round of income some fraction is saved rather than spent."
  explanation: "The multiplier logic is why consumption's stability matters to macroeconomists: because C is such a large share of GDP and because MPC determines the multiplier, small changes in household spending behavior have large aggregate effects. It also explains why the permanent income hypothesis refines multiplier predictions — if households save temporary income, actual MPC out of transitory shocks is lower than the average MPC, and the effective multiplier for one-time fiscal interventions is smaller than the simple formula predicts."
```

## Explainer

From your study of the circular flow model, you know that household consumption (C) is the largest component of aggregate demand in most economies, often comprising 60–70% of GDP. Understanding what drives consumption is therefore central to macroeconomics. The **consumption function** is the relationship that formalizes this — it describes, at the aggregate level, how total household spending responds to changes in income and other factors.

Keynes's original specification was elegantly simple: C = a + b·Y_d, where Y_d is disposable income (after-tax income), a is **autonomous consumption** (spending that occurs even at zero income, funded by savings or borrowing), and b is the **marginal propensity to consume (MPC)**. The MPC is the most important parameter: it tells you what fraction of each additional dollar of income gets spent rather than saved. If MPC = 0.8, households spend 80 cents of every new dollar they receive and save 20 cents. Keynes argued MPC is between 0 and 1 — people neither save everything (MPC = 0) nor spend everything (MPC = 1). Your prerequisite work on the budget constraint gives you the microeconomic foundation: households face an intertemporal tradeoff between spending today and saving for the future, and MPC < 1 is the natural result of that optimization.

This simple structure already generates powerful macroeconomic insights. Because MPC < 1, a $1 increase in income raises consumption by less than $1. This is why the economy's spending response to a shock is not one-for-one — it builds toward the **fiscal multiplier** you'll study next, where an initial injection of spending circulates through the economy and amplifies into a larger total effect. The gap between income and consumption (1 − MPC = marginal propensity to save) represents the leakage from the circular flow that prevents infinite amplification.

The consumption function has been extended substantially since Keynes. The **permanent income hypothesis** (Milton Friedman) argues households smooth consumption over their lifetime — they respond mainly to changes in permanent (expected long-run) income, not transitory fluctuations. A one-time tax rebate has a smaller consumption effect than a permanent tax cut of the same initial size, because households know the rebate is temporary and mostly save it. The **life-cycle model** (Franco Modigliani) emphasizes that consumption depends on lifetime wealth — young workers borrow, middle-aged workers save, retirees dissave. These extensions don't overturn Keynes's basic framework but refine it: wealth effects, interest rates, and expectations all shift the consumption function, while the core relationship between income and spending remains the foundation of aggregate demand analysis.
