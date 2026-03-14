---
id: process-model-identification-relay-autotuning
title: Process Model Identification and Relay Autotuning
domain: engineering
course: control-systems
prerequisites:
- id: pid-tuning-methods
  type: hard
- id: sinusoidal-response-magnitude-phase-angle
  type: soft
builds-toward:
- practical-control-system-implementation
tags:
- system-identification
- relay-feedback
- autotuning
- critical-frequency
- model-estimation
stage: abstract-reasoning
status: draft
---

# Process Model Identification and Relay Autotuning

## Core Idea
Relay feedback autotuning applies a relay controller to excite the process at its critical frequency (phase = −180°) without requiring an explicit plant model. Amplitude and frequency of resulting oscillation directly give the critical frequency and magnitude for PID tuning.
