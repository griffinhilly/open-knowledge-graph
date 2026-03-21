---
id: intertemporal-choice-savings
title: Intertemporal Choice and Consumption-Savings Decisions
domain: economics
course: microeconomics
prerequisites:
- id: consumption-smoothing-intertemporal
  type: hard
- id: euler-equation-intertemporal-choice
  type: hard
builds-toward:
- asset-valuation-and-returns
tags:
- intertemporal economics
- consumption
- savings
stage: advanced
status: draft
---

# Intertemporal Choice and Consumption-Savings Decisions

## Core Idea
Households optimize consumption across periods: maximizing lifetime utility subject to a lifetime budget constraint. The marginal rate of intertemporal substitution (consumption tradeoff between periods) equals the real interest rate in optimum. Higher interest rates induce substitution (save more now) but also income effects (savers are better off). The Euler equation links current and future marginal utility: MU_t = β(1+r) MU_{t+1}. Life-cycle consumption depends on lifetime income, not current income.

## Questions

```yaml
- question: "A worker receives a one-time bonus equal to one month's salary. According to the life-cycle/permanent income hypothesis, how should this affect their consumption this month?"
  type: multiple-choice
  options:
    - "Consumption should rise by the full amount of the bonus — income rose, so spending rises"
    - "Consumption should rise by only a small fraction of the bonus, spread across remaining lifetime"
    - "Consumption is unaffected — only permanent income changes consumption"
    - "Consumption should fall, because rational households always save windfalls"
  answer: 1
  explanation: "A one-time bonus is a small, temporary income shock relative to lifetime wealth. Rational households smooth consumption across their lifetimes, so they distribute the windfall over all remaining periods. If a worker has 40 years of remaining life, the bonus raises lifetime wealth by roughly 1/40th per year — a small fraction of the total bonus. This is the permanent income insight: temporary shocks have small consumption effects; permanent shocks (like a permanent raise) shift consumption by the full present-value increment."

- question: "Interest rates rise from 3% to 6%. A household that was previously saving 15% of income is now deciding how much to save. The net effect on their savings is:"
  type: multiple-choice
  options:
    - "Unambiguously positive — higher rates reward saving, so households always save more"
    - "Unambiguously negative — higher rates mean the same retirement target requires less saving"
    - "Theoretically ambiguous — the substitution and income effects work in opposite directions"
    - "Zero — rational households are indifferent to interest rate changes in the long run"
  answer: 2
  explanation: "This is a classic case of substitution and income effects working in opposite directions. The substitution effect favors more saving: future consumption is now cheaper (higher return per dollar saved), so you shift toward saving more today. But the income effect for a net saver works the other way: the same savings now yield more income, making the household richer, which tends to increase current consumption and reduce saving. Empirically, these effects roughly cancel, and estimated interest-rate elasticities of savings are small — sometimes even negative."

- question: "According to the life-cycle hypothesis, a worker who expects a large permanent salary increase next year should rationally increase consumption immediately, before receiving the raise."
  type: true-false
  answer: true
  explanation: "The life-cycle framework treats consumption as determined by lifetime wealth, not current income. A permanent raise shifts the entire future income stream, substantially increasing lifetime wealth today (in present value). Rational consumption-smoothing says to spread this higher lifetime wealth over all periods — including now. This is why forward-looking households borrow against expected future income: a medical student with low income today but high expected future earnings should consume more than their current income, not less."

- question: "A higher real interest rate unambiguously increases aggregate household savings."
  type: true-false
  answer: false
  explanation: "The effect is theoretically ambiguous because the substitution and income effects work in opposite directions for net savers. The substitution effect pushes toward more saving (future consumption is cheaper). The income effect for savers pushes toward less saving (they are richer, so they can consume more now and still meet future goals). For net borrowers, both effects reduce savings. Empirical studies find small and sometimes negative interest elasticities of savings, consistent with these offsetting forces."

- question: "What is the key difference between a temporary and a permanent income shock in the intertemporal framework, and why does it matter for consumption behavior?"
  type: short-answer
  answer: "A temporary shock (like a one-time bonus) adds a small amount to lifetime wealth — spread over all remaining periods, it justifies only a tiny increase in current consumption. A permanent shock (like a permanent raise) shifts every future period's income, adding much more to lifetime wealth and justifying a proportionally larger immediate increase in consumption. The distinction matters because it predicts that consumers will be relatively unresponsive to transitory fluctuations (unemployment benefits, tax rebates) but highly responsive to permanent changes in earning capacity."
  explanation: "This is one of the most empirically powerful predictions of the intertemporal framework. It underlies debates about fiscal stimulus: if consumers treat a one-time tax rebate as temporary, consumption effects will be small. Evidence from stimulus checks and tax refunds broadly supports this — households save much of a windfall rather than spending it fully — consistent with consumption-smoothing over lifetime wealth."
```

## Explainer

You've already studied consumption smoothing and the Euler equation as individual building blocks. This topic connects them into a unified framework for understanding *why* households save and how saving decisions respond to interest rates and income shocks. The key shift in thinking: your current paycheck is almost irrelevant to rational consumption — what matters is your entire lifetime income stream.

The **lifetime budget constraint** is the starting point. If you live two periods, earn income Y₁ now and Y₂ later, and face a real interest rate r, your constraint is: C₁ + C₂/(1+r) = Y₁ + Y₂/(1+r). The right-hand side is your **lifetime wealth** — present value of all earnings. Saving in period 1 allows you to consume more than Y₂ in period 2; borrowing allows you to consume more than Y₁ now. The budget line has slope -(1+r), which is the relative price of consuming today versus tomorrow: giving up one unit of consumption now buys you (1+r) units in the future. The optimal point on this budget line is where the **marginal rate of intertemporal substitution** — how many future consumption units you'd trade for one more now — equals (1+r). This is exactly the Euler equation condition you've already derived: MU_t = β(1+r) MU_{t+1}.

The interest rate effect on saving has two components that work in opposite directions. The **substitution effect** of a higher r makes future consumption cheaper relative to current consumption, so you shift toward saving more today and consuming more tomorrow — savings rise. But the **income effect** works differently for net savers versus net borrowers: if you're a saver, a higher interest rate makes you richer (your savings yield more), which tends to *increase* current consumption — savings fall. The net effect of r on aggregate savings is theoretically ambiguous, and empirical estimates are small. This is a recurring example of why comparative statics requires careful separation of substitution and income effects.

The deepest insight here is the **life-cycle hypothesis**: rational households plan consumption over their entire lifetime, not paycheck to paycheck. A young worker expecting a higher future income (say, after finishing a degree) optimally borrows against that future income to maintain smooth consumption now. A retiree draws down savings accumulated during working years. Temporary income fluctuations — a one-time bonus or a brief unemployment spell — have small effects on optimal consumption, because they're small relative to lifetime wealth. **Permanent income shocks**, however, shift consumption strongly because they change the entire lifetime wealth calculation. This distinction — temporary versus permanent shocks — is one of the most empirically powerful predictions of the intertemporal framework, and it underpins the Permanent Income Hypothesis developed by Milton Friedman.
