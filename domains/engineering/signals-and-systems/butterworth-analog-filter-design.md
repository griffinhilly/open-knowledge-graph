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
stage: expert
status: draft
---

# Butterworth Analog Filter Design

## Core Idea
Butterworth filters maximize passband flatness by placing poles on a circle in the s-plane with monotonic magnitude response. The order determines rolloff rate (20 dB/decade per order) and passband ripple (zero). Pole locations follow standard normalized tables, and designs scale easily to any cutoff frequency or implementation topology.

## Questions

```yaml
- question: "An engineer needs a lowpass filter where the passband response must be as flat as possible — zero ripple across all passband frequencies — and she can tolerate a gradual transition to the stopband. A second engineer needs the sharpest possible transition at the same filter order, even if it introduces passband ripple. Which filter type should each engineer choose?"
  type: multiple-choice
  options:
    - "Both should use Butterworth filters — Butterworth is optimal for all design goals"
    - "First engineer: Butterworth (maximally flat passband, monotonic rolloff); Second engineer: Chebyshev or elliptic (sharper rolloff at same order, at the cost of passband or stopband ripple)"
    - "First engineer: Chebyshev (flatter passband); Second engineer: Butterworth (steeper rolloff)"
    - "First engineer: elliptic (lowest ripple); Second engineer: Butterworth (sharpest rolloff)"
  answer: 1
  explanation: "The Butterworth filter's defining property is maximally flat magnitude response in the passband — no ripple, monotonically decreasing from DC to the cutoff. This flatness comes at a cost: for a given filter order N, Butterworth has a less steep transition band than Chebyshev (which allows equiripple in the passband) or elliptic (which allows ripple in both bands). Chebyshev and elliptic filters achieve sharper rolloff at the same order by trading passband or stopband flatness. The choice among filter families is always a tradeoff between flatness and rolloff steepness."

- question: "A 3rd-order Butterworth lowpass filter has a cutoff frequency of 1 kHz. At 10 kHz (one decade above cutoff), what is the approximate attenuation?"
  type: multiple-choice
  options:
    - "20 dB, since one decade always produces 20 dB of attenuation regardless of filter order"
    - "60 dB, since each order contributes 20 dB/decade and three orders give 60 dB/decade"
    - "3 dB, since the −3 dB point is at the cutoff frequency"
    - "120 dB, since each pole contributes 40 dB/decade in the rolloff region"
  answer: 1
  explanation: "The Butterworth rolloff rate is 20N dB/decade, where N is the filter order. For N=3, that is 60 dB/decade. One decade above the cutoff (10 kHz vs. 1 kHz) gives approximately 60 dB of attenuation. This follows directly from |H(jω)| ≈ (ω_c/ω)^N for ω ≫ ω_c — at 10× the cutoff, the magnitude is (1/10)^3 = 10^−3, which is −60 dB. Option A confuses the rolloff rate of a first-order filter with an order-independent rule; option D (40 dB/pole) is a misconception that arises from confusing double poles with single poles."

- question: "All Butterworth lowpass filters, regardless of order, have exactly −3 dB attenuation at their cutoff frequency ω_c."
  type: true-false
  answer: true
  explanation: "This follows directly from the Butterworth magnitude formula: |H(jω_c)|² = 1/(1 + (ω_c/ω_c)^(2N)) = 1/(1+1) = 1/2, so |H(jω_c)| = 1/√2 ≈ 0.707 ≈ −3.01 dB for any N. This is a defining property of the Butterworth design: the −3 dB point is always exactly at the cutoff frequency, regardless of order. The order N only controls how quickly the response rolls off beyond ω_c, not where the −3 dB point is. This makes the cutoff frequency a well-defined, order-independent design parameter."

- question: "A higher-order Butterworth filter always achieves steeper stopband attenuation than a lower-order Chebyshev filter of any type."
  type: true-false
  answer: false
  explanation: "Chebyshev filters achieve steeper rolloff than Butterworth filters of the same order, precisely because they allow ripple in the passband (Type I) or stopband (Type II). The passband ripple is the 'payment' for the extra rolloff sharpness. So a 3rd-order Chebyshev Type I can have steeper attenuation at a given stopband frequency than a 4th- or even 5th-order Butterworth, depending on the allowed ripple level. The order comparison only holds within the same filter family. Across families, the tradeoff is always flatness vs. transition-band sharpness, and higher order alone does not overcome a family's fundamental design tradeoff."

- question: "Why do Butterworth filters place all their poles on a circle in the left-half s-plane, and how does this geometric arrangement produce the maximally flat magnitude response?"
  type: short-answer
  answer: "Placing poles evenly spaced on a circle of radius ω_c in the left-half s-plane produces a magnitude response |H(jω)|² = 1/(1 + (ω/ω_c)^(2N)) — a function that equals exactly 1 at ω=0, equals 1/2 at ω=ω_c, and rolls off monotonically with no ripple. The 'maximally flat' property means the first 2N−1 derivatives of |H(jω)|² with respect to ω are zero at ω=0, making the passband deviate from unity as slowly as possible. Geometrically, the even angular spacing of poles on the circle distributes the rolloff contribution uniformly — no single pole dominates, and there are no resonant peaks or troughs. The poles must be in the left-half plane to ensure stability."
  explanation: "Understanding why the circle placement works requires connecting the s-plane pole locations to the frequency response. Along the imaginary axis (jω), the magnitude of the transfer function is the product of distances from jω to each zero divided by distances to each pole. When poles are evenly spaced on a circle, the denominator polynomial factors to produce exactly the Butterworth magnitude formula. The result is elegant: a purely geometric constraint (poles on a circle) produces an optimal mathematical property (maximally flat passband). This is why the Butterworth is often the first filter design introduced — the geometry and the math reinforce each other."
```

## Explainer

From your work on transfer functions and Bode plots, you know that a filter's frequency response is shaped entirely by its pole and zero locations in the s-plane. The closer a pole is to the imaginary axis, the more it boosts nearby frequencies; poles on or beyond the imaginary axis cause instability. The design problem for a lowpass filter is: given a desired frequency response shape (flat passband, sharp rolloff, attenuated stopband), where should you place the poles? The **Butterworth filter** answers this with an elegant geometric principle: place all N poles evenly spaced on a circle of radius ω_c in the left-half s-plane.

The resulting magnitude response is |H(jω)|² = 1 / (1 + (ω/ω_c)^(2N)). At ω = 0, the response is exactly 1 (0 dB). At ω = ω_c, the response is 1/√2 (−3 dB) regardless of order. Beyond ω_c, the response rolls off monotonically — no ripple, no bumps, just a smooth decay. This **maximally flat** property is what the Butterworth optimization achieves: among all polynomial filters of order N with −3 dB at ω_c, the Butterworth has the maximum number of derivatives equal to zero at ω = 0, meaning the passband deviates from unity as slowly as possible. The tradeoff is that this flatness comes at the cost of rolloff sharpness: a Butterworth is less steep in the transition band than a Chebyshev or elliptic filter of the same order.

The rolloff rate follows directly from the mathematics: |H(jω)| ≈ (ω_c/ω)^N for ω ≫ ω_c. Each decade of frequency above ω_c attenuates by a factor of 10^N, which is 20N dB/decade. A first-order Butterworth gives −20 dB/decade; second order −40 dB/decade; and so on. This is why filter order is a design variable: if your stopband attenuation requirement is 80 dB at one decade above the cutoff, you need at least a fourth-order filter. From your Bode plot knowledge, you can also recognize this as N poles clustered near ω_c all contributing approximately −20 dB/decade each in the rolloff region.

The design procedure is standardized through **normalized prototype tables**. The normalized Butterworth lowpass prototype has ω_c = 1 rad/s; its pole locations for order N are s_k = e^(jπ(2k+N−1)/2N) for k = 1, 2, ..., N (only the left-half plane poles are used). For N = 2, the poles are at ±j·e^(jπ/4) = (−1/√2) ± j(1/√2), giving the familiar second-order transfer function with Q = 1/√2 ≈ 0.707 (the Butterworth Q). To design a filter for a different cutoff frequency, you scale the prototype poles by ω_c. To implement in hardware (an op-amp active filter or an LC ladder network), you map the pole locations to component values using standard topologies like Sallen-Key or multiple-feedback. To convert to a digital filter, you apply the bilinear transform — which you'll encounter as a follow-on topic. The prototype-then-scale workflow makes Butterworth filters among the most routinely implemented analog filter designs in instrumentation and audio engineering.
