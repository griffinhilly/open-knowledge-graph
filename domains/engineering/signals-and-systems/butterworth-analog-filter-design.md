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

## Explainer

From your work on transfer functions and Bode plots, you know that a filter's frequency response is shaped entirely by its pole and zero locations in the s-plane. The closer a pole is to the imaginary axis, the more it boosts nearby frequencies; poles on or beyond the imaginary axis cause instability. The design problem for a lowpass filter is: given a desired frequency response shape (flat passband, sharp rolloff, attenuated stopband), where should you place the poles? The **Butterworth filter** answers this with an elegant geometric principle: place all N poles evenly spaced on a circle of radius ω_c in the left-half s-plane.

The resulting magnitude response is |H(jω)|² = 1 / (1 + (ω/ω_c)^(2N)). At ω = 0, the response is exactly 1 (0 dB). At ω = ω_c, the response is 1/√2 (−3 dB) regardless of order. Beyond ω_c, the response rolls off monotonically — no ripple, no bumps, just a smooth decay. This **maximally flat** property is what the Butterworth optimization achieves: among all polynomial filters of order N with −3 dB at ω_c, the Butterworth has the maximum number of derivatives equal to zero at ω = 0, meaning the passband deviates from unity as slowly as possible. The tradeoff is that this flatness comes at the cost of rolloff sharpness: a Butterworth is less steep in the transition band than a Chebyshev or elliptic filter of the same order.

The rolloff rate follows directly from the mathematics: |H(jω)| ≈ (ω_c/ω)^N for ω ≫ ω_c. Each decade of frequency above ω_c attenuates by a factor of 10^N, which is 20N dB/decade. A first-order Butterworth gives −20 dB/decade; second order −40 dB/decade; and so on. This is why filter order is a design variable: if your stopband attenuation requirement is 80 dB at one decade above the cutoff, you need at least a fourth-order filter. From your Bode plot knowledge, you can also recognize this as N poles clustered near ω_c all contributing approximately −20 dB/decade each in the rolloff region.

The design procedure is standardized through **normalized prototype tables**. The normalized Butterworth lowpass prototype has ω_c = 1 rad/s; its pole locations for order N are s_k = e^(jπ(2k+N−1)/2N) for k = 1, 2, ..., N (only the left-half plane poles are used). For N = 2, the poles are at ±j·e^(jπ/4) = (−1/√2) ± j(1/√2), giving the familiar second-order transfer function with Q = 1/√2 ≈ 0.707 (the Butterworth Q). To design a filter for a different cutoff frequency, you scale the prototype poles by ω_c. To implement in hardware (an op-amp active filter or an LC ladder network), you map the pole locations to component values using standard topologies like Sallen-Key or multiple-feedback. To convert to a digital filter, you apply the bilinear transform — which you'll encounter as a follow-on topic. The prototype-then-scale workflow makes Butterworth filters among the most routinely implemented analog filter designs in instrumentation and audio engineering.
