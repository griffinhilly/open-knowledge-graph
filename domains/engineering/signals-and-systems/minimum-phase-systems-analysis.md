---
id: minimum-phase-systems-analysis
title: Minimum Phase Systems and Factorization
domain: engineering
course: signals-and-systems
prerequisites:
- id: all-pass-filters-phase-shaping
  type: hard
- id: transfer-function-poles-zeros
  type: hard
tags:
- minimum-phase
- all-pass
- transfer-function
- stability
stage: advanced
status: draft
---

# Minimum Phase Systems and Factorization

## Core Idea
A minimum-phase system has all poles and zeros inside the unit circle (digital) or left half-plane (analog), resulting in minimum group delay for its magnitude response. Any transfer function factors as H(z) = Hmin(z)·Hap(z), where Hmin is minimum-phase and Hap is all-pass. This decomposition enables simultaneous specification of magnitude response and phase characteristics.

## Explainer

You know from transfer function poles and zeros that a system's frequency response is determined by the locations of poles and zeros in the complex plane. Poles set the resonances and stability properties; zeros shape the amplitude response by introducing nulls and notches. What is less obvious is that a system's magnitude response |H(e^jω)| and phase response ∠H(e^jω) are not independent — for a certain special class of systems, the phase is entirely determined by the magnitude. Those systems are the **minimum-phase** systems, and understanding them is the key to understanding how phase and magnitude can be specified independently.

A system is minimum-phase if all of its zeros lie inside the unit circle (discrete-time) or in the left half-plane (continuous-time). The name comes from the comparison: among all stable, causal systems with the same magnitude spectrum |H(e^jω)|, the minimum-phase system introduces the smallest possible phase lag at every frequency — it has minimum **group delay**. From your study of all-pass filters, you know that an all-pass system has unit magnitude at all frequencies but introduces frequency-dependent phase shifts by placing zeros outside the unit circle (with corresponding poles inside). If you take a minimum-phase system and move one of its zeros from inside to outside the unit circle (to the conjugate reciprocal position 1/z*), the magnitude response is unchanged but the phase lag increases. The minimum-phase system is the uniquely "most efficient" phase choice for a given magnitude response.

Every stable, causal transfer function factors as H(z) = H_min(z) · H_ap(z), where H_min is minimum-phase and H_ap is all-pass (|H_ap(e^jω)| = 1 ∀ω). H_ap is constructed by taking all zeros outside the unit circle, reflecting them inside to their conjugate reciprocal positions to form H_min, and placing the original outside-unit-circle zeros in H_ap along with stabilizing poles. Because |H_ap| = 1 everywhere, the magnitude of H equals the magnitude of H_min alone — all magnitude shaping comes from the minimum-phase factor. All excess phase (beyond what H_min would introduce) comes from H_ap. This decomposition is not just algebraic bookkeeping: it separates the "what does this system do to amplitudes" question from the "how much extra phase delay does it introduce" question.

This factorization has profound practical consequences. Minimum-phase systems are **stably invertible**: their causal inverse H_min⁻¹(z) = 1/H_min(z) has all poles inside the unit circle (since H_min's zeros are inside the unit circle). This means a minimum-phase channel or filter can be perfectly equalized with a stable causal filter. Non-minimum-phase systems cannot be causally inverted stably — attempting to equalize a zero outside the unit circle requires placing a pole outside, producing an unstable inverse. Applications include communications channel equalization (remove the channel's distortion at the receiver), acoustic echo cancellation (invert the room impulse response), and seismic deconvolution (remove the source wavelet from recorded reflections). In each case, the first diagnostic question is: is this system minimum-phase? If yes, perfect causal inversion is feasible. If no, approximations, acausal processing, or regularized inversion are required.
