---
id: z-transform-discrete-time-signals
title: 'Z-Transform: Fundamentals for Discrete-Time Signals'
domain: engineering
course: signals-and-systems
prerequisites:
- id: laplace-transform-fundamentals
  type: hard
- id: signal-classification-continuous-discrete
  type: hard
- id: complex-numbers-intro
  type: soft
- id: geometric-series
  type: hard
- id: complex-functions-mappings
  type: hard
- id: sequences-and-series
  type: soft
builds-toward:
- z-transform-properties-inverse
- digital-signal-processing-fundamentals
tags:
- z-transform
- discrete-time
- digital-systems
stage: advanced
status: draft
---

# Z-Transform: Fundamentals for Discrete-Time Signals

## Core Idea
The Z-Transform X(z) = Σ x[n]z^(-n) is the discrete-time analog of the Laplace transform, mapping discrete sequences into the complex z-plane. It converts difference equations to algebraic equations and is essential for analyzing and designing digital filters and discrete-time systems.

## Questions

```yaml
- question: "Two Z-transforms both simplify to the same algebraic expression X(z) = 1/(1 − az⁻¹). One has ROC |z| > |a| and the other has ROC |z| < |a|. What does this tell you?"
  type: multiple-choice
  options:
    - "The two ROCs correspond to the same time-domain sequence — the ROC is just a mathematical detail"
    - "The two ROCs correspond to different time-domain sequences: one causal, one anti-causal"
    - "The ROC |z| < |a| is always invalid because the Z-transform only converges outside a circle"
    - "Having two different ROCs means there is an error in the calculation"
  answer: 1
  explanation: "This is the central reason the ROC must always be specified. The algebraic expression alone does not uniquely determine the time-domain signal — the same X(z) can correspond to a causal right-sided sequence (ROC: |z| > |a|) or an anti-causal left-sided sequence (ROC: |z| < |a|). Without the ROC, the inverse Z-transform is ambiguous. Carrying the ROC is not a formality; it encodes causality and stability information that the fraction itself cannot."

- question: "A digital filter has transfer function H(z) with poles at z = 0.9 and z = −0.5. Assuming the system is causal, is it stable?"
  type: multiple-choice
  options:
    - "No — the pole at z = 0.9 is too close to the unit circle and will cause oscillations"
    - "No — stability requires all poles to lie outside the unit circle for causal systems"
    - "Yes — for a causal system, stability requires all poles to lie strictly inside the unit circle, and both poles satisfy |z| < 1"
    - "Cannot be determined without knowing the zeros of H(z)"
  answer: 2
  explanation: "For a causal LTI discrete-time system, BIBO stability requires all poles to lie strictly inside the unit circle (|z| < 1). Both poles here satisfy this: |0.9| < 1 and |−0.5| < 1. This is the discrete-time analog of the Laplace stability condition (all poles with negative real part). The zeros of H(z) do not affect stability — only poles do. Closeness to the unit circle affects the filter's frequency response shape but does not by itself cause instability as long as the pole is strictly inside."

- question: "A causal digital system is stable if and only if all its poles lie exactly on the unit circle (|z| = 1)."
  type: true-false
  answer: false
  explanation: "Poles on the unit circle (|z| = 1) make a causal system marginally stable, not stable. A pole at z = 1 corresponds to an accumulator — a bounded nonzero input produces an output that grows without bound. Stability requires all poles to lie *strictly inside* the unit circle (|z| < 1). The distinction between 'on' and 'inside' is critical: a pole at z = e^(jω) on the unit circle produces an undamped oscillation in the impulse response, which grows unboundedly for certain inputs."

- question: "Evaluating the Z-transform X(z) on the unit circle (z = e^(jω)) yields the discrete-time Fourier transform (DTFT) of the sequence x[n]."
  type: true-false
  answer: true
  explanation: "This is the precise relationship between the Z-transform and the DTFT. Substituting z = e^(jω) into X(z) = Σ x[n]z^(−n) gives Σ x[n]e^(−jωn), which is exactly the DTFT definition. This mirrors the Laplace–Fourier relationship: just as the Fourier transform is the Laplace transform evaluated on the imaginary axis (s = jω), the DTFT is the Z-transform evaluated on the unit circle. For this evaluation to be valid, the unit circle must lie within the ROC of X(z)."

- question: "Why must the region of convergence (ROC) always be specified alongside the algebraic expression for a Z-transform? What goes wrong if it is omitted?"
  type: short-answer
  answer: "The ROC must be specified because the same algebraic expression X(z) can correspond to multiple different time-domain sequences — differing in causality and stability — depending on which region of the z-plane is used. Without the ROC, the inverse Z-transform is ambiguous. Additionally, the ROC directly determines whether a system is stable: for causal systems, stability requires all poles to be strictly inside the unit circle, which means the ROC must include the unit circle. Omitting the ROC strips away the information needed to determine causality and stability."
  explanation: "The Z-transform is defined as a power series, and like all series it converges only in certain regions. The algebraic form that results from simplification looks identical regardless of which ROC applies, but the time-domain signals they represent can be completely different (e.g., causal vs. anti-causal versions of the same exponential). The ROC is not a byproduct — it is part of the answer."
```

## Explainer

The Z-transform is to discrete-time signals what the Laplace transform is to continuous-time signals. If you already understand the Laplace transform, you know it converts differential equations into algebraic equations in the s-domain, making analysis tractable. The Z-transform does exactly the same thing for **difference equations** — the discrete-time counterpart of differential equations. The definition X(z) = Σ x[n]z^(-n) looks like an infinite series, and the geometric series from your prerequisites is directly relevant: many common Z-transforms converge precisely because they reduce to geometric series, and the ratio-test conditions on |z| determine where convergence holds.

The key to building intuition is understanding what z represents geometrically. Just as s = σ + jω in the Laplace transform, z is a complex variable living in the complex z-plane. When you evaluate the Z-transform on the **unit circle** — z = e^(jω) — you recover the discrete-time Fourier transform (DTFT). This mirrors the Laplace-to-Fourier connection exactly: evaluating on |z| = 1 corresponds to the imaginary axis in the s-plane. The **region of convergence (ROC)** is the set of z-values for which the series converges; it must always be specified alongside X(z) because the same algebraic expression can represent multiple different time-domain sequences depending on the ROC. Carrying the ROC is not a formality — it determines causality and stability.

The **poles and zeros** of X(z) are the fundamental diagnostic tool. A system's stability hinges on pole locations: for a causal system, stability holds if and only if all poles lie strictly inside the unit circle |z| < 1. This is the discrete analog of the Laplace stability condition requiring all poles to have negative real part. An accumulator (running sum), y[n] = y[n−1] + x[n], has transfer function H(z) = 1/(1 − z^{−1}), with a pole at z = 1 — exactly on the unit circle — making it marginally stable. That matches intuition: summing a bounded nonzero input indefinitely produces an unbounded output.

Perhaps the most practically important application is **digital filter design**. The transfer function H(z) = Y(z)/X(z) encapsulates everything about a linear, time-invariant discrete system. By placing poles and zeros at strategic locations in the z-plane, engineers design filters with prescribed frequency responses — low-pass, high-pass, band-pass, notch. The Z-transform converts the filter specification into a difference equation that a processor executes sample-by-sample. This computational core underlies everything from audio equalizers to communications receivers to medical-device signal chains.
