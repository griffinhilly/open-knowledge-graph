---
id: rl-circuit-transient-analysis
title: RL Circuit Transient Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: inductive-elements-behavior-properties
  type: hard
- id: voltage-and-current-source-characteristics
  type: hard
- id: circuit-laws-kvl-and-kcl
  type: hard
builds-toward:
- rlc-circuit-transient-analysis-overview
tags:
- transient-response
- RL-circuits
- exponential-growth
stage: formal-systems
status: draft
---

# RL Circuit Transient Analysis

## Core Idea
When a voltage source is applied to an RL circuit, the inductor resists current change; the current grows exponentially as i(t) = (V/R)(1 − e^(−t/τ)), where τ = L/R. The inductor produces a voltage spike when the circuit is opened. RL transients model inductive kick and switching transients in real circuits.
