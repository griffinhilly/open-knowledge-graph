---
id: difference-in-differences-estimation
title: 'Difference-in-Differences: Estimation and Interpretation'
domain: economics
course: econometrics
prerequisites:
- id: difference-in-differences
  type: hard
- id: multiple-regression-model
  type: hard
- id: linear-algebra
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- parallel-trends-assumption-validity
tags:
- causal-inference
- difference-in-differences
- treatment-effects
stage: formal-systems
status: draft
---

# Difference-in-Differences: Estimation and Interpretation

## Core Idea
DD estimates the causal treatment effect by comparing outcome changes before-after in treated vs. control groups: DD = (Yₜ_treat - Ypre_treat) - (Yₜ_control - Ypre_control). This double-difference eliminates common time trends and time-invariant group differences, yielding unbiased treatment effect under parallel trends.

## Questions

```yaml
- question: "In the standard DD regression Y = β₀ + β₁D + β₂P + β₃(D×P) + ε, which coefficient is the difference-in-differences estimate of the treatment effect?"
  type: multiple-choice
  options:
    - "β₁ — it captures the permanent difference between treated and control groups"
    - "β₂ — it captures what happened over time across all groups"
    - "β₃ — it captures the additional change in the treated group beyond the common time trend"
    - "β₀ — it represents the baseline outcome for the control group before treatment"
  answer: 2
  explanation: "β₃ is the coefficient on the interaction term D×P. Tracing the four cell means: a treated unit after treatment has outcome β₀ + β₁ + β₂ + β₃. Subtracting the pre-treatment treated mean (β₀ + β₁) gives β₂ + β₃; subtracting the control group's change over time (β₂) leaves β₃. This double-difference is exactly the DD estimator: it removes both the permanent group difference (absorbed by β₁) and the common time trend (absorbed by β₂), leaving only the treatment effect."

- question: "Card and Krueger studied New Jersey's 1992 minimum wage increase using Pennsylvania as a control. What bias does comparing only New Jersey's before-after employment change fail to remove?"
  type: multiple-choice
  options:
    - "Selection bias from employers choosing to operate in New Jersey"
    - "Common time trends — nationwide changes in fast-food employment that affect both states"
    - "Attrition bias from restaurants going out of business"
    - "Omitted variable bias from differences in minimum wages across restaurant chains"
  answer: 1
  explanation: "A simple before-after comparison for New Jersey conflates the effect of the wage increase with any national trends in fast-food employment. If employment was rising (or falling) everywhere in 1992 for unrelated reasons, the before-after change in New Jersey would be biased. The DD design adds Pennsylvania as a control: Pennsylvania's before-after change captures this common trend, and subtracting it isolates New Jersey's change relative to what would have happened anyway — the treatment effect."

- question: "The DD estimator eliminates time-invariant differences between treatment and control groups, so pre-existing differences in levels do not bias the estimate."
  type: true-false
  answer: true
  explanation: "The D indicator (treatment group dummy) in the regression absorbs any permanent, time-invariant difference between groups — differences in baseline outcome levels, regional cost structures, demographic composition, and so on. By including this group fixed effect, DD allows the treated and control groups to have different average levels; what it requires is that their trends would have been parallel absent treatment. This is exactly why DD is more credible than a simple cross-sectional comparison."

- question: "If treated and control groups had different pre-treatment trends, the DD estimator still provides an unbiased treatment effect estimate because the double-differencing procedure removes all forms of trend bias."
  type: true-false
  answer: false
  explanation: "DD only removes a common time trend — the change that would have been identical for both groups absent treatment. If the two groups were already on different trajectories before the policy (diverging pre-treatment trends), DD mistakes this divergence for a treatment effect and is biased. The parallel trends assumption requires that treated and control groups would have followed the same time trend absent treatment. Pre-treatment trend tests (event-study plots) can partially validate this, but the assumption is fundamentally untestable for the treatment period."

- question: "What two sources of bias does the difference-in-differences design eliminate, and what assumption must hold for the remaining estimate to be a valid causal treatment effect?"
  type: short-answer
  answer: "DD eliminates (1) time-invariant group differences — permanent differences between treated and control units that exist regardless of treatment — by taking the before-after change within each group; and (2) common time trends — changes that affect all units equally over the period — by subtracting the control group's change from the treated group's change. The remaining estimate is a valid causal effect only if the parallel trends assumption holds: treated and control groups would have changed by the same amount absent treatment."
  explanation: "The intuition is that a naive cross-sectional comparison confounds treatment with pre-existing group differences, and a naive before-after comparison confounds treatment with time trends. DD removes both by differencing twice. But it cannot remove differential trends — if the two groups were on different trajectories before treatment, DD will mistake that divergence for an effect. This is why pre-treatment parallel trends are so important to verify empirically."
```

## Explainer

You already know that difference-in-differences removes bias from a simple before-after comparison. Now the goal is to see exactly how that logic translates into a regression framework you can run on data, test statistically, and extend to richer settings.

The standard regression implementation adds three terms to your multiple regression model: a **treatment indicator** (D = 1 if unit is ever treated), a **post indicator** (P = 1 after the policy change), and their **interaction** (D × P). The coefficient on the interaction is the DD estimate. To see why, trace the four cell means. For a control unit before treatment: β₀. For a control unit after: β₀ + β_post. For a treated unit before: β₀ + β_treat. For a treated unit after: β₀ + β_treat + β_post + β_DD. The interaction coefficient β_DD is exactly the double-difference — it captures the extra change in the treated group beyond whatever happened to the control group over the same period.

A classic application is Card and Krueger's minimum wage study. New Jersey raised its minimum wage in 1992; Pennsylvania did not. Fast-food employment in both states was surveyed before and after. The pre-period employment difference between states reflects all permanent New Jersey–Pennsylvania differences (cost of living, labor market tightness, local preferences). The post-period change in Pennsylvania captures the nationwide time trend — whatever happened to fast-food employment generally. Subtracting the Pennsylvania trend from the New Jersey change isolates the wage law's effect, leaving a nearly zero estimate. This was striking because the prevailing theory predicted significant job losses.

The **parallel trends assumption** — that treated and control groups would have moved identically absent treatment — cannot be directly tested for the treatment period, but you can partially validate it by examining pre-treatment trends. If the two groups were drifting apart before the policy, DD is biased. The regression framework makes this diagnostic straightforward: include event-time dummies and check whether pre-period coefficients are statistically indistinguishable from zero. When you have the matrix operations from your prerequisites, you can see that the OLS estimator is just (X'X)⁻¹X'y, where the design matrix X encodes your treatment and time indicators — the algebra confirms that the interaction term cleanly identifies the cells you care about, provided your sample design balances the four cells adequately.

Extensions such as staggered treatment timing (different units treated at different times) complicate the simple 2×2 logic considerably. Recent econometrics literature has shown that the standard two-way fixed effects regression can give misleading estimates when treatment effects are heterogeneous across cohorts. But the intuition from the basic DD setup — control for group fixed effects, control for time fixed effects, and the interaction identifies treatment — remains the foundation for understanding why these extensions are needed and what they are correcting for.
