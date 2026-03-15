---
id: frequency-response-magnitude-and-phase
title: 'Frequency Response: Magnitude and Phase'
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
- id: bode-plot-construction
  type: hard
- id: magnitude-phase-spectrum-representation
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- bandwidth-and-cutoff-frequencies
- gain-phase-margins-stability-robustness
tags:
- frequency-response
- magnitude
- phase
- bode
stage: advanced
status: draft
---

# Frequency Response: Magnitude and Phase

## Core Idea
Frequency response describes how a system responds to sinusoidal inputs across all frequencies: magnitude response |G(jω)| shows amplitude attenuation or amplification, while phase response ∠G(jω) shows timing lag or lead. Bode plots (log magnitude vs log frequency, phase vs log frequency) visualize these relationships and reveal bandwidth, resonance, and high-frequency behavior essential for control design.
