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
stage: formal-systems
status: validated
---

# Elementary Signals: Impulse, Step, and Exponential Functions

## Core Idea
The impulse (Dirac delta), unit step, and exponential signals are fundamental building blocks for representing and analyzing arbitrary signals. The impulse response of a system completely characterizes its input-output behavior for any input signal.

## Questions

```yaml
- question: "A student claims: 'Since the unit impulse δ(t) is zero everywhere except at t = 0, applying it to a system should produce zero output for t > 0 — there is nothing driving the system after the instant the impulse fires.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct for stable systems but wrong for unstable ones, where energy accumulates indefinitely"
    - "The impulse deposits energy into the system at t = 0, exciting its natural modes; the system then evolves freely according to its own dynamics, producing a nonzero impulse response for t > 0 that reveals the system's poles and resonances"
    - "The student is correct — a physically realizable system cannot respond after the impulse has ended"
    - "The unit impulse is actually nonzero at all times (it approaches 1/ε for interval ε), so the system is continuously driven"
  answer: 1
  explanation: "The impulse acts as an instantaneous 'kick' that excites all of the system's natural modes simultaneously. After t = 0, the system evolves freely according to its internal dynamics — the stored energy (in capacitors, inductors, springs, or the system's state variables) drives the output. A first-order RC circuit hit by an impulse at t = 0 produces an exponentially decaying voltage for all t > 0; the decay rate reveals the system's time constant. The impulse response encodes the system's complete dynamic character, not just its instantaneous reaction."

- question: "Why is the complex exponential e^{st} (where s is complex) considered the 'eigenfunction' of a linear time-invariant system?"
  type: multiple-choice
  options:
    - "Because all natural signals can be expressed as sums of complex exponentials, making them universally applicable"
    - "Because if the input to an LTI system is e^{st}, the output is H(s)·e^{st} — the same function, scaled by a complex constant H(s) that depends only on the system and the frequency s, not on time"
    - "Because complex exponentials have the smallest Fourier bandwidth of any signal class"
    - "Because the impulse response of every LTI system is itself a complex exponential"
  answer: 1
  explanation: "An eigenfunction of a linear operator is one that the operator maps to a scalar multiple of itself. For LTI systems, complex exponentials have this property: the system changes only the amplitude and phase of e^{st}, not its functional form. H(s) is the transfer function — it tells you how the system scales the complex exponential at each frequency s. This eigenfunction property is why the Laplace and Fourier transforms are so powerful: they decompose arbitrary inputs into complex exponentials, apply H(s) to each component, and reassemble the output. The entire theory of frequency-domain analysis rests on this fact."

- question: "The unit impulse function δ(t) is a classical function with a well-defined, finite value at t = 0 and zero everywhere else."
  type: true-false
  answer: false
  explanation: "The Dirac delta δ(t) is not a classical function — it has no well-defined finite value at t = 0. It is a mathematical distribution (generalized function) defined operationally by its sifting property: ∫f(t)δ(t − t₀)dt = f(t₀) for any continuous function f. Think of it as the limit of a rectangular pulse of width ε and height 1/ε as ε → 0: the height is infinite, the width is zero, but the area (integral) remains exactly 1. Classical pointwise values are undefined; only integrals involving δ(t) have meaning."

- question: "The unit step function u(t) and the unit impulse δ(t) are related by differentiation and integration: the impulse is the derivative of the step, and the step is the integral of the impulse."
  type: true-false
  answer: true
  explanation: "u(t) = ∫_{−∞}^{t} δ(τ)dτ and δ(t) = du/dt (in the distributional sense). This relationship has direct practical consequences: if you know an LTI system's step response s(t), you can differentiate to get the impulse response h(t) = ds/dt. Conversely, integrate h(t) to get the step response. The ramp response integrates the step response. This chain of relationships means measuring one response gives access to all others."

- question: "Explain why the impulse response completely characterizes the input-output behavior of a linear time-invariant system for any input signal, connecting the properties of the impulse to the principles of linearity and time-invariance."
  type: short-answer
  answer: "Any input signal x(t) can be decomposed into a continuum of scaled, shifted impulses: x(t) = ∫x(τ)δ(t − τ)dτ (the sifting property). By time-invariance, if δ(t) produces h(t), then δ(t − τ) produces h(t − τ). By linearity, the response to a scaled, shifted impulse x(τ)δ(t − τ) is x(τ)h(t − τ). Summing (integrating) over all τ gives the system output: y(t) = ∫x(τ)h(t − τ)dτ — the convolution integral. Since this holds for any input x(t), knowing h(t) is sufficient to compute the output for every possible input."
  explanation: "The impulse acts as the identity element of convolution: x(t) ★ δ(t) = x(t). This means if you can express the input as a superposition of impulses (which you always can, by the sifting property), and you know how the system responds to each impulse (the impulse response), linearity and time-invariance guarantee the output is the corresponding superposition of impulse responses — convolution. The impulse response is thus the complete 'fingerprint' of an LTI system."
```

## Explainer

From your study of continuous and discrete signal classification, you know that a signal is simply a function of time (or another independent variable) that carries information. But to analyze systems, you need more than arbitrary signals — you need a small set of canonical signals that are both mathematically tractable and physically meaningful. The impulse, unit step, and exponential functions are that toolkit. Every signal analysis technique you encounter builds on these three foundations.

The **unit step** u(t) is the simplest: it is 0 for t < 0 and 1 for t ≥ 0. It models switching-on events — turning on a voltage, opening a valve, initiating a process. The step is useful because it has a clean frequency content (its Fourier transform is concentrated at low frequencies) and because many physical systems are tested by applying a step input and observing the transient response. The **unit impulse** δ(t), or Dirac delta, is more subtle. It is not a function in the classical sense — it has zero width and infinite height, but its integral is exactly 1. Think of it as the limiting case of a very short, very tall rectangular pulse whose area stays constant as the duration shrinks to zero. The impulse models instantaneous events: a sharp hammer blow on a structure, a brief voltage spike, a single sample in a discrete sequence. Its defining mathematical property is the **sifting property**: ∫ f(t) δ(t − t₀) dt = f(t₀). An impulse extracts the value of any function at the moment it fires.

The relationship between the impulse and step is exact: the unit step is the integral of the unit impulse (u(t) = ∫_{−∞}^{t} δ(τ) dτ), and the impulse is the derivative of the step. This means if you know how a system responds to a step, you can differentiate to get its impulse response — and vice versa. The **complex exponential** e^{st} (where s = σ + jω is a complex number) is the third building block and arguably the deepest. When σ = 0, it becomes e^{jωt} = cos(ωt) + j·sin(ωt) — a pure sinusoid. When ω = 0, it becomes e^{σt} — a real exponential growth or decay. The general complex exponential combines both: a sinusoid whose amplitude grows (σ > 0) or decays (σ < 0) exponentially. These are precisely the natural modes of linear systems: the poles of a transfer function in the s-plane tell you which complex exponentials the system "rings at" when disturbed.

The reason the impulse response completely characterizes a linear time-invariant system is that any input can be decomposed into a continuum of weighted, shifted impulses — and by linearity and time-invariance, the output is the corresponding sum of shifted, weighted impulse responses. This decomposition is convolution, and it works because the impulse is the identity element for convolution: convolving any signal with an impulse returns the original signal unchanged. Similarly, in the frequency domain, complex exponentials are the eigenfunctions of LTI systems: if the input is e^{st}, the output is H(s)e^{st}, where H(s) is the transfer function. This eigenfunction property is why the Laplace and Fourier transforms — both built from superpositions of complex exponentials — are so powerful for LTI system analysis.
