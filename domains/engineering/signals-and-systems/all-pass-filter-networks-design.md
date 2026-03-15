---
id: all-pass-filter-networks-design
title: All-Pass Filter Networks and Phase Equalization
domain: engineering
course: signals-and-systems
prerequisites:
- id: frequency-response-and-bode-plots
  type: hard
builds-toward:
- linear-phase-filter-design-preservation
- group-delay-phase-characterization
tags:
- filters
- all-pass
- phase
- equalization
stage: concrete-operations
status: draft
---

# All-Pass Filter Networks and Phase Equalization

## Core Idea
All-pass filters have unity magnitude response across all frequencies but introduce frequency-dependent phase shifts. They have poles inside the unit circle (or left s-plane) and zeros as their mirror images, creating complementary magnitude. Used as phase equalizers to correct non-linear phase from other filters, or to create group delay for frequency-selective delay adjustments.

## How It's Best Learned
Design a 2nd-order all-pass filter and verify its magnitude response is unity while phase changes significantly. Cascade it with a non-minimum-phase filter to equalize phase response.

## Common Misconceptions
- Thinking all-pass filters change magnitude (they don't).
- Confusing all-pass with low-pass or high-pass.
- Not recognizing that all-pass adds no attenuation, only delay variation.
