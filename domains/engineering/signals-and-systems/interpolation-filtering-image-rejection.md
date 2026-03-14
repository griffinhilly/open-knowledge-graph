---
id: interpolation-filtering-image-rejection
title: Interpolation, Image Rejection, and Upsampling
domain: engineering
course: signals-and-systems
prerequisites:
- id: reconstruction-filters-post-interpolation-design
  type: hard
builds-toward:
- polyphase-filter-decomposition-multirate
tags:
- interpolation
- upsampling
- image-rejection
- multirate
stage: concrete-application
status: draft
---

# Interpolation, Image Rejection, and Upsampling

## Core Idea
Interpolation by factor L involves upsampling by inserting L-1 zeros between each sample, then filtering to remove spectral images. Unfiltered upsampling creates images at multiples of the original sampling rate. The anti-imaging filter must eliminate these images (frequencies above the original Nyquist rate) while preserving the baseband signal in the wider frequency range. Interpolation increases sample rate while maintaining signal information.

## How It's Best Learned
Upsample a discrete signal by factor 2 with and without anti-imaging filter. Observe spectral images in the unfiltered case; verify filter removes them while preserving baseband.

## Common Misconceptions
- Thinking upsampling creates new information (zeros don't add information).
- Confusing anti-imaging filter cutoff with original Nyquist frequency.
- Not recognizing that interpolation is dual of decimation.
