---
id: difference-in-differences-biostatistics
title: Difference-in-Differences in Biostatistics
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: causal-inference-methods-biostatistics
  type: hard
- id: study-design-biostatistics
  type: hard
builds-toward:
- interrupted-time-series-biostatistics
tags:
- difference-in-differences
- DiD
- parallel-trends
- natural-experiment
- policy-evaluation
stage: expert
status: validated
---

# Difference-in-Differences in Biostatistics

## Core Idea
Difference-in-differences (DiD) estimates causal effects by comparing the change in outcomes over time between a group affected by a treatment or policy (treatment group) and a group not affected (control group). The treatment effect is the difference in the before-to-after change between groups: (Y_treatment_after - Y_treatment_before) - (Y_control_after - Y_control_before). DiD removes both time-invariant group differences (the treatment group may have been sicker all along) and common time trends (both groups may have been improving). The critical assumption is **parallel trends**: in the absence of treatment, both groups would have experienced the same change over time. DiD is widely used in health policy evaluation — assessing the effects of smoking bans, Medicaid expansions, or new hospital regulations — because these policies create natural experiments where randomization is impossible.

## Questions

```yaml
- question: "A state implements a smoking ban in restaurants in 2015. A researcher compares lung cancer rates in that state before and after 2015 and finds a decline. Why is this simple pre-post comparison insufficient to identify the causal effect of the ban?"
  type: multiple-choice
  options:
    - "Lung cancer rates may have been declining anyway due to national trends in smoking cessation — the pre-post change confounds the policy effect with the secular trend"
    - "The sample size is too small for one state"
    - "Lung cancer takes decades to develop, so effects would not be visible by 2015"
    - "Pre-post comparisons are never valid in health research"
  answer: 0
  explanation: "A simple pre-post comparison cannot distinguish the policy effect from other things changing over time (secular trends, other health policies, demographic shifts). DiD addresses this by using states without the ban as a control group. If the control states' lung cancer rates declined by 5% and the ban state's declined by 12%, the DiD estimate attributes the additional 7% decline to the ban. This requires the parallel trends assumption — both states would have declined by the same amount without the ban."

- question: "In a DiD analysis of Medicaid expansion on emergency department visits, the parallel trends assumption requires that treatment and control states had the same level of ED visits before expansion."
  type: true-false
  answer: false
  explanation: "Parallel trends requires the same CHANGE (slope/trend), not the same level. Treatment states may have higher ED visit rates than control states at all time points — what matters is that the trends were moving in the same direction and at the same rate before the intervention. If treatment states' ED visits were declining at 2% per year and control states' were also declining at 2% per year before expansion, parallel trends is supported. This is assessed by examining pre-intervention trends visually and with statistical tests, though the assumption about the post-intervention counterfactual trend is ultimately untestable."

- question: "A researcher presents a DiD analysis but has only one pre-intervention time point and one post-intervention time point. Why does having multiple pre-intervention time points strengthen the analysis?"
  type: short-answer
  answer: "Multiple pre-intervention time points allow you to visually and statistically assess whether treatment and control groups had parallel trends before the intervention. With only one pre-period, you can compute the DiD estimate but cannot verify the parallel trends assumption — you are taking it on faith that the groups would have continued on parallel paths. With multiple pre-periods, you can plot the outcome trajectories and test whether they diverge before the intervention (which would indicate the assumption fails). Pre-intervention trend divergence would undermine the entire causal interpretation."
  explanation: "Event-study plots — showing the treatment-control difference at each time point relative to the intervention — are the standard diagnostic. If the pre-intervention differences fluctuate around zero (no pre-trend), the parallel trends assumption is supported. If they show a systematic trend before the intervention, the DiD estimate is unreliable because the groups were already diverging before the policy change."
```

## Explainer

Many of the most important questions in health policy cannot be studied with randomized trials. You cannot randomly assign states to expand Medicaid, randomly impose smoking bans, or randomly close hospitals. But these policy changes create **natural experiments** — situations where some populations are exposed to a policy and others are not, with the timing and location of the change determined by political or administrative processes rather than by health characteristics. Difference-in-differences exploits this structure.

The DiD logic is simple but powerful. Compare the treatment group's outcome before and after the policy to get the within-group change. Do the same for the control group. Subtract. The first differencing (before vs. after) removes time-invariant differences between groups. The second differencing (treatment vs. control change) removes common time trends. What remains — the difference of differences — is attributable to the policy, provided the **parallel trends** assumption holds.

Consider evaluating a state-level smoking ban. You observe lung cancer rates in the ban state and several non-ban states for years before and after implementation. The ban state may have always had higher cancer rates (population differences) and cancer rates may have been declining nationally (secular trend). DiD removes both: (ban state change) minus (non-ban state change) = policy effect. If non-ban states' rates declined by 3% and the ban state's rates declined by 8%, DiD attributes the extra 5% to the ban.

The **parallel trends assumption** is the backbone of the method and deserves scrutiny. It states that without the policy, the treatment and control groups would have experienced the same change in outcomes over time. This is about trends, not levels — groups can start at different baselines. The assumption is supported (but not proven) by showing that pre-intervention trends were parallel. **Event-study plots** are the diagnostic standard: they show the treatment-control difference at each time point, with the intervention date as reference. Flat pre-intervention differences support the assumption; diverging pre-trends undermine it. Extensions like triple-difference (DDD), synthetic control methods, and staggered adoption designs address complications that arise when the simple two-group, two-period framework does not fit the data.
