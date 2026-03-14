---
id: propensity-score-matching
title: Propensity Score Matching for Observational Studies
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: selection-bias-econometrics
  type: hard
builds-toward:
- treatment-effect-estimation
tags:
- causal-inference
- matching
- observational
stage: formal-systems
status: draft
---

# Propensity Score Matching for Observational Studies

## Core Idea
Propensity score matching (PSM) estimates the probability of treatment given covariates, then matches treated and untreated units with similar propensity scores. This balances pre-treatment characteristics, reducing selection bias when unconfoundedness (no unmeasured confounders) holds.
