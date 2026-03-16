---
id: interrupted-time-series-analysis
title: Interrupted Time Series Design
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: difference-in-differences
  type: soft
- id: temporal-clustering-analysis
  type: soft
tags:
- time-series
- policy-evaluation
- intervention-effects
stage: advanced
status: draft
---

# Interrupted Time Series Design

## Core Idea
Interrupted time series (ITS) exploits a known intervention timepoint to estimate its effect on disease incidence. Regression models fit pre- and post-intervention trends, testing whether the intervention caused a level change and/or slope change. ITS accommodates seasonality and is useful when randomization or comparison groups are infeasible.

## Explainer

From your study of difference-in-differences, you know that causal inference in observational data requires comparing what happened to what *would have happened* in the absence of the intervention — the counterfactual. Difference-in-differences constructs that counterfactual using a comparison group. **Interrupted time series (ITS)** takes a different path: instead of comparing treated and untreated groups at two time points, it uses *the same group's own prior trend* as the counterfactual. If monthly hospital admissions were declining at a steady rate before a new health policy was implemented, the ITS model projects that trend forward and asks: after the intervention, did admissions deviate from where the pre-intervention trend predicted they would be?

The statistical model encodes this logic in regression form. A simple ITS model includes three terms beyond baseline: (1) a **time** variable capturing the underlying secular trend, (2) a binary **intervention indicator** (0 = pre-intervention, 1 = post-intervention) capturing any immediate **level change** at the break point, and (3) an **interaction between time and intervention** capturing a change in *slope* — whether the trend itself accelerated or decelerated after the intervention. The key question is whether the coefficients on terms 2 and 3 are significantly different from zero. A policy that reduces hospitalizations might show a sudden drop (level change), a change in the rate of decline (slope change), both, or neither. The model distinguishes these scenarios explicitly.

**Seasonality** is a major practical complication. Many health outcomes cycle predictably with the calendar — flu peaks in winter, drowning in summer, respiratory illness in autumn. If an intervention is implemented in October and the outcome rises through December, a naive analysis might attribute the rise to the intervention when it reflects the usual autumn pattern. ITS models address this by including Fourier terms (sine and cosine functions of time) or month indicators to explicitly model periodic variation. Failure to do so produces a biased estimate of the intervention effect. This is one reason ITS requires a sufficiently long pre-intervention series — you need enough data to characterize the seasonal pattern before the break.

The key threats to ITS validity are **secular trends** that coincide with the intervention, **regression to the mean** (the intervention may have been triggered by an unusual spike, which would naturally resolve), and **co-interventions** (other events happening simultaneously). The strongest ITS designs include a **control series** — a similar outcome from a population or location that experienced the same secular trends and seasonal patterns but was *not* subject to the intervention. When treated and control series move together in the pre-period but diverge after the intervention, the causal inference is substantially more credible. This controlled ITS is essentially the time-series analog of difference-in-differences, combining the richness of longitudinal data with the structure of a comparison group.
