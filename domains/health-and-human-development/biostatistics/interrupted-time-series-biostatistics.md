---
id: interrupted-time-series-biostatistics
title: Interrupted Time Series Analysis
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: difference-in-differences-biostatistics
  type: soft
- id: linear-regression
  type: hard
- id: study-design-biostatistics
  type: hard
builds-toward: []
tags:
- interrupted-time-series-biostatistics
- ITS
- segmented-regression
- policy-evaluation
- autocorrelation
stage: expert
status: validated
---

# Interrupted Time Series Analysis

## Core Idea
Interrupted time series (ITS) analysis evaluates the impact of an intervention at a known time point by modeling the outcome trend before and after the intervention. The approach uses segmented regression with four key parameters: the pre-intervention level, the pre-intervention trend (slope), the immediate level change at the intervention point, and the change in trend after the intervention. Unlike DiD, ITS can be applied with a single group (no control series needed), relying instead on the pre-intervention trend to project the counterfactual trajectory that would have occurred without the intervention. The deviation of the observed post-intervention trajectory from this counterfactual provides the estimated intervention effect. ITS must account for autocorrelation in the time series (observations close in time are correlated) and is most convincing when the pre-intervention series is long enough to establish a stable trend.

## Questions

```yaml
- question: "An ITS analysis of a hand hygiene intervention in a hospital models monthly infection rates for 24 months before and 24 months after the intervention. The model estimates two types of effects: a level change (immediate) and a trend change (gradual). Why is distinguishing between these two effects important?"
  type: multiple-choice
  options:
    - "Only the level change matters because it represents the true intervention effect"
    - "An intervention might produce an immediate drop in infections (level change) and also alter the ongoing trajectory (trend change) — capturing both provides a complete picture of the intervention's impact over time"
    - "The trend change is always larger than the level change"
    - "The distinction is only important for statistical reasons, not for clinical interpretation"
  answer: 1
  explanation: "Some interventions produce immediate effects (a new antibiotic formulary reducing infections immediately) while others change the rate of improvement (a quality improvement program that gradually reduces infections over months). Some produce both. An ITS model that only captures level change would miss a gradual effect that accumulates over time; one that only captures trend change would miss an immediate impact. The segmented regression framework estimates both, allowing researchers to distinguish between immediate and sustained impacts of the intervention."

- question: "An ITS analysis uses OLS regression and finds a significant level change after a policy intervention. However, the Durbin-Watson statistic is 0.8. What is the concern?"
  type: multiple-choice
  options:
    - "The model has too many parameters"
    - "The Durbin-Watson statistic of 0.8 indicates strong positive autocorrelation — standard errors from OLS are too small because consecutive observations are not independent, inflating the significance of the intervention effect"
    - "The intervention effect is overestimated by 0.8"
    - "The pre-intervention trend was not linear"
  answer: 1
  explanation: "Time series data are typically autocorrelated — adjacent monthly observations are more similar than distant ones. OLS assumes independence of errors, producing standard errors that are too small when autocorrelation is present. A Durbin-Watson statistic well below 2 indicates positive autocorrelation. Solutions include Newey-West standard errors, generalized least squares (GLS) with an autoregressive error structure, or ARIMA-based ITS models. Ignoring autocorrelation leads to false significance — an apparent intervention effect that is really just serial correlation."

- question: "ITS is often considered a strong quasi-experimental design even without a concurrent control group because the pre-intervention trend serves as the counterfactual. What is the main threat to this internal validity?"
  type: short-answer
  answer: "A co-occurring event or change that happens at the same time as the intervention (a 'history' threat) could produce the observed change in level or trend. Without a control group, it is impossible to distinguish the intervention effect from other changes occurring simultaneously. For example, if a hospital implements hand hygiene protocols at the same time a new antibiotic is introduced, the ITS cannot separate their effects. Adding a control series (a similar hospital without the intervention) substantially strengthens the design by controlling for co-occurring temporal events."
  explanation: "This is the fundamental limitation of single-group ITS designs. The pre-intervention trend controls for existing trajectories but cannot account for new events coinciding with the intervention. The addition of a control series creates a controlled ITS (similar to DiD with time series data), which is considered one of the strongest quasi-experimental designs because it combines the trend-based counterfactual with a between-group comparison."
```

## Explainer

Many health interventions are implemented at a specific point in time — a hospital installs hand sanitizer dispensers, a government bans a pesticide, or a new prescribing guideline takes effect. **Interrupted time series** analysis is designed for exactly this situation: you have repeated measurements of an outcome over time, and an intervention occurs at a known point, "interrupting" the series. The question is whether the series changes after the intervention in a way that would not have occurred otherwise.

The standard approach is **segmented regression**, which fits a piecewise linear model with four parameters. The **pre-intervention intercept** and **pre-intervention slope** establish the baseline trend. The **level change** (the coefficient on a step function at the intervention point) captures any immediate jump or drop in the outcome. The **trend change** (the coefficient on the interaction between time and the post-intervention indicator) captures any change in the ongoing slope after the intervention. The counterfactual — what would have happened without the intervention — is the extrapolation of the pre-intervention trend into the post-intervention period.

Two technical issues require attention. First, time series data exhibit **autocorrelation** — observations close in time are more similar than distant ones. OLS assumes independence and produces standard errors that are too small when autocorrelation is present. Solutions include Newey-West robust standard errors, generalized least squares with an autoregressive error structure (e.g., AR(1)), or full ARIMA modeling. Second, **seasonality** is common in health data (influenza peaks in winter, trauma peaks in summer). If the intervention point coincides with a seasonal pattern, the apparent intervention effect may be spurious. Including seasonal indicators (monthly dummy variables or harmonic terms) controls for this.

The main threat to ITS validity is **co-intervention** — something else changing at the same time as the intervention. A single-group ITS cannot distinguish between the intended intervention and a coincident policy change, staffing shift, or data collection modification. Adding a **control series** — a comparable population that did not receive the intervention — transforms the design into a controlled ITS, which controls for any temporal event that affects both groups equally. This is closely related to DiD but leverages the full time series rather than collapsing to pre-post means, making it more powerful and more informative about the temporal dynamics of the intervention effect.
