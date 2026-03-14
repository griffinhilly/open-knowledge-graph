---
id: marginal-structural-models
title: Marginal Structural Models
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: time-varying-exposures-and-covariates
  type: hard
- id: counterfactual-framework
  type: hard
- id: propensity-score-methods
  type: soft
tags:
- g-methods
- time-dependent-confounding
- causal-inference
stage: advanced
status: draft
---

# Marginal Structural Models

## Core Idea
Marginal structural models (MSMs) are weighted regression models that estimate causal effects in the presence of time-dependent confounding—when past exposure affects future confounders that also affect the outcome. Standard regression adjustment is biased when confounders are affected by prior exposure. MSMs use inverse probability of treatment weights (IPTW) to create a pseudopopulation in which exposure is independent of confounders; analyzing this pseudopopulation yields unbiased effect estimates. MSMs are particularly useful for evaluating sequential treatment decisions and studying treatment switching.
