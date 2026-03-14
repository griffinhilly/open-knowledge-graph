---
id: bode-plot-stability-analysis
title: Bode Plot Stability Analysis
domain: engineering
course: control-systems
prerequisites:
- id: frequency-response-and-bode-plots
  type: hard
- id: transfer-functions-control
  type: hard
- id: logarithms-intro
  type: hard
- id: operations-with-complex-numbers
  type: soft
builds-toward:
- nyquist-stability-criterion
- gain-and-phase-margins
- lead-lag-compensators
tags:
- bode-plot
- crossover-frequency
- loop-gain
- open-loop
- frequency-domain
stage: advanced
status: validated
---

# Bode Plot Stability Analysis

## Core Idea
Bode plot stability analysis applies the open-loop frequency response G(jω)H(jω) to assess closed-loop stability without solving for closed-loop poles. The gain crossover frequency ωgc is where the open-loop magnitude equals 0 dB, and the phase crossover frequency ωpc is where the phase equals −180°. For minimum-phase systems in a unity feedback loop, closed-loop stability requires that the phase at ωgc exceeds −180° and the gain at ωpc is below 0 dB. These crossover relationships define the gain and phase margins, which quantify how much additional gain or phase lag the system can tolerate before becoming unstable.

## How It's Best Learned
Sketch asymptotic Bode plots for several open-loop transfer functions and identify crossover frequencies by hand. Compare with computed Bode plots to calibrate the accuracy of asymptotic approximations, especially near corners.

## Common Misconceptions
- Bode's stability criterion applies directly only to minimum-phase, single-loop systems — non-minimum-phase systems (with RHP zeros or time delays) require the Nyquist criterion.
- A large gain margin alone does not guarantee a robust design — both gain and phase margins must be adequate (typical targets: GM > 6 dB, PM > 45°).
- The Bode plot used for stability analysis is the open-loop transfer function G(jω)H(jω), not G(jω) alone when H ≠ 1.
