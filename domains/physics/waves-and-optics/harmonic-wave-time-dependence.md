---
id: harmonic-wave-time-dependence
title: Harmonic Waves and Sinusoidal Form
domain: physics
course: waves-and-optics
prerequisites:
- id: trigonometric-functions
  type: hard
- id: wave-equation-one-dimensional
  type: hard
builds-toward:
- phase-of-oscillation-initial
- interference-two-sources-interference-pattern
tags:
- waves
- sinusoids
- periodicity
stage: advanced
status: validated
---

# Harmonic Waves and Sinusoidal Form

## Core Idea
A harmonic wave has the form u(x,t) = A sin(kx - ωt + φ), where amplitude A, wavenumber k, angular frequency ω, and phase φ completely describe the wave's behavior. This sinusoidal form emerges naturally from the wave equation for periodic sources and is the building block for any periodic wave via Fourier analysis.

## Questions

```yaml
- question: "Two waves are described by u₁ = A sin(kx − ωt) and u₂ = A sin(kx + ωt). They have identical amplitude, wavenumber, and angular frequency. What is the fundamental physical difference between them?"
  type: multiple-choice
  options:
    - "They travel in opposite directions"
    - "They have different wave speeds, since one has a minus sign and one a plus sign"
    - "u₂ does not satisfy the wave equation, because the sign must be negative"
    - "They oscillate with different angular frequencies at any fixed point"
  answer: 0
  explanation: "The sign between kx and ωt encodes the direction of propagation. To 'ride' a crest — keep the phase constant — you set kx − ωt = C. As t increases, x must increase at rate ω/k, so u₁ travels in the +x direction. For u₂, setting kx + ωt = C requires x to decrease as t increases: it travels in the −x direction. Both waves have the same speed v = ω/k and both satisfy the wave equation. The minus sign is not just convention — it is the physical statement that the wave moves right."

- question: "For the wave u(x, t) = 5 sin(3x − 6t + π/4), what is the wave speed?"
  type: multiple-choice
  options:
    - "6 m/s, because ω = 6 is the rate of oscillation"
    - "2 m/s, because v = ω/k = 6/3"
    - "3 m/s, because k = 3 sets the spatial scale"
    - "5 m/s, because the amplitude determines the energy and thus the speed"
  answer: 1
  explanation: "Wave speed is v = ω/k. Reading off the parameters: k = 3 (coefficient of x), ω = 6 (coefficient of t), so v = 6/3 = 2 m/s. The amplitude A = 5 sets the displacement magnitude but has no effect on propagation speed — speed is determined entirely by ω and k (or equivalently by the medium's properties). Choosing ω = 6 as the speed is the most common error; ω is the angular frequency (radians per second), not meters per second."

- question: "For a harmonic wave u = A sin(kx − ωt + φ), a crest (point of maximum displacement) moves in the +x direction at speed ω/k as time advances."
  type: true-false
  answer: true
  explanation: "True. A crest corresponds to a fixed value of the phase: kx − ωt + φ = π/2 (or any value giving sin = 1). Differentiating with respect to t: k(dx/dt) − ω = 0, so dx/dt = ω/k. The crest moves in the +x direction at speed v = ω/k. This is exactly what 'wave propagation' means: patterns of phase (crests, troughs, zero-crossings) translate through space at this speed."

- question: "Increasing the amplitude A of a harmonic wave causes the wave to propagate faster through the medium."
  type: true-false
  answer: false
  explanation: "False. Wave speed v = ω/k depends only on the angular frequency and wavenumber — or equivalently, on the medium's physical properties (tension and density for a string, bulk modulus and density for sound, etc.). The amplitude controls how far the medium is displaced from equilibrium but has no effect on how fast the pattern travels. A louder sound wave and a quiet sound wave in the same air travel at the same speed."

- question: "What does it mean for the phase of a harmonic wave to be constant, and how does this connect to the concept of wave speed?"
  type: short-answer
  answer: "The phase of u(x, t) = A sin(kx − ωt + φ) is the argument kx − ωt + φ. Holding the phase constant means setting kx − ωt + φ = C and asking how x must change as t increases to keep C fixed. Differentiating: k(dx/dt) = ω, so dx/dt = ω/k. A surface of constant phase — a crest, trough, or zero-crossing — moves through space at this speed v = ω/k. Wave speed is precisely the speed at which phase patterns propagate."
  explanation: "This framing unifies the mathematical and physical descriptions of a wave. The wave equation's solutions are sinusoids because they are the functions whose spatial and temporal oscillations are locked together in a fixed ratio ω/k = v. Fourier's theorem then extends this: any periodic waveform is a superposition of sinusoids, so understanding how one sinusoid propagates gives you the tools for arbitrary periodic waves."
```

## Explainer

You already know that the wave equation ∂²u/∂t² = v²∂²u/∂x² governs how disturbances propagate. The question is: what functions actually satisfy it? The answer is sinusoids, and this isn't arbitrary — it falls directly out of the mathematics. When you substitute u(x,t) = A sin(kx - ωt + φ) into the wave equation, the time derivative brings down a factor of ω² and the spatial derivative brings down k², and the equation is satisfied whenever ω²/k² = v². This ratio — angular frequency squared over wavenumber squared — is the wave speed squared, which is why the relationship ω = vk (the **dispersion relation**) connects all the parameters.

Unpack each parameter systematically. **Amplitude** A is the peak displacement — how far the medium moves from equilibrium. **Wavenumber** k = 2π/λ measures how rapidly the wave oscillates in space; larger k means shorter wavelength and more oscillation cycles per meter. **Angular frequency** ω = 2π/T = 2πf measures how rapidly the wave oscillates in time; larger ω means higher frequency and more oscillation cycles per second. The **phase constant** φ shifts the entire waveform, encoding initial conditions: it tells you where in its cycle the wave is at the reference point x = 0, t = 0.

The combination kx - ωt is the engine of the formula and captures wave motion. Fix position x and watch time advance: the argument decreases at rate ω, so the medium at that point oscillates sinusoidally in time like a mass on a spring. Fix time t and scan along x: the argument increases at rate k, giving a spatial snapshot — a frozen sine wave. The minus sign between kx and ωt is what makes the pattern propagate in the +x direction. To "ride" the wave — to keep the phase kx - ωt constant as time increases — you must move in the +x direction at speed v = ω/k. Switching to kx + ωt gives a wave traveling in the −x direction.

The deepest result is Fourier's theorem: *any* periodic waveform can be written as a sum of harmonic waves at different frequencies and amplitudes. This makes the sinusoidal form universal rather than merely special. A square wave, a sawtooth wave, the complex waveform of a musical instrument — all are superpositions of harmonics. Understanding how one sinusoidal wave propagates, reflects, and interferes therefore gives you the tools to analyze any periodic wave, because every such wave is just a weighted collection of these building blocks.
