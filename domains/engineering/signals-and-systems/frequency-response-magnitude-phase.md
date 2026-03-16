---
id: frequency-response-magnitude-phase
title: 'Frequency Response: Magnitude and Phase'
domain: engineering
course: signals-and-systems
prerequisites:
- id: transfer-function-poles-zeros
  type: hard
- id: magnitude-phase-spectrum-representation
  type: hard
builds-toward:
- bode-plot-construction-interpretation
- nyquist-stability-analysis-systems
- filter-classification-design-basics
tags:
- frequency-response
- magnitude
- phase
stage: advanced
status: draft
---

# Frequency Response: Magnitude and Phase

## Core Idea
The frequency response H(jω) = |H(jω)|e^(jφ(ω)) shows how a system responds to sinusoidal inputs at different frequencies. Magnitude response reveals gain at each frequency; phase response shows time delay or lead. Together they fully characterize the steady-state behavior of linear systems.

## Explainer

From your study of transfer functions and poles and zeros, you know that a linear time-invariant (LTI) system is fully described by its transfer function H(s). You also know the representation of signals as magnitude and phase spectra. The frequency response connects these two ideas: it is what you get when you evaluate H(s) along the imaginary axis, replacing s with jω. The result H(jω) is a complex function of real frequency ω, and its magnitude and phase tell you exactly how any sinusoidal input is transformed by the system.

**Why evaluate on the imaginary axis?** Any stable LTI system driven by a sinusoidal input A·cos(ωt) at steady state produces an output A·|H(jω)|·cos(ωt + φ(ω)). The input frequency is preserved — LTI systems cannot create new frequencies — but the amplitude is scaled by **magnitude response** |H(jω)| and the phase is shifted by **phase response** φ(ω) = ∠H(jω). This is the foundation of filter design: a lowpass filter has |H(jω)| ≈ 1 at low frequencies (signals pass through unchanged) and |H(jω)| ≈ 0 at high frequencies (signals are attenuated). The phase response tells you how much each frequency component is delayed relative to the input.

**Computing H(jω) from H(s).** Given a transfer function H(s) = N(s)/D(s) with numerator and denominator polynomials, substitute s = jω to get H(jω) = N(jω)/D(jω). The magnitude is |H(jω)| = |N(jω)|/|D(jω)| and the phase is φ = ∠N(jω) − ∠D(jω). For factored forms H(s) = K·∏(s−z_i)/∏(s−p_j), the magnitude is the product of distances from ω on the jω-axis to each zero divided by distances to each pole, scaled by K. The phase is the sum of angles from ω to each zero minus the sum of angles to each pole. This geometric interpretation directly connects the pole-zero plot to the frequency response: poles near the imaginary axis create peaks in |H(jω)| at the corresponding frequency (resonances), while zeros on or near the axis create dips or notches.

**Phase response and group delay.** Phase response φ(ω) is not just a nuisance — it matters for signal fidelity. If φ(ω) is linear in ω (φ = −τω), then every frequency component is delayed by the same time τ, and the output waveform is a perfect replica of the input, just shifted. This is **linear phase**. Non-linear phase distorts waveforms: different frequency components arrive at different times, smearing pulses or creating dispersion. **Group delay** τ_g(ω) = −dφ/dω is a frequency-resolved measure of delay: constant group delay = linear phase = no dispersion. Audio amplifiers and communications receivers must have near-linear phase over their operating band; control systems care about phase at specific frequencies because phase shift determines stability margins.

**Bode plots as a practical tool.** The magnitude response plotted in decibels (dB = 20·log₁₀|H(jω)|) on a log-frequency axis is a Bode magnitude plot. In this representation, products become sums: |H| = |K|·∏|s−z_i|/∏|s−p_j| becomes a sum of log-magnitude contributions, one per pole and zero. Each real pole at s = −a contributes a −20 dB/decade rolloff above ω = a; each real zero contributes +20 dB/decade. Complex conjugate pole pairs near the imaginary axis create resonance peaks whose height depends on the **quality factor** Q (or equivalently the damping ratio ζ). These asymptotic approximations — the Bode straight-line method — let you sketch magnitude and phase responses by inspection from the pole-zero locations, building powerful intuition for filter behavior before any numerical computation.

## Questions

```yaml
- question: "A system has transfer function H(s) = 10/(s + 10). What is the magnitude and phase of the frequency response at ω = 10 rad/s?"
  type: short-answer
  answer: "|H(j10)| = 10/|j10 + 10| = 10/√(100 + 100) = 10/(10√2) = 1/√2 ≈ 0.707. Phase = ∠10 − ∠(j10+10) = 0° − arctan(10/10) = −45°."
  explanation: "Substitute s = j10: H(j10) = 10/(10 + j10) = 10/[10(1 + j)] = 1/(1 + j). The magnitude is 1/√2 and the angle is −arctan(1) = −45°. This is the classic first-order lowpass response at its −3 dB frequency: gain is reduced to 1/√2 (≈ −3 dB) and phase lag is exactly 45°."

- question: "Why does a pole near the imaginary axis cause a peak in the magnitude response?"
  type: short-answer
  answer: "The magnitude |H(jω)| = K · (product of distances from jω to zeros) / (product of distances from jω to poles). As jω sweeps up the imaginary axis and passes close to a pole, the distance from the evaluation point to that pole becomes very small, making the denominator small and |H(jω)| large — a resonance peak."
  explanation: "The geometric interpretation from the pole-zero plot makes this intuitive: proximity of a pole to the evaluation point on the jω axis directly drives up the magnitude. A pole exactly on the imaginary axis (marginally stable system) produces infinite gain at that frequency — an ideal resonator. Moving the pole into the left half-plane (adding damping) produces a finite peak whose width and height depend on how far from the axis the pole sits."
```
