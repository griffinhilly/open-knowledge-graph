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
builds-toward:
- convolution-continuous-discrete-systems
- transfer-function-poles-zeros
tags:
- systems
- lti
- impulse-response
stage: advanced
status: draft
---

# LTI Systems and Impulse Response

## Core Idea
For a linear time-invariant system, the impulse response h(t) or h[n] fully characterizes the system's input-output relationship. Any output can be computed as the convolution of the input with the impulse response, making the impulse response the most fundamental descriptor of an LTI system.

## Explainer

From your study of system properties, you know that a **linear** system obeys superposition: if input x₁ produces output y₁ and input x₂ produces y₂, then αx₁ + βx₂ produces αy₁ + βy₂ for any constants α, β. A **time-invariant** system has behavior that doesn't change over time: if x(t) produces y(t), then x(t−t₀) produces y(t−t₀). These two properties together — LTI — are a remarkably powerful combination because they allow any input-output relationship to be captured by a single function: the **impulse response**.

The logic works as follows. The impulse δ(t) is the idealized "spike" signal from your elementary signals prerequisite — infinite height, zero width, unit area. Apply it to an LTI system and record the output: that output is h(t), the impulse response. Now consider any arbitrary input x(t). You can decompose it as a sum (really, integral) of scaled, shifted impulses: x(t) = ∫ x(τ)·δ(t−τ) dτ. By linearity, the output is the sum of the responses to each scaled impulse; by time-invariance, the response to a shifted impulse δ(t−τ) is a shifted version of h, namely h(t−τ). Combining: y(t) = ∫ x(τ)·h(t−τ) dτ. This integral is **convolution**, written y = x * h. Everything the system can do to any input is encoded in h.

To build intuition, think of a simple echo system: if you clap in a concert hall, the hall responds with a decaying sequence of echoes. That decay pattern is the impulse response h(t) of the hall. Any sound x(t) played in the hall produces the output y(t) = x * h — the dry signal convolved with the echo pattern. Audio engineers record impulse responses of real spaces (by firing a starter pistol) and then convolve any dry recording with that impulse response to digitally place the recording in that acoustic environment. The system is the concert hall; its complete behavior is captured by one measurement.

In discrete time the same logic applies exactly, with sums replacing integrals: y[n] = Σ x[k]·h[n−k]. A digital filter is completely defined by its impulse response sequence h[n]. An **FIR (finite impulse response) filter** has h[n] that is nonzero for only finitely many values of n; an **IIR (infinite impulse response) filter** has a response that continues indefinitely, typically implemented with feedback. The connection to frequency domain analysis is direct: the Fourier transform of h(t) is the **transfer function** H(f), which tells you how the system scales and phase-shifts each frequency component of the input. This connects the time-domain convolution picture to the frequency-domain multiplication picture that will be essential for pole-zero analysis in future topics.
