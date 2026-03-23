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
stage: expert
status: draft
---

# Interrupted Time Series Design

## Core Idea
Interrupted time series (ITS) exploits a known intervention timepoint to estimate its effect on disease incidence. Regression models fit pre- and post-intervention trends, testing whether the intervention caused a level change and/or slope change. ITS accommodates seasonality and is useful when randomization or comparison groups are infeasible.

## Questions

```yaml
- question: "Monthly emergency department visits were rising before an intervention. After the intervention, visits continue rising — but at a slower rate. What is the correct ITS interpretation?"
  type: multiple-choice
  options:
    - "The intervention had no effect because visits continued to increase"
    - "The intervention caused a negative level change at the breakpoint"
    - "The intervention caused a negative slope change — the trend still went up, but grew more slowly"
    - "ITS cannot be interpreted when the outcome moves in the same direction before and after"
  answer: 2
  explanation: "ITS distinguishes two types of intervention effects: an immediate level change (a jump or drop at the breakpoint) and a slope change (a change in the rate of trend). Visits continuing to rise but more slowly is a negative slope change — the intervention didn't reverse the trend, it decelerated it. Option A is the classic misconception: equating 'no reversal' with 'no effect,' which ignores slope-change detection entirely."

- question: "What is the fundamental difference between ITS and a simple pre-post comparison of means?"
  type: multiple-choice
  options:
    - "ITS requires a comparison group; pre-post comparison does not"
    - "ITS explicitly models the pre-intervention trend and tests whether outcomes deviated from where that trend predicted they would be"
    - "ITS can only detect level changes, while pre-post comparisons measure both level and slope changes"
    - "Pre-post comparison controls for seasonality; ITS does not"
  answer: 1
  explanation: "The core ITS insight is that the pre-intervention trend itself serves as the counterfactual — what would have happened without the intervention. The model projects that trend forward and asks whether the post-intervention data deviates from the projection. A simple pre-post comparison of means ignores whether a trend was already present, making it unable to distinguish a genuine intervention effect from a continuation of an existing trajectory."

- question: "A statistically significant level change at the ITS intervention point proves that the intervention caused that change."
  type: true-false
  answer: false
  explanation: "A significant level change is consistent with causation but does not prove it. The key threats to ITS validity are co-interventions (other events occurring simultaneously at the breakpoint) and secular trends that coincide with the intervention. If a new hospital policy and a nationwide health campaign both launched in the same month, the level change could reflect either or both. Strong causal inference requires ruling out these competing explanations, ideally through a control series that shares secular trends but was not exposed to the intervention."

- question: "Seasonality in the outcome variable can be addressed within an ITS regression model by including Fourier terms or monthly indicator variables."
  type: true-false
  answer: true
  explanation: "Many health outcomes cycle predictably with the calendar — flu peaks in winter, drowning in summer. If an intervention coincides with a seasonal peak, a naive ITS model will misattribute the seasonal change to the intervention. Fourier terms (sine and cosine functions of time) or month indicators model the periodic variation explicitly, separating seasonal effects from the estimated intervention effect. This is why a long pre-intervention series is important: you need enough data to characterize the seasonal pattern before the breakpoint."

- question: "Why is a long pre-intervention time series important for ITS validity, and which two specific threats does sufficient pre-intervention data most directly address?"
  type: short-answer
  answer: "A long pre-intervention series is essential for two reasons: (1) it allows the model to reliably estimate the underlying secular trend and seasonal pattern, providing a credible counterfactual against which to measure post-intervention deviation; (2) it helps distinguish a genuine intervention effect from regression to the mean — if the intervention was triggered by an unusual spike, a long baseline shows whether the spike was anomalous or part of a real trend. Without sufficient pre-intervention data, the trend estimate is unreliable, and seasonal confounding cannot be adequately controlled."
  explanation: "The ITS design's strength is using the unit's own prior trajectory as the counterfactual. But this requires that trajectory to be well-characterized. Short pre-periods cannot reliably separate seasonal patterns from trend. They also cannot identify regression to the mean: an outcome that triggered intervention by spiking unusually high will naturally decline afterward, which can mimic a genuine intervention effect. A long pre-period makes these confounds visible and estimable."
```

## Explainer

From your study of difference-in-differences, you know that causal inference in observational data requires comparing what happened to what *would have happened* in the absence of the intervention — the counterfactual. Difference-in-differences constructs that counterfactual using a comparison group. **Interrupted time series (ITS)** takes a different path: instead of comparing treated and untreated groups at two time points, it uses *the same group's own prior trend* as the counterfactual. If monthly hospital admissions were declining at a steady rate before a new health policy was implemented, the ITS model projects that trend forward and asks: after the intervention, did admissions deviate from where the pre-intervention trend predicted they would be?

The statistical model encodes this logic in regression form. A simple ITS model includes three terms beyond baseline: (1) a **time** variable capturing the underlying secular trend, (2) a binary **intervention indicator** (0 = pre-intervention, 1 = post-intervention) capturing any immediate **level change** at the break point, and (3) an **interaction between time and intervention** capturing a change in *slope* — whether the trend itself accelerated or decelerated after the intervention. The key question is whether the coefficients on terms 2 and 3 are significantly different from zero. A policy that reduces hospitalizations might show a sudden drop (level change), a change in the rate of decline (slope change), both, or neither. The model distinguishes these scenarios explicitly.

**Seasonality** is a major practical complication. Many health outcomes cycle predictably with the calendar — flu peaks in winter, drowning in summer, respiratory illness in autumn. If an intervention is implemented in October and the outcome rises through December, a naive analysis might attribute the rise to the intervention when it reflects the usual autumn pattern. ITS models address this by including Fourier terms (sine and cosine functions of time) or month indicators to explicitly model periodic variation. Failure to do so produces a biased estimate of the intervention effect. This is one reason ITS requires a sufficiently long pre-intervention series — you need enough data to characterize the seasonal pattern before the break.

The key threats to ITS validity are **secular trends** that coincide with the intervention, **regression to the mean** (the intervention may have been triggered by an unusual spike, which would naturally resolve), and **co-interventions** (other events happening simultaneously). The strongest ITS designs include a **control series** — a similar outcome from a population or location that experienced the same secular trends and seasonal patterns but was *not* subject to the intervention. When treated and control series move together in the pre-period but diverge after the intervention, the causal inference is substantially more credible. This controlled ITS is essentially the time-series analog of difference-in-differences, combining the richness of longitudinal data with the structure of a comparison group.
