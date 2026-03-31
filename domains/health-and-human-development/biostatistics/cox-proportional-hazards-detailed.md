---
id: cox-proportional-hazards-detailed
title: Cox Proportional Hazards Model
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: survival-analysis-kaplan-meier
  type: hard
- id: log-rank-test
  type: hard
- id: logistic-regression-biostatistics
  type: soft
- id: linear-regression
  type: hard
builds-toward:
- time-varying-covariates
- competing-risks-analysis-biostatistics
- joint-longitudinal-survival-models
tags:
- Cox
- proportional-hazards
- hazard-ratio
- partial-likelihood
- semi-parametric
stage: expert
status: validated
---

# Cox Proportional Hazards Model

## Core Idea
The Cox proportional hazards model relates the hazard (instantaneous event rate) to covariates without specifying the baseline hazard function: h(t|X) = h_0(t) × exp(beta_1*x_1 + ... + beta_k*x_k). This semi-parametric structure separates the time dependence (absorbed into the unspecified h_0(t)) from the covariate effects (the exponential term). Exponentiated coefficients exp(beta_j) are hazard ratios — the multiplicative change in the instantaneous event rate per unit increase in x_j. The proportional hazards assumption requires that these hazard ratios remain constant over time: the curves for different covariate values can never cross on the hazard scale. Estimation uses partial likelihood, which depends only on the ordering of event times and eliminates h_0(t), making the model remarkably flexible yet powerful.

## Questions

```yaml
- question: "A Cox model of mortality after cardiac surgery includes age, sex, and ejection fraction. The hazard ratio for female sex is 0.75. What does this mean?"
  type: multiple-choice
  options:
    - "Females have a 75% higher hazard of death compared to males"
    - "Females have a 25% lower instantaneous rate of death at any time point compared to males with the same age and ejection fraction"
    - "75% of females survive the surgery"
    - "The median survival for females is 0.75 times the median survival for males"
  answer: 1
  explanation: "A hazard ratio of 0.75 means the hazard (instantaneous event rate) for females is 75% of the hazard for males, adjusted for age and ejection fraction — equivalently, a 25% lower hazard. Under the proportional hazards assumption, this ratio holds at every time point. It does not directly translate to a difference in median survival or a survival probability without additional information about the baseline hazard."

- question: "The Cox model's semi-parametric nature means it does not require specifying the baseline hazard function h_0(t). Why is this considered an advantage over fully parametric survival models?"
  type: multiple-choice
  options:
    - "It makes the model faster to compute"
    - "It avoids the need to assume a particular distributional form for event times (exponential, Weibull, etc.), making the model robust to misspecification of the time dependence"
    - "It eliminates the need for the proportional hazards assumption"
    - "It allows the model to handle continuous outcomes, not just time-to-event data"
  answer: 1
  explanation: "Parametric models (exponential, Weibull, log-normal) require specifying the mathematical form of the baseline hazard — if this specification is wrong, the covariate effect estimates may be biased. The Cox model leaves h_0(t) completely unspecified and estimates covariate effects using only the relative ordering of event times (partial likelihood). This semi-parametric approach sacrifices some efficiency when the parametric form is correct but gains robustness when it is not — a favorable tradeoff in most applied settings where the true hazard shape is unknown."

- question: "Schoenfeld residuals plotted against time show a clear upward trend for a covariate in a Cox model. This indicates the proportional hazards assumption holds for that covariate."
  type: true-false
  answer: false
  explanation: "Schoenfeld residuals that trend with time indicate a violation of the proportional hazards assumption — the effect of that covariate is changing over time rather than remaining constant. Under proportional hazards, Schoenfeld residuals should show no systematic pattern over time (random scatter around zero). A trend suggests the hazard ratio increases or decreases as time progresses, and the model may need a time-covariate interaction, stratification by that variable, or a time-varying coefficient approach."

- question: "Explain how partial likelihood estimation allows the Cox model to estimate covariate effects without specifying the baseline hazard."
  type: short-answer
  answer: "At each event time, partial likelihood considers only which subject experienced the event relative to all subjects still at risk. The probability that the specific subject who died is the one who died, given that one death occurred, depends only on the relative hazard values exp(Xβ) across subjects in the risk set — the baseline hazard h_0(t) cancels because it multiplies both the numerator and denominator equally. The partial likelihood is the product of these conditional probabilities across all event times, and maximizing it yields estimates of β without ever estimating h_0(t)."
  explanation: "Cox's key insight was that the ordering of events contains sufficient information to estimate covariate effects. At each event time, the partial likelihood asks: given the risk set (everyone who could have had an event), what is the probability that the subject with covariates X_i is the one who did? This depends on exp(X_i β) / sum of exp(X_j β) over all j at risk — which is structurally identical to a conditional logistic regression. The baseline hazard determines when events tend to happen but not who they happen to, so the covariate effects are identifiable without it."
```

## Explainer

The Kaplan-Meier estimator and log-rank test compare survival between groups but cannot adjust for multiple covariates simultaneously. If Treatment A enrolls older, sicker patients, the unadjusted KM comparison is confounded. The **Cox proportional hazards model** solves this by relating the hazard to multiple covariates through a multiplicative model: h(t|X) = h_0(t) × exp(Xβ). This is to survival analysis what multiple regression is to continuous outcomes — it allows you to estimate the independent effect of each variable while controlling for others.

The model's defining feature is its **semi-parametric** structure. The baseline hazard h_0(t) — which captures how the overall event rate changes with time — is left completely unspecified. All the parametric assumptions are in the covariate effects: the exponential term exp(Xβ) multiplies the baseline hazard by a constant factor that depends on the patient's characteristics but not on time. This means the model assumes that the ratio of hazards for any two patients remains constant throughout follow-up. If Patient A has twice the hazard of Patient B at 1 year, the model requires this ratio to hold at 5 years and 10 years as well. This is the **proportional hazards assumption**.

Estimation uses **partial likelihood**, a concept introduced by Cox in his landmark 1972 paper. The key insight is that the covariate effects can be estimated from the event ordering alone. At each event time, consider all subjects still at risk. The probability that the specific subject who experienced the event is the one who did depends on the relative hazards exp(Xβ) across all subjects at risk — and the baseline hazard cancels out of this conditional probability because it multiplies both numerator and denominator. The partial likelihood is the product of these conditional probabilities across all event times. Maximizing it yields β estimates without ever estimating h_0(t). If h_0(t) is needed (for predicted survival curves), it can be recovered afterward using the Breslow estimator.

Checking the proportional hazards assumption is essential. If the assumption fails — say, a new drug reduces early mortality but its effect wanes with time — the hazard ratio is not constant, and the Cox model produces a single hazard ratio that averages over time in a potentially misleading way. Diagnostics include plotting **Schoenfeld residuals** against time (a trend indicates violation), testing the significance of a time-covariate interaction, and visually inspecting log-log survival plots (parallel curves support proportional hazards). When the assumption fails, remedies include stratifying on the offending variable, including a time-covariate interaction, or using models that explicitly allow time-varying effects.
