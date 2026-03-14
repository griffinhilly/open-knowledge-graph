---
id: gain-phase-margin-stability-measures
title: Gain and Phase Margins as Stability Measures
domain: engineering
course: control-systems
prerequisites:
- id: bode-plot-phase-response-analysis
  type: hard
- id: frequency-response-magnitude-phase-basics
  type: soft
builds-toward:
- nichols-chart-design-method
- nyquist-stability-from-frequency-response
- compensation-design-tradeoffs-cascadefeedback
tags:
- gain-margin
- phase-margin
- stability-margins
- robustness
stage: concrete-application
status: draft
---

# Gain and Phase Margins as Stability Measures

## Core Idea
Gain margin (GM) is the amount the loop gain can increase before instability (dB at phase = -180°); phase margin (PM) is how much phase can lag before instability (degrees at magnitude = 0 dB). Both measure robustness to parameter variations. Typical design targets: GM > 6 dB, PM > 45°.
