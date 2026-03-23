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

## Questions

```yaml
- question: "An audio amplifier manufacturer needs a low-pass filter with the top priority that all frequencies within the passband are reproduced at the same volume — no frequency should be louder or quieter than another. Which filter family is most appropriate?"
  type: multiple-choice
  options:
    - "Chebyshev — because it achieves the steepest roll-off for a given order"
    - "Elliptic — because it achieves the steepest possible roll-off and has the sharpest stopband"
    - "Butterworth — because it has a maximally flat passband with no ripple"
    - "Any filter family works equally well; the choice doesn't affect audio reproduction"
  answer: 2
  explanation: "The Butterworth filter achieves a maximally flat (monotonically decreasing) magnitude response with no ripple anywhere in the passband. For audio, uniform gain across all passband frequencies is essential to avoid coloring the sound. Chebyshev and elliptic filters achieve sharper cutoffs but introduce passband ripple — some frequencies are slightly louder or quieter — which is audible as tonal distortion. The tradeoff is that Butterworth requires higher order (more components) to achieve the same stopband attenuation as a Chebyshev or elliptic design."

- question: "A designer cascades two second-order filter sections to create a 4th-order low-pass filter. At frequencies well above the cutoff, what roll-off rate does this filter achieve?"
  type: multiple-choice
  options:
    - "20 dB/decade — each section contributes equally, and they average out"
    - "40 dB/decade — only the steeper of the two sections dominates"
    - "80 dB/decade — each second-order section contributes 40 dB/decade, and they add"
    - "160 dB/decade — the sections cascade exponentially"
  answer: 2
  explanation: "Roll-off rate scales as n × 20 dB/decade, where n is the filter order. A 4th-order filter rolls off at 4 × 20 = 80 dB/decade. Each second-order section contributes 40 dB/decade, and cascading sections multiplies their transfer functions — their dB attenuation values add. This additive property in dB is why cascading biquad sections is the standard way to build high-order filters with steep stopband attenuation."

- question: "A Chebyshev filter achieves a steeper roll-off than a Butterworth filter of the same order, but at the cost of ripple in the passband."
  type: true-false
  answer: true
  explanation: "This is the fundamental Butterworth-Chebyshev tradeoff. A Chebyshev filter allows equiripple behavior in the passband — the gain oscillates between defined limits — and uses this 'budget' of allowable variation to achieve significantly steeper roll-off at the passband edge. For the same stopband attenuation requirement, a Chebyshev design needs fewer poles than a Butterworth, reducing circuit complexity. The cost is passband ripple, acceptable in communications receivers but not in audio reproduction."

- question: "Increasing filter order always improves every aspect of filter performance simultaneously, with no downside."
  type: true-false
  answer: false
  explanation: "Higher filter order increases roll-off rate and achieves tighter transition bands, but it comes with real costs: more poles require more circuit elements (more biquad sections, more components), increasing size, cost, power consumption, and component sensitivity. For active filters, each additional stage adds noise and phase shift. Higher-order filters also have more complex group delay characteristics. Filter design is always a tradeoff; raising order alone does not eliminate the fundamental tensions between passband flatness, roll-off sharpness, and circuit complexity."

- question: "Why can't a filter simultaneously have a perfectly flat passband, an infinitely steep transition, and infinite stopband attenuation?"
  type: short-answer
  answer: "A filter with a perfectly flat passband, zero transition band width, and infinite stopband attenuation would require an impulse response of infinite duration (the ideal 'brick wall' filter), which is physically unrealizable. In practice, filter performance is limited by filter order: sharpness of the transition band, passband flatness, and stopband attenuation all improve with order, but any finite-order filter must trade among these properties. The Butterworth, Chebyshev, and elliptic families each represent different choices about which property to optimize given the constraint of finite order."
  explanation: "This is why filter design is fundamentally a tradeoff problem. Real-world filters make deliberate engineering choices about which deviations from ideal behavior are acceptable for the application at hand. The three classical families systematize these tradeoffs into well-characterized designs with predictable behavior."
```

## Explainer

From Bode plots and frequency response, you know how a circuit's gain and phase vary across frequency. A filter is a circuit engineered to exploit this variation deliberately: you shape the frequency response so that certain frequency ranges pass through with minimal attenuation while others are strongly suppressed. **Filter design** is the process of translating signal-processing requirements into a circuit topology and component values that achieve the desired frequency-selective behavior.

Every filter specification starts with four key parameters. The **passband** is the frequency range the filter must preserve, with at most a small **passband ripple** (measured in dB). The **stopband** is the frequency range the filter must suppress, attenuating signals by at least a specified amount (e.g., −40 dB). The gap between passband and stopband is the **transition band**, where the filter's gain rolls off. A steeper roll-off produces a sharper filter — better frequency selectivity — but typically requires higher circuit complexity. The **cutoff frequency** ω_c marks the boundary between passband and transition band, conventionally defined as the −3 dB point where gain has dropped to 1/√2 of its passband value.

The three classical filter families each make a different tradeoff. A **Butterworth filter** achieves a maximally flat (monotonically decreasing) magnitude response with no ripple anywhere, at the cost of a gentler roll-off for a given filter order. A **Chebyshev filter** allows controlled ripple in the passband but achieves a much steeper roll-off — for the same stopband attenuation requirement, fewer poles are needed than Butterworth. An **elliptic (Cauer) filter** tolerates ripple in both passband and stopband, achieving the steepest possible roll-off for a given order. The right choice depends on the application: audio equipment often prefers Butterworth's flat passband, while communications receivers may need the sharp selectivity of Chebyshev or elliptic designs where a small amount of passband ripple is acceptable.

Filter order n determines the ultimate roll-off rate: n × 20 dB/decade. A first-order filter (single RC) rolls off at 20 dB/decade. A second-order filter (the RLC circuits from your prerequisites) rolls off at 40 dB/decade. Higher-order filters are built by cascading second-order sections called **biquads**, each with its own resonant frequency and quality factor Q. Your prerequisite work on the Q factor directly applies here: each biquad section's Q controls how peaked its response is near its center frequency, and the specific Q values for each section in a cascade are chosen from standard design tables to achieve the target Butterworth, Chebyshev, or elliptic response overall.
