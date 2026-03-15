---
id: filter-order-and-transition-band
title: Filter Order, Rolloff Rate, and Transition Band
domain: engineering
course: signals-and-systems
prerequisites:
- id: filter-specifications-design-parameters
  type: hard
builds-toward:
- butterworth-filter-maximally-flat-response
- chebyshev-filter-equiripple-response
tags:
- filters
- order
- rolloff
- transition-band
stage: formal-systems
status: draft
---

# Filter Order, Rolloff Rate, and Transition Band

## Core Idea
Filter order determines the steepness of the transition band; an Nth-order filter rolls off at approximately 20N dB/decade for Butterworth designs. Higher order filters have sharper transitions but require more computation and can introduce instability or ringing. The transition band width is bounded by the filter specifications and cannot be made arbitrarily small without increasing order.

## How It's Best Learned
Design low-, medium-, and high-order Butterworth filters with identical edge frequencies and measure their rolloff rates. Plot magnitude responses on log scale to see the asymptotic slopes.

## Common Misconceptions
- Thinking transition band can be eliminated.
- Forgetting the 20N dB/decade rule for non-Butterworth filters.
- Not considering numerical stability of high-order filters.
