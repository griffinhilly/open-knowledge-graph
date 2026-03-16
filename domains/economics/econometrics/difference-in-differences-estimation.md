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

## Explainer

You already know that difference-in-differences removes bias from a simple before-after comparison. Now the goal is to see exactly how that logic translates into a regression framework you can run on data, test statistically, and extend to richer settings.

The standard regression implementation adds three terms to your multiple regression model: a **treatment indicator** (D = 1 if unit is ever treated), a **post indicator** (P = 1 after the policy change), and their **interaction** (D × P). The coefficient on the interaction is the DD estimate. To see why, trace the four cell means. For a control unit before treatment: β₀. For a control unit after: β₀ + β_post. For a treated unit before: β₀ + β_treat. For a treated unit after: β₀ + β_treat + β_post + β_DD. The interaction coefficient β_DD is exactly the double-difference — it captures the extra change in the treated group beyond whatever happened to the control group over the same period.

A classic application is Card and Krueger's minimum wage study. New Jersey raised its minimum wage in 1992; Pennsylvania did not. Fast-food employment in both states was surveyed before and after. The pre-period employment difference between states reflects all permanent New Jersey–Pennsylvania differences (cost of living, labor market tightness, local preferences). The post-period change in Pennsylvania captures the nationwide time trend — whatever happened to fast-food employment generally. Subtracting the Pennsylvania trend from the New Jersey change isolates the wage law's effect, leaving a nearly zero estimate. This was striking because the prevailing theory predicted significant job losses.

The **parallel trends assumption** — that treated and control groups would have moved identically absent treatment — cannot be directly tested for the treatment period, but you can partially validate it by examining pre-treatment trends. If the two groups were drifting apart before the policy, DD is biased. The regression framework makes this diagnostic straightforward: include event-time dummies and check whether pre-period coefficients are statistically indistinguishable from zero. When you have the matrix operations from your prerequisites, you can see that the OLS estimator is just (X'X)⁻¹X'y, where the design matrix X encodes your treatment and time indicators — the algebra confirms that the interaction term cleanly identifies the cells you care about, provided your sample design balances the four cells adequately.

Extensions such as staggered treatment timing (different units treated at different times) complicate the simple 2×2 logic considerably. Recent econometrics literature has shown that the standard two-way fixed effects regression can give misleading estimates when treatment effects are heterogeneous across cohorts. But the intuition from the basic DD setup — control for group fixed effects, control for time fixed effects, and the interaction identifies treatment — remains the foundation for understanding why these extensions are needed and what they are correcting for.
