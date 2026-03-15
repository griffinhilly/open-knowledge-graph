---
id: dithering-techniques-quantization-improvement
title: Dithering Techniques and Quantization Noise Shaping
domain: engineering
course: signals-and-systems
prerequisites:
- id: quantization-error-and-noise-analysis
  type: hard
builds-toward:
- anti-aliasing-filters-pre-sampling-design
- reconstruction-filters-post-interpolation-design
tags:
- dithering
- quantization
- noise-shaping
- resolution
stage: formal-systems
status: draft
---

# Dithering Techniques and Quantization Noise Shaping

## Core Idea
Dithering adds small random noise before quantization to randomize quantization error, converting correlated (colored) error into white noise. This prevents patterns, banding, and harmonic distortion but at the cost of slightly increased noise floor. Noise-shaping dithering distributes quantization error toward frequencies where it's less perceptible (e.g., high frequencies for audio). Delta-sigma modulation uses noise-shaping to achieve high effective resolution from low-bit quantizers.

## How It's Best Learned
Quantize a low-amplitude sinusoid with and without dithering. Observe that dithering eliminates distortion at the cost of white noise. Compare frequency spectrum before and after dithering.

## Common Misconceptions
- Thinking dithering always improves SNR (it trades distortion for noise).
- Assuming all dithering is equivalent (subtractive dithering differs from noise-shaping).
- Not recognizing perceptual benefits beyond SNR improvement.
