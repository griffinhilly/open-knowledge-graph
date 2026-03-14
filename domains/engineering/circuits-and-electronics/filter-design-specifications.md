---
id: filter-design-specifications
title: Filter Design and Specifications
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: frequency-response-analysis-bode
  type: hard
- id: quality-factor-bandwidth-tradeoff
  type: soft
tags:
- filters
- filter-design
stage: formal-systems
status: draft
---

# Filter Design and Specifications

## Core Idea
Filters selectively pass or attenuate frequency ranges defined by cutoff frequencies, stopband attenuation, and passband ripple. Lowpass filters pass low frequencies; highpass pass high frequencies; bandpass pass a band; bandstop reject a band. Filter order determines roll-off rate (n×20 dB/decade for n-th order). Butterworth (flat passband, monotonic), Chebyshev (rippled passband, sharper cutoff), and Elliptic (rippled passband and stopband) filters optimize different design tradeoffs.
