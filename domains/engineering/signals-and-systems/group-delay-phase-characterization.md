---
id: group-delay-phase-characterization
title: Group Delay and Phase Characterization
domain: engineering
course: signals-and-systems
prerequisites:
- id: frequency-response-and-bode-plots
  type: hard
builds-toward:
- all-pass-filters-phase-shaping
tags:
- phase-response
- group-delay
- dispersion
- filters
stage: advanced
status: draft
---

# Group Delay and Phase Characterization

## Core Idea
Phase response φ(ω) = arg[H(e^jω)] describes phase shift as a function of frequency. Group delay τg(ω) = –dφ/dω represents delay of signal components at each frequency. Linear-phase filters have constant group delay, avoiding signal distortion. Non-constant group delay disperses frequency components at different rates, causing waveform degradation.

## Explainer

From your study of frequency response and Bode plots, you are familiar with characterizing a filter or system by two frequency-domain plots: the **magnitude response** |H(jω)| and the **phase response** φ(ω) = ∠H(jω). You have spent most of your time with magnitude — understanding passband, stopband, rolloff, ripple. Phase is equally important, and in some applications it matters more. The reason is that a real signal is not a single sinusoid but a superposition of many frequencies. When those frequency components emerge from a filter with different amounts of phase shift, they arrive at the output at different times relative to each other — and the reconstructed waveform looks different from the input. This is **phase distortion**.

**Group delay** is the tool that quantifies this effect. It is defined as τ_g(ω) = −dφ/dω — the negative derivative of the phase response with respect to frequency. The intuition: if φ(ω) = −ωτ₀ (phase changes linearly with frequency), then all components are delayed by the same amount τ₀, and the output waveform is just a time-shifted copy of the input — no distortion, just a constant delay. Group delay in this case is constant: τ_g(ω) = τ₀ everywhere. Deviations from constant group delay indicate that some frequency components are delayed more than others, causing them to "drift apart" in time. A frequency component at ω₁ is delayed by τ_g(ω₁) seconds; a component at ω₂ is delayed by τ_g(ω₂) seconds. If these differ, the reconstructed signal is distorted.

A filter with **linear phase** (φ(ω) = −ωτ₀ + constant) has constant group delay and introduces no waveform distortion. **FIR filters with symmetric coefficients** have exactly linear phase — this is one of their key advantages over IIR designs. The symmetry of the impulse response guarantees that the phase response is linear, hence group delay is constant across all frequencies. IIR filters (Butterworth, Chebyshev, elliptic) have non-linear phase and non-constant group delay, which is why they are problematic in applications that cannot tolerate waveform distortion.

**Dispersion** is the phenomenon that results from non-constant group delay. In optical fibers, different wavelengths of light travel at different group velocities (group velocity v_g(ω) = 1/τ_g(ω) in appropriate units), so a pulse that starts as a clean Gaussian broadens and smears as it propagates — limiting the data rate of fiber links. In audio, non-constant group delay across the audible band is sometimes audible as a smearing of transients (the sharp "attack" of a drum strike). In data communications, intersymbol interference occurs when symbols spread into adjacent symbol periods due to group delay variation. Measuring group delay with a vector network analyzer, and then compensating it with an **all-pass filter** (which adds phase shift without changing magnitude), is a standard technique in RF system design.
