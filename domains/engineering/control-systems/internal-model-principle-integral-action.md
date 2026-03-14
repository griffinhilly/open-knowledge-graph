---
id: internal-model-principle-integral-action
title: Internal Model Principle and Integral Control Action
domain: engineering
course: control-systems
prerequisites:
- id: steady-state-error-system-type
  type: hard
- id: pid-control
  type: soft
tags:
- internal-model
- integral-action
- steady-state-error
- pid
stage: advanced
status: draft
---

# Internal Model Principle and Integral Control Action

## Core Idea
Internal model principle: to track or reject a signal of a given form with zero error, the controller must contain a model (poles) of that signal. To track constant references (step), controller needs integrator (pole at origin). To track ramps, controller needs double integrator. This principle explains why PI controllers eliminate steady-state error to steps, and why proper controller structure (integrators) is essential, not just tuning gain.
