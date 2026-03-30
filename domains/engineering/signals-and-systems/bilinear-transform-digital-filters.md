---
id: bilinear-transform-digital-filters
title: Bilinear Transform for Digital Filter Design
domain: engineering
course: signals-and-systems
prerequisites:
- id: z-transform-discrete-time-signals
  type: hard
- id: butterworth-analog-filter-design
  type: soft
- id: chebyshev-type-i-filters
  type: soft
tags:
- filter-design
- digital-filters
- discretization
- z-transform
stage: advanced
status: validated
---

# Bilinear Transform for Digital Filter Design

## Core Idea
The bilinear transform s = (2/T)(z–1)/(z+1) maps analog filter designs to digital via a conformal transformation. It preserves stability and causality, mapping the imaginary axis to the unit circle. Frequency warping compresses high analog frequencies near fs/2, but pre-warping at a specific frequency can correct this effect.

## Explainer

You already have a solid analog filter design in the s-domain — perhaps a Butterworth lowpass prototype or a Chebyshev bandpass filter. You also know the z-transform and how discrete-time systems work in the z-domain. The bilinear transform is the bridge between these two worlds: a substitution rule that converts your continuous-time transfer function H(s) into a discrete-time transfer function H(z) that you can implement as a digital filter.

**Why not just discretize directly?** The most naive approach — replacing derivatives with finite differences, i.e., s → (z−1)/T — leads to the **forward Euler** method, which maps the stable left half s-plane into a small circle near z = 1, not the unit circle. Poles that were barely stable in continuous time can end up outside the unit circle in discrete time: the method is conditionally stable and creates aliasing problems. The **bilinear transform** avoids this by using the substitution s = (2/T)(z−1)/(z+1), which maps the entire left half s-plane to the *interior* of the unit circle and the imaginary axis (jω) to the unit circle itself. Stability is preserved by construction: any causal, stable analog filter becomes a causal, stable digital filter after the bilinear transform.

**Frequency warping: the unavoidable distortion.** The bilinear transform is a conformal map, but it is not linear in frequency. The relationship between the analog frequency Ω and the digital frequency ω is: Ω = (2/T)·tan(ω/2). At low frequencies, ω and Ω track each other well. But as ω approaches π (the Nyquist frequency), the analog frequency Ω stretches toward infinity — the entire semi-infinite analog frequency axis is compressed into the finite range 0 to π. This **frequency warping** means that if your Butterworth filter had a −3 dB point at Ω₀ in the analog domain, the digital filter's −3 dB point will not be at the corresponding digital frequency ω₀ = Ω₀·T unless you correct for this compression.

**Pre-warping: the fix.** The standard procedure is to **pre-warp** the critical frequency before designing the analog prototype. You choose the digital frequency ω_c you want (in radians per sample), compute the pre-warped analog frequency Ω_c = (2/T)·tan(ω_c/2), design the analog prototype at Ω_c, and then apply the bilinear transform. After the transform, the warping maps Ω_c exactly back to ω_c. The filter's gain is exactly correct at that one frequency; all other frequencies are still warped, but for well-designed filters (especially equiripple designs), this is acceptable. The pre-warping step is essential whenever you have a specific cutoff, notch, or center frequency requirement — it is the step most commonly omitted by beginners, leading to digital filters whose cutoff frequency is significantly off from the target.

**Putting it all together: the design recipe.** (1) Specify the desired digital cutoff frequency ω_c. (2) Pre-warp: compute Ω_c = (2/T)·tan(ω_c/2). (3) Design an analog prototype H_a(s) with cutoff at Ω_c using Butterworth, Chebyshev, or Elliptic design tables. (4) Apply the bilinear substitution: replace every s in H_a(s) with (2/T)(z−1)/(z+1). (5) Expand and simplify to get H(z) in standard form. The result is a digital IIR filter with the desired frequency response characteristics — stable, causal, and directly implementable as a difference equation. This design path from analog prototype to digital filter is standard in DSP toolboxes; knowing the mathematics tells you exactly what the tool is doing and lets you debug when results are unexpected.

## Questions

```yaml
- question: "Why does the bilinear transform preserve stability while the forward Euler substitution does not?"
  type: short-answer
  answer: "The bilinear transform maps the entire left half s-plane onto the interior of the unit circle in the z-plane. Any pole with Re(s) < 0 in the analog domain lands at |z| < 1 in the digital domain, preserving stability. Forward Euler maps the stable left half-plane to a small disk near z = 1, which does not encompass all stable digital poles — some stable analog poles map outside the unit circle."
  explanation: "The bilinear transform is a Möbius transformation that maps the imaginary jω axis to the unit circle. This bijection between the stability regions is exactly the property you need. Euler's method is a first-order approximation of the exponential map, which is globally accurate only at low frequencies and fails for lightly damped or near-Nyquist poles."

- question: "You want a digital lowpass filter with −3 dB at 1000 Hz, sampled at 8000 Hz. What is the pre-warped analog frequency Ω_c to use in the analog prototype design?"
  type: short-answer
  answer: "Digital frequency: ω_c = 2π × 1000/8000 = π/4 rad/sample. T = 1/8000 s. Pre-warped: Ω_c = (2/T)·tan(ω_c/2) = 16000·tan(π/8) ≈ 16000 × 0.4142 ≈ 6628 rad/s."
  explanation: "The pre-warp formula Ω_c = (2/T)·tan(ω_c/2) ensures that after the bilinear transform, the digital filter's −3 dB point lands exactly at ω_c = π/4 (1000 Hz). Without pre-warping, the bilinear transform's frequency compression would shift the −3 dB point lower than intended."
```
