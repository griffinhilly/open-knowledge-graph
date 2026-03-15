---
id: gaussian-and-colored-noise-characterization
title: Gaussian and Colored Noise Characterization
domain: engineering
course: signals-and-systems
prerequisites:
- id: random-signals-autocorrelation-psd
  type: hard
builds-toward:
- signal-detection-and-hypothesis-testing
- quantization-error-and-noise-analysis
tags:
- noise
- gaussian
- colored-noise
- characterization
stage: concrete-operations
status: draft
---

# Gaussian and Colored Noise Characterization

## Core Idea
White noise has flat power spectral density and zero autocorrelation except at lag zero; colored (shaped) noise has frequency-dependent spectral content determined by its autocorrelation function. Gaussian noise has Gaussian amplitude distribution and is fully characterized by mean and variance. Non-Gaussian noise (e.g., uniform, laplacian) has different amplitude statistics. Understanding noise type is essential for signal detection, estimation, and filter design.

## How It's Best Learned
Generate white and colored noise (filter white noise with lowpass). Compare their autocorrelation functions and power spectral densities. Fit parametric models (AR) to colored noise.

## Common Misconceptions
- Thinking white noise means quiet (it means flat spectrum).
- Confusing Gaussian amplitude distribution with white spectrum.
- Assuming all practical noise is white or Gaussian.
