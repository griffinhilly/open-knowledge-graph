---
id: frequency-response-magnitude-phase-basics
title: 'Frequency Response: Magnitude and Phase Relationships'
domain: engineering
course: control-systems
prerequisites:
- id: impulse-response-and-convolution-control
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- bode-plot-magnitude-asymptotes-rules
- bode-plot-phase-response-analysis
- gain-phase-margin-stability-measures
- nyquist-stability-from-frequency-response
tags:
- frequency-response
- magnitude
- phase
- jω
stage: advanced
status: draft
---

# Frequency Response: Magnitude and Phase Relationships

## Core Idea
Frequency response G(jω) describes how a system responds to sinusoidal inputs at different frequencies. The magnitude |G(jω)| indicates gain (amplification or attenuation), while ∠G(jω) indicates phase shift. Together, these quantities define stability margins and closed-loop performance.

## Explainer

From your study of impulse response and convolution, you know that a linear system's time-domain output is the convolution of the input with the impulse response h(t). The **frequency response** G(jω) is the Fourier transform of h(t) — it tells you exactly the same information, but organized by frequency instead of by time. The key insight: a sinusoidal input A·sin(ωt) always produces a sinusoidal output at the same frequency ω, but with a different amplitude and a shifted phase. G(jω) captures both changes. This is the defining property of linear time-invariant systems, and it makes frequency-domain analysis the natural language for understanding how systems filter, delay, and distort signals.

The **magnitude** |G(jω)| is the ratio of output amplitude to input amplitude at frequency ω. If |G(jω)| = 3 at some frequency, a sinusoid at that frequency is amplified threefold. If |G(jω)| = 0.1, the system attenuates that frequency by a factor of ten. Magnitude greater than one means amplification; less than one means attenuation. When plotted in decibels — 20·log₁₀(|G|) — a magnitude of 1 becomes 0 dB, attenuation to half becomes −6 dB, and tenfold amplification becomes +20 dB. The decibel scale converts multiplicative effects into additive ones, which makes cascaded systems easy to analyze: just add the dB gains of each stage.

The **phase** ∠G(jω) is the angle by which the output sinusoid lags behind the input. If ∠G(jω) = −90° at some frequency, the output is a quarter-cycle behind the input. Phase shift is not just a curiosity — it represents real time delay. A −90° shift at frequency f means the output lags by a time t = (90°/360°) · (1/f) = 1/(4f). Accumulated phase lag is the primary mechanism by which feedback systems become unstable: if a system intended as negative feedback accumulates −180° of phase at the frequency where its gain is still high, the fed-back signal arrives inverted and amplified, driving the system into oscillation.

Evaluating G(jω) is straightforward from the transfer function G(s): substitute s = jω and compute the resulting complex number at each frequency of interest. If G(s) = 1/(s + a), then G(jω) = 1/(jω + a), which has magnitude 1/√(ω² + a²) and phase −arctan(ω/a). These expressions reveal the system's behavior across all frequencies at once — no simulation needed. As you move toward Bode plots and stability analysis, you'll use these magnitude and phase expressions to build asymptotic approximations, read off stability margins, and design compensators that reshape the frequency response to meet performance specifications.
