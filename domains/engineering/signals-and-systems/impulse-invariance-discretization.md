---
id: impulse-invariance-discretization
title: Impulse Invariance for Digital Filter Design
domain: engineering
course: signals-and-systems
prerequisites:
- id: z-transform-discrete-time-signals
  type: hard
- id: laplace-transform-fundamentals
  type: hard
- id: aliasing-reconstruction-signals
  type: hard
- id: bilinear-transform-digital-filters
  type: soft
- id: fir-filter-design-realization
  type: soft
- id: iir-filter-design-realization
  type: soft
tags:
- filter-design
- digital-filters
- discretization
- impulse-response
stage: expert
status: validated
---
# Impulse Invariance for Digital Filter Design

## Core Idea
Impulse invariance maps analog filter impulse response to digital by sampling: h[n] = T·ha(nT). This preserves the shape of the analog response at sample times but introduces aliasing if the analog filter is not sufficiently bandlimited. Unlike bilinear transform, it does not preserve stability for poles outside the left half-plane.

## Questions

```yaml
- question: "A designer uses impulse invariance to discretize a Butterworth lowpass filter and finds that even at very high sampling rates, some aliasing error always remains in the stopband. Why can't increasing the sampling rate eliminate this error entirely?"
  type: multiple-choice
  options:
    - "Impulse invariance maps poles incorrectly at high sampling rates, amplifying stopband error"
    - "Butterworth filters have infinite bandwidth — their magnitude rolls off polynomially but never reaches zero, so spectral copies always overlap no matter the sampling rate"
    - "High sampling rates cause the digital poles to migrate outside the unit circle, introducing instability and ripple"
    - "The partial fraction expansion used in impulse invariance becomes numerically unstable at high sampling rates"
  answer: 1
  explanation: "Butterworth and Chebyshev filters are never truly bandlimited — their frequency response decays toward zero but never reaches it. The digital filter's spectrum is (1/T) × sum of shifted copies of the analog spectrum. Even at very high sampling rates, the copies are pushed further apart, but the polynomial roll-off of the Butterworth filter means there is always some residual energy in the shifted copies that overlaps with the baseband. The aliasing asymptotically approaches zero but never reaches it. For practical purposes, if attenuation at Nyquist is −40 dB or better, the aliasing may be negligible — but it is never truly absent."

- question: "What is the key advantage of the bilinear transform over impulse invariance when designing digital highpass filters?"
  type: multiple-choice
  options:
    - "The bilinear transform exactly preserves the analog impulse response at every sample instant"
    - "The bilinear transform eliminates aliasing by compressing the entire infinite analog frequency axis onto [−π, π] without spectral overlap"
    - "The bilinear transform is computationally cheaper, requiring fewer multiply-accumulate operations"
    - "The bilinear transform maps unstable analog poles outside the unit circle to stable digital poles inside it"
  answer: 1
  explanation: "The bilinear transform uses the substitution s = (2/T)(z−1)/(z+1) to map the entire left half s-plane to the interior of the unit disk in a one-to-one, onto fashion. The infinite analog frequency axis is compressed (warped) onto the finite interval [−π, π] with no aliasing: there are no repeated spectral copies, so there is no overlap. The cost is frequency warping — a nonlinear distortion of the frequency axis that must be pre-compensated by warping the analog design specifications before applying the transform. For highpass filters, impulse invariance fails because the high-frequency spectral copies alias directly into the passband."

- question: "In impulse invariance, a stable analog pole at s = sₖ (with Re(sₖ) < 0) maps to a stable digital pole at z = e^(sₖT) inside the unit circle."
  type: true-false
  answer: true
  explanation: "This pole mapping is the constructive heart of impulse invariance. For a stable analog pole with Re(sₖ) < 0, we have |e^(sₖT)| = e^(Re(sₖ)T) < 1, placing the digital pole inside the unit circle. Stability is preserved in the pole-by-pole mapping. This is a genuine advantage of impulse invariance over some ad hoc discretization methods. The stability issue mentioned in the Core Idea — 'does not preserve stability for poles outside the left half-plane' — refers to the impossibility of mapping unstable analog poles (Re(sₖ) > 0) to stable digital poles, not to instability of stable analog designs."

- question: "Impulse invariance is the preferred method for designing digital highpass filters because it preserves the analog frequency response without distortion."
  type: true-false
  answer: false
  explanation: "Impulse invariance is poorly suited for highpass filter design precisely because it does NOT preserve the frequency response without distortion. The digital filter's spectrum is a periodic repetition of the analog spectrum. For a highpass filter, the high-frequency content of the analog prototype aliases directly into the passband of the digital filter, corrupting it completely. Bilinear transform is preferred for highpass designs because it avoids aliasing entirely. Impulse invariance is best reserved for cases where matching the time-domain samples of the analog prototype matters more than accurately reproducing the frequency response."

- question: "Explain why impulse invariance inevitably introduces aliasing even when the analog prototype is a well-designed lowpass filter, and under what conditions the aliasing error is acceptable in practice."
  type: short-answer
  answer: "Impulse invariance samples the continuous impulse response at intervals T. In the frequency domain, sampling a continuous signal creates a spectrum that is the sum of shifted copies of the original, spaced 2π/T apart. Because all practical analog filters (Butterworth, Chebyshev, etc.) have infinite bandwidth — their response approaches but never reaches zero — these spectral copies always have some nonzero magnitude at the edges, and adjacent copies overlap. The aliasing error is the integrated magnitude of this overlap. It is acceptable in practice when the analog filter provides sufficient attenuation before the Nyquist frequency: if the analog response is −40 dB or better at π/T, the aliasing contributions are small enough to be negligible for most applications. For wideband or highpass filters where significant energy remains near Nyquist, aliasing error is large and bilinear transform is required instead."
  explanation: "The practical decision rule: impulse invariance works when the analog filter is a narrow-band lowpass with strong rolloff before Nyquist. It fails for highpass, bandpass with high center frequencies, or any design where substantial analog energy exists near and above π/T. The bilinear transform is the general-purpose alternative when aliasing-free frequency response accuracy is required."
```

## Explainer

From your study of the Laplace transform, you know how to design analog filters — Butterworth, Chebyshev — specified by poles in the s-plane. From the z-transform, you know how to analyze discrete-time systems. Impulse invariance is one bridge between these two worlds: it constructs a digital filter whose behavior deliberately mimics a known analog prototype, starting from the analog impulse response.

The method begins by expanding the analog transfer function H_a(s) into partial fractions: H_a(s) = Σ A_k / (s − s_k). Each term corresponds to a decaying exponential in the time domain: h_a(t) = Σ A_k e^(s_k t) u(t). **Impulse invariance** samples this continuous impulse response at intervals T to define the digital impulse response: h[n] = T · h_a(nT) = T · Σ A_k e^(s_k nT) u[n]. Taking the z-transform of each term gives H(z) = T · Σ A_k / (1 − e^(s_k T) z^{-1}). This is the key mapping rule: each analog pole at s = s_k becomes a digital pole at z = e^(s_k T). Poles in the left half s-plane (where Re(s_k) < 0) map to poles inside the unit circle (where |e^(s_k T)| < 1), preserving stability. The frequency axis maps as ω_digital = Ω_analog × T — digital frequencies are a scaled version of analog frequencies, with no warping.

The fatal limitation is **aliasing**, and your prerequisite on aliasing tells you exactly why it arises. The digital filter's frequency response is a periodic repetition of the analog: H(e^{jω}) = (1/T) Σ_k H_a(j(ω − 2πk)/T). If the analog filter has significant energy above the Nyquist frequency π/T, adjacent copies overlap and corrupt the spectrum. Butterworth and Chebyshev filters have infinite bandwidth — their magnitude falls off polynomially, never reaching exactly zero. Applying impulse invariance to these filters inevitably introduces aliasing. For a well-designed lowpass filter with substantial attenuation before Nyquist (say, −40 dB or better at π/T), the aliasing error may be acceptable. For highpass or wideband filters, the copies wrap around and add in-band, making the result useless.

This is why **bilinear transform** is often the preferred alternative: it maps the entire left half-plane to the unit disk interior without aliasing by compressing the infinite analog frequency axis onto [−π, π]. The trade-off is frequency **warping** — a nonlinear compression that distorts the filter shape unless pre-warped during design. Impulse invariance is preferred when you specifically need the digital filter's time-domain samples to match the analog prototype's values — for instance, when digitally simulating an analog physical system where matching the step response at sample instants matters more than matching the stopband at high frequencies. Knowing both methods, and when each is appropriate, is the practical skill.
