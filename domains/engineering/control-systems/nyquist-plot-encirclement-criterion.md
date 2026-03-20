---
id: nyquist-plot-encirclement-criterion
title: Nyquist Plot and Encirclement Criterion
domain: engineering
course: control-systems
prerequisites:
- id: nyquist-stability-criterion
  type: hard
- id: sinusoidal-response-magnitude-phase-angle
  type: hard
- id: complex-analysis
  type: soft
builds-toward:
- gain-margin-phase-margin-stability
tags:
- nyquist-diagram
- encirclement
- stability-test
- closed-loop-poles
- frequency-response
stage: advanced
status: draft
---

# Nyquist Plot and Encirclement Criterion

## Core Idea
The Nyquist criterion states: the closed-loop system is stable if and only if the plot of G(jω) encircles the point −1 a number of times equal to the number of RHP poles in the open-loop transfer function G(s). This elegant result connects open-loop frequency response to closed-loop stability.

## Explainer

The Bode plot displays magnitude and phase as separate graphs against frequency. The **Nyquist plot** displays the same information as a single curve in the complex plane: as ω sweeps from −∞ to +∞, the complex number G(jω) traces a closed curve. Each point's distance from the origin is the gain |G(jω)| and its angle is the phase ∠G(jω). Your prerequisite on sinusoidal magnitude and phase gave you the raw material; the Nyquist plot is a different coordinate system for the same data — one that makes stability analysis geometric.

The criterion emerges from the **argument principle** of complex analysis. For a closed contour in the s-plane encircling certain poles and zeros of a function F(s), the image contour under F encircles the origin a number of times equal to (Z − P), where Z is the enclosed zeros and P is the enclosed poles. For stability analysis, take F(s) = 1 + G(s) — the closed-loop characteristic polynomial. Its zeros are the closed-loop poles; its poles are the open-loop poles (which you know). Stability requires all closed-loop poles in the left half-plane, meaning zero zeros of 1 + G(s) inside the right half-plane (RHP) contour.

The Nyquist D-contour encloses the entire RHP. By the argument principle, the number of RHP closed-loop poles Z = N + P, where N is the number of clockwise encirclements of the origin by the image of 1 + G(jω), and P is the known count of open-loop RHP poles. Since 1 + G encircling the origin is equivalent to G encircling −1 + 0j, the criterion states: for a stable closed-loop system, the Nyquist plot of G must encircle the **critical point −1** exactly P times counterclockwise.

For systems with no open-loop RHP poles (the common stable-plant case), this simplifies dramatically: stability holds if and only if the Nyquist plot does *not* encircle −1. The gain margin and phase margin from your Bode analysis are now geometric: gain margin is how much you could scale the Nyquist curve before it passes through −1; phase margin is how many degrees of rotation would bring the curve to −1. The Nyquist criterion is strictly more general than Bode-based reasoning — it handles unstable plants (P > 0) and non-minimum-phase systems rigorously, situations where Bode plot intuition can fail silently.
