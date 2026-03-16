---
id: window-functions-spectral-leakage
title: Window Functions and Spectral Leakage
domain: engineering
course: signals-and-systems
prerequisites:
- id: dft-and-fft-algorithms
  type: hard
- id: fourier-transform-definition-properties
  type: hard
builds-toward:
- power-spectral-density-estimation
- digital-spectral-analysis-nonparametric
tags:
- windowing
- spectral-analysis
- dft
- frequency-domain
stage: advanced
status: draft
---

# Window Functions and Spectral Leakage

## Core Idea
Spectral leakage occurs when analyzing finite-length signals with the DFT because the signal is not periodic within the window. Window functions taper the signal at the edges to reduce leakage at the cost of broader mainlobes. Common windows (Hann, Hamming, Blackman, Kaiser) trade off mainlobe width and sidelobe attenuation, making the choice critical for spectral accuracy.

## Explainer

The DFT assumes the N samples you provide represent one complete period of a periodic signal. When you compute the N-point DFT, you are implicitly tiling the signal — pretending the N samples repeat forever. If the signal contains a frequency that does not fit an integer number of cycles within your window, the signal's value jumps discontinuously at the boundary between repetitions. That jump has energy at all frequencies, so it contaminates every spectral bin — this is **spectral leakage**. A pure sinusoid at exactly bin 5 produces energy only at bin 5; a sinusoid at frequency 5.3 (not a whole number of cycles in the window) smears its energy across all N bins.

This connects directly to what you learned about the Fourier transform and the DFT. Computing the N-point DFT of a finite segment of a signal is mathematically equivalent to multiplying the infinite signal by a rectangular pulse of width N, then transforming. In the frequency domain, multiplication becomes convolution: the DFT output is the convolution of the true spectrum with the Fourier transform of the rectangular window. The rectangular window's spectrum is a sinc-like function with a narrow mainlobe but **sidelobes** at only −13 dB below the peak — meaning a strong frequency can contaminate neighboring bins at 1/5 of its amplitude. The sidelobes fall off slowly, so leakage from a strong tone can bury a nearby weak tone.

The solution is a **window function**: taper the signal to zero at both edges before computing the DFT. A Hann window multiplies each sample n by w(n) = 0.5(1 − cos(2πn/N)), smoothly reaching zero at n = 0 and n = N−1. This eliminates the edge discontinuity. The cost is that the window's frequency-domain representation has a wider mainlobe — instead of resolving frequencies that differ by 1/N, you now need a separation of roughly 2/N. But the sidelobes drop to −31 dB, dramatically reducing the contamination. A Blackman window achieves −58 dB sidelobes at the cost of a 3/N mainlobe width.

The **Kaiser window** makes this tradeoff continuous via a parameter β: β = 0 gives a rectangular window, and increasing β widens the mainlobe while suppressing sidelobes. This lets you design the window to meet a specification — if you need to detect a signal 40 dB weaker than a nearby tone, choose β to give ≥40 dB sidelobe attenuation, then accept the resulting resolution loss. The design question is always: do you need to *resolve* close frequencies (want narrow mainlobe, tolerate sidelobes) or *detect* weak signals near strong ones (want low sidelobes, tolerate wider mainlobe)? These requirements pull in opposite directions, and no window satisfies both simultaneously.
