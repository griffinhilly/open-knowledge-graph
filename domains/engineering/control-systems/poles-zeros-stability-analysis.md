---
id: poles-zeros-stability-analysis
title: Poles, Zeros, and System Stability
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
- id: transfer-function-poles-zeros
  type: hard
builds-toward:
- characteristic-equation-and-stability
- root-locus-pole-placement
- frequency-stability-from-bode-and-nyquist
tags:
- poles
- zeros
- stability
- dynamics
stage: advanced
status: draft
---

# Poles, Zeros, and System Stability

## Core Idea
System poles in the s-plane directly determine stability: poles in the left half-plane produce bounded responses (stable), poles on the imaginary axis produce sustained oscillation (marginally stable), and poles in the right half-plane cause exponential divergence (unstable). Zeros affect the shape of transient response and can create undershoot or non-minimum-phase behavior. Pole-zero locations comprehensively characterize system dynamics without requiring time-domain solution.

## Explainer

You've worked with transfer functions H(s) = N(s)/D(s) as ratios of polynomials in the Laplace variable s. **Poles** are the values of s where the denominator D(s) equals zero — equivalently, where H(s) blows up. **Zeros** are the values where the numerator N(s) equals zero — where H(s) vanishes. Both are generally complex numbers, and plotting them in the **s-plane** (real axis = σ, imaginary axis = jω) gives an immediate visual picture of what the system does.

The connection between poles and time-domain behavior is exact and mechanical. Each pole p_k contributes a term of the form e^(p_k · t) to the system's natural response after a disturbance. If p_k = −2 (a real pole in the left half-plane), that term is e^(−2t) — an exponential that decays to zero. The system is stable. If p_k = +1 (a real pole in the right half-plane), the term is e^t — exponential growth. The system is unstable. If p_k = ±jω₀ (purely imaginary poles), the terms combine to give a pure sinusoid at frequency ω₀ that neither grows nor decays — **marginal stability**, sustained oscillation. Complex conjugate poles p_k = −σ ± jω₀ give damped sinusoids e^(−σt)·cos(ω₀t + φ): oscillatory but decaying if σ > 0. The real part of the pole determines whether the response grows or decays; the imaginary part determines the oscillation frequency.

Zeros shape *how* the system responds, not whether it's stable. A zero at s = z forces the numerator to zero at that frequency, suppressing the system's response there. A pair of zeros in the right half-plane creates **non-minimum-phase behavior**: the step response initially moves in the wrong direction (undershoot) before settling. This is common in systems with internal delays, such as a large ship that briefly swings the wrong way when the rudder is first turned, or a bicycle that must initially steer into a turn. Recognizing non-minimum-phase zeros is essential because they impose hard limits on feedback bandwidth — you cannot close a fast feedback loop around a non-minimum-phase system without inducing instability.

The s-plane is the foundation for **root locus analysis**: as you add feedback gain K, the closed-loop poles migrate from the open-loop poles (at K = 0) toward the zeros (as K → ∞). Drawing or computing this migration path — the root locus — tells you at a glance whether increasing gain will move poles toward or away from the unstable right half-plane. Every closed-loop stability condition you'll encounter (Routh-Hurwitz criterion, phase and gain margins from Bode plots, Nyquist stability criterion) is ultimately a check on where the closed-loop poles end up in the s-plane. Poles and zeros are the grammar; stability is the sentence you're trying to construct.
