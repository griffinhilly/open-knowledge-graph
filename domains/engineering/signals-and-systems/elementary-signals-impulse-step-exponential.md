---
id: elementary-signals-impulse-step-exponential
title: 'Elementary Signals: Impulse, Step, and Exponential Functions'
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-classification-continuous-discrete
  type: hard
builds-toward:
- lti-systems-and-impulse-response
- convolution-continuous-discrete-systems
tags:
- signals
- elementary
- foundations
stage: advanced
status: draft
---

# Elementary Signals: Impulse, Step, and Exponential Functions

## Core Idea
The impulse (Dirac delta), unit step, and exponential signals are fundamental building blocks for representing and analyzing arbitrary signals. The impulse response of a system completely characterizes its input-output behavior for any input signal.

## Explainer

From your study of continuous and discrete signal classification, you know that a signal is simply a function of time (or another independent variable) that carries information. But to analyze systems, you need more than arbitrary signals — you need a small set of canonical signals that are both mathematically tractable and physically meaningful. The impulse, unit step, and exponential functions are that toolkit. Every signal analysis technique you encounter builds on these three foundations.

The **unit step** u(t) is the simplest: it is 0 for t < 0 and 1 for t ≥ 0. It models switching-on events — turning on a voltage, opening a valve, initiating a process. The step is useful because it has a clean frequency content (its Fourier transform is concentrated at low frequencies) and because many physical systems are tested by applying a step input and observing the transient response. The **unit impulse** δ(t), or Dirac delta, is more subtle. It is not a function in the classical sense — it has zero width and infinite height, but its integral is exactly 1. Think of it as the limiting case of a very short, very tall rectangular pulse whose area stays constant as the duration shrinks to zero. The impulse models instantaneous events: a sharp hammer blow on a structure, a brief voltage spike, a single sample in a discrete sequence. Its defining mathematical property is the **sifting property**: ∫ f(t) δ(t − t₀) dt = f(t₀). An impulse extracts the value of any function at the moment it fires.

The relationship between the impulse and step is exact: the unit step is the integral of the unit impulse (u(t) = ∫_{−∞}^{t} δ(τ) dτ), and the impulse is the derivative of the step. This means if you know how a system responds to a step, you can differentiate to get its impulse response — and vice versa. The **complex exponential** e^{st} (where s = σ + jω is a complex number) is the third building block and arguably the deepest. When σ = 0, it becomes e^{jωt} = cos(ωt) + j·sin(ωt) — a pure sinusoid. When ω = 0, it becomes e^{σt} — a real exponential growth or decay. The general complex exponential combines both: a sinusoid whose amplitude grows (σ > 0) or decays (σ < 0) exponentially. These are precisely the natural modes of linear systems: the poles of a transfer function in the s-plane tell you which complex exponentials the system "rings at" when disturbed.

The reason the impulse response completely characterizes a linear time-invariant system is that any input can be decomposed into a continuum of weighted, shifted impulses — and by linearity and time-invariance, the output is the corresponding sum of shifted, weighted impulse responses. This decomposition is convolution, and it works because the impulse is the identity element for convolution: convolving any signal with an impulse returns the original signal unchanged. Similarly, in the frequency domain, complex exponentials are the eigenfunctions of LTI systems: if the input is e^{st}, the output is H(s)e^{st}, where H(s) is the transfer function. This eigenfunction property is why the Laplace and Fourier transforms — both built from superpositions of complex exponentials — are so powerful for LTI system analysis.
