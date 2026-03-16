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
- id: fourier-series-representation
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

## Explainer

From Bode plots and frequency response, you know how a circuit's gain and phase vary across frequency. A filter is a circuit engineered to exploit this variation deliberately: you shape the frequency response so that certain frequency ranges pass through with minimal attenuation while others are strongly suppressed. **Filter design** is the process of translating signal-processing requirements into a circuit topology and component values that achieve the desired frequency-selective behavior.

Every filter specification starts with four key parameters. The **passband** is the frequency range the filter must preserve, with at most a small **passband ripple** (measured in dB). The **stopband** is the frequency range the filter must suppress, attenuating signals by at least a specified amount (e.g., −40 dB). The gap between passband and stopband is the **transition band**, where the filter's gain rolls off. A steeper roll-off produces a sharper filter — better frequency selectivity — but typically requires higher circuit complexity. The **cutoff frequency** ω_c marks the boundary between passband and transition band, conventionally defined as the −3 dB point where gain has dropped to 1/√2 of its passband value.

The three classical filter families each make a different tradeoff. A **Butterworth filter** achieves a maximally flat (monotonically decreasing) magnitude response with no ripple anywhere, at the cost of a gentler roll-off for a given filter order. A **Chebyshev filter** allows controlled ripple in the passband but achieves a much steeper roll-off — for the same stopband attenuation requirement, fewer poles are needed than Butterworth. An **elliptic (Cauer) filter** tolerates ripple in both passband and stopband, achieving the steepest possible roll-off for a given order. The right choice depends on the application: audio equipment often prefers Butterworth's flat passband, while communications receivers may need the sharp selectivity of Chebyshev or elliptic designs where a small amount of passband ripple is acceptable.

Filter order n determines the ultimate roll-off rate: n × 20 dB/decade. A first-order filter (single RC) rolls off at 20 dB/decade. A second-order filter (the RLC circuits from your prerequisites) rolls off at 40 dB/decade. Higher-order filters are built by cascading second-order sections called **biquads**, each with its own resonant frequency and quality factor Q. Your prerequisite work on the Q factor directly applies here: each biquad section's Q controls how peaked its response is near its center frequency, and the specific Q values for each section in a cascade are chosen from standard design tables to achieve the target Butterworth, Chebyshev, or elliptic response overall.
