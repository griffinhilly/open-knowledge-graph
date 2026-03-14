---
id: resonance-and-peaking-response
title: Resonance, Peaking, and Bandwidth Relationships
domain: engineering
course: control-systems
prerequisites:
- id: bandwidth-and-cutoff-frequencies
  type: hard
- id: natural-frequency-damping-second-order
  type: soft
builds-toward:
- lead-lag-compensation-design
tags:
- resonance
- peaking
- bandwidth
- frequency-response
stage: advanced
status: draft
---

# Resonance, Peaking, and Bandwidth Relationships

## Core Idea
Resonance occurs when system natural frequency aligns with input frequency, causing amplitude amplification above DC gain. Peak resonance magnitude (Mr, resonance peak) and resonant frequency (ωr) depend on damping: lower damping yields higher peaks and sharpened resonance. The relationship between Mr, bandwidth, and damping provides design insight: reducing damping increases bandwidth but increases peaking and overshoot—a fundamental design trade-off.
