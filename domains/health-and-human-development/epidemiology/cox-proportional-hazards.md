---
id: cox-proportional-hazards
title: Cox Proportional Hazards Model
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: kaplan-meier-estimator
  type: hard
- id: multivariable-regression-epi
  type: soft
tags:
- cox-regression
- hazard-ratio
- survival-analysis
- semi-parametric
stage: expert
status: draft
---

# Cox Proportional Hazards Model

## Core Idea
The Cox proportional hazards model is a semi-parametric regression for time-to-event data that estimates adjusted hazard ratios (HRs) comparing groups while controlling for confounders. It assumes the hazard ratio is constant over time (proportional hazards assumption). Cox regression is flexible, accommodates censoring naturally, and permits simultaneous adjustment for multiple covariates.

## Questions

```yaml
- question: "In a clinical trial, the Cox model estimates a hazard ratio of 0.6 for the treated group versus controls. At month 12, the control group's hazard is 0.08 events/month. Under the proportional hazards assumption, what is the treated group's hazard at month 12?"
  type: multiple-choice
  options:
    - "0.6 events/month — the hazard ratio directly gives the treated group's hazard rate"
    - "0.048 events/month — the hazard ratio multiplies the baseline hazard: 0.6 × 0.08"
    - "0.048 events/month, but only if the baseline hazard is constant over time"
    - "Cannot be determined without fitting a parametric survival model to specify the baseline hazard"
  answer: 1
  explanation: "The Cox model specifies h(t|X) = h₀(t) × exp(βX). For the treated group, HR = exp(β) = 0.6, so h_treated(t) = 0.6 × h₀(t) at every time point t. At month 12: h_treated = 0.6 × 0.08 = 0.048 events/month. This is the proportional hazards assumption in action — the hazard ratio is constant across time, so you can compute the treated group's hazard at any time point by multiplying the control group's hazard by 0.6. The baseline hazard h₀(t) does NOT need to be constant over time — it can be any function of t. The Cox model leaves it completely unspecified."

- question: "After fitting a Cox model, the Kaplan-Meier survival curves for the treated and control groups cross at month 18. Why is this a concern?"
  type: multiple-choice
  options:
    - "Crossing curves indicate a data entry error in the recorded event times"
    - "Crossing curves suggest the proportional hazards assumption is violated — the hazard ratio appears to change direction over time"
    - "Crossing curves indicate the treatment is definitively harmful after month 18 and the trial should be stopped"
    - "Crossing curves mean the log-rank test statistic cannot be computed"
  answer: 1
  explanation: "If the proportional hazards assumption holds, survival curves for two groups should diverge (or stay proportionally apart) without crossing — one group should consistently have lower hazard than the other. When KM curves cross, it means that one group has higher hazard early and lower hazard late (or vice versa), implying the hazard ratio changes sign over time. This directly violates the proportional hazards assumption. The formal test uses Schoenfeld residuals, but visually crossing KM curves are a warning sign that Cox regression may produce misleading results without modification (e.g., adding a time-interaction term)."

- question: "The proportional hazards assumption in the Cox model requires that the hazard rate for each group remains constant over time."
  type: true-false
  answer: false
  explanation: "This is the most common misstatement of the PH assumption. The assumption is NOT that hazards are constant over time — that would be an exponential distribution assumption. The assumption is that the *ratio* of any two groups' hazards is constant over time. Both the treated and control hazards can vary freely (and typically do — hazard often increases with age or disease duration), as long as they vary proportionally. This is why Cox is called semi-parametric: the baseline hazard h₀(t) is left completely unspecified and can have any shape, but the ratio between groups is fixed at exp(β)."

- question: "The Cox model's semi-parametric nature means it can estimate adjusted hazard ratios for multiple covariates without requiring the analyst to specify the shape of the underlying survival time distribution."
  type: true-false
  answer: true
  explanation: "This is the key practical advantage of Cox regression over parametric survival models (exponential, Weibull, log-normal). The 'semi' in semi-parametric refers to this split: the covariate effects are fully parametrized (βs estimated from partial likelihood), but the baseline hazard h₀(t) is left entirely non-parametric — it is never modeled or estimated directly. The partial likelihood cleverly conditions on who is at risk at each event time, extracting information about the βs without ever needing to specify or estimate h₀(t). This gives Cox regression the flexibility of non-parametric methods with the confounder-adjustment power of regression."

- question: "Why is the Cox proportional hazards model preferred over a simple comparison of Kaplan-Meier curves when analyzing an observational study comparing treated and untreated patients?"
  type: short-answer
  answer: "Kaplan-Meier curves describe survival patterns for groups as observed, without adjusting for any differences in patient characteristics. In an observational study, treated and untreated patients may differ systematically in age, disease severity, comorbidities, or other confounders — making a raw KM comparison misleading. The Cox model is a regression framework that can simultaneously adjust for multiple covariates, estimating the treatment hazard ratio 'holding all other measured covariates equal.' This confounder adjustment is essential for causal inference in observational data. Additionally, the Cox model can handle continuous covariates, interactions, and time-varying covariates — capabilities KM cannot provide."
  explanation: "The parallel to linear regression is useful: just as a t-test comparing group means is replaced by multiple regression when confounders are present, the log-rank test comparing KM curves is replaced by Cox regression. Both pairs of methods address the same limitation — unadjusted group comparisons conflate the effect of interest with confounding. Cox regression is to survival outcomes what linear regression is to continuous outcomes."
```

## Explainer

From your work with the **Kaplan-Meier estimator**, you know how to describe survival curves for two or more groups and use the log-rank test to ask whether they differ. But KM has a critical limitation: it cannot adjust for confounders. If treated and untreated patients differ in age, disease severity, and comorbidities, a raw KM comparison conflates the treatment effect with selection bias. The **Cox proportional hazards model** solves this by extending survival analysis into a regression framework — the same intuition as moving from comparing group means to running a regression that controls for covariates.

The Cox model works with the **hazard function** h(t): the instantaneous rate of experiencing the event at time t, conditional on having survived to t. Think of it as the risk per unit of time at a particular moment. The model specifies that each subject's hazard is their baseline hazard h₀(t) — shared by everyone and left unspecified — multiplied by an exponential function of their covariates: h(t|X) = h₀(t) × exp(β₁X₁ + β₂X₂ + ...). This is why Cox is called **semi-parametric**: the covariate part is fully specified (parametric), but the baseline hazard is left completely flexible (non-parametric). You never need to assume survival follows an exponential or Weibull distribution. The model estimates the βs from the data using **partial likelihood**, a clever method that conditions on who is at risk at each event time — this naturally handles censored observations, which are the norm in longitudinal studies.

The coefficient β₁ exponentiated gives the **hazard ratio** (HR) for a one-unit change in X₁: HR = exp(β₁). An HR of 1.5 means the hazard rate for the exposed group is 50% higher at every point in time compared to the reference group, after adjusting for all other covariates in the model. This constant-ratio relationship is the **proportional hazards assumption**: the ratio of any two subjects' hazards stays the same over time. It doesn't mean the hazard itself is constant (it changes for everyone as time passes), only that the *ratio* between groups doesn't change. Practically, this means the survival curves should diverge (or converge) proportionally rather than crossing. Crossing Kaplan-Meier curves are a warning sign that this assumption is violated.

Testing the proportional hazards assumption is standard practice. The most common method uses **Schoenfeld residuals**: if the assumption holds, residuals for each covariate should be uncorrelated with time. Violations require remedies — stratifying by the violating variable (allowing its baseline hazard to be group-specific), adding a time-interaction term (HR(t) = exp(β + γ·time)), or switching to a parametric or time-varying-coefficient model. Cox regression is the workhorse of survival analysis in clinical and epidemiologic research precisely because it pairs KM-style flexibility about the underlying time process with the confounder-adjusting power of regression — letting you answer "what is the adjusted hazard ratio for treatment, holding everything else equal?" with minimal distributional assumptions.
