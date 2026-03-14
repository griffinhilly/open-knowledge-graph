---
id: first-order-system-response-analysis
title: First-Order System Response Analysis
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
- id: laplace-transform-control
  type: hard
builds-toward:
- rise-time-settling-time-overshoot
- sinusoidal-response-magnitude-phase-angle
tags:
- transient-response
- time-constant
- exponential
- step-response
stage: abstract-reasoning
status: draft
---

# First-Order System Response Analysis

## Core Idea
First-order systems, characterized by a single pole in the transfer function, respond exponentially to inputs with a time constant τ that controls the rate of approach to steady state. The step response rises as 1 − e^(−t/τ), reaching 63% of final value at t = τ.
