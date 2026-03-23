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
stage: expert
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

## Questions

```yaml
- question: "An audio engineer needs to process a signal where any ripple within the passband would be audible and objectionable, but a gradual transition to the stopband is acceptable. Which filter design is most appropriate?"
  type: multiple-choice
  options:
    - "Chebyshev Type I — it has equiripple in the passband, providing very sharp rolloff"
    - "Elliptic (Cauer) — it has ripple in both passband and stopband but achieves the sharpest possible transition"
    - "Butterworth — maximally flat passband means no audible coloration within the passband, at the cost of a gradual rolloff"
    - "Chebyshev Type II — it has equiripple in the stopband but a monotonically decreasing passband, providing sharper rolloff than Butterworth"
  answer: 2
  explanation: "Butterworth is the correct choice when passband flatness is paramount. Its defining property — the first 2N−1 derivatives of the magnitude response are zero at ω = 0 — ensures no ripple within the passband, so no frequency is amplified or attenuated relative to others. The tradeoff is a gradual transition band: a same-order Chebyshev Type I achieves sharper rolloff by accepting equiripple in the passband. In audio, passband ripple causes frequency coloration. Chebyshev Type II (option D) does have a monotone passband, but its passband is not maximally flat and it still outperforms Butterworth on rolloff sharpness, so it would be preferred when transition sharpness matters more than ultimate flatness."

- question: "A 6th-order Butterworth lowpass filter has a cutoff frequency of ωc = 1 rad/s. At a frequency of 10 rad/s (one decade above cutoff), approximately how much is the signal attenuated?"
  type: multiple-choice
  options:
    - "−20 dB — only the first-order term dominates at high frequencies"
    - "−60 dB — each order contributes 10 dB/decade"
    - "−120 dB — the 6th-order filter rolls off at 20×6 = 120 dB/decade"
    - "−3 dB — the −3 dB point is fixed at ωc regardless of order"
  answer: 2
  explanation: "Butterworth rolls off at 20N dB/decade in the stopband. For N = 6: 20 × 6 = 120 dB/decade. At 10 rad/s (one decade above the 1 rad/s cutoff), the attenuation is approximately 120 dB. This can also be verified from the magnitude formula: |H(j·10)|² = 1/(1 + 10^12) ≈ 10^{−12}, corresponding to −120 dB in power or −60 dB in amplitude — but since dB for voltage/amplitude is 20 log₁₀, we get 20 × log₁₀(10^6) = 120 dB. The steep stopband attenuation at high order is one of Butterworth's strengths, offset by its slow initial rolloff near ωc."

- question: "A Butterworth filter of any order reaches exactly −3 dB at the cutoff frequency ωc, regardless of the order N."
  type: true-false
  answer: true
  explanation: "This is a defining property of the Butterworth design. The squared magnitude at ω = ωc is |H(jωc)|² = 1/(1 + (ωc/ωc)^{2N}) = 1/(1 + 1) = 1/2 for every N. Since −10 log₁₀(1/2) ≈ 3.01 dB, the −3 dB point is exactly at ωc regardless of order. This consistent −3 dB definition of cutoff frequency makes Butterworth filters straightforward to specify and compare across orders."

- question: "A Butterworth filter is the optimal choice whenever steep stopband attenuation is required, because its monotonic rolloff means it reaches full stopband attenuation faster than any other filter type."
  type: true-false
  answer: false
  explanation: "This is the primary Butterworth misconception. Butterworth is optimal for *passband flatness*, not stopband rolloff speed. For a given filter order, Chebyshev Type I achieves steeper rolloff by allowing equiripple in the passband; Chebyshev Type II achieves steep rolloff by allowing equiripple in the stopband; the elliptic (Cauer) filter achieves the steepest possible rolloff by allowing ripple in both. When stopband attenuation is the priority, Butterworth is one of the *worst* choices at a given order — it sacrifices rolloff sharpness to preserve its monotonically flat passband."

- question: "Explain the core tradeoff that defines the Butterworth filter, and describe the type of application where this tradeoff is favorable."
  type: short-answer
  answer: "Butterworth maximizes passband flatness (the first 2N−1 derivatives of the magnitude are zero at DC) at the cost of a gradual transition band. The passband has zero ripple — the magnitude decreases monotonically — but the rolloff is slower than same-order Chebyshev or elliptic designs. This tradeoff is favorable in audio processing, measurement instrumentation, and any application where amplitude accuracy within the passband matters more than sharp frequency separation."
  explanation: "The tradeoff can be summarized as: Butterworth spends all its 'design degrees of freedom' on passband flatness, leaving little margin for a sharp transition. Chebyshev and elliptic filters redistribute those degrees of freedom to achieve steeper rolloff by accepting ripple somewhere. Understanding where each design sits on the flatness-vs-sharpness tradeoff surface is the key to selecting the right filter for an application."
```

## Explainer

From your study of filter order and transition bands, you know that a higher-order filter produces steeper rolloff but also more complexity — more poles, more components, more phase shift. You also know that no filter has a perfectly sharp transition from passband to stopband; every realizable filter is a tradeoff between passband behavior, transition bandwidth, and stopband attenuation. The Butterworth design is one specific, principled way to navigate this tradeoff, and its defining choice is to sacrifice transition bandwidth in exchange for the smoothest possible passband.

The Butterworth design criterion is **maximally flat at ω = 0**. Mathematically, the squared magnitude response is |H(jω)|² = 1 / (1 + (ω/ωc)^(2N)), where N is the filter order and ωc is the cutoff frequency. At ω = 0, this equals exactly 1 regardless of N. As ω increases, the denominator grows, but the flatness property guarantees that the first 2N−1 derivatives of the magnitude response are zero at ω = 0. Intuitively: the response is as flat as possible at DC, and it stays flat into the passband before rolling off. At ω = ωc, the response is always exactly −3 dB, regardless of order. Beyond ωc, it rolls off at 20N dB/decade — steeper with higher order.

The poles of the Butterworth filter lie on a circle of radius ωc in the left half of the s-plane, equally spaced in angle by 180°/N. This elegant geometric distribution is what makes the passband so flat: the poles are spread symmetrically so that no one frequency sees a strong resonance. For a stable causal filter, only the N left-half-plane poles are used. The resulting **Butterworth polynomials** — the denominators of the transfer function — have real coefficients and are tabulated for each order. A second-order Butterworth, for example, has poles at angles ±45° from the imaginary axis, giving the familiar denominator s² + √2·s + 1 in normalized form.

The fundamental limitation of Butterworth is that maximally flat at DC comes at the cost of a gradual transition from passband to stopband. Compare to a same-order **Chebyshev Type I** filter: Chebyshev allows equiripple oscillations in the passband (the magnitude bounces between 1 and 1−δ repeatedly rather than monotonically decreasing from 1). By "wasting" some flatness tolerance in the passband, Chebyshev achieves a steeper rolloff at the same order. An 8th-order Chebyshev with 1 dB passband ripple will have a much sharper transition than an 8th-order Butterworth. The right choice depends on application: audio processing often favors Butterworth's flat passband (no frequency coloration within the pass band); data communications might accept passband ripple to achieve sharper frequency separation. Recognizing Butterworth as the "flatness-optimized" point on the design tradeoff surface is the key conceptual takeaway.
