---
id: time-varying-confounders
title: Time-Varying Confounders and Longitudinal Exposure
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: person-time-follow-up-studies
  type: hard
- id: confounding-epidemiology
  type: hard
builds-toward:
- marginal-structural-models
- g-estimation-causal-effects
tags:
- longitudinal-analysis
- time-varying-confounding
- exposure-dynamics
stage: advanced
status: draft
---

# Time-Varying Confounders and Longitudinal Exposure

## Core Idea
Time-varying confounding occurs when a variable is a confounder at some timepoint but is also affected by prior exposure. Standard regression adjustment introduces bias because adjusting for a mediator of prior exposure induces collider bias. Methods like marginal structural models or g-estimation handle this scenario.
