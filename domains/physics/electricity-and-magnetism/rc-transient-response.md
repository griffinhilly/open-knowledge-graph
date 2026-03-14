---
id: rc-transient-response
title: Transient Response in RC Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: dc-circuit-analysis
  type: hard
builds-toward:
- rl-transient-response
tags:
- rc-circuit
- transient
- time-constant
stage: formal-systems
status: draft
---

# Transient Response in RC Circuits

## Core Idea
In an RC circuit, capacitor charge evolves as Q(t) = Q₀(1 − e^(−t/τ)) during charging and Q(t) = Q₀e^(−t/τ) during discharging, where τ = RC is the time constant. Current decays exponentially: I(t) = (V/R)e^(−t/τ). The time constant characterizes the speed of charge redistribution; larger R or C gives slower response.
