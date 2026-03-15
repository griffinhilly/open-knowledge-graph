---
id: first-order-system-transient-response
title: 'First-Order System Response: Time Constant and Behavior'
domain: engineering
course: control-systems
prerequisites:
- id: response-specifications-performance-metrics
  type: hard
builds-toward:
- second-order-system-damping-ratio
tags:
- first-order
- time-constant
- exponential-response
stage: concrete-operations
status: draft
---

# First-Order System Response: Time Constant and Behavior

## Core Idea
First-order systems have one pole; step response is y(t) = 1 - e^(-t/τ) where τ is time constant. At t = τ, response reaches 63%. At t = 4τ (settling time), response is within 2% of final value. Frequency response has corner frequency at ω = 1/τ. Time constant directly controls response speed.
