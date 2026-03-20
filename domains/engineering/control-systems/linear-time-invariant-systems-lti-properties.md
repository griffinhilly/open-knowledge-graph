---
id: linear-time-invariant-systems-lti-properties
title: Linear Time-Invariant (LTI) Systems and Properties
domain: engineering
course: control-systems
prerequisites:
- id: laplace-transform-fundamentals
  type: soft
builds-toward:
- transfer-function-derivation-differential-equations
- frequency-response-magnitude-phase-basics
- impulse-response-and-convolution-control
tags:
- fundamentals
- lti
- linearity
- time-invariance
stage: advanced
status: draft
---

# Linear Time-Invariant (LTI) Systems and Properties

## Core Idea
LTI systems are fundamental to control theory because their behavior can be fully characterized by impulse response and frequency response. A system is linear if it satisfies superposition and homogeneity; time-invariant if its parameters do not change with time. These properties enable use of Laplace transforms and frequency-domain analysis.

## Explainer

The phrase "linear time-invariant" describes two independent properties, each worth understanding on its own before considering them together. **Linearity** has two components: **superposition** and **homogeneity** (scaling). Superposition means that if input x₁(t) produces output y₁(t), and input x₂(t) produces output y₂(t), then input x₁(t) + x₂(t) produces output y₁(t) + y₂(t). Homogeneity means if x(t) produces y(t), then αx(t) produces αy(t) for any scalar α. Together, these mean the system response to a sum of scaled inputs is the same sum of scaled outputs — you can analyze each input component independently, then add the results. This is the principle of superposition, and it is what makes linear systems analytically tractable.

**Time-invariance** means the system's behavior does not depend on when you apply the input. If input x(t) produces output y(t), then input x(t − t₀) produces output y(t − t₀) — the same response, just shifted in time. Practically, this means the differential equation describing the system has constant coefficients: a resistor's resistance doesn't change over time, a spring's stiffness doesn't change, a control gain doesn't drift. Systems with time-varying parameters (e.g., a pendulum whose pivot is moving, or a process with temperature-dependent reaction rates) are not time-invariant and require significantly more complex analysis.

Why do these two properties matter so much? Because together they unlock the **Laplace transform** and **frequency-domain analysis** — your soft prerequisite. For an LTI system, applying the Laplace transform to the differential equation converts it to an algebraic equation in the complex variable s. The ratio of output to input in this domain is the **transfer function** G(s), which completely characterizes the system. Furthermore, for a sinusoidal input at frequency ω, the output of an LTI system is a sinusoid at the *same* frequency, possibly with different amplitude and phase — the system cannot create new frequencies. This is the foundation of Bode plots, Nyquist analysis, and every frequency-domain design method.

The **impulse response** h(t) is the system output when the input is a Dirac delta function δ(t) — an infinitely brief, unit-area pulse. Because of linearity and time-invariance, any input can be decomposed into a weighted sum of shifted impulses, and the output is the corresponding weighted sum of shifted impulse responses. This operation is **convolution**: y(t) = x(t) * h(t) = ∫ x(τ)h(t−τ)dτ. Knowing h(t) completely determines how the system responds to any input — it is the system's fingerprint. In the Laplace domain, convolution becomes multiplication: Y(s) = X(s)·G(s), which is why transfer functions are so much easier to work with than time-domain convolution. The LTI assumption is what makes this simplification valid, and it is the bedrock assumption underlying virtually every classical control analysis and design technique.
