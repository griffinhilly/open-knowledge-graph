---
id: interrupted-time-series-analysis
title: Interrupted Time Series Design
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: difference-in-differences
  type: hard
- id: temporal-clustering-analysis
  type: soft
tags:
- time-series
- policy-evaluation
- intervention-effects
stage: advanced
status: draft
---

# Interrupted Time Series Design

## Core Idea
Interrupted time series (ITS) exploits a known intervention timepoint to estimate its effect on disease incidence. Regression models fit pre- and post-intervention trends, testing whether the intervention caused a level change and/or slope change. ITS accommodates seasonality and is useful when randomization or comparison groups are infeasible.
