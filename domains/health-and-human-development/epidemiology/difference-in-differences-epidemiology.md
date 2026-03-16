---
id: difference-in-differences-epidemiology
title: Difference-in-Differences Analysis
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: natural-experiments
  type: hard
- id: temporal-clustering-analysis
  type: soft
builds-toward:
- interrupted-time-series-analysis
tags:
- quasi-experimental
- policy-evaluation
- temporal-analysis
stage: advanced
status: draft
---

# Difference-in-Differences Analysis

## Core Idea
Difference-in-differences (DiD) compares changes over time between exposed and unexposed groups, differencing out time-invariant confounding. If pre-exposure trends are parallel, DiD estimates the causal effect of a policy or intervention. DiD generalizes to multiple time periods and accommodates time-varying confounders unaffected by the intervention.

## Explainer

You know from your study of natural experiments that some real-world events create exposure variation that is not determined by individual choice — a policy rollout that affects some states but not others, a factory closure in one town, a sudden price change. These events give researchers leverage to estimate causal effects without randomized assignment. **Difference-in-differences (DiD)** is the statistical technique that formalizes this leverage into an estimator.

The logic of DiD is easiest to grasp through a concrete example. Suppose a new smoking cessation program is introduced in California in 2015, but not in Nevada. You observe lung cancer incidence in both states from 2010 to 2020. Naively, you might compare post-2015 lung cancer rates in California to Nevada — but California might have had lower rates to begin with, biasing the comparison. Instead, DiD asks: how much did California's rate *change* relative to Nevada's rate? If California's incidence dropped by 8 per 100,000 between 2010–2015 and 2015–2020, while Nevada's dropped by 3 per 100,000 over the same period, the DiD estimate is 8 − 3 = **5 per 100,000**, the excess reduction attributable to the program.

More formally, the estimator is: **DiD = (Exposed post − Exposed pre) − (Unexposed post − Unexposed pre)**. The first difference removes time-invariant differences between California and Nevada (perhaps California always had lower smoking rates). The second differencing removes secular trends affecting both states equally (perhaps incidence was falling nationally due to improved treatment). What remains — the *difference in the differences* — isolates the variation attributable to the intervention.

The key assumption is **parallel trends**: in the absence of the intervention, both groups would have followed the same trajectory. This is not testable for the post-period (counterfactual), but it can be assessed by examining pre-intervention trends. If California and Nevada had similar trends from 2010 to 2015 before the program was introduced, the parallel trends assumption is more credible. A visual plot of pre-period trends is the standard diagnostic. When pre-trends diverge, DiD estimates are biased, because the trend difference itself would have produced outcome differences even without any intervention.

DiD generalizes powerfully. With panel data across many states and multiple years, DiD estimates are implemented via regression models with entity fixed effects (removing time-invariant confounders for each state) and time fixed effects (removing common temporal trends). This two-way fixed-effects design is the workhorse of policy evaluation in economics and epidemiology. More recent methodological work has complicated this picture — showing that when treatment timing is staggered across units, two-way FE estimators can produce distorted estimates if treatment effects evolve over time — leading to newer "heterogeneity-robust" DiD estimators. Understanding the classical DiD framework first gives you the conceptual foundation to follow and apply these refinements.
