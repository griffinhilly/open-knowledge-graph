---
id: second-order-passive-filters
title: Second-Order Passive Filters
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: passive-filter-transfer-function-analysis
  type: hard
- id: rlc-circuit-transient-analysis-overview
  type: hard
builds-toward:
- bandpass-and-bandstop-filter-design
tags:
- RLC-filters
- damping
- resonance
- steeper-rolloff
stage: formal-systems
status: draft
---

# Second-Order Passive Filters

## Core Idea
Second-order filters built from RLC circuits provide -40 dB/decade rolloff and can exhibit resonance peaks or dips depending on damping. The quality factor Q controls the sharpness; low Q gives smooth response while high Q causes peaking. Series and parallel RLC configurations yield different filter characteristics (e.g., series RLC is notch, parallel RLC is peaking).
