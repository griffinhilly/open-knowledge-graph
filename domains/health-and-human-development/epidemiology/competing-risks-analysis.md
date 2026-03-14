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
tags:
- survival-analysis
- competing-events
- cumulative-incidence
stage: advanced
status: draft
---

# Competing Risks Analysis

## Core Idea
Competing risks occur when individuals may experience one of several mutually exclusive events. Standard Kaplan-Meier and Cox methods are inappropriate because censoring is not independent. Cumulative incidence functions and competing risk regression properly estimate the probability of each event.
