---
id: g-estimation-causal-effects
title: G-Estimation and Structural Nested Models
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: counterfactual-framework
  type: hard
- id: directed-acyclic-graphs
  type: hard
builds-toward:
- marginal-structural-models
- time-varying-confounders
tags:
- causal-inference
- structural-models
- effect-estimation
stage: advanced
status: draft
---

# G-Estimation and Structural Nested Models

## Core Idea
G-estimation estimates causal effects in the presence of baseline and time-varying confounding by parameterizing the structural relationship between exposure and outcome, then using estimating equations to find parameter values such that residuals are uncorrelated with exposure history, thereby identifying unconfounded effects.
