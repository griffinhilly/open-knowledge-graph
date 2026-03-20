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
status: draft
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

## Explainer

From your study of magnitude and phase from pole-zero diagrams, you know that a filter's frequency response is complex-valued: at each frequency ω, the filter applies a gain |H(ω)| and a phase shift ∠H(ω). An ideal lowpass filter has a flat magnitude response in the passband (all frequencies passed equally) and zero magnitude in the stopband. But magnitude is only half the picture. What the filter does to the *timing* of frequency components is equally important, and this is what phase response controls.

Imagine a square wave, which is the sum of a fundamental frequency and all its odd harmonics. If a filter delays the fundamental by 1 ms but delays the third harmonic by 3 ms and the fifth by 5 ms, the harmonics arrive at different times and the square wave is smeared — the fast rise and fall are gone even if all harmonics pass through with equal gain. This is **phase distortion** (also called **waveform distortion**): different frequency components arriving at different times destroy the temporal structure of the signal even when no frequencies are lost. In audio processing, phase distortion can make transients (drum attacks, consonants in speech) sound soft or pre-ringing. In digital communications, it causes intersymbol interference. In medical imaging, it blurs sharp edges.

**Linear phase** means the phase shift is proportional to frequency: ∠H(ω) = −kω for some constant k. In this case, every frequency component is delayed by exactly the same amount — k seconds. The signal shape is perfectly preserved; it simply arrives k seconds later. The **group delay** τ_g(ω) = −d∠H(ω)/dω measures how much a narrowband signal centered at ω is delayed. For a linear-phase filter, the group delay is constant (equal to k at every frequency) — this is the defining characteristic. A constant group delay is equivalent to a pure time delay, which distorts nothing.

**Symmetric FIR filters** guarantee linear phase, and this is why they are widely used in applications that demand waveform fidelity. A length-N FIR filter with coefficients symmetric about its center (h[n] = h[N−1−n]) has a frequency response that can be written as a real-valued function multiplied by a linear phase term e^{−jωM/2}, where M = N−1. The linear phase factor is exactly what we want; the real-valued function in front determines the magnitude response. This structure means you can design any magnitude response you want (using windowing or equiripple methods) while the symmetry condition automatically guarantees linear phase — the two design goals are decoupled. IIR filters cannot achieve exact linear phase because their recursive structure prevents the coefficient symmetry needed; they can only approximate it over limited frequency ranges using all-pass equalizers. This fundamental tradeoff — IIR filters are more efficient for a given magnitude specification, but FIR filters are the only way to get exact linear phase — drives nearly every filter design decision in practice.
