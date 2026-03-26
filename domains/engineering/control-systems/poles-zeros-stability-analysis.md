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
stage: expert
status: validated
---

# Poles, Zeros, and System Stability

## Core Idea
System poles in the s-plane directly determine stability: poles in the left half-plane produce bounded responses (stable), poles on the imaginary axis produce sustained oscillation (marginally stable), and poles in the right half-plane cause exponential divergence (unstable). Zeros affect the shape of transient response and can create undershoot or non-minimum-phase behavior. Pole-zero locations comprehensively characterize system dynamics without requiring time-domain solution.

## Questions

```yaml
- question: "A system's transfer function has poles at s = −1 ± 2j and a zero at s = +3. What is the stability of this system, and which feature determines it?"
  type: multiple-choice
  options:
    - "Unstable — the zero in the right half-plane causes the system to diverge"
    - "Stable — only the pole locations determine stability, and both poles are in the left half-plane"
    - "Marginally stable — the imaginary parts of the poles cause undamped oscillation"
    - "Unstable — complex poles always lead to instability when paired with a right-half-plane zero"
  answer: 1
  explanation: "Stability is determined entirely by pole locations. The poles at s = −1 ± 2j have negative real parts (σ = −1), so each contributes a decaying sinusoidal term e^(−t)·cos(2t + φ) to the natural response — the system is stable. The zero at s = +3 is in the right half-plane (non-minimum-phase), which creates undershoot in the step response, but zeros do not cause instability. Mixing up poles and zeros on stability is the most common error in this topic."

- question: "A closed-loop system has a pole at s = 2 + j. Describe the expected behavior of its step response."
  type: multiple-choice
  options:
    - "A decaying oscillation settling to the step value, because the imaginary part dominates"
    - "A pure sinusoid at 1 rad/s that neither grows nor decays, because the real and imaginary parts balance"
    - "An exponentially growing oscillation — the positive real part causes divergence regardless of the imaginary part"
    - "A step response identical to a first-order system — the imaginary part only affects frequency response"
  answer: 2
  explanation: "A pole at s = 2 + j contributes a term proportional to e^(2t)·cos(t + φ) to the response. The real part (+2) drives exponential growth; the imaginary part (1) modulates the oscillation frequency. Because the real part is positive, the envelope grows without bound — the system is unstable. No matter how small the imaginary part, a positive real part always causes divergence."

- question: "A system with most poles in the left half-plane but a zero in the right half-plane (non-minimum-phase zero) is unstable."
  type: true-false
  answer: false
  explanation: "False. Stability is determined solely by pole locations. A system with all poles in the left half-plane is stable regardless of where its zeros are. A right-half-plane (non-minimum-phase) zero causes the step response to initially move in the wrong direction (undershoot) before settling, and it limits how tightly you can close a feedback loop, but it does not cause instability on its own. Confusing zeros with poles on stability questions is a very common error."

- question: "A system with a pair of purely imaginary poles (e.g., at s = ±3j) is called marginally stable because its natural response neither grows nor decays."
  type: true-false
  answer: true
  explanation: "True. Purely imaginary poles at s = ±jω₀ contribute a pure sinusoid cos(ω₀t + φ) to the natural response — amplitude constant, neither increasing nor decreasing. The system oscillates indefinitely at frequency ω₀. This is called marginal stability: technically BIBO (bounded-input, bounded-output) stability fails because a sinusoidal input at ω₀ produces a response that grows without bound (resonance), but zero-input response is bounded. Most control systems aim for poles strictly in the left half-plane to guarantee convergence."

- question: "What is the relationship between the location of a pole in the s-plane and the time-domain behavior it contributes to the system's natural response?"
  type: short-answer
  answer: "Each pole p contributes a term of the form e^(pt) to the natural response. The real part of p (σ) determines growth or decay: if σ < 0, the term decays exponentially (stable contribution); if σ > 0, the term grows exponentially (unstable); if σ = 0, the term is a constant or pure sinusoid (marginally stable). The imaginary part (jω) determines oscillation frequency — complex conjugate pole pairs contribute damped sinusoids e^(σt)·cos(ωt + φ). The real part is the key: left half-plane means stability, right half-plane means instability."
  explanation: "This pole-to-time-domain correspondence is exact (via inverse Laplace transform partial fractions) and makes the s-plane a complete map of system dynamics. Engineers can read off decay rate (|σ|), oscillation frequency (ω), and damping ratio (ζ = −σ/|p|) directly from the pole location — no need to solve differential equations. This geometric intuition is why root locus and pole placement are such powerful design methods."
```

## Explainer

You've worked with transfer functions H(s) = N(s)/D(s) as ratios of polynomials in the Laplace variable s. **Poles** are the values of s where the denominator D(s) equals zero — equivalently, where H(s) blows up. **Zeros** are the values where the numerator N(s) equals zero — where H(s) vanishes. Both are generally complex numbers, and plotting them in the **s-plane** (real axis = σ, imaginary axis = jω) gives an immediate visual picture of what the system does.

The connection between poles and time-domain behavior is exact and mechanical. Each pole p_k contributes a term of the form e^(p_k · t) to the system's natural response after a disturbance. If p_k = −2 (a real pole in the left half-plane), that term is e^(−2t) — an exponential that decays to zero. The system is stable. If p_k = +1 (a real pole in the right half-plane), the term is e^t — exponential growth. The system is unstable. If p_k = ±jω₀ (purely imaginary poles), the terms combine to give a pure sinusoid at frequency ω₀ that neither grows nor decays — **marginal stability**, sustained oscillation. Complex conjugate poles p_k = −σ ± jω₀ give damped sinusoids e^(−σt)·cos(ω₀t + φ): oscillatory but decaying if σ > 0. The real part of the pole determines whether the response grows or decays; the imaginary part determines the oscillation frequency.

Zeros shape *how* the system responds, not whether it's stable. A zero at s = z forces the numerator to zero at that frequency, suppressing the system's response there. A pair of zeros in the right half-plane creates **non-minimum-phase behavior**: the step response initially moves in the wrong direction (undershoot) before settling. This is common in systems with internal delays, such as a large ship that briefly swings the wrong way when the rudder is first turned, or a bicycle that must initially steer into a turn. Recognizing non-minimum-phase zeros is essential because they impose hard limits on feedback bandwidth — you cannot close a fast feedback loop around a non-minimum-phase system without inducing instability.

The s-plane is the foundation for **root locus analysis**: as you add feedback gain K, the closed-loop poles migrate from the open-loop poles (at K = 0) toward the zeros (as K → ∞). Drawing or computing this migration path — the root locus — tells you at a glance whether increasing gain will move poles toward or away from the unstable right half-plane. Every closed-loop stability condition you'll encounter (Routh-Hurwitz criterion, phase and gain margins from Bode plots, Nyquist stability criterion) is ultimately a check on where the closed-loop poles end up in the s-plane. Poles and zeros are the grammar; stability is the sentence you're trying to construct.
