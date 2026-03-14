---
id: maximum-power-transfer
title: Maximum Power Transfer Theorem
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: thevenin-circuit-equivalent
  type: hard
- id: power-energy-in-circuits
  type: hard
builds-toward:
- sinusoidal-steady-state-analysis
tags:
- maximum-power
- impedance-matching
- power-transfer
stage: formal-systems
status: draft
---

# Maximum Power Transfer Theorem

## Core Idea
Maximum power is delivered to a load when load resistance equals the Thévenin resistance of the source (impedance matching condition). The maximum power available is P_max = V_th²/(4R_th). This result is important for signal transmission systems, though maximum efficiency (R_load >> R_source) is preferred in power delivery applications.
