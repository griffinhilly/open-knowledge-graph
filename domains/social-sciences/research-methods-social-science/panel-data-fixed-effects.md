---
id: panel-data-fixed-effects
title: Fixed and Random Effects Models
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: longitudinal-data-analysis
  type: hard
- id: multilevel-modeling-hierarchical
  type: soft
- id: linear-regression
  type: hard
builds-toward:
- dynamic-panel-models
- system-gmm-estimators
tags:
- panel-methods
- causal
- confounding
- estimators
stage: advanced
status: draft
---

# Fixed and Random Effects Models

## Core Idea
Fixed-effects estimators use within-unit variation to identify causal effects while removing time-invariant confounds (e.g., personality, geographic characteristics). Random-effects models assume unit-level heterogeneity is uncorrelated with predictors, allowing estimation of between-unit and within-unit effects. The choice between fixed and random effects depends on research assumptions: fixed effects trades precision for robustness when time-invariant confounds are suspected.
