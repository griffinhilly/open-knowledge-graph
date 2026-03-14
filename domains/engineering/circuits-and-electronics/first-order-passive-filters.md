---
id: first-order-passive-filters
title: First-Order Passive Filters
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: passive-filter-transfer-function-analysis
  type: hard
- id: rc-circuit-charging-and-discharging
  type: soft
builds-toward:
- bandpass-and-bandstop-filter-design
tags:
- RC-filters
- RL-filters
- rolloff
- corner-frequency
stage: formal-systems
status: draft
---

# First-Order Passive Filters

## Core Idea
First-order RC and RL filters have a single pole at the corner frequency ω_c = 1/τ. Low-pass filters (RC or RL) have -20 dB/decade rolloff above the corner; high-pass filters have +20 dB/decade rolloff below the corner. Phase shift varies from 0° to ±90° around the corner frequency. These simple filters are building blocks for complex filter designs.
