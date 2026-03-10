---
id: gain-and-phase-margins
title: Gain and Phase Margins
domain: engineering
course: control-systems
prerequisites:
- id: bode-plot-stability-analysis
  type: hard
- id: nyquist-stability-criterion
  type: soft
builds-toward:
- pid-control
- lead-lag-compensators
tags:
- gain-margin
- phase-margin
- stability-margin
- robustness
- crossover-frequency
stage: advanced
status: draft
---

# Gain and Phase Margins

## Core Idea
Gain margin (GM) is the factor by which the open-loop gain can be increased before instability, measured at the phase crossover frequency ωpc where phase = −180°; it is expressed in dB as GM = −20log|G(jωpc)H(jωpc)|. Phase margin (PM) is the additional phase lag that would bring the system to instability, measured at the gain crossover frequency ωgc as PM = 180° + ∠G(jωgc)H(jωgc). Both margins together quantify robustness: practical design typically requires GM > 6 dB and PM between 30° and 60°. Phase margin is approximately related to closed-loop damping ratio by PM ≈ 100ζ for ζ < 0.7, making it a convenient design handle.

## How It's Best Learned
Read gain and phase margins directly from Bode plots and verify consistency with Nyquist encirclement analysis. Observe how increasing the gain K shifts only the magnitude curve downward, simultaneously changing both margins.

## Common Misconceptions
- Positive GM and PM guarantee stability for minimum-phase single-loop systems, but not for MIMO or non-minimum-phase systems where more sophisticated criteria are needed.
- Infinite gain margin is not the same as unconditional stability — it occurs when the phase never reaches −180°, which is only possible for specific system types.
- The PM ≈ 100ζ approximation breaks down for systems with zeros or additional poles near the imaginary axis.
