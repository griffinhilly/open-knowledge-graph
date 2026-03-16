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
stage: advanced
status: draft
---

# Cox Proportional Hazards Model

## Core Idea
The Cox proportional hazards model is a semi-parametric regression for time-to-event data that estimates adjusted hazard ratios (HRs) comparing groups while controlling for confounders. It assumes the hazard ratio is constant over time (proportional hazards assumption). Cox regression is flexible, accommodates censoring naturally, and permits simultaneous adjustment for multiple covariates.

## Explainer

From your work with the **Kaplan-Meier estimator**, you know how to describe survival curves for two or more groups and use the log-rank test to ask whether they differ. But KM has a critical limitation: it cannot adjust for confounders. If treated and untreated patients differ in age, disease severity, and comorbidities, a raw KM comparison conflates the treatment effect with selection bias. The **Cox proportional hazards model** solves this by extending survival analysis into a regression framework — the same intuition as moving from comparing group means to running a regression that controls for covariates.

The Cox model works with the **hazard function** h(t): the instantaneous rate of experiencing the event at time t, conditional on having survived to t. Think of it as the risk per unit of time at a particular moment. The model specifies that each subject's hazard is their baseline hazard h₀(t) — shared by everyone and left unspecified — multiplied by an exponential function of their covariates: h(t|X) = h₀(t) × exp(β₁X₁ + β₂X₂ + ...). This is why Cox is called **semi-parametric**: the covariate part is fully specified (parametric), but the baseline hazard is left completely flexible (non-parametric). You never need to assume survival follows an exponential or Weibull distribution. The model estimates the βs from the data using **partial likelihood**, a clever method that conditions on who is at risk at each event time — this naturally handles censored observations, which are the norm in longitudinal studies.

The coefficient β₁ exponentiated gives the **hazard ratio** (HR) for a one-unit change in X₁: HR = exp(β₁). An HR of 1.5 means the hazard rate for the exposed group is 50% higher at every point in time compared to the reference group, after adjusting for all other covariates in the model. This constant-ratio relationship is the **proportional hazards assumption**: the ratio of any two subjects' hazards stays the same over time. It doesn't mean the hazard itself is constant (it changes for everyone as time passes), only that the *ratio* between groups doesn't change. Practically, this means the survival curves should diverge (or converge) proportionally rather than crossing. Crossing Kaplan-Meier curves are a warning sign that this assumption is violated.

Testing the proportional hazards assumption is standard practice. The most common method uses **Schoenfeld residuals**: if the assumption holds, residuals for each covariate should be uncorrelated with time. Violations require remedies — stratifying by the violating variable (allowing its baseline hazard to be group-specific), adding a time-interaction term (HR(t) = exp(β + γ·time)), or switching to a parametric or time-varying-coefficient model. Cox regression is the workhorse of survival analysis in clinical and epidemiologic research precisely because it pairs KM-style flexibility about the underlying time process with the confounder-adjusting power of regression — letting you answer "what is the adjusted hazard ratio for treatment, holding everything else equal?" with minimal distributional assumptions.
