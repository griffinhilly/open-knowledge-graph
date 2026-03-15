---
id: butterworth-filter-maximally-flat-response
title: Butterworth Filters and Maximally-Flat Passband
domain: engineering
course: signals-and-systems
prerequisites:
- id: filter-order-and-transition-band
  type: hard
builds-toward:
- filter-bank-design-multiband-analysis
- iir-filter-design-realization
tags:
- filters
- butterworth
- maximally-flat
- response-shape
stage: formal-systems
status: draft
---

# Butterworth Filters and Maximally-Flat Passband

## Core Idea
Butterworth filters have maximally-flat passband magnitude (no ripple) with monotonic decrease in stopband. The magnitude response magnitude squared is a rational function whose denominators are Butterworth polynomials with real coefficients. Nth-order Butterworth rolls off at 20N dB/decade. Butterworth designs maximize passband flatness at the cost of slower transition band rolloff compared to equiripple designs.

## How It's Best Learned
Design a 4th-order Butterworth lowpass filter with 1-rad/s cutoff; plot magnitude response and verify -3dB point. Compare rolloff rate to Chebyshev design at same order.

## Common Misconceptions
- Thinking Butterworth is optimal for all applications.
- Confusing Butterworth polynomial zeros with filter zeros.
- Not recognizing that Butterworth sacrifices rolloff sharpness for passband flatness.
