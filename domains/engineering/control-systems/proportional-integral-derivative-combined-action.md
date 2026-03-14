---
id: proportional-integral-derivative-combined-action
title: 'Proportional-Integral-Derivative Control: Combined Action'
domain: engineering
course: control-systems
prerequisites:
- id: pid-control
  type: hard
builds-toward:
- process-model-identification-relay-autotuning
tags:
- pid-controller
- proportional-action
- integral-action
- derivative-action
- tuning
stage: abstract-reasoning
status: draft
---

# Proportional-Integral-Derivative Control: Combined Action

## Core Idea
PID control law u(t) = Kₚ e(t) + Kᵢ ∫e(τ)dτ + Kd de/dt combines three actions: proportional provides immediate response; integral eliminates steady-state error but can destabilize; derivative improves stability and damping by responding to error rate.
