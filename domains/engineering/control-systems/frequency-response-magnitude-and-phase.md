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

## Explainer

From your work on transfer functions, you know that a system's behavior is captured by G(s), evaluated as a rational function of the Laplace variable s. From Bode plot construction, you know how to sketch the magnitude and phase of G(jω) — the transfer function evaluated along the imaginary axis — as a function of frequency. Now we focus on what this picture actually *tells* you about the system, and why the frequency domain is such a powerful lens for control design.

The core physical insight: a linear time-invariant system driven by a sinusoidal input at frequency ω produces, in steady state, a sinusoidal output at the same frequency ω — scaled by |G(jω)| and shifted in phase by ∠G(jω). No other frequencies are generated. This is the defining property of LTI systems, and it is why the frequency response is complete: knowing |G(jω)| and ∠G(jω)| for all ω tells you everything about how the system processes any signal (since any signal can be decomposed into sinusoids). **Magnitude response** |G(jω)| answers: at this frequency, does the system amplify or attenuate? Values above 1 (positive dB) mean amplification; below 1 (negative dB) mean attenuation. **Phase response** ∠G(jω) answers: how much does the output lag or lead the input? Negative phase (lag) is typical for physical systems with inertia — the output trails the input, reflecting that the system takes time to respond.

Reading the Bode plot tells you immediately where the system can and cannot track signals. The **bandwidth** — typically the frequency where |G(jω)| drops to −3 dB — defines the usable tracking range. Inputs varying faster than bandwidth are attenuated; the system cannot faithfully follow them. A **resonant peak** in the magnitude plot (a bump above 0 dB near the natural frequency ω_n) signals a lightly damped system that will oscillate when disturbed — the peak height is related to the damping ratio: peak ≈ 1/(2ζ) for small ζ. The phase plot is equally critical for stability analysis. As phase approaches −180°, the system's feedback is becoming regenerative rather than stabilizing. The margin of phase above −180° at the gain crossover frequency is the **phase margin** — a direct measure of how close the closed-loop system is to instability. Both bandwidth and phase margin are read directly off the Bode plot.

The frequency response is also a **system identification** tool. If you inject sinusoids of known frequency and amplitude into a physical system and measure the output amplitude and phase shift, you directly measure |G(jω)| and ∠G(jω)| — without needing to know the system's differential equations. The shape of the measured curves tells you the system's order (from the high-frequency roll-off slope), its natural frequencies (from peaks in the magnitude), and its damping (from how sharp those peaks are). For control design, the frequency domain gives you direct design handles: a compensator is chosen to reshape the open-loop Bode plot — raising the gain crossover frequency to increase bandwidth, adding phase lead near crossover to improve phase margin, or adding a notch to suppress a resonance. The frequency response connects the mathematical machinery of transfer functions to the physical behavior you actually need to control.
