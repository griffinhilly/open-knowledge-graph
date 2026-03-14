---
id: second-order-active-filters
title: Second-Order Active Filters
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: first-order-active-filters
  type: hard
- id: resonance-circuits
  type: soft
tags:
- sallen-key
- butterworth
- chebyshev
- q-factor
- second-order
- damping-ratio
- active-filter
- band-pass
stage: formal-systems
status: draft
---

# Second-Order Active Filters

## Core Idea
Second-order active filters achieve -40 dB/decade roll-off using a single op-amp with two reactive elements, providing steeper frequency selectivity than first-order designs. The Sallen-Key topology is the most common: it uses a non-inverting op-amp configuration with two RC sections and positive feedback through the filter network to create complex conjugate poles. The filter's behavior is characterized by three parameters: cutoff frequency f_0, quality factor Q (or equivalently damping ratio zeta = 1/2Q), and passband gain. Butterworth response (Q = 0.707, maximally flat passband) provides no ripple with moderate roll-off steepness. Chebyshev response (Q > 0.707) allows passband ripple in exchange for a steeper transition band. Bessel response (Q < 0.707) preserves signal waveform shape with maximally flat group delay at the expense of a more gradual roll-off. Higher-order filters are built by cascading second-order sections (biquads), each designed with specific Q values from filter tables to achieve the desired overall response. Band-pass and band-stop second-order filters are also realizable, with the band-pass Q determining selectivity.

## How It's Best Learned
Derive the transfer function of the Sallen-Key low-pass filter by writing KCL at both RC nodes, then express it in standard second-order form H(s) = H_0 * w_0^2 / (s^2 + (w_0/Q)*s + w_0^2). Plot the magnitude response for Q = 0.5, 0.707, and 2 to see underdamped peaking, maximally flat, and rippled responses. Use filter design tables to build a fourth-order Butterworth by cascading two Sallen-Key sections with prescribed Q values.

## Common Misconceptions
- Assuming higher Q is always better — high Q produces peaking near the cutoff that distorts signals with energy near that frequency; Butterworth (Q = 0.707) is the standard choice when flat passband response is needed.
- Believing a single Sallen-Key stage can achieve arbitrarily steep roll-off — it is always second-order (-40 dB/decade); steeper roll-off requires cascading multiple sections.
- Ignoring component sensitivity — the Sallen-Key topology is sensitive to component tolerances, especially at high Q; a 5% change in one resistor can shift the cutoff frequency and Q significantly, requiring precision components for demanding applications.
