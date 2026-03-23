---
id: notch-filters-and-resonators
title: Notch Filters and Resonator Design
domain: engineering
course: signals-and-systems
prerequisites:
- id: frequency-response-and-bode-plots
  type: hard
builds-toward:
- butterworth-filter-maximally-flat-response
- chebyshev-filter-equiripple-response
tags:
- filters
- notch
- resonator
- narrow-band
stage: expert
status: validated
---

# Notch Filters and Resonator Design

## Core Idea
Notch filters provide deep attenuation at a specific frequency while leaving other frequencies unaffected. They place zeros on the unit circle (or s-plane) at the notch frequency. Resonators amplify energy at a resonant frequency, placing poles near the unit circle with high quality factor Q. Both filters are useful for tone removal (notches) or tone enhancement (resonators), and Q controls bandwidth.

## How It's Best Learned
Design a simple notch filter by placing complex conjugate zeros on the unit circle. Measure attenuation at the notch frequency and 3-dB bandwidth away from notch.

## Common Misconceptions
- Thinking notches eliminate frequencies completely (not possible with finite filter).
- Confusing notch depth (determined by zero location) with bandwidth (determined by pole placement).
- Not recognizing that narrow notches require high Q, which affects numerical stability.

## Questions

```yaml
- question: "A notch filter is designed with complex-conjugate zeros placed exactly on the unit circle at frequency ω₀, but no poles are added. What is the main limitation of this design?"
  type: multiple-choice
  options:
    - "The filter will be unstable because zeros on the unit circle always cause instability"
    - "The filter achieves zero gain only at ω₀ but attenuates a very wide band of frequencies around it, not just the target frequency"
    - "The filter cannot be implemented digitally because zeros on the unit circle require infinite precision"
    - "The notch depth will be less than 3 dB, making it ineffective for interference rejection"
  answer: 1
  explanation: "Zeros on the unit circle guarantee zero gain at exactly ω₀ — perfect attenuation at one point. But without poles, the frequency response falls off gradually on both sides, creating a broad notch that attenuates many nearby frequencies you want to preserve. To create a narrow, sharp notch, poles must be added just inside the unit circle at the same angle. The poles partially cancel the effect of the zeros everywhere except at ω₀ itself, dramatically narrowing the affected band."

- question: "In a discrete-time notch filter with poles at radius r near the unit circle, what happens as r approaches 1?"
  type: multiple-choice
  options:
    - "The notch becomes broader because the poles move farther from the zeros"
    - "The filter becomes an all-pass filter because the poles cancel the zeros"
    - "The notch becomes narrower and sharper (higher Q), but numerical sensitivity increases"
    - "The filter becomes a resonator, amplifying the target frequency instead of attenuating it"
  answer: 2
  explanation: "As r → 1, the poles move toward the unit circle, approaching the zeros. Everywhere except at ω₀, the poles increasingly counteract the zeros' attenuation, preserving those frequencies at nearly unit gain. Only at ω₀ do the zeros still dominate. The result is a sharper, higher-Q notch. The cost: when r is very close to 1, tiny coefficient errors (from finite-precision arithmetic) produce large shifts in the effective pole position, dramatically changing notch depth and bandwidth. High-Q designs require careful numerical implementation."

- question: "A digital resonator with pole radius r = 1 (poles exactly on the unit circle) produces a stable, sharp-peaked response at the resonant frequency."
  type: true-false
  answer: false
  explanation: "Poles exactly on the unit circle correspond to a marginally stable system — the output grows without bound for an input at the resonant frequency, producing an unstable sinusoidal oscillator, not a stable filter. A practical resonator requires r slightly less than 1, so the poles are just inside the unit circle. This produces a large but finite peak at ω₀ with the peak height and bandwidth controlled by how close r is to 1. As r → 1, the peak grows and bandwidth narrows, but stability is only guaranteed strictly inside the unit circle."

- question: "High-Q notch filters require poles placed very close to the unit circle, which introduces numerical sensitivity — small coefficient errors can dramatically degrade notch performance."
  type: true-false
  answer: true
  explanation: "This is an important practical constraint. When r is close to 1, the filter's frequency response is extremely sensitive to the exact pole position. A small change in r or in the cosine coefficient (due to quantization in fixed-point arithmetic) shifts the pole, changing the effective notch frequency, depth, and bandwidth significantly. High-Q designs often require double-precision arithmetic, specialized filter structures (such as coupled-form second-order sections), or careful coefficient wordlength analysis to maintain performance."

- question: "Explain the relationship between pole radius r and the quality factor Q in a notch filter, and describe the tradeoff that determines how to choose r in practice."
  type: short-answer
  answer: "The pole radius r controls how close the poles are to the zeros on the unit circle. Near the zero at ω₀, both poles and zeros nearly cancel everywhere except at the notch frequency itself. As r increases toward 1, the poles move closer to the unit circle, more aggressively narrowing the affected band — Q rises and bandwidth decreases as approximately Q ≈ ω₀ / (2(1−r)·f_s/2π) for a symmetric notch. The practical tradeoff is between selectivity and numerical robustness: a high-r (high-Q) design isolates a very narrow frequency band but becomes increasingly sensitive to coefficient quantization errors, which can shift the effective notch frequency or reduce attenuation. In practice, r is chosen to achieve the required bandwidth while remaining feasible given the available arithmetic precision."
  explanation: "The geometric picture is key: the notch is narrow because the poles almost cancel the zeros' effect at nearby frequencies. The closer r is to 1, the more complete this near-cancellation is at off-notch frequencies, and the more surgical the attenuation. The numerical sensitivity arises because small perturbations to nearly-canceling pole-zero pairs produce large changes in the residual response — a fundamental sensitivity inherent to high-Q filter structures."
```

## Explainer

From your work with Bode plots and frequency response, you know that a filter's behavior is completely characterized by the locations of its poles and zeros in the s-plane (continuous-time) or z-plane (discrete-time). Poles amplify frequencies near them; zeros attenuate frequencies near them. A **notch filter** is the extreme case of targeted attenuation: place a pair of complex-conjugate zeros exactly on the unit circle at angle ω₀, and the filter response goes to zero at precisely that frequency. In discrete-time, the transfer function for the zero pair alone is H(z) = z² − 2cos(ω₀)z + 1, which evaluates to zero when z = e^(±jω₀). Everything else in the spectrum is unaffected — except that you must also add a gain scaling factor to preserve unity gain at DC or some other reference frequency.

The problem with zeros alone is that the notch is very broad — you attenuate a wide band around ω₀. To narrow it, add a pair of poles just inside the unit circle at the same angle: H(z) = (z² − 2cos(ω₀)z + 1) / (z² − 2r·cos(ω₀)z + r²), where r < 1 is the pole radius. As r → 1, the poles move toward the unit circle and nearly cancel the effect of the zeros everywhere except right at ω₀, where the zeros still dominate. The **quality factor Q** = ω₀ / (2-bandwidth) characterizes the sharpness: high Q means narrow notch. The cost is numerical sensitivity — when r is close to 1, small coefficient errors (from fixed-point arithmetic or finite-precision implementation) shift the poles and dramatically alter the notch depth and bandwidth. High-Q notch filters require careful implementation, sometimes using second-order sections or specialized structures.

A **resonator** is the dual: instead of zeros on the unit circle, place poles close to but inside the unit circle at the resonant frequency ω₀, with zeros placed away from that frequency (or at DC/Nyquist). The response peaks sharply at ω₀ and falls off at other frequencies. The higher the pole radius r, the closer to the unit circle, the sharper and taller the peak, and the higher the Q. An ideal resonator with r = 1 (poles on the unit circle) would produce infinite gain — an unstable sinusoidal oscillator. A practical digital resonator with r slightly below 1 is a stable narrow-band amplifier that can serve as a **tone detector**, a channel in a filter bank, or the basis for a sinusoidal signal generator in music synthesis.

Notch filters appear constantly in real systems: removing 50 or 60 Hz power line interference from physiological recordings (ECG, EEG), canceling a specific mechanical vibration frequency in a motor controller, or eliminating a pilot tone in audio equipment. The design recipe is straightforward: identify the exact frequency to remove, place zeros on the unit circle there, and choose a pole radius r to set the acceptable bandwidth. A bandwidth of 2 Hz centered on 60 Hz requires r ≈ 1 − π·(2)/f_s, so at 1 kHz sample rate, r ≈ 0.994. The resulting filter passes all other frequencies with nearly unit gain while achieving 40–60 dB attenuation at 60 Hz — an elegant piece of geometry that requires nothing but two zeros and two poles.


