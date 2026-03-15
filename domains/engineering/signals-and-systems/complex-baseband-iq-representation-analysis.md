---
id: complex-baseband-iq-representation-analysis
title: Complex Baseband and In-Phase/Quadrature Representation
domain: engineering
course: signals-and-systems
prerequisites:
- id: modulation-amplitude-frequency-shift-keying
  type: hard
builds-toward:
- instantaneous-amplitude-and-frequency
- bandpass-sampling-and-undersampling
tags:
- baseband
- IQ
- complex
- representation
stage: concrete-operations
status: draft
---

# Complex Baseband and In-Phase/Quadrature Representation

## Core Idea
Complex baseband representation decomposes a real bandpass signal (modulated at carrier frequency fc) into I (in-phase, real) and Q (quadrature, imaginary) components at baseband via mixing with cosine and sine. This representation halves the required sampling rate compared to passband sampling, enables efficient digital processing, and simplifies modulation/demodulation. The analytic signal (Hilbert transform output) naturally produces I-Q components through multiplication by complex exponential.

## How It's Best Learned
Take a modulated signal and generate I-Q components by mixing with cos and sin at carrier frequency, then lowpass filtering. Verify that I-Q signal is complex baseband representation of original. Recover original by upconverting I-Q.

## Common Misconceptions
- Thinking I-Q components are magnitude and phase (they're orthogonal components).
- Confusing complex baseband with analytic signal (related but different).
- Not recognizing that I-Q sampling rate is 2fs instead of 4fs for passband signal.
