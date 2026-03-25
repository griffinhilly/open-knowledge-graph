---
id: lti-systems-and-impulse-response
title: LTI Systems and Impulse Response
domain: engineering
course: signals-and-systems
prerequisites:
- id: systems-classification-properties
  type: hard
- id: elementary-signals-impulse-step-exponential
  type: hard
- id: system-causality-and-realizability
  type: soft
builds-toward:
- convolution-continuous-discrete-systems
- transfer-function-poles-zeros
tags:
- systems
- lti
- impulse-response
stage: expert
status: validated
---
# LTI Systems and Impulse Response

## Core Idea
For a linear time-invariant system, the impulse response h(t) or h[n] fully characterizes the system's input-output relationship. Any output can be computed as the convolution of the input with the impulse response, making the impulse response the most fundamental descriptor of an LTI system.

## Questions

```yaml
- question: "An audio engineer fires a starter pistol in a concert hall and records the resulting decaying echoes. She then convolves this recording with a dry piano track. Why does the result sound like the piano played in that hall?"
  type: multiple-choice
  options:
    - "The impulse response captures the hall's frequency spectrum, which is then added to the piano's power"
    - "By linearity, each scaled impulse in the piano signal produces a scaled copy of h(t); by time-invariance, each delayed impulse produces a delayed copy of h(t) — the sum of all these copies is the convolution y = x * h"
    - "The impulse response averages the room reflections, and convolution applies this average uniformly to the piano signal"
    - "Convolution blends the two signals by computing a running average of their amplitudes"
  answer: 1
  explanation: "This is the direct derivation of why convolution works. The piano signal x(t) decomposes into scaled, shifted impulses. Linearity says the response to a scaled impulse is a scaled output; time-invariance says the response to a shifted impulse δ(t−τ) is a shifted h(t−τ). Summing all these responses gives y(t) = ∫x(τ)h(t−τ)dτ — convolution. Options A and C misrepresent the mechanism; D confuses convolution with averaging (only true for a box filter, not in general)."

- question: "Two different LTI systems produce identical outputs when given a 440 Hz sinusoidal test signal. What can you conclude about the two systems?"
  type: multiple-choice
  options:
    - "The systems are identical — matching outputs for any single input means they have the same impulse response"
    - "The systems have the same gain and phase shift at 440 Hz, but may differ for every other frequency"
    - "The systems have identical impulse responses except at a single point in time"
    - "The systems are time-invariant but may not be linear"
  answer: 1
  explanation: "The impulse response encodes a system's behavior across ALL frequencies and ALL possible inputs. Matching output for a single sinusoidal input tells you only about behavior at that one frequency. The two systems could have entirely different impulse responses — and thus entirely different outputs — for any other input. This illustrates why the impulse response is a complete characterization: you need to test with the impulse (which contains all frequencies) to determine the full system."

- question: "For an LTI system, knowing the impulse response h(t) is sufficient to determine the system's output for any possible input."
  type: true-false
  answer: true
  explanation: "This is the central theorem of LTI system analysis. The output is always y(t) = x(t) * h(t) — the convolution of the input with the impulse response. This single function h(t) encodes everything the system can do to any input. The key caveat is that the system must truly be LTI; if the system is nonlinear or time-varying, the impulse response does not fully characterize it."

- question: "The impulse response h(t) of an LTI system is defined as the input signal that produces the most useful output from the system."
  type: true-false
  answer: false
  explanation: "This reverses the definition. The impulse response is the system's OUTPUT when the INPUT is an impulse δ(t). It is not a special input — it is what the system produces in response to an idealized spike. The confusion between 'input to the system' and 'output from the system' is the most common error in understanding this definition."

- question: "Explain why time-invariance is just as essential as linearity for the impulse response to fully characterize an LTI system."
  type: short-answer
  answer: "Linearity alone allows the output to be written as a sum of responses to scaled, shifted impulses: ∫x(τ)·(response to δ(t−τ)) dτ. But without time-invariance, the system's response to δ(t−τ) could be an entirely different function depending on when τ occurs — not simply a shifted version of h(t). Time-invariance guarantees that the response to δ(t−τ) is exactly h(t−τ). Without this, no single function can summarize the system's behavior for all possible inputs and times."
  explanation: "The convolution formula y(t) = ∫x(τ)h(t−τ)dτ requires both properties simultaneously. Linearity enables superposition (building the output from individual impulse responses); time-invariance ensures those responses are all just shifts of the same h(t). Remove either property and the formula breaks down."
```

## Explainer

From your study of system properties, you know that a **linear** system obeys superposition: if input x₁ produces output y₁ and input x₂ produces y₂, then αx₁ + βx₂ produces αy₁ + βy₂ for any constants α, β. A **time-invariant** system has behavior that doesn't change over time: if x(t) produces y(t), then x(t−t₀) produces y(t−t₀). These two properties together — LTI — are a remarkably powerful combination because they allow any input-output relationship to be captured by a single function: the **impulse response**.

The logic works as follows. The impulse δ(t) is the idealized "spike" signal from your elementary signals prerequisite — infinite height, zero width, unit area. Apply it to an LTI system and record the output: that output is h(t), the impulse response. Now consider any arbitrary input x(t). You can decompose it as a sum (really, integral) of scaled, shifted impulses: x(t) = ∫ x(τ)·δ(t−τ) dτ. By linearity, the output is the sum of the responses to each scaled impulse; by time-invariance, the response to a shifted impulse δ(t−τ) is a shifted version of h, namely h(t−τ). Combining: y(t) = ∫ x(τ)·h(t−τ) dτ. This integral is **convolution**, written y = x * h. Everything the system can do to any input is encoded in h.

To build intuition, think of a simple echo system: if you clap in a concert hall, the hall responds with a decaying sequence of echoes. That decay pattern is the impulse response h(t) of the hall. Any sound x(t) played in the hall produces the output y(t) = x * h — the dry signal convolved with the echo pattern. Audio engineers record impulse responses of real spaces (by firing a starter pistol) and then convolve any dry recording with that impulse response to digitally place the recording in that acoustic environment. The system is the concert hall; its complete behavior is captured by one measurement.

In discrete time the same logic applies exactly, with sums replacing integrals: y[n] = Σ x[k]·h[n−k]. A digital filter is completely defined by its impulse response sequence h[n]. An **FIR (finite impulse response) filter** has h[n] that is nonzero for only finitely many values of n; an **IIR (infinite impulse response) filter** has a response that continues indefinitely, typically implemented with feedback. The connection to frequency domain analysis is direct: the Fourier transform of h(t) is the **transfer function** H(f), which tells you how the system scales and phase-shifts each frequency component of the input. This connects the time-domain convolution picture to the frequency-domain multiplication picture that will be essential for pole-zero analysis in future topics.
