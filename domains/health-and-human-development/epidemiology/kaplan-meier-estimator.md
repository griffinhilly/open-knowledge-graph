---
id: kaplan-meier-estimator
title: Kaplan-Meier Survival Analysis and Curves
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: disease-frequency-measures
  type: hard
- id: person-time-follow-up-studies
  type: soft
builds-toward:
- cox-proportional-hazards
tags:
- survival-analysis
- kaplan-meier
- censoring
- time-to-event
stage: advanced
status: draft
---

# Kaplan-Meier Survival Analysis and Curves

## Core Idea
The Kaplan-Meier estimator is a non-parametric method for estimating survival probability over time, properly accounting for censored observations. It calculates the cumulative probability of surviving to each event time by multiplying conditional survival probabilities. Kaplan-Meier curves allow visual comparison of survival between groups and provide median survival estimates, forming the foundation for survival analysis.
