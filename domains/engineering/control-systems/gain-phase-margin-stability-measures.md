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
stage: advanced
status: draft
---

# Gain and Phase Margins as Stability Measures

## Core Idea
Gain margin (GM) is the amount the loop gain can increase before instability (dB at phase = -180°); phase margin (PM) is how much phase can lag before instability (degrees at magnitude = 0 dB). Both measure robustness to parameter variations. Typical design targets: GM > 6 dB, PM > 45°.

## Explainer

From your study of Bode plots and frequency response, you know how to plot a loop's gain (in dB) and phase (in degrees) against frequency on logarithmic axes. Now the question is: what do those plots tell you about whether a closed-loop system will be stable? The Bode stability criterion provides the answer — and gain margin and phase margin are the two numbers that quantify how far the system is from the edge of instability.

The core condition for marginal stability in a negative-feedback loop is that the loop gain equals 1 (0 dB) *at the same frequency* where the phase shift equals −180°. At that condition, the loop is delivering positive feedback at unity gain — any disturbance is sustained indefinitely (oscillation). If gain is greater than 1 at the −180° phase frequency, the system is unstable: disturbances grow. **Gain margin** measures the safety distance on the gain axis: it is how many dB below 0 dB the loop gain sits at the **phase crossover frequency** (where phase = −180°). A GM of 10 dB means the gain could increase by 10 dB before hitting the instability condition. A positive GM indicates stability; a negative GM means the system is already unstable.

**Phase margin** approaches the same condition from the other axis. Find the **gain crossover frequency** — where the loop gain magnitude crosses 0 dB. At that frequency, read off the phase. How far is it from −180°? That gap is the phase margin. A PM of 50° means the phase could lag an additional 50° before reaching −180° at unity gain — a generous safety buffer. As PM decreases toward 0°, the closed-loop system approaches marginal stability and will exhibit sustained oscillations; negative PM means unstable. Practically, PM also predicts closed-loop transient behavior: higher PM produces more damped step responses, while PM around 45–60° corresponds to a good balance of speed and damping.

Together, GM and PM tell a complete story about robustness. A system with GM = 20 dB but PM = 10° is vulnerable to a small increase in phase lag (from cable delays, neglected dynamics, or temperature-dependent components) even though the gain could vary widely. Conversely, high PM but low GM is vulnerable to gain variations. The standard engineering rule of thumb — GM > 6 dB and PM > 45° — is not a magic formula but a heuristic that provides reasonable robustness for most applications. When designing a controller, you read the open-loop Bode plot and add compensator elements (lead, lag, or lead-lag networks; or a PID) to reshape the gain and phase curves until both margins comfortably exceed these targets.
