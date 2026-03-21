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

## Questions

```yaml
- question: "Why does knowing a linear time-invariant system's impulse response h(t) allow you to compute its output for any input?"
  type: multiple-choice
  options:
    - "Because the impulse is the most powerful input signal, so the system's response to it bounds all other responses"
    - "Because any input signal can be decomposed into a weighted, time-shifted collection of impulses, and superposition gives the total response via convolution"
    - "Because h(t) reveals the system's poles and zeros, from which all outputs can be derived analytically"
    - "Because the impulse response is only defined for linear systems, which by definition respond predictably to all inputs"
  answer: 1
  explanation: "The Dirac delta is the identity element of convolution: any signal u(t) can be written as the convolution of u with δ, i.e., u(t) = ∫u(τ)δ(t-τ)dτ. For an LTI system, linearity means responses to each impulse slice add, and time-invariance means a delayed impulse produces a delayed h(t). Summing all the delayed, scaled responses gives y(t) = ∫h(τ)u(t-τ)dτ. So h(t) is a complete characterization — knowing it is equivalent to knowing everything about the system's input-output behavior."

- question: "Two linear time-invariant systems with transfer functions G₁(s) and G₂(s) are connected in series (output of System 1 feeds input of System 2). What is the combined system's transfer function?"
  type: multiple-choice
  options:
    - "G₁(s) + G₂(s) — signals pass through both systems so their effects add"
    - "G₁(s) · G₂(s) — cascaded systems multiply in the Laplace domain"
    - "G₁(s) / G₂(s) — the second system partially cancels the effect of the first"
    - "The combined transfer function cannot be determined without knowing the time-domain impulse responses"
  answer: 1
  explanation: "In the Laplace domain, Y(s) = G(s)U(s). For cascaded systems: if U₂(s) = G₁(s)U₁(s) and Y(s) = G₂(s)U₂(s), then Y(s) = G₂(s)G₁(s)U₁(s) = [G₁(s)G₂(s)]U₁(s). The combined transfer function is the product. This is why the Laplace domain is so powerful for control design: complex cascades of filters, plants, and controllers reduce to polynomial multiplication and division, avoiding the messy convolution integrals that would be required in the time domain."

- question: "Taking the Laplace transform of the convolution integral y(t) = ∫h(τ)u(t-τ)dτ yields Y(s) = G(s) + U(s) — convolution transforms to addition."
  type: true-false
  answer: false
  explanation: "Convolution in the time domain transforms to MULTIPLICATION in the Laplace domain: Y(s) = G(s) · U(s). This is the convolution theorem of Laplace transforms. Addition in the Laplace domain corresponds to addition in the time domain (superposition of signals), not to convolution. The multiplication property is precisely what makes the Laplace domain so useful: it converts the integral operation of convolution into simple algebraic multiplication, enabling all frequency-domain analysis tools."

- question: "A system with an impulse response that decays to near zero within 0.1 seconds has a short memory — inputs from more than 0.1 seconds ago have negligible influence on the current output."
  type: true-false
  answer: true
  explanation: "The convolution integral y(t) = ∫h(τ)u(t-τ)dτ sums contributions from all past inputs, weighted by h(τ). If h(τ) ≈ 0 for τ > 0.1 s, then inputs more than 0.1 seconds in the past contribute negligibly to the current output. The duration of h(t) is the system's 'memory length.' Systems with long-duration h(t) — such as lightly damped resonators — integrate past inputs over a long window, making them sensitive to disturbances from far in the past and typically harder to control."

- question: "Explain why the transfer function G(s) is defined as the Laplace transform of the impulse response h(t), and why this makes G(s) central to frequency-domain control analysis."
  type: short-answer
  answer: "G(s) = L{h(t)} because of the convolution theorem: in the time domain, output equals input convolved with h, but in the Laplace domain this becomes Y(s) = G(s)U(s) — simple multiplication. This algebraic relationship is the foundation of frequency-domain analysis. To analyze stability, evaluate G(s) at the poles (roots of the denominator). To compute frequency response, evaluate G(jω) for real ω. To design controllers, manipulate G(s) algebraically rather than solving differential equations. Bode plots, Nyquist diagrams, and root locus all arise from analyzing G(s) in different ways — all of which trace back to the convolution theorem that converts h(t) into the multiplication Y(s) = G(s)U(s)."
  explanation: "The transfer function is not a separate object invented for control theory — it is exactly the Laplace transform of the impulse response. Understanding this connection reveals why frequency-domain methods work: they are simply a convenient coordinate system (frequency instead of time) for the same underlying convolution relationship that describes how LTI systems respond to inputs."
```

## Explainer

From your study of standard test signals, you know that step inputs, ramp inputs, and sinusoids are used to probe how a system behaves. The **impulse** — the Dirac delta function δ(t) — is the most fundamental of all test signals. It has zero duration, infinite amplitude, and unit area. This sounds like an abstraction, but its power is that any input signal can be decomposed into a weighted, time-shifted collection of impulses: if you know how the system responds to a single impulse, you know how it responds to anything.

The **impulse response h(t)** is defined as the system's output when the input is exactly δ(t), with all initial conditions zero. For a first-order system like a low-pass filter or a simple RC circuit, h(t) is a decaying exponential — the system "rings down" after being poked. For a second-order underdamped system, h(t) is a damped sinusoid. The shape of h(t) encodes everything about the system's dynamics: how fast it responds, whether it oscillates, and how long the memory of a disturbance persists. A system with a short-duration h(t) forgets past inputs quickly; a system with a long-duration h(t) has long memory.

Once you have h(t), you can compute the output for any input u(t) using the **convolution integral**: y(t) = ∫₋∞^∞ h(τ) · u(t − τ) dτ. The mechanics are: slide a time-reversed copy of h across u, multiply pointwise, and integrate. Intuitively, this is summing up the system's responses to all the "impulse slices" that make up u, each delayed by the appropriate amount. Convolution in the time domain is the exact general solution — it works for any input, not just the special cases you tested with step and ramp signals.

The Laplace domain reveals why this matters for control design. Taking the Laplace transform of the convolution integral, the integral becomes a simple multiplication: **Y(s) = G(s) · U(s)**, where G(s) is the transfer function — the Laplace transform of h(t). This is the central equation of linear control theory. It means that in the s-domain, a complicated integral (convolution) becomes multiplication by the transfer function. Cascading two systems corresponds to multiplying their transfer functions. Analyzing frequency response corresponds to evaluating G(s) along the imaginary axis. Every tool you will use in frequency-domain control — Bode plots, Nyquist diagrams, root locus — descends from this Y(s) = G(s)U(s) relationship, which itself is just convolution expressed in Laplace coordinates.
