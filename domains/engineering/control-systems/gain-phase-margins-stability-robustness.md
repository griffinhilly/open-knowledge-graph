---
id: gain-phase-margins-stability-robustness
title: 'Gain and Phase Margins: Stability Robustness'
domain: engineering
course: control-systems
prerequisites:
- id: frequency-response-magnitude-and-phase
  type: hard
- id: gain-and-phase-margins
  type: hard
builds-toward:
- model-uncertainty-robust-stability
- lead-lag-compensation-design
tags:
- stability
- robustness
- margins
- frequency-domain
stage: advanced
status: draft
---

# Gain and Phase Margins: Stability Robustness

## Core Idea
Gain margin (amount of gain increase before instability) and phase margin (amount of phase lag before instability) quantify how much system uncertainty the feedback loop can tolerate. These metrics are read directly from Bode plots: gain margin at phase=-180°, phase margin at magnitude=0dB. Typical requirements are gain margin >2 (6dB) and phase margin >30-45° to ensure adequate robustness against unmodeled dynamics and parametric variations.
