---
id: time-delay-dead-time-transport-lag
title: Time Delay and Dead-Time Effects in Control
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
- id: frequency-response-magnitude-and-phase
  type: hard
builds-toward:
- model-uncertainty-robust-stability
tags:
- time-delay
- dead-time
- transport-lag
- stability
stage: advanced
status: draft
---

# Time Delay and Dead-Time Effects in Control

## Core Idea
Time delay (transport lag, e^(-sτ)) introduces phase lag proportional to frequency: at high frequencies, phase lag approaches -∞, severely limiting achievable bandwidth and destabilizing feedback. Dead time cannot be canceled by any causal controller; only reduced through faster sensing or predictive control. Design must explicitly account for delay through reduced bandwidth requirements and increased robustness margins.
