---
id: butterworth-analog-filter-design
title: Butterworth Analog Filter Design
domain: engineering
course: signals-and-systems
prerequisites:
- id: transfer-function-poles-zeros
  type: hard
- id: frequency-response-and-bode-plots
  type: hard
- id: laplace-transform-fundamentals
  type: hard
builds-toward:
- bilinear-transform-digital-filters
- elliptic-filter-design
- chebyshev-type-i-filters
tags:
- filter-design
- analog-filters
- butterworth
- magnitude-response
stage: advanced
status: draft
---

# Butterworth Analog Filter Design

## Core Idea
Butterworth filters maximize passband flatness by placing poles on a circle in the s-plane with monotonic magnitude response. The order determines rolloff rate (20 dB/decade per order) and passband ripple (zero). Pole locations follow standard normalized tables, and designs scale easily to any cutoff frequency or implementation topology.
