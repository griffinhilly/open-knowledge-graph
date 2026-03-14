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
