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
stage: advanced
status: draft
---

# Fourier Series Representation of Periodic Signals

## Core Idea
Any periodic signal can be decomposed as a sum of sinusoids (harmonics) at integer multiples of the fundamental frequency. The Fourier series provides both real (cosine/sine) and complex exponential forms for representing periodic signals.

## Explainer

You know from signal properties that a periodic signal repeats with some fundamental period T₀, and from orthogonal signal decomposition that signals can be expressed as weighted sums of basis functions. The Fourier series unites these two ideas: for periodic signals, the natural basis functions are sinusoids at the **fundamental frequency** f₀ = 1/T₀ and its integer multiples, called **harmonics**. These are orthogonal over one period — they do not interfere with each other — which means the decomposition into harmonics is unique. Every periodic signal (subject to the Dirichlet conditions) has exactly one Fourier series expansion.

The **real form** of the Fourier series writes a periodic signal x(t) as x(t) = a₀/2 + Σ[aₙ cos(nω₀t) + bₙ sin(nω₀t)], where ω₀ = 2π/T₀ is the fundamental angular frequency and the sum runs over all positive integers n. The **Fourier coefficients** aₙ and bₙ are computed by integrating x(t) against cos(nω₀t) and sin(nω₀t) respectively over one full period. These integrals project x(t) onto each basis function — they extract "how much" of each harmonic is present. The orthogonality of the basis functions guarantees that this projection works cleanly: computing a₁ picks up only the fundamental cosine component, with zero contribution from all other harmonics.

The **complex exponential form** is often more elegant and mathematically convenient: x(t) = Σ cₙ e^(jnω₀t), where cₙ = (1/T₀)∫x(t)e^(−jnω₀t)dt over one period. Using Euler's formula e^(jθ) = cosθ + j sinθ, you can show that the real and complex forms are equivalent — cₙ is simply the complex number whose real and imaginary parts encode the cosine and sine amplitudes together. The magnitude |cₙ| is the amplitude of the nth harmonic, and arg(cₙ) is its phase. Plotting |cₙ| versus n gives the **amplitude spectrum** of the signal — a discrete display showing exactly which frequencies are present and with what strength.

The Fourier series reveals a key insight: the "shape" of a periodic signal in the time domain is equivalent to a distribution of amplitudes and phases at discrete frequencies. A pure sine wave has only one nonzero coefficient (its fundamental). A square wave has energy at the fundamental plus all odd harmonics with amplitudes 1, 1/3, 1/5, 1/7, ... — this is why a square wave sounds harsh compared to a sine wave, and why it takes many harmonics to reconstruct one (a partial sum overshoots at the discontinuities — the **Gibbs phenomenon**). This frequency-domain view is the foundation for everything that follows: the Fourier transform extends the series to non-periodic signals, and the spectrum concept underlies all of filtering, modulation, and system frequency response analysis.

