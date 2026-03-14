---
id: transient-response-rc-circuits
title: Transient Response in RC Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: network-circuit-analysis-methods
  type: hard
- id: differential-equations-intro-separable
  type: hard
builds-toward:
- magnetic-force-moving-charges
tags:
- transient
- rc-circuit
- time-constant
stage: formal-systems
status: draft
---

# Transient Response in RC Circuits

## Core Idea
RC charging: Q(t) = Q₀(1 − e^(−t/RC)), with time constant τ = RC. RC discharging: Q(t) = Q₀e^(−t/RC). Voltage and current similarly decay exponentially. Time constant determines how quickly the circuit reaches steady state.
