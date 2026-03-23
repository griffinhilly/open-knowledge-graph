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
stage: expert
status: draft
---

# Discrete-Time Fourier Transform (DTFT)

## Core Idea
The DTFT X(e^(jω)) = Σ x[n]e^(-jωn) is the Fourier transform of a discrete-time signal, relating discrete-time signals to periodic continuous frequency responses. Unlike the Z-transform (valid on the unit circle), the DTFT is defined only for |z|=1.

## Questions

```yaml
- question: "A discrete-time system has poles at z = 0.5 and z = 1.5. Can its DTFT be computed?"
  type: multiple-choice
  options:
    - "Yes — the DTFT is always defined for any discrete-time system by evaluating X(z) at z = e^(jω)"
    - "No — the pole at z = 1.5 places it outside the unit circle, so the ROC of the Z-transform excludes the unit circle and the DTFT does not exist"
    - "Yes — the DTFT averages the contributions of stable and unstable poles, converging to a finite result"
    - "No — the DTFT cannot be computed for systems with more than one pole, regardless of their location"
  answer: 1
  explanation: "The DTFT is the Z-transform evaluated on the unit circle |z| = 1. For this evaluation to be valid, the unit circle must lie inside the Z-transform's region of convergence (ROC). A pole at z = 1.5 means the ROC is |z| > 1.5 (for a causal system), which does not include the unit circle. Physically, this corresponds to an unstable system whose impulse response grows without bound — no frequency-domain representation exists via the DTFT. The pole at z = 0.5 alone would give ROC |z| > 0.5, which includes the unit circle and allows the DTFT."

- question: "What is the fundamental reason why the DTFT X(e^(jω)) is exactly periodic with period 2π in ω?"
  type: multiple-choice
  options:
    - "Digital frequency must be normalized to fit within a bounded range, so periodicity is a mathematical convention"
    - "Multiplying a discrete sequence x[n] by e^(j(ω+2π)n) produces exactly the same result as multiplying by e^(jωn), because e^(j2πn) = 1 for all integers n"
    - "The Z-transform is defined on a circle, making all evaluations naturally periodic in the angular variable"
    - "The DFT (which approximates the DTFT) is computed over N discrete points, introducing periodicity as a numerical artifact"
  answer: 1
  explanation: "The 2π-periodicity is not a convention or approximation — it is an exact algebraic identity. For any integer n, e^(j2πn) = cos(2πn) + j·sin(2πn) = 1. Therefore e^(j(ω+2π)n) = e^(jωn)·e^(j2πn) = e^(jωn)·1 = e^(jωn). Substituting into the DTFT sum, X(e^(j(ω+2π)}) = Σx[n]e^(-j(ω+2π)n) = Σx[n]e^(-jωn) = X(e^(jω)). The periodicity is baked into integer-indexed sampling: a discrete-time signal simply cannot distinguish frequencies that differ by 2π."

- question: "The DTFT of any stable discrete-time system (all poles strictly inside the unit circle) always exists and is a continuous, periodic function of digital frequency ω."
  type: true-false
  answer: true
  explanation: "For a stable system, all poles are inside the unit circle, which means the ROC of the Z-transform includes the unit circle. Evaluating X(z) on the unit circle (z = e^(jω)) is therefore valid, and the result X(e^(jω)) exists for all ω. It is continuous in ω (since the sum defining the DTFT is a sum of continuous functions of ω) and exactly 2π-periodic. This is the theoretical foundation for frequency-domain analysis of stable digital filters."

- question: "The 2π-periodicity of the DTFT is a limitation of discrete sampling that can be overcome by using a higher sampling rate, which extends the usable frequency range beyond 2π radians."
  type: true-false
  answer: false
  explanation: "The 2π-periodicity is a fundamental, exact property of discrete-time representation — not a limitation of the sampling rate. Every discrete-time system has a DTFT that is 2π-periodic, regardless of sampling rate. Increasing the sampling rate f_s changes the mapping between analog frequency Ω and digital frequency ω = 2πΩ/f_s (allowing higher analog frequencies to be represented before aliasing), but the digital DTFT itself remains 2π-periodic with exactly the same structure. The periodicity reflects the irreducible ambiguity of integer-indexed sequences: samples alone cannot distinguish frequencies that differ by integer multiples of the sampling rate."

- question: "Explain how the 2π-periodicity of the DTFT is the frequency-domain expression of aliasing in sampled signals."
  type: short-answer
  answer: "When a continuous signal is sampled at rate f_s, any continuous frequency Ω and any frequency Ω + k·f_s (for integer k) produce identical sample sequences — they are aliased together and cannot be distinguished from the samples alone. In the digital frequency domain, these aliased frequencies map to the same digital frequency ω = 2πΩ/f_s. Aliasing is not a defect that appears only when the sampling rate is too low — it is structurally built into the discrete representation: the samples carry no information that distinguishes ω from ω + 2π. The DTFT's 2π-periodicity directly expresses this: X(e^(jω)) = X(e^(j(ω+2π)}) exactly, because both evaluate the spectrum of the same sample sequence at frequencies that are by definition indistinguishable."
  explanation: "The Nyquist theorem tells us how to avoid aliasing of the desired signal, but the periodicity is always present in the DTFT regardless. It is not a problem to be solved but a property to be understood when designing and analyzing discrete-time systems."
```

## Explainer

You already know two Fourier tools: the continuous-time Fourier transform (CTFT), which decomposes a continuous signal x(t) into complex exponentials e^(jΩt) over all real frequencies Ω, and the Z-transform, which maps a discrete sequence x[n] to a function X(z) of a complex variable z. The **DTFT** bridges these — it is the Fourier transform for discrete-time signals, and it turns out to be the Z-transform evaluated on a specific contour in the z-plane.

Start from the Z-transform: X(z) = Σ x[n]z^(-n). This sum converges for values of z within the **region of convergence** (ROC). Now restrict z to the unit circle: z = e^(jω), so |z| = 1 and the angle ω is the normalized digital frequency in radians. Substituting gives X(e^(jω)) = Σ x[n]e^(-jωn) — the DTFT. The signal x[n] at each sample n is being multiplied by a phasor of frequency ω and summed, exactly analogous to the CTFT integral. The output X(e^(jω)) is a **continuous function of ω** that completely describes the frequency content of the discrete sequence. The crucial constraint is that the unit circle must lie inside the Z-transform ROC; for a stable system (poles inside unit circle), this is always satisfied.

The most important structural property of the DTFT is its **2π-periodicity**: X(e^(j(ω+2π)}) = X(e^(jω)) for all ω. This is not an approximation — it is exact and fundamental. Digital frequency ω is only meaningful modulo 2π, because multiplying a discrete sequence by e^(j(ω+2π)n) = e^(jωn)e^(j2πn) = e^(jωn)·1^n = e^(jωn). Frequencies that differ by 2π are indistinguishable to a discrete-time system. This is the frequency-domain signature of the aliasing you already understand from sampling: when you sample a continuous signal at rate f_s, all continuous frequencies Ω and Ω + k·f_s map to the same digital frequency ω = Ω/f_s·2π. The DTFT's periodicity reflects that aliasing is baked into the discrete-time representation.

In practice, the DTFT tells you the **frequency response** of a discrete-time filter. If h[n] is the impulse response of a digital filter and you compute H(e^(jω)), you get the complex gain the filter applies at each digital frequency ω — magnitude |H(e^(jω))| is the amplitude response, and angle ∠H(e^(jω)) is the phase shift. Designing a digital filter is equivalent to shaping H(e^(jω)) to pass desired frequencies and attenuate others. The DTFT is not directly computable for infinite-length sequences (the sum has infinitely many terms), which is why the **DFT** (its finite, sampled version) and the FFT algorithm exist — but the DTFT is the theoretical foundation. Every digital filter specification, every frequency response plot, and every aliasing argument ultimately rests on the DTFT's continuous periodic frequency-domain representation of discrete-time signals.

