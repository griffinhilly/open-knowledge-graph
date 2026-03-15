---
id: anti-aliasing-filters-pre-sampling-design
title: Anti-Aliasing Filters and Pre-Sampling Design
domain: engineering
course: signals-and-systems
prerequisites:
- id: sampling-theorem-nyquist-rate
  type: hard
builds-toward:
- decimation-anti-aliasing-and-downsampling
- reconstruction-filters-post-interpolation-design
tags:
- anti-aliasing
- filters
- sampling
- design
stage: formal-systems
status: draft
---

# Anti-Aliasing Filters and Pre-Sampling Design

## Core Idea
Aliasing occurs when frequency components above the Nyquist rate (fs/2) are not removed before sampling. Anti-aliasing filters (lowpass) eliminate out-of-band content before the ADC to prevent spectral folding. The filter must have sharp transition band near fs/2 and sufficient stopband attenuation to reduce aliases below noise floor. Trade-offs exist between filter sharpness (cost, latency) and aliasing suppression.

## How It's Best Learned
Demonstrate aliasing on a signal without anti-aliasing filter, then add a lowpass filter before sampling and observe aliased components are suppressed. Design filter specifications from acceptable alias level.

## Common Misconceptions
- Thinking sampling theorem eliminates need for anti-aliasing filters (it justifies their requirement).
- Assuming filter edge must be exactly at fs/2 (should be below to account for filter transition).
- Not accounting for filter delay when designing data acquisition pipelines.
