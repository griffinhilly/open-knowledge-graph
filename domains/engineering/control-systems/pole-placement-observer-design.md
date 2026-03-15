---
id: pole-placement-observer-design
title: Pole Placement via State Feedback and Observer Design
domain: engineering
course: control-systems
prerequisites:
- id: observability-controllability-tests
  type: hard
- id: state-space-representation-control
  type: soft
- id: eigenvalues-eigenvectors
  type: hard
builds-toward:
- compensation-design-tradeoffs-cascadefeedback
tags:
- pole-placement
- state-feedback
- observer
- eigenvalue-assignment
stage: concrete-operations
status: draft
---

# Pole Placement via State Feedback and Observer Design

## Core Idea
If system is controllable, state feedback u = -Kx can place closed-loop poles at arbitrary locations. Observer estimates unmeasured states from y; if observable, observer poles can be placed arbitrarily. Pole-placement design trade-off: faster response requires higher gain and larger control effort; observer poles typically placed faster than controller poles (separation principle).
