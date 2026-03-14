---
id: inverse-probability-weighting
title: Inverse Probability Weighting
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: propensity-score-analysis
  type: hard
- id: stratification-and-adjustment
  type: soft
builds-toward:
- marginal-structural-models
- g-estimation-causal-effects
tags:
- causal-inference
- confounding
- weighting
- marginal-effects
stage: advanced
status: draft
---

# Inverse Probability Weighting

## Core Idea
Inverse probability weighting (IPW) constructs weights so that the weighted sample is pseudo-randomized with respect to measured confounders. IPW directly produces marginal (population-average) treatment effects and is particularly useful for survival and time-to-event analyses where standard adjustment would be biased.
