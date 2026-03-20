---
id: notch-filters-and-resonators
title: Notch Filters and Resonator Design
domain: engineering
course: signals-and-systems
prerequisites:
- id: frequency-response-and-bode-plots
  type: hard
builds-toward:
- butterworth-filter-maximally-flat-response
- chebyshev-filter-equiripple-response
tags:
- filters
- notch
- resonator
- narrow-band
stage: advanced
status: draft
---

# Notch Filters and Resonator Design

## Core Idea
Notch filters provide deep attenuation at a specific frequency while leaving other frequencies unaffected. They place zeros on the unit circle (or s-plane) at the notch frequency. Resonators amplify energy at a resonant frequency, placing poles near the unit circle with high quality factor Q. Both filters are useful for tone removal (notches) or tone enhancement (resonators), and Q controls bandwidth.

## How It's Best Learned
Design a simple notch filter by placing complex conjugate zeros on the unit circle. Measure attenuation at the notch frequency and 3-dB bandwidth away from notch.

## Common Misconceptions
- Thinking notches eliminate frequencies completely (not possible with finite filter).
- Confusing notch depth (determined by zero location) with bandwidth (determined by pole placement).
- Not recognizing that narrow notches require high Q, which affects numerical stability.

## Explainer

From your work with Bode plots and frequency response, you know that a filter's behavior is completely characterized by the locations of its poles and zeros in the s-plane (continuous-time) or z-plane (discrete-time). Poles amplify frequencies near them; zeros attenuate frequencies near them. A **notch filter** is the extreme case of targeted attenuation: place a pair of complex-conjugate zeros exactly on the unit circle at angle ω₀, and the filter response goes to zero at precisely that frequency. In discrete-time, the transfer function for the zero pair alone is H(z) = z² − 2cos(ω₀)z + 1, which evaluates to zero when z = e^(±jω₀). Everything else in the spectrum is unaffected — except that you must also add a gain scaling factor to preserve unity gain at DC or some other reference frequency.

The problem with zeros alone is that the notch is very broad — you attenuate a wide band around ω₀. To narrow it, add a pair of poles just inside the unit circle at the same angle: H(z) = (z² − 2cos(ω₀)z + 1) / (z² − 2r·cos(ω₀)z + r²), where r < 1 is the pole radius. As r → 1, the poles move toward the unit circle and nearly cancel the effect of the zeros everywhere except right at ω₀, where the zeros still dominate. The **quality factor Q** = ω₀ / (2-bandwidth) characterizes the sharpness: high Q means narrow notch. The cost is numerical sensitivity — when r is close to 1, small coefficient errors (from fixed-point arithmetic or finite-precision implementation) shift the poles and dramatically alter the notch depth and bandwidth. High-Q notch filters require careful implementation, sometimes using second-order sections or specialized structures.

A **resonator** is the dual: instead of zeros on the unit circle, place poles close to but inside the unit circle at the resonant frequency ω₀, with zeros placed away from that frequency (or at DC/Nyquist). The response peaks sharply at ω₀ and falls off at other frequencies. The higher the pole radius r, the closer to the unit circle, the sharper and taller the peak, and the higher the Q. An ideal resonator with r = 1 (poles on the unit circle) would produce infinite gain — an unstable sinusoidal oscillator. A practical digital resonator with r slightly below 1 is a stable narrow-band amplifier that can serve as a **tone detector**, a channel in a filter bank, or the basis for a sinusoidal signal generator in music synthesis.

Notch filters appear constantly in real systems: removing 50 or 60 Hz power line interference from physiological recordings (ECG, EEG), canceling a specific mechanical vibration frequency in a motor controller, or eliminating a pilot tone in audio equipment. The design recipe is straightforward: identify the exact frequency to remove, place zeros on the unit circle there, and choose a pole radius r to set the acceptable bandwidth. A bandwidth of 2 Hz centered on 60 Hz requires r ≈ 1 − π·(2)/f_s, so at 1 kHz sample rate, r ≈ 0.994. The resulting filter passes all other frequencies with nearly unit gain while achieving 40–60 dB attenuation at 60 Hz — an elegant piece of geometry that requires nothing but two zeros and two poles.


