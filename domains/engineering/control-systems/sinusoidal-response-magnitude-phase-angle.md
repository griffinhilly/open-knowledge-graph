---
id: sinusoidal-response-magnitude-phase-angle
title: 'Sinusoidal Response: Magnitude and Phase Angle'
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
builds-toward:
- frequency-response-magnitude-phase-plots
- gain-margin-phase-margin-stability
tags:
- frequency-response
- magnitude
- phase
- complex-numbers
- phasor
stage: abstract-reasoning
status: draft
---

# Sinusoidal Response: Magnitude and Phase Angle

## Core Idea
When a linear system is excited by sinusoidal input u(t) = A sin(ωt), steady-state output is y(t) = A|G(jω)| sin(ωt + ∠G(jω)). The magnitude |G(jω)| and phase ∠G(jω) of the transfer function at frequency ω completely characterize the system's steady-state sinusoidal response.

## Explainer

You already know from transfer functions that G(s) maps Laplace-domain inputs to Laplace-domain outputs. Sinusoidal response is what happens when you evaluate this on the imaginary axis — substituting s = jω. At any frequency ω, G(jω) is a complex number. The **magnitude** |G(jω)| tells you how much the system scales the amplitude of a sinusoidal input at that frequency; the **phase angle** ∠G(jω) tells you how much the output lags or leads the input.

The result is clean: for a stable linear system driven by u(t) = A sin(ωt), the steady-state output is always y(t) = A|G(jω)| sin(ωt + ∠G(jω)). The system cannot generate new frequencies — it can only amplify or attenuate and shift in time. This follows from linearity and the eigenfunction property of complex exponentials: sinusoids are the natural "eigenfunctions" of linear time-invariant systems, in the same way that eigenvectors are the natural inputs for linear transformations.

To compute |G(jω)| and ∠G(jω) at a specific frequency, substitute s = jω into G(s) and treat the result as a complex number. For a transfer function G(s) = (s + 2)/((s + 1)(s + 5)), evaluating at ω = 3 gives G(3j) = (3j + 2)/((3j + 1)(3j + 5)). Compute numerator and denominator separately, multiply out the denominator, then divide. The magnitude is the ratio of absolute values: |numerator|/|denominator|. The phase is the difference of arguments: ∠numerator − ∠denominator. At low frequencies (ω → 0), G(jω) → G(0), the DC gain. At high frequencies, physical systems with more poles than zeros have magnitude that falls off because the denominator grows faster.

This sinusoidal characterization is the foundation for all frequency-domain design methods. Every point on a Bode plot — the magnitude in dB and phase in degrees — is just |G(jω)| and ∠G(jω) evaluated at many values of ω. The Nyquist plot traces the path of G(jω) in the complex plane as ω sweeps from 0 to ∞. These plots become your primary tools for assessing stability margins, understanding bandwidth, and designing compensators. The ability to read magnitude and phase directly from G(jω) at any specific frequency is the entry skill for all of that analysis.
