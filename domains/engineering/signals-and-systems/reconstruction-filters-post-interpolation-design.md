---
id: reconstruction-filters-post-interpolation-design
title: Reconstruction Filters and Post-Interpolation Design
domain: engineering
course: signals-and-systems
prerequisites:
- id: sampling-theorem-nyquist-rate
  type: hard
builds-toward:
- interpolation-filtering-image-rejection
- complex-baseband-iq-representation-analysis
tags:
- reconstruction
- filters
- DAC
- interpolation
stage: concrete-operations
status: draft
---

# Reconstruction Filters and Post-Interpolation Design

## Core Idea
Digital-to-analog conversion produces a staircase-like signal with spectral images at multiples of sampling frequency. Reconstruction filters (lowpass) remove these images, leaving only the baseband signal. Ideal reconstruction requires a sinc filter; practical filters trade transition band sharpness against attenuation of spectral images. The reconstruction filter prevents aliasing during DAC conversion, complementing the anti-aliasing filter on the input side.

## How It's Best Learned
Generate sampled sinusoid, convert to analog with zero-order-hold (produces staircase), then filter with lowpass. Observe spectral images are suppressed. Compare different filter orders and corner frequencies.

## Common Misconceptions
- Thinking DAC output is automatically reconstructed (it's staircase without filter).
- Confusing reconstruction filter with anti-aliasing filter (both are lowpass but at different locations).
- Not recognizing that practical DACs use internal reconstruction filters.
