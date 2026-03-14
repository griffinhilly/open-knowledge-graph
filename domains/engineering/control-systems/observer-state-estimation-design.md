---
id: observer-state-estimation-design
title: State Observer Design and Estimation
domain: engineering
course: control-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: controllability-and-observability
  type: hard
builds-toward:
- separation-principle-control-theory
tags:
- observer
- estimation
- state-space
- sensor
stage: advanced
status: draft
---

# State Observer Design and Estimation

## Core Idea
Not all states are measurable; observers estimate unmeasurable states from available outputs. Full-state observer reconstructs all n states from m outputs (requires observability). Observer eigenvalues are assigned like state feedback to control estimation error convergence. Faster observer response improves tracking but increases noise sensitivity. Trade-off between estimation accuracy and robustness to measurement noise.
