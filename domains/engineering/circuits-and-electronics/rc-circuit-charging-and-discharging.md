---
id: rc-circuit-charging-and-discharging
title: RC Circuit Charging and Discharging
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: capacitive-elements-behavior-properties
  type: hard
- id: voltage-and-current-source-characteristics
  type: hard
- id: circuit-laws-kvl-and-kcl
  type: hard
builds-toward:
- rlc-circuit-transient-analysis-overview
- first-order-passive-filters
tags:
- transient-response
- RC-circuits
- exponential-decay
stage: formal-systems
status: draft
---

# RC Circuit Charging and Discharging

## Core Idea
When a voltage source is applied to an RC circuit, the capacitor charges exponentially according to v_C(t) = V(1 − e^(−t/τ)), where τ = RC is the time constant. The capacitor voltage and current change according to first-order differential equations. Understanding RC transients is crucial for analyzing step responses, filters, and timing circuits.
