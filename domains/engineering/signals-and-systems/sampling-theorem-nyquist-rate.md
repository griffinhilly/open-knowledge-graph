---
id: sampling-theorem-nyquist-rate
title: Sampling Theorem and Nyquist Sampling Rate
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-classification-continuous-discrete
  type: hard
- id: fourier-transform-definition-properties
  type: hard
builds-toward:
- aliasing-reconstruction-signals
- dft-and-fft-algorithms
tags:
- sampling
- nyquist
- discrete-time
stage: advanced
status: draft
---

# Sampling Theorem and Nyquist Sampling Rate

## Core Idea
The Nyquist sampling theorem states that a bandlimited signal with maximum frequency f_max must be sampled at f_s ≥ 2·f_max to avoid losing information. If this condition is violated, aliasing—overlap of frequency components—corrupts the discrete signal and makes reconstruction impossible.
