---
id: signal-classification-continuous-discrete
title: 'Signal Classification: Continuous vs. Discrete Time'
domain: engineering
course: signals-and-systems
prerequisites: []
builds-toward:
- elementary-signals-impulse-step-exponential
- basic-signal-operations-transformations
- convolution-continuous-discrete-systems
tags:
- signals
- foundations
- classification
stage: advanced
status: draft
---

# Signal Classification: Continuous vs. Discrete Time

## Core Idea
Signals represent physical phenomena and can be classified as continuous-time (defined for all t) or discrete-time (defined only at integer intervals). Understanding the distinction is fundamental because the mathematical tools, properties, and analysis techniques differ significantly between the two domains.

## How It's Best Learned
Start with examples from real systems: a continuous analog voltage vs. digital audio samples. Sketch both types of signals and observe how sampling converts one to the other.

## Common Misconceptions
Not all signals are sinusoids or simple functions. Discrete-time signals are not merely 'sampled' versions of continuous signals—they are their own mathematical objects with specific properties and transformations.

## Explainer

A **signal** is any quantity that varies over time and carries information. The temperature outside your window right now is a signal — it changes continuously as seconds pass. The daily high temperature logged by a weather station is also a signal, but it only exists as a sequence of values recorded once per day. The first is **continuous-time (CT)**; the second is **discrete-time (DT)**. This single distinction — whether the signal is defined for every instant or only at isolated moments — determines almost everything about how you analyze it.

In continuous time, a signal x(t) is a function from the real line (or some interval of it) to the real numbers. Every value of t has a corresponding value of x(t). Physical phenomena are inherently continuous: voltage on a wire, pressure in a pipe, position of a mass. The mathematics of CT signals draws on calculus — derivatives, integrals, differential equations. The Fourier transform for CT signals integrates over all time using the familiar integral ∫ x(t) e^{−jωt} dt.

In discrete time, a signal x[n] is defined only at integer indices n = …, −2, −1, 0, 1, 2, …. There is no x[1.5] — the question is meaningless for a DT signal. Digital computers, by their nature, process discrete-time signals: a microphone outputs a voltage, but your sound card samples it 44,100 times per second and stores a sequence of numbers. The mathematics shifts from calculus to sequences and summations: differences replace derivatives, summations replace integrals, and the Discrete-Time Fourier Transform (DTFT) is a sum ∑ x[n] e^{−jωn}.

The key insight is that DT signals are not just "sampled" CT signals with gaps — they are their own complete mathematical world with different rules. For example, the concept of **frequency** means something subtly different: a DT sinusoid with frequency ω₀ and one with frequency ω₀ + 2π are *identical* sequences, so DT frequency is periodic with period 2π. No such periodicity exists in continuous time. Understanding both domains and how sampling connects them (the Sampling Theorem, covered later) is the foundation for all of modern signal processing, communications, and control systems.

