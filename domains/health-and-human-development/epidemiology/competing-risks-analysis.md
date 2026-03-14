---
id: competing-risks-analysis
title: Competing Risks Analysis
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: cox-proportional-hazards
  type: hard
- id: kaplan-meier-estimator
  type: hard
builds-toward:
- joint-longitudinal-competing-event-models
tags:
- survival-analysis
- incidence
- multiple-events
stage: advanced
status: draft
---

# Competing Risks Analysis

## Core Idea
Competing risks occur when subjects can experience multiple distinct events (e.g., death from cancer vs. other causes, treatment switching vs. continuation) and the occurrence of one event prevents future observation of the other. Standard survival methods (Kaplan-Meier, Cox regression) overestimate event risks by treating competing events as censoring. Competing risks analysis properly estimates event probabilities using cause-specific hazards or cumulative incidence functions that account for risk competition.

## How It's Best Learned
Compare standard Kaplan-Meier and cumulative incidence curves for a disease outcome when competing mortality exists; interpret differences.

## Common Misconceptions
Treating competing events as censored gives correct risk estimates. Cause-specific hazards directly show absolute risk; cumulative incidence is needed for that.
