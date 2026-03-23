---
id: fourier-series-representation
title: Fourier Series Representation of Periodic Signals
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-properties-periodicity-energy-power
  type: hard
- id: trigonometric-identities
  type: soft
- id: orthogonal-signal-decomposition-basis
  type: hard
- id: trigonometric-functions-review
  type: hard
- id: trigonometric-functions
  type: hard
builds-toward:
- fourier-transform-definition-properties
- magnitude-phase-spectrum-representation
tags:
- fourier-series
- periodic-signals
- frequency-domain
stage: expert
status: draft
---

# Fourier Series Representation of Periodic Signals

## Core Idea
Any periodic signal can be decomposed as a sum of sinusoids (harmonics) at integer multiples of the fundamental frequency. The Fourier series provides both real (cosine/sine) and complex exponential forms for representing periodic signals.

## Questions

```yaml
- question: "A square wave is passed through a low-pass filter that removes all frequency components above the 5th harmonic. What would the output most likely look like compared to the original square wave?"
  type: multiple-choice
  options:
    - "An identical square wave — the first 5 harmonics capture the essential shape"
    - "A smoother, rounded wave with the same period but less sharp transitions and visible ripples near the edges"
    - "Silence — removing harmonics above the fundamental destroys the signal"
    - "A signal at five times the original frequency"
  answer: 1
  explanation: "A square wave is built from the fundamental plus all odd harmonics (1st, 3rd, 5th, 7th…) with amplitudes 1, 1/3, 1/5, 1/7… Removing harmonics above the 5th leaves only three components (1st, 3rd, 5th). The result still has the correct period and approximate shape, but it loses the high-frequency content that produces sharp edges — resulting in a smoother wave with Gibbs-phenomenon overshoot near the transitions. This demonstrates concretely that time-domain shape corresponds to frequency-domain content."

- question: "What property of sinusoids at harmonic frequencies guarantees that the Fourier series decomposition of a periodic signal is unique?"
  type: multiple-choice
  options:
    - "All harmonics have the same amplitude at t = 0, so their sum is well-defined"
    - "Harmonics are orthogonal over one period — integrating the product of two different harmonics over T₀ gives zero"
    - "Harmonics are all bounded by the fundamental frequency, so they can't interfere"
    - "Each harmonic has a unique phase, preventing overlap"
  answer: 1
  explanation: "Orthogonality is the key. Because ∫cos(mω₀t)·cos(nω₀t)dt = 0 for m≠n over one period, computing the coefficient aₙ by integrating x(t) against cos(nω₀t) extracts only the nth harmonic with zero contamination from all others. This is exactly like projecting a vector onto perpendicular basis vectors — each projection picks up only one component. Without orthogonality, the decomposition would be non-unique (different combinations of harmonics could produce the same signal), making the frequency-domain representation meaningless."

- question: "The Fourier series of a periodic signal contains energy at all frequencies, not just at integer multiples of the fundamental."
  type: true-false
  answer: false
  explanation: "The Fourier series of a periodic signal contains energy only at the fundamental frequency f₀ = 1/T₀ and its integer multiples (harmonics): f₀, 2f₀, 3f₀, … This produces a discrete amplitude spectrum. Energy at arbitrary (non-harmonic) frequencies would imply the signal is aperiodic — the Fourier transform (not series) handles that case and produces a continuous spectrum. The discreteness of the Fourier series spectrum is a direct consequence of the signal's periodicity."

- question: "When approximating a square wave by summing finitely many Fourier harmonics, the overshoot near the discontinuities persists at roughly 9% of the jump height no matter how many harmonics are included — it never disappears."
  type: true-false
  answer: true
  explanation: "This is the Gibbs phenomenon. As more harmonics are added, the overshoot region near a jump discontinuity narrows but its height does not vanish — it converges to approximately 8.9% of the total jump. The partial sum converges pointwise everywhere except at the discontinuity, where it converges to the average of the left and right limits. This is one of the first places students encounter a subtle distinction between pointwise convergence and uniform convergence, and it shows that sharp discontinuities have a specific frequency-domain signature (slowly decaying harmonic amplitudes)."

- question: "Explain why a pure sine wave requires exactly one nonzero Fourier coefficient while a square wave requires infinitely many. What does this tell you about the relationship between a signal's time-domain shape and its frequency-domain content?"
  type: short-answer
  answer: "A pure sine wave at frequency f₀ is already one of the Fourier basis functions — it has energy only at f₀ and all other coefficients are zero by orthogonality. A square wave, with its instantaneous vertical edges, contains energy at the fundamental plus all odd harmonics because sharp discontinuities require high-frequency content to form. The more abrupt or complex the time-domain shape, the richer its frequency-domain representation. Smooth, slowly varying signals have most energy in low harmonics; signals with sharp features require high harmonics to reconstruct their detail."
  explanation: "This is the core insight of Fourier analysis: time-domain shape and frequency-domain content are two equivalent descriptions of the same signal. A time-domain discontinuity (jump) is a frequency-domain statement: 'this signal has significant energy at arbitrarily high harmonic frequencies.' A bandlimited signal (all energy below some maximum frequency) must be smooth in the time domain. This equivalence is the foundation for filtering — a low-pass filter removes high harmonics and smooths sharp features — and for the sampling theorem, which governs digitizing signals."
```

## Explainer

You know from signal properties that a periodic signal repeats with some fundamental period T₀, and from orthogonal signal decomposition that signals can be expressed as weighted sums of basis functions. The Fourier series unites these two ideas: for periodic signals, the natural basis functions are sinusoids at the **fundamental frequency** f₀ = 1/T₀ and its integer multiples, called **harmonics**. These are orthogonal over one period — they do not interfere with each other — which means the decomposition into harmonics is unique. Every periodic signal (subject to the Dirichlet conditions) has exactly one Fourier series expansion.

The **real form** of the Fourier series writes a periodic signal x(t) as x(t) = a₀/2 + Σ[aₙ cos(nω₀t) + bₙ sin(nω₀t)], where ω₀ = 2π/T₀ is the fundamental angular frequency and the sum runs over all positive integers n. The **Fourier coefficients** aₙ and bₙ are computed by integrating x(t) against cos(nω₀t) and sin(nω₀t) respectively over one full period. These integrals project x(t) onto each basis function — they extract "how much" of each harmonic is present. The orthogonality of the basis functions guarantees that this projection works cleanly: computing a₁ picks up only the fundamental cosine component, with zero contribution from all other harmonics.

The **complex exponential form** is often more elegant and mathematically convenient: x(t) = Σ cₙ e^(jnω₀t), where cₙ = (1/T₀)∫x(t)e^(−jnω₀t)dt over one period. Using Euler's formula e^(jθ) = cosθ + j sinθ, you can show that the real and complex forms are equivalent — cₙ is simply the complex number whose real and imaginary parts encode the cosine and sine amplitudes together. The magnitude |cₙ| is the amplitude of the nth harmonic, and arg(cₙ) is its phase. Plotting |cₙ| versus n gives the **amplitude spectrum** of the signal — a discrete display showing exactly which frequencies are present and with what strength.

The Fourier series reveals a key insight: the "shape" of a periodic signal in the time domain is equivalent to a distribution of amplitudes and phases at discrete frequencies. A pure sine wave has only one nonzero coefficient (its fundamental). A square wave has energy at the fundamental plus all odd harmonics with amplitudes 1, 1/3, 1/5, 1/7, ... — this is why a square wave sounds harsh compared to a sine wave, and why it takes many harmonics to reconstruct one (a partial sum overshoots at the discontinuities — the **Gibbs phenomenon**). This frequency-domain view is the foundation for everything that follows: the Fourier transform extends the series to non-periodic signals, and the spectrum concept underlies all of filtering, modulation, and system frequency response analysis.

