---
id: survival-analysis-econometrics
title: Survival Analysis and Duration Models
domain: economics
course: econometrics
prerequisites:
- id: maximum-likelihood-econometrics
  type: hard
- id: time-series-basics-econometrics
  type: soft
tags:
- survival-analysis
- duration
- hazard-rate
stage: advanced
status: draft
---

# Survival Analysis and Duration Models

## Core Idea
Duration models analyze the time until an event occurs (unemployment spells, firm entry/exit, marriage dissolution). The hazard rate measures the instantaneous risk of the event; Cox proportional hazards and parametric models estimate covariate effects.

## Explainer

Standard regression models assume your outcome variable is a number you observe for every unit in the sample. But many economically important outcomes are *durations* — the length of time until something happens: how long a worker stays unemployed, how long a firm survives before exit, how long a loan remains current before default. These outcomes violate a basic assumption of standard regression: many observations are **censored**, meaning the event hasn't occurred yet when your data collection ends. A worker still unemployed at the end of your survey is not the same as a worker with infinite unemployment — you know their spell lasted *at least* as long as the observation window. Ignoring censoring by dropping or coding these observations causes severe selection bias. Survival analysis handles censoring correctly by building it directly into the likelihood function.

The central object in survival analysis is the **survival function** S(t), which gives the probability that the event has not yet occurred by time t: S(t) = P(T > t). Related to it is the **hazard function** h(t), which measures the instantaneous risk of the event at time t, conditional on having survived until t. Mathematically, h(t) = lim Δt→0 [P(t ≤ T < t + Δt | T ≥ t)] / Δt. The hazard is not a probability but a rate — it can exceed 1 — and its shape reveals whether the event becomes more likely over time (**positive duration dependence**, like machine failure) or less likely (**negative duration dependence**, like unemployment spells that become harder to exit the longer they last). This connection between your maximum likelihood prerequisite and survival analysis is direct: you construct the likelihood by multiplying contributions from observed events and censored observations, and maximize over the parameters.

The **Cox proportional hazards model** is the workhorse of applied survival analysis. It specifies that the hazard for individual i at time t is h(t|Xᵢ) = h₀(t) · exp(Xᵢ'β), where h₀(t) is an unspecified **baseline hazard** and exp(Xᵢ'β) is a multiplicative factor depending on covariates. The "proportional" in the name means that covariates scale the hazard by a constant factor across time — if being a college graduate reduces the unemployment exit hazard by 30% at week 10, it reduces it by 30% at week 30 too. The genius of Cox's approach is that you can estimate the covariate coefficients β using **partial likelihood** without ever specifying h₀(t). This semiparametric structure makes the model highly flexible and is why it dominates applied work: you get covariate estimates without committing to a parametric duration distribution.

Parametric alternatives — exponential (constant hazard), Weibull (monotone hazard), log-logistic (non-monotone) — impose a specific shape on h₀(t) and can be more efficient when that shape is correct, but are sensitive to misspecification. The choice between Cox and parametric models parallels the tradeoffs you've seen elsewhere in econometrics between flexibility and efficiency. A critical practical skill is testing the proportional hazards assumption — if hazard ratios change over time (e.g., the effect of education on re-employment fades as duration lengthens), stratified models or time-varying covariates are needed. Duration models connect naturally to time series concepts you've studied: duration dependence is essentially autocorrelation in the hazard, and unobserved heterogeneity in survival models (the "frailty" problem) mirrors omitted variable bias in standard regression.
