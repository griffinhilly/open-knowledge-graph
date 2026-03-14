---
id: disturbance-rejection-and-feedforward
title: Disturbance Rejection and Feedforward Control
domain: engineering
course: control-systems
prerequisites:
- id: error-signal-feedback-configuration
  type: hard
- id: cascade-and-feedforward-control
  type: soft
builds-toward:
- sensitivity-and-robustness-functions
tags:
- disturbance
- rejection
- feedforward
- control-architecture
stage: advanced
status: draft
---

# Disturbance Rejection and Feedforward Control

## Core Idea
Disturbance rejection capability depends on where the disturbance enters the plant relative to the feedback path. Feedback alone cannot reject disturbances before they affect output. Feedforward control (estimating disturbances and applying compensating input) can reject measured disturbances without feedback delay. Combined feedback-feedforward architectures offer superior disturbance attenuation.
