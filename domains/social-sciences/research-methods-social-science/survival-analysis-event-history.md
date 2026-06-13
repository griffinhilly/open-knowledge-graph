---
id: survival-analysis-event-history
title: Survival Analysis and Event History Methods
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: linear-regression-social-science
  type: hard
- id: exponential-distribution
  type: soft
- id: probability-mass-functions
  type: soft
- id: differential-equations-intro
  type: soft
tags:
- survival-analysis
- event-history
- duration
- censoring
stage: advanced
status: validated
---

# Survival Analysis and Event History Methods

## Core Idea
Event history methods analyze timing of social events—divorce, job transitions, political regime changes. These methods handle censoring (incomplete observation periods) and allow time-varying covariates. Survival curves and hazard functions describe rates of event occurrence over time.

## Questions

```yaml
- question: "A study tracks how long it takes laid-off workers to find new employment, ending after 2 years. Some workers have not found employment by the study's end. A researcher proposes excluding these workers since the event was never observed. Why is this a problem?"
  type: multiple-choice
  options:
    - "It reduces the sample size too much, making the model statistically underpowered"
    - "It introduces selection bias — censored observations contribute information that the subject survived at least 2 years without finding employment, and discarding that information biases results downward"
    - "It violates the proportional hazards assumption required by the Cox model"
    - "It prevents estimation of time-varying covariates since those workers' employment status was never resolved"
  answer: 1
  explanation: "Censored observations are not useless — they are informative about survival up to the censoring point. A worker still unemployed after 2 years tells us their job-finding time exceeds 2 years, which is real data. Excluding them discards that information and biases the analysis by leaving only shorter spells in the sample, making job-finding appear faster than it is. Survival analysis handles censoring correctly by treating these observations as contributing information up to their censoring time without assuming what would have happened afterward."

- question: "The hazard function h(t) is best interpreted as:"
  type: multiple-choice
  options:
    - "The probability that the event has occurred by time t — the cumulative incidence at that point"
    - "The probability that the subject survives beyond time t without experiencing the event"
    - "The instantaneous rate of event occurrence at time t, conditional on having survived to that point"
    - "The expected time until the event occurs, given covariate values measured at baseline"
  answer: 2
  explanation: "The hazard function is a conditional instantaneous rate: how quickly is the event occurring right now, among those who haven't experienced it yet? This conditioning on survival is what makes it distinct from simple probability. Option A describes roughly the CDF; option B describes the survival function S(t). The hazard function can vary over time — divorce risk is highest in early marriage and around the 'seventh year'; political regime vulnerability varies across regime age — capturing patterns that a single regression coefficient cannot represent."

- question: "Standard linear regression is well-suited for analyzing the timing of events like divorce or job transitions, provided time is included as a predictor variable."
  type: true-false
  answer: false
  explanation: "Linear regression cannot handle censoring correctly. When subjects haven't experienced the event by the observation window's end, their event time is unknown — it is 'at least X years,' not a specific value. Including their censoring time as if it were a complete observation creates bias; excluding them discards information. Beyond censoring, regression models the level of an outcome, not the instantaneous rate of event occurrence, which may vary over time in ways a single coefficient cannot capture. Survival analysis was developed specifically to address these problems."

- question: "A hazard ratio of 2 in a Cox proportional hazards model means that the group with that characteristic experiences the event at twice the rate of the reference group at any given point in time, assuming the proportional hazards assumption holds."
  type: true-false
  answer: true
  explanation: "This is the correct interpretation of a Cox hazard ratio. Unlike regression coefficients (which describe differences in levels) or odds ratios (which describe odds), hazard ratios describe the ratio of instantaneous event rates between groups at each moment in time. The proportional hazards assumption states that this ratio remains constant across time — the two groups' hazard functions are parallel on a log scale. Violating this assumption means the hazard ratio changes over time, requiring extensions like time-varying coefficients or stratified models."

- question: "What is censoring in the context of event history analysis, and why does it require a different analytical approach than standard regression?"
  type: short-answer
  answer: "Censoring occurs when a subject is observed for a period but the event of interest has not occurred by the end of observation — for example, a couple still married when a divorce study ends. The event time is unknown; it is only known to exceed the observation period. Standard regression requires a complete outcome value and cannot incorporate this partial information correctly — either excluding censored cases (biasing estimates) or imputing their event time (introducing error). Survival analysis handles censoring by allowing each observation to contribute information about survival up to its censoring point without making any assumption about what would have happened afterward. The likelihood function is constructed to correctly weight complete and censored observations, extracting the maximum information from incomplete data."
  explanation: "Censoring is the fundamental challenge that motivates the entire survival analysis framework. Once you understand it, the survival function, hazard function, and Cox model all follow naturally as tools for extracting information from data where some event times are observed and others are only bounded from below."
```

## Explainer

Your training in linear regression taught you to model the *level* of an outcome — how high or low is Y given X? But many social science questions are about *timing*: not whether someone gets divorced, but when. Not whether a political regime collapses, but how long it survives. Not whether a worker finds a new job, but how quickly after being laid off. Standard regression is poorly suited to timing questions, partly because of a data problem your regression training didn't prepare you for: **censoring**.

**Censoring** occurs when you observe a subject for a period but the event has not yet occurred by the end of observation. A study tracking divorces that ends in 2020 includes couples still married at that date — they haven't experienced the event, but their marriages lasted *at least* as long as the observation window. Simply excluding these cases biases the analysis by discarding information: a marriage that has survived 15 years tells you something important even if it isn't yet ended. Survival analysis incorporates censored observations correctly by treating them as contributing information about survival *up to* the censoring point, even though the event was not observed. Your background in probability distributions — especially the exponential — will help here, since the exponential distribution describes constant-hazard survival processes and is the simplest baseline case.

The two core functions build on your probability background. The **survival function** S(t) gives the probability that the event has not yet occurred by time t — it starts at 1 and declines over time as events accumulate. The **hazard function** h(t) is the instantaneous rate of event occurrence at time t, given that the subject has survived to that point. Think of the hazard as the *risk rate right now for those still at risk* — it can vary over time. Divorce risk is highest in the early years of marriage and again around the seventh year; political regimes are often most vulnerable just after transitional periods. The hazard function captures this time-varying risk in a way that a single regression coefficient cannot.

The **Cox proportional hazards model** is the workhorse of event history analysis, and it generalizes linear regression in a specific way. Rather than modeling the level of an outcome, it models the *ratio of hazards* between subjects with different covariate values. The model estimates a **hazard ratio** for each covariate: a ratio of 2 means subjects with that characteristic experience the event at twice the rate of the reference group at any given point in time. The "proportional" assumption — that this ratio is constant over time — is a testable constraint. Extensions allow **time-varying covariates** (a subject's employment status can change during observation), **competing risks** (subjects can exit via multiple distinct events, such as retirement versus layoff), and **discrete-time** formulations for data where time is measured in intervals rather than continuously.
