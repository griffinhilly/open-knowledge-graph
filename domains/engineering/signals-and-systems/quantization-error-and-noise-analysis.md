---
id: quantization-error-and-noise-analysis
title: Quantization Error and Noise Analysis
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-classification-continuous-discrete
  type: hard
builds-toward:
- dithering-techniques-quantization-improvement
- anti-aliasing-filters-pre-sampling-design
tags:
- quantization
- ADC
- noise
- error
stage: concrete-application
status: draft
---

# Quantization Error and Noise Analysis

## Core Idea
Analog-to-digital conversion introduces quantization error when rounding continuous values to discrete levels. For uniform quantization with step size Δ, quantization error is uniformly distributed on [-Δ/2, Δ/2], producing noise power of Δ²/12. Signal-to-quantization-noise-ratio (SQNR) improves 6 dB per additional bit. For small quantization error, treating it as white noise is a reasonable approximation, though this breaks down for underutilized quantizers or signals near quantization boundaries.

## How It's Best Learned
Quantize sinusoids of various amplitudes to 8-bit resolution. Measure quantization noise power and verify SQNR matches theoretical predictions. Observe non-white behavior when signal underutilizes quantizer range.

## Common Misconceptions
- Thinking quantization noise is always white (depends on signal characteristics).
- Assuming n-bit quantization gives n bits of information (doesn't account for underutilization).
- Not recognizing the 6 dB per bit rule applies only in saturation regime.
