---
id: notch-filters-and-resonators
title: Notch Filters and Resonator Design
domain: engineering
course: signals-and-systems
prerequisites:
- id: frequency-response-and-bode-plots
  type: hard
builds-toward:
- butterworth-filter-maximally-flat-response
- chebyshev-filter-equiripple-response
tags:
- filters
- notch
- resonator
- narrow-band
stage: concrete-application
status: draft
---

# Notch Filters and Resonator Design

## Core Idea
Notch filters provide deep attenuation at a specific frequency while leaving other frequencies unaffected. They place zeros on the unit circle (or s-plane) at the notch frequency. Resonators amplify energy at a resonant frequency, placing poles near the unit circle with high quality factor Q. Both filters are useful for tone removal (notches) or tone enhancement (resonators), and Q controls bandwidth.

## How It's Best Learned
Design a simple notch filter by placing complex conjugate zeros on the unit circle. Measure attenuation at the notch frequency and 3-dB bandwidth away from notch.

## Common Misconceptions
- Thinking notches eliminate frequencies completely (not possible with finite filter).
- Confusing notch depth (determined by zero location) with bandwidth (determined by pole placement).
- Not recognizing that narrow notches require high Q, which affects numerical stability.
