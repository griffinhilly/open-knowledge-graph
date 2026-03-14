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
