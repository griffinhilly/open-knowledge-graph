---
id: time-varying-exposures-and-covariates
title: Time-Varying Exposures and Confounders
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: cox-proportional-hazards
  type: hard
- id: person-time-follow-up-studies
  type: hard
builds-toward:
- marginal-structural-models
tags:
- time-dependent-exposure
- confounding-control
- causal-inference
stage: advanced
status: draft
---

# Time-Varying Exposures and Confounders

## Core Idea
Many exposures and confounders change over follow-up (treatment initiation or switching, medication adherence changes, smoking cessation), creating time-varying exposure patterns. Time-varying exposure analysis requires restructuring data into person-time units and using methods like extended Cox regression or marginal structural models to properly account for time-dependent exposure and confounding. Naive analysis ignoring time-variation can severely bias causal effect estimates by conflating concurrent confounding with causal effects.

## How It's Best Learned
Reshape follow-up data into person-time records with time-varying exposure and covariates; fit extended Cox and compare to naive analysis.

## Common Misconceptions
Baseline exposure analysis is valid even when exposure changes (can severely bias causal effects). Ordinary regression adjustment handles time-varying confounding adequately.
