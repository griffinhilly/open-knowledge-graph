---
id: interrupted-time-series
title: Interrupted Time Series Design
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: time-series-cross-section
  type: hard
- id: natural-experiments-design
  type: soft
tags:
- quasi-experimental
- policy
- causal
- temporal
stage: advanced
status: validated
---

# Interrupted Time Series Design

## Core Idea
Interrupted time series (ITS) exploits sharp temporal boundaries when an intervention is implemented to the entire population. The design measures outcome trajectories before and after the intervention, estimating both level changes and trend changes. Unlike experiments, ITS requires no control group but demands careful specification of time trends and control for alternative explanations (simultaneous shocks). ITS is prevalent in policy evaluation, public health, and organizational change research.

## Explainer

From your work with time series data, you know that outcomes in social settings rarely jump around randomly — they tend to follow trends, seasonal rhythms, and autocorrelated trajectories. Interrupted time series exploits this regularity. The core idea is simple: if a series was following a stable trajectory before an intervention, you can project that pre-intervention trajectory forward and ask whether the post-intervention data diverge from what would have been predicted. The divergence is your estimate of the intervention's effect. ITS makes the "what would have happened without the intervention?" question concrete by letting the pre-period trend answer it.

There are two distinct effects to estimate: the **level change** (did the series jump up or down immediately when the intervention hit?) and the **slope change** (did the trend accelerate or decelerate after the intervention?). Consider a city that bans tobacco advertising. Traffic-accident fatalities (an unrelated series) should show no discontinuity — but lung cancer diagnoses might show a slow trend change as smoking rates gradually fall. These two effects have different policy interpretations: a level change suggests an immediate shock; a slope change suggests a gradual mechanism. Your time-series cross-section background equips you to model both with a segmented regression that includes an indicator for post-intervention periods and an interaction term capturing the trend shift.

The critical threat to validity is **simultaneous shocks** — other things that changed at the same moment as your intervention. A natural experiment on a law passed in January will be confounded by anything else that happened in January. The classic defense is a control series: a comparable unit or outcome that was not subject to the intervention but would have been affected by the same historical confounders. If tobacco advertising was banned only in one state, the same-month trend in a neighboring state serves as a control; if lung cancer trends diverge only in the treated state, you gain confidence. When no control series is available, you must argue persuasively that no plausible alternative explanation coincides with the intervention's timing — a harder argumentative burden.

ITS has a natural home in policy evaluation precisely because many policies are implemented population-wide at a specific moment: speed limit changes, vaccine rollouts, sentencing reforms, financial regulations. Randomization is impossible; difference-in-differences may lack clean controls; regression discontinuity requires a continuous assignment variable. ITS asks only for a sharp temporal boundary and a long enough pre-period to establish the baseline trend reliably. The longer and more stable the pre-intervention series, the more credible the counterfactual projection — which is why ITS studies in public health routinely use 24–48 months of pre-data and why administrative data archives matter so much to the design's feasibility.

## Questions

```yaml
- question: "An ITS study finds a significant level change but no slope change after a new seat-belt law takes effect. What does each finding tell you?"
  type: short-answer
  answer: "The level change indicates an immediate, step-function effect — compliance jumped when the law took effect. The absence of a slope change means there was no gradual trend acceleration afterward; the benefit was front-loaded. This suggests the law worked through immediate behavioral compliance rather than gradual norm change."
  explanation: "Distinguishing level from slope effects is central to ITS interpretation. They imply different causal mechanisms and different long-run projections."

- question: "A researcher uses ITS to evaluate a statewide gun-control law passed in March. A major mass shooting had occurred in February of the same year. Why is this a problem, and what can the researcher do?"
  type: short-answer
  answer: "The February shooting is a simultaneous shock — it may have independently changed behavior or public attention regardless of the law. The researcher should add a control series (a comparable state without the law) to check whether gun-related outcomes changed similarly there, and should conduct a placebo test examining whether the apparent 'effect' shows up in outcomes unrelated to gun control."
  explanation: "Simultaneous shocks are the core validity threat in ITS. The researcher must argue that the timing of the intervention is independent of the confounder, or use design controls to isolate the law's effect."
```
