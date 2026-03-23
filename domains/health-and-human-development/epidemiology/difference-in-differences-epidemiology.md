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
stage: expert
status: validated
---

# Difference-in-Differences Analysis

## Core Idea
Difference-in-differences (DiD) compares changes over time between exposed and unexposed groups, differencing out time-invariant confounding. If pre-exposure trends are parallel, DiD estimates the causal effect of a policy or intervention. DiD generalizes to multiple time periods and accommodates time-varying confounders unaffected by the intervention.

## Questions

```yaml
- question: "A researcher uses DiD to evaluate a new public health program introduced in California in 2015 but not in Nevada. Pre-intervention, California's health outcome was improving faster than Nevada's. After applying DiD, the estimate is positive. What is the most serious problem with this analysis?"
  type: multiple-choice
  options:
    - "The researcher should have used a randomized controlled trial instead"
    - "The parallel trends assumption is violated — pre-period trends already diverged, so DiD cannot isolate the program's effect"
    - "DiD requires that both states have the same baseline outcome level before the intervention"
    - "The estimate is biased because California's larger population makes the comparison unfair"
  answer: 1
  explanation: "DiD's validity rests entirely on parallel trends: in the absence of the intervention, both groups would have changed at the same rate. If pre-period trends already diverged (California improving faster), then even without the program, California's outcome would have continued improving relative to Nevada. The DiD estimate would conflate this pre-existing trend difference with the program's effect. Baseline levels do not need to be equal — only the *rates of change* must match. Option A confuses the method's purpose (DiD is specifically designed for settings where RCTs are infeasible)."

- question: "Using DiD, a researcher finds that a smoking ban in treatment cities reduced hospital admissions by 12 per 10,000 while control cities showed no change. A colleague argues the estimate is confounded because treatment cities have older populations. Why does DiD address this concern — and when does it not?"
  type: multiple-choice
  options:
    - "DiD removes all confounding; age differences between cities are fully controlled"
    - "DiD removes time-invariant confounders like population age structure, but would be biased if age distributions changed differentially after the ban"
    - "DiD only removes confounders that affect both cities equally, so age differences are not controlled"
    - "DiD requires propensity score matching to control for demographic differences before the estimate is valid"
  answer: 1
  explanation: "The first difference (post minus pre within each city) removes anything that is constant over time within that city — including stable demographic characteristics like age structure. This is DiD's key advantage over a simple post-intervention comparison. However, if the treatment and control cities' age distributions *diverged* over the study period (perhaps because older residents moved away from treatment cities after the ban), that time-varying confounder is not removed by DiD. The estimator handles time-invariant differences, not time-varying ones."

- question: "The parallel trends assumption in DiD can be directly tested by examining pre-intervention data from both groups."
  type: true-false
  answer: true
  explanation: "True — the parallel trends assumption can and should be assessed using pre-intervention data. By examining whether the treatment and control groups showed similar trends *before* the intervention, researchers gain evidence for or against the plausibility of the assumption. Visual plots of pre-period outcomes are the standard diagnostic. Note, however, that this only tests whether the assumption held in the pre-period; it cannot prove the assumption holds in the post-period (that is untestable, because the counterfactual outcome for the treated group is never observed). Pre-trend parallel behavior is necessary but not sufficient evidence."

- question: "Difference-in-differences removes both pre-existing level differences and secular trends by subtracting the control group's change from the treated group's change — so a valid DiD estimate requires that the two groups had similar outcome levels at baseline."
  type: true-false
  answer: false
  explanation: "False. DiD does not require baseline level equivalence — it requires parallel *trends*. The first difference (post minus pre within each group) removes whatever is fixed within each group, including their different starting levels. What matters is that both groups would have changed at the same rate absent the intervention. A city with much higher baseline disease rates than the control can still yield a valid DiD estimate if both cities were trending at the same rate before the intervention. Confusing level equivalence with trend parallelism is one of the most common misunderstandings of the method."

- question: "Why does DiD use two differences rather than one, and what type of confounding does each difference address?"
  type: short-answer
  answer: "The first difference — comparing post- to pre-intervention outcomes within each group — removes time-invariant confounders: anything that is constant across time within a group (stable demographics, geography, baseline health culture). The second difference — subtracting the control group's change from the treated group's change — removes common temporal trends: secular changes affecting both groups equally (national health improvements, economic cycles, seasonal patterns). Together, the two differences isolate variation attributable to the intervention itself."
  explanation: "Without the first difference, you compare across groups that may differ in fundamental ways. Without the second difference, you cannot distinguish the program's effect from changes that would have happened anyway. Neither difference alone is sufficient: the first still confounds trends, the second still confounds baseline differences. DiD's power is precisely that the combination eliminates both — provided the parallel trends assumption holds."
```

## Explainer

You know from your study of natural experiments that some real-world events create exposure variation that is not determined by individual choice — a policy rollout that affects some states but not others, a factory closure in one town, a sudden price change. These events give researchers leverage to estimate causal effects without randomized assignment. **Difference-in-differences (DiD)** is the statistical technique that formalizes this leverage into an estimator.

The logic of DiD is easiest to grasp through a concrete example. Suppose a new smoking cessation program is introduced in California in 2015, but not in Nevada. You observe lung cancer incidence in both states from 2010 to 2020. Naively, you might compare post-2015 lung cancer rates in California to Nevada — but California might have had lower rates to begin with, biasing the comparison. Instead, DiD asks: how much did California's rate *change* relative to Nevada's rate? If California's incidence dropped by 8 per 100,000 between 2010–2015 and 2015–2020, while Nevada's dropped by 3 per 100,000 over the same period, the DiD estimate is 8 − 3 = **5 per 100,000**, the excess reduction attributable to the program.

More formally, the estimator is: **DiD = (Exposed post − Exposed pre) − (Unexposed post − Unexposed pre)**. The first difference removes time-invariant differences between California and Nevada (perhaps California always had lower smoking rates). The second differencing removes secular trends affecting both states equally (perhaps incidence was falling nationally due to improved treatment). What remains — the *difference in the differences* — isolates the variation attributable to the intervention.

The key assumption is **parallel trends**: in the absence of the intervention, both groups would have followed the same trajectory. This is not testable for the post-period (counterfactual), but it can be assessed by examining pre-intervention trends. If California and Nevada had similar trends from 2010 to 2015 before the program was introduced, the parallel trends assumption is more credible. A visual plot of pre-period trends is the standard diagnostic. When pre-trends diverge, DiD estimates are biased, because the trend difference itself would have produced outcome differences even without any intervention.

DiD generalizes powerfully. With panel data across many states and multiple years, DiD estimates are implemented via regression models with entity fixed effects (removing time-invariant confounders for each state) and time fixed effects (removing common temporal trends). This two-way fixed-effects design is the workhorse of policy evaluation in economics and epidemiology. More recent methodological work has complicated this picture — showing that when treatment timing is staggered across units, two-way FE estimators can produce distorted estimates if treatment effects evolve over time — leading to newer "heterogeneity-robust" DiD estimators. Understanding the classical DiD framework first gives you the conceptual foundation to follow and apply these refinements.
