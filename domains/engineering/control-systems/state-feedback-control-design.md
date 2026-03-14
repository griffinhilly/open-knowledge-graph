---
id: state-feedback-control-design
title: State Feedback Control and Pole Placement
domain: engineering
course: control-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: controllability-and-observability
  type: hard
builds-toward:
- observer-state-estimation-design
- separation-principle-control-theory
tags:
- state-feedback
- pole-placement
- state-space
- design
stage: advanced
status: draft
---

# State Feedback Control and Pole Placement

## Core Idea
State feedback u = -Kx moves closed-loop poles to arbitrary locations (if system is controllable) by feeding back weighted state variables. Unlike transfer function design, state feedback directly assigns poles without iterative methods. Design involves: (1) specifying desired closed-loop poles from performance specs, (2) computing feedback gain K using pole placement, (3) verifying stability and margins.
