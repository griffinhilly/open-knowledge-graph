---
id: transient-response-rl-circuits
title: Transient Response in RL Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: series-parallel-inductor-networks
  type: hard
- id: dc-analysis-steady-state
  type: hard
builds-toward:
- transient-response-rlc-circuits
tags:
- transients
- rl-circuits
- time-domain
stage: formal-systems
status: draft
---

# Transient Response in RL Circuits

## Core Idea
RL transients describe current changes when inductors energize or de-energize through resistors. The current in a series RL circuit follows i(t) = I_f + (I_i - I_f)·exp(-t/τ), where τ = L/R is the time constant. Inductors oppose current changes, resulting in exponential approach to steady-state current. RL transients appear in switching power supplies, motor control, and relay circuits.
