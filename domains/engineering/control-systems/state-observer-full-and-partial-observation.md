---
id: state-observer-full-and-partial-observation
title: 'State Observer: Full-State and Partial Observation'
domain: engineering
course: control-systems
prerequisites:
- id: observer-based-control
  type: hard
- id: state-space-representation-control
  type: hard
builds-toward:
- output-feedback-and-dynamic-compensation
tags:
- state-estimation
- observer-design
- luenberger-observer
- measurement-equation
stage: abstract-reasoning
status: draft
---

# State Observer: Full-State and Partial Observation

## Core Idea
When not all states are measured, a state observer estimates them from available measurements. The observer is a copy of the system with correction term proportional to measurement error: x̂̇ = Ax̂ + Bu + L(y − ŷ). Observer gain L can place observer eigenvalues anywhere in the LHP.
