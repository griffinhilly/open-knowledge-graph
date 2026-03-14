---
id: joint-longitudinal-competing-event-models
title: Joint Longitudinal-Competing Event Models
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: cox-proportional-hazards
  type: hard
- id: competing-risks-analysis
  type: hard
- id: hierarchical-models-epidemiology
  type: soft
tags:
- joint-models
- repeated-measures
- longitudinal-survival
stage: advanced
status: draft
---

# Joint Longitudinal-Competing Event Models

## Core Idea
Joint models simultaneously analyze longitudinal biomarker or quality-of-life trajectories and time to competing events (death, disease progression), accounting for correlation between longitudinal marker evolution and event risk. They properly handle informative censoring (subjects with worse markers more likely to experience events). Joint models improve event prediction as longitudinal measurements accumulate and allow investigation of biomarker-event associations while avoiding selection bias from differential event probabilities. Applications include cancer prognosis and cardiovascular risk prediction incorporating repeated clinical measurements.
