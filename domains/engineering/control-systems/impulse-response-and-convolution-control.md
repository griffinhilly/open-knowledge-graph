---
id: impulse-response-and-convolution-control
title: Impulse Response, Convolution, and System Characterization
domain: engineering
course: control-systems
prerequisites:
- id: standard-test-signals-control
  type: hard
builds-toward:
- frequency-response-magnitude-phase-basics
tags:
- impulse-response
- convolution
- h(t)
- characterization
stage: advanced
status: draft
---

# Impulse Response, Convolution, and System Characterization

## Core Idea
The impulse response h(t) is the output when input is a Dirac delta; the convolution integral y(t) = ∫h(τ)u(t-τ)dτ gives output for any input. In the Laplace domain, this becomes multiplication: Y(s) = G(s)U(s). This relationship is central to both time-domain and frequency-domain analysis.

## Explainer

From your study of standard test signals, you know that step inputs, ramp inputs, and sinusoids are used to probe how a system behaves. The **impulse** — the Dirac delta function δ(t) — is the most fundamental of all test signals. It has zero duration, infinite amplitude, and unit area. This sounds like an abstraction, but its power is that any input signal can be decomposed into a weighted, time-shifted collection of impulses: if you know how the system responds to a single impulse, you know how it responds to anything.

The **impulse response h(t)** is defined as the system's output when the input is exactly δ(t), with all initial conditions zero. For a first-order system like a low-pass filter or a simple RC circuit, h(t) is a decaying exponential — the system "rings down" after being poked. For a second-order underdamped system, h(t) is a damped sinusoid. The shape of h(t) encodes everything about the system's dynamics: how fast it responds, whether it oscillates, and how long the memory of a disturbance persists. A system with a short-duration h(t) forgets past inputs quickly; a system with a long-duration h(t) has long memory.

Once you have h(t), you can compute the output for any input u(t) using the **convolution integral**: y(t) = ∫₋∞^∞ h(τ) · u(t − τ) dτ. The mechanics are: slide a time-reversed copy of h across u, multiply pointwise, and integrate. Intuitively, this is summing up the system's responses to all the "impulse slices" that make up u, each delayed by the appropriate amount. Convolution in the time domain is the exact general solution — it works for any input, not just the special cases you tested with step and ramp signals.

The Laplace domain reveals why this matters for control design. Taking the Laplace transform of the convolution integral, the integral becomes a simple multiplication: **Y(s) = G(s) · U(s)**, where G(s) is the transfer function — the Laplace transform of h(t). This is the central equation of linear control theory. It means that in the s-domain, a complicated integral (convolution) becomes multiplication by the transfer function. Cascading two systems corresponds to multiplying their transfer functions. Analyzing frequency response corresponds to evaluating G(s) along the imaginary axis. Every tool you will use in frequency-domain control — Bode plots, Nyquist diagrams, root locus — descends from this Y(s) = G(s)U(s) relationship, which itself is just convolution expressed in Laplace coordinates.
