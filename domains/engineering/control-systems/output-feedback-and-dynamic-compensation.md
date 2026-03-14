---
id: output-feedback-and-dynamic-compensation
title: Output Feedback and Dynamic Compensation
domain: engineering
course: control-systems
prerequisites:
- id: state-observer-full-and-partial-observation
  type: hard
- id: state-feedback-pole-placement
  type: hard
builds-toward:
- cascade-control-loop-interaction-analysis
tags:
- dynamic-controller
- observer-based-feedback
- output-feedback
- compensation
stage: abstract-reasoning
status: draft
---

# Output Feedback and Dynamic Compensation

## Core Idea
Output feedback control combines state observer with state feedback: estimate states from measurements, then apply state feedback law u = −Kx̂. The resulting compensator is dynamic (order equals plant order) and can place closed-loop poles at desired locations via the separation principle.
