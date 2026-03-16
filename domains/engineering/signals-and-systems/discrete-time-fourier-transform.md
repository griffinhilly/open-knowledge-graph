---
id: discrete-time-fourier-transform
title: Discrete-Time Fourier Transform (DTFT)
domain: engineering
course: signals-and-systems
prerequisites:
- id: fourier-transform-definition-properties
  type: hard
- id: z-transform-discrete-time-signals
  type: soft
builds-toward:
- dft-and-fft-algorithms
- frequency-response-magnitude-phase
tags:
- dtft
- discrete-time
- frequency-domain
stage: advanced
status: draft
---

# Discrete-Time Fourier Transform (DTFT)

## Core Idea
The DTFT X(e^(jω)) = Σ x[n]e^(-jωn) is the Fourier transform of a discrete-time signal, relating discrete-time signals to periodic continuous frequency responses. Unlike the Z-transform (valid on the unit circle), the DTFT is defined only for |z|=1.

## Explainer

You already know two Fourier tools: the continuous-time Fourier transform (CTFT), which decomposes a continuous signal x(t) into complex exponentials e^(jΩt) over all real frequencies Ω, and the Z-transform, which maps a discrete sequence x[n] to a function X(z) of a complex variable z. The **DTFT** bridges these — it is the Fourier transform for discrete-time signals, and it turns out to be the Z-transform evaluated on a specific contour in the z-plane.

Start from the Z-transform: X(z) = Σ x[n]z^(-n). This sum converges for values of z within the **region of convergence** (ROC). Now restrict z to the unit circle: z = e^(jω), so |z| = 1 and the angle ω is the normalized digital frequency in radians. Substituting gives X(e^(jω)) = Σ x[n]e^(-jωn) — the DTFT. The signal x[n] at each sample n is being multiplied by a phasor of frequency ω and summed, exactly analogous to the CTFT integral. The output X(e^(jω)) is a **continuous function of ω** that completely describes the frequency content of the discrete sequence. The crucial constraint is that the unit circle must lie inside the Z-transform ROC; for a stable system (poles inside unit circle), this is always satisfied.

The most important structural property of the DTFT is its **2π-periodicity**: X(e^(j(ω+2π)}) = X(e^(jω)) for all ω. This is not an approximation — it is exact and fundamental. Digital frequency ω is only meaningful modulo 2π, because multiplying a discrete sequence by e^(j(ω+2π)n) = e^(jωn)e^(j2πn) = e^(jωn)·1^n = e^(jωn). Frequencies that differ by 2π are indistinguishable to a discrete-time system. This is the frequency-domain signature of the aliasing you already understand from sampling: when you sample a continuous signal at rate f_s, all continuous frequencies Ω and Ω + k·f_s map to the same digital frequency ω = Ω/f_s·2π. The DTFT's periodicity reflects that aliasing is baked into the discrete-time representation.

In practice, the DTFT tells you the **frequency response** of a discrete-time filter. If h[n] is the impulse response of a digital filter and you compute H(e^(jω)), you get the complex gain the filter applies at each digital frequency ω — magnitude |H(e^(jω))| is the amplitude response, and angle ∠H(e^(jω)) is the phase shift. Designing a digital filter is equivalent to shaping H(e^(jω)) to pass desired frequencies and attenuate others. The DTFT is not directly computable for infinite-length sequences (the sum has infinitely many terms), which is why the **DFT** (its finite, sampled version) and the FFT algorithm exist — but the DTFT is the theoretical foundation. Every digital filter specification, every frequency response plot, and every aliasing argument ultimately rests on the DTFT's continuous periodic frequency-domain representation of discrete-time signals.

