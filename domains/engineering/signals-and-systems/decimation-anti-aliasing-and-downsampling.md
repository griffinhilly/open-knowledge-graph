---
id: decimation-anti-aliasing-and-downsampling
title: Decimation, Anti-Aliasing, and Downsampling
domain: engineering
course: signals-and-systems
prerequisites:
- id: anti-aliasing-filters-pre-sampling-design
  type: hard
builds-toward:
- polyphase-filter-decomposition-multirate
tags:
- decimation
- downsampling
- anti-aliasing
- multirate
stage: concrete-application
status: draft
---

# Decimation, Anti-Aliasing, and Downsampling

## Core Idea
Decimation by factor M involves lowpass filtering to avoid aliasing, then downsampling by keeping every Mth sample. The anti-aliasing filter must eliminate frequencies above the new Nyquist rate (fs/M). Unfiltered downsampling causes aliasing from frequency components between fs/M and fs/2 to fold into the passband. Proper decimation preserves information in the signal band of interest while reducing data rate.

## How It's Best Learned
Demonstrate aliasing from direct downsampling by factor 3 on a signal containing energy above the new Nyquist rate. Design anti-aliasing filter, apply, then downsample. Verify aliasing is eliminated.

## Common Misconceptions
- Thinking downsampling preserves the entire signal (information outside new Nyquist rate is lost).
- Confusing the original and reduced Nyquist rates in filter design.
- Not accounting for filter order when specifying decimation system complexity.
