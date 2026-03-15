---
id: synthetic-control-methods-research-methods-social-science
title: Synthetic Control Methods
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: natural-experiments-identification-strategy
  type: hard
- id: time-series-cross-section
  type: soft
- id: linear-regression
  type: soft
builds-toward:
- generalized-synthetic-control
- augmented-synthetic-control
tags:
- causal-inference
- comparative
- counterfactual
- policy-evaluation
stage: advanced
status: draft
---

# Synthetic Control Methods

## Core Idea
Synthetic control constructs a counterfactual for a treated unit by taking a weighted combination of untreated units. When a single unit (country, region, organization) experiences an intervention, its pre-intervention trends may not match any single control unit, but a weighted average may. The method estimates the treatment effect as the post-intervention difference between the treated unit and its synthetic control. It is particularly useful for policy evaluation when aggregate data is available but individual randomization is infeasible.
