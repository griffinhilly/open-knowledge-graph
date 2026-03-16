---
id: impulse-invariance-discretization
title: Impulse Invariance for Digital Filter Design
domain: engineering
course: signals-and-systems
prerequisites:
- id: z-transform-discrete-time-signals
  type: hard
- id: laplace-transform-fundamentals
  type: hard
- id: aliasing-reconstruction-signals
  type: hard
tags:
- filter-design
- digital-filters
- discretization
- impulse-response
stage: advanced
status: draft
---

# Impulse Invariance for Digital Filter Design

## Core Idea
Impulse invariance maps analog filter impulse response to digital by sampling: h[n] = T·ha(nT). This preserves the shape of the analog response at sample times but introduces aliasing if the analog filter is not sufficiently bandlimited. Unlike bilinear transform, it does not preserve stability for poles outside the left half-plane.

## Explainer

From your study of the Laplace transform, you know how to design analog filters — Butterworth, Chebyshev — specified by poles in the s-plane. From the z-transform, you know how to analyze discrete-time systems. Impulse invariance is one bridge between these two worlds: it constructs a digital filter whose behavior deliberately mimics a known analog prototype, starting from the analog impulse response.

The method begins by expanding the analog transfer function H_a(s) into partial fractions: H_a(s) = Σ A_k / (s − s_k). Each term corresponds to a decaying exponential in the time domain: h_a(t) = Σ A_k e^(s_k t) u(t). **Impulse invariance** samples this continuous impulse response at intervals T to define the digital impulse response: h[n] = T · h_a(nT) = T · Σ A_k e^(s_k nT) u[n]. Taking the z-transform of each term gives H(z) = T · Σ A_k / (1 − e^(s_k T) z^{-1}). This is the key mapping rule: each analog pole at s = s_k becomes a digital pole at z = e^(s_k T). Poles in the left half s-plane (where Re(s_k) < 0) map to poles inside the unit circle (where |e^(s_k T)| < 1), preserving stability. The frequency axis maps as ω_digital = Ω_analog × T — digital frequencies are a scaled version of analog frequencies, with no warping.

The fatal limitation is **aliasing**, and your prerequisite on aliasing tells you exactly why it arises. The digital filter's frequency response is a periodic repetition of the analog: H(e^{jω}) = (1/T) Σ_k H_a(j(ω − 2πk)/T). If the analog filter has significant energy above the Nyquist frequency π/T, adjacent copies overlap and corrupt the spectrum. Butterworth and Chebyshev filters have infinite bandwidth — their magnitude falls off polynomially, never reaching exactly zero. Applying impulse invariance to these filters inevitably introduces aliasing. For a well-designed lowpass filter with substantial attenuation before Nyquist (say, −40 dB or better at π/T), the aliasing error may be acceptable. For highpass or wideband filters, the copies wrap around and add in-band, making the result useless.

This is why **bilinear transform** is often the preferred alternative: it maps the entire left half-plane to the unit disk interior without aliasing by compressing the infinite analog frequency axis onto [−π, π]. The trade-off is frequency **warping** — a nonlinear compression that distorts the filter shape unless pre-warped during design. Impulse invariance is preferred when you specifically need the digital filter's time-domain samples to match the analog prototype's values — for instance, when digitally simulating an analog physical system where matching the step response at sample instants matters more than matching the stopband at high frequencies. Knowing both methods, and when each is appropriate, is the practical skill.
