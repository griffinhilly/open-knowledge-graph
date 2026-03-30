---
id: linear-phase-filter-design-preservation
title: Linear Phase Response and Signal Distortion
domain: engineering
course: signals-and-systems
prerequisites:
- id: magnitude-phase-computation-pole-zero
  type: hard
builds-toward:
- fir-filter-design-realization
- group-delay-phase-characterization
tags:
- filters
- linear-phase
- distortion
- group-delay
stage: advanced
status: validated
---

# Linear Phase Response and Signal Distortion

## Core Idea
Linear phase response (phase proportional to frequency) means all frequency components are delayed equally, preserving signal shape. Non-linear phase causes different delays at different frequencies, creating waveform distortion. Symmetric impulse responses guarantee linear phase in FIR filters; IIR filters cannot achieve true linear phase but can approximate it with all-pass equalizers.

## How It's Best Learned
Design a non-causal symmetric FIR filter and verify its linear phase. Compare its output on a chirp signal to that of a non-symmetric filter showing group delay variation.

## Common Misconceptions
- Thinking magnitude response alone determines distortion.
- Assuming constant group delay is the same as zero delay.
- Not recognizing that phase delay differs from group delay.

## Questions

```yaml
- question: "A communications engineer applies an elliptic IIR lowpass filter to a digital audio signal. The filter has excellent magnitude performance: all passband frequencies have equal gain, and the stopband is heavily attenuated. Yet the output still sounds distorted relative to the input. What is the most likely cause?"
  type: multiple-choice
  options:
    - "Finite-precision arithmetic in the IIR implementation is introducing quantization noise"
    - "The filter's non-linear phase response delays different frequency components by different amounts, smearing transients and destroying waveform shape even though no frequencies are lost"
    - "The stopband attenuation is insufficient — some high-frequency energy is leaking through"
    - "The sampling rate is too low for the signal bandwidth, causing aliasing distortion"
  answer: 1
  explanation: "This is the classic phase distortion scenario. An elliptic IIR filter achieves very sharp magnitude transitions but has highly non-linear phase — group delay varies strongly with frequency. Even when all passband frequencies pass with equal gain, they arrive at the output at different times. For audio signals with sharp transients (drum attacks, consonants in speech), this timing smear destroys temporal detail. The distortion is purely in the phase domain, invisible in the magnitude response. This is why applications requiring waveform fidelity use linear-phase FIR filters despite their higher computational cost."

- question: "A symmetric FIR filter with N = 51 coefficients (h[n] = h[50−n]) is designed as a lowpass filter. What is the expected group delay of this filter?"
  type: multiple-choice
  options:
    - "0 samples — linear phase means the filter introduces no delay whatsoever"
    - "25 samples — a constant group delay equal to (N−1)/2, independent of frequency"
    - "Variable, from 0 to 50 samples depending on the frequency band"
    - "Infinite at the passband edge, where the transition from passband to stopband occurs"
  answer: 1
  explanation: "A symmetric FIR filter of length N has a linear phase response: ∠H(ω) = −ω(N−1)/2. The group delay τ_g = −d∠H/dω = (N−1)/2 = 25 samples, constant across all frequencies. This constant group delay means every frequency component is delayed by the same 25 samples — the signal is shifted in time but not distorted in shape. The common misconception is that 'linear phase' means 'zero phase'; it means phase proportional to frequency, which corresponds to a fixed time delay. Zero phase would require a non-causal filter."

- question: "A symmetric FIR filter (h[n] = h[N−1−n]) automatically achieves linear phase regardless of what magnitude response it is designed to produce."
  type: true-false
  answer: true
  explanation: "This is the key result that makes symmetric FIR filters so useful. The frequency response of a symmetric FIR filter can always be written as a real-valued amplitude function multiplied by a linear phase factor e^{−jω(N−1)/2}. The symmetry condition forces the phase to be exactly linear — the magnitude design (windowing, Parks-McClellan, etc.) controls the real amplitude function, but the phase linearity is guaranteed by symmetry regardless of what magnitude shape results. This decoupling of magnitude and phase design is the defining advantage of symmetric FIR filters."

- question: "IIR filters are generally preferred over FIR filters in applications that require exact linear phase, because IIR filters achieve sharper magnitude cutoffs with fewer coefficients."
  type: true-false
  answer: false
  explanation: "IIR filters cannot achieve exact linear phase — their recursive structure prevents the coefficient symmetry required for linear phase. An IIR filter's denominator (feedback) terms create poles in the z-plane, and poles are inherently associated with non-linear phase. IIR filters can approximate linear phase over limited frequency ranges using all-pass equalizers, but this is an approximation with added complexity, not exact linear phase. When exact linear phase is required (medical imaging, digital communications, high-fidelity audio), FIR filters with symmetric coefficients are the only option — the computational cost is the price paid for phase integrity."

- question: "Why is constant group delay equivalent to linear phase? And why does non-constant group delay cause waveform distortion even when the magnitude response is perfectly flat?"
  type: short-answer
  answer: "Group delay τ_g(ω) = −d∠H(ω)/dω measures how much a narrowband signal centered at frequency ω is delayed by the filter. If group delay is constant (τ_g = k for all ω), integrating gives ∠H(ω) = −kω, which is exactly the definition of linear phase. A linear phase filter delays every frequency component by the same k seconds, so all components of a signal arrive simultaneously — the waveform shape is preserved, just shifted in time by k. If group delay varies with frequency, different components arrive at different times. Even if all pass with equal gain, their misalignment at the output changes the waveform shape: fast transients (which rely on many harmonics adding up in phase at the right moment) are smeared or distorted because the harmonics arrive asynchronously."
  explanation: "An intuitive analogy: a symphony orchestra sounds right only if all sections play in time. Magnitude response determines which instruments are audible; phase response determines whether they play together. A flat magnitude with non-linear phase is like an orchestra where every instrument plays the right notes at the right loudness but the percussion arrives late, the brass early, and the strings on time — the music is unrecognizable even though no notes were dropped."
```

## Explainer

From your study of magnitude and phase from pole-zero diagrams, you know that a filter's frequency response is complex-valued: at each frequency ω, the filter applies a gain |H(ω)| and a phase shift ∠H(ω). An ideal lowpass filter has a flat magnitude response in the passband (all frequencies passed equally) and zero magnitude in the stopband. But magnitude is only half the picture. What the filter does to the *timing* of frequency components is equally important, and this is what phase response controls.

Imagine a square wave, which is the sum of a fundamental frequency and all its odd harmonics. If a filter delays the fundamental by 1 ms but delays the third harmonic by 3 ms and the fifth by 5 ms, the harmonics arrive at different times and the square wave is smeared — the fast rise and fall are gone even if all harmonics pass through with equal gain. This is **phase distortion** (also called **waveform distortion**): different frequency components arriving at different times destroy the temporal structure of the signal even when no frequencies are lost. In audio processing, phase distortion can make transients (drum attacks, consonants in speech) sound soft or pre-ringing. In digital communications, it causes intersymbol interference. In medical imaging, it blurs sharp edges.

**Linear phase** means the phase shift is proportional to frequency: ∠H(ω) = −kω for some constant k. In this case, every frequency component is delayed by exactly the same amount — k seconds. The signal shape is perfectly preserved; it simply arrives k seconds later. The **group delay** τ_g(ω) = −d∠H(ω)/dω measures how much a narrowband signal centered at ω is delayed. For a linear-phase filter, the group delay is constant (equal to k at every frequency) — this is the defining characteristic. A constant group delay is equivalent to a pure time delay, which distorts nothing.

**Symmetric FIR filters** guarantee linear phase, and this is why they are widely used in applications that demand waveform fidelity. A length-N FIR filter with coefficients symmetric about its center (h[n] = h[N−1−n]) has a frequency response that can be written as a real-valued function multiplied by a linear phase term e^{−jωM/2}, where M = N−1. The linear phase factor is exactly what we want; the real-valued function in front determines the magnitude response. This structure means you can design any magnitude response you want (using windowing or equiripple methods) while the symmetry condition automatically guarantees linear phase — the two design goals are decoupled. IIR filters cannot achieve exact linear phase because their recursive structure prevents the coefficient symmetry needed; they can only approximate it over limited frequency ranges using all-pass equalizers. This fundamental tradeoff — IIR filters are more efficient for a given magnitude specification, but FIR filters are the only way to get exact linear phase — drives nearly every filter design decision in practice.
