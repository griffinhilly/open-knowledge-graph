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
stage: advanced
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

## Explainer

From your study of filter order and transition bands, you know that a higher-order filter produces steeper rolloff but also more complexity — more poles, more components, more phase shift. You also know that no filter has a perfectly sharp transition from passband to stopband; every realizable filter is a tradeoff between passband behavior, transition bandwidth, and stopband attenuation. The Butterworth design is one specific, principled way to navigate this tradeoff, and its defining choice is to sacrifice transition bandwidth in exchange for the smoothest possible passband.

The Butterworth design criterion is **maximally flat at ω = 0**. Mathematically, the squared magnitude response is |H(jω)|² = 1 / (1 + (ω/ωc)^(2N)), where N is the filter order and ωc is the cutoff frequency. At ω = 0, this equals exactly 1 regardless of N. As ω increases, the denominator grows, but the flatness property guarantees that the first 2N−1 derivatives of the magnitude response are zero at ω = 0. Intuitively: the response is as flat as possible at DC, and it stays flat into the passband before rolling off. At ω = ωc, the response is always exactly −3 dB, regardless of order. Beyond ωc, it rolls off at 20N dB/decade — steeper with higher order.

The poles of the Butterworth filter lie on a circle of radius ωc in the left half of the s-plane, equally spaced in angle by 180°/N. This elegant geometric distribution is what makes the passband so flat: the poles are spread symmetrically so that no one frequency sees a strong resonance. For a stable causal filter, only the N left-half-plane poles are used. The resulting **Butterworth polynomials** — the denominators of the transfer function — have real coefficients and are tabulated for each order. A second-order Butterworth, for example, has poles at angles ±45° from the imaginary axis, giving the familiar denominator s² + √2·s + 1 in normalized form.

The fundamental limitation of Butterworth is that maximally flat at DC comes at the cost of a gradual transition from passband to stopband. Compare to a same-order **Chebyshev Type I** filter: Chebyshev allows equiripple oscillations in the passband (the magnitude bounces between 1 and 1−δ repeatedly rather than monotonically decreasing from 1). By "wasting" some flatness tolerance in the passband, Chebyshev achieves a steeper rolloff at the same order. An 8th-order Chebyshev with 1 dB passband ripple will have a much sharper transition than an 8th-order Butterworth. The right choice depends on application: audio processing often favors Butterworth's flat passband (no frequency coloration within the pass band); data communications might accept passband ripple to achieve sharper frequency separation. Recognizing Butterworth as the "flatness-optimized" point on the design tradeoff surface is the key conceptual takeaway.
