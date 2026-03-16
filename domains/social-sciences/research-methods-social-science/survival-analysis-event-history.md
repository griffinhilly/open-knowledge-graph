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
  type: hard
tags:
- survival-analysis
- event-history
- duration
- censoring
stage: advanced
status: draft
---

# Survival Analysis and Event History Methods

## Core Idea
Event history methods analyze timing of social events—divorce, job transitions, political regime changes. These methods handle censoring (incomplete observation periods) and allow time-varying covariates. Survival curves and hazard functions describe rates of event occurrence over time.

## Explainer

Your training in linear regression taught you to model the *level* of an outcome — how high or low is Y given X? But many social science questions are about *timing*: not whether someone gets divorced, but when. Not whether a political regime collapses, but how long it survives. Not whether a worker finds a new job, but how quickly after being laid off. Standard regression is poorly suited to timing questions, partly because of a data problem your regression training didn't prepare you for: **censoring**.

**Censoring** occurs when you observe a subject for a period but the event has not yet occurred by the end of observation. A study tracking divorces that ends in 2020 includes couples still married at that date — they haven't experienced the event, but their marriages lasted *at least* as long as the observation window. Simply excluding these cases biases the analysis by discarding information: a marriage that has survived 15 years tells you something important even if it isn't yet ended. Survival analysis incorporates censored observations correctly by treating them as contributing information about survival *up to* the censoring point, even though the event was not observed. Your background in probability distributions — especially the exponential — will help here, since the exponential distribution describes constant-hazard survival processes and is the simplest baseline case.

The two core functions build on your probability background. The **survival function** S(t) gives the probability that the event has not yet occurred by time t — it starts at 1 and declines over time as events accumulate. The **hazard function** h(t) is the instantaneous rate of event occurrence at time t, given that the subject has survived to that point. Think of the hazard as the *risk rate right now for those still at risk* — it can vary over time. Divorce risk is highest in the early years of marriage and again around the seventh year; political regimes are often most vulnerable just after transitional periods. The hazard function captures this time-varying risk in a way that a single regression coefficient cannot.

The **Cox proportional hazards model** is the workhorse of event history analysis, and it generalizes linear regression in a specific way. Rather than modeling the level of an outcome, it models the *ratio of hazards* between subjects with different covariate values. The model estimates a **hazard ratio** for each covariate: a ratio of 2 means subjects with that characteristic experience the event at twice the rate of the reference group at any given point in time. The "proportional" assumption — that this ratio is constant over time — is a testable constraint. Extensions allow **time-varying covariates** (a subject's employment status can change during observation), **competing risks** (subjects can exit via multiple distinct events, such as retirement versus layoff), and **discrete-time** formulations for data where time is measured in intervals rather than continuously.
