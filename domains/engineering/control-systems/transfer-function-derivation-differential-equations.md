---
id: transfer-function-derivation-differential-equations
title: Deriving Transfer Functions from Differential Equations
domain: engineering
course: control-systems
prerequisites:
- id: linear-time-invariant-systems-lti-properties
  type: hard
- id: laplace-transform-fundamentals
  type: hard
- id: differential-equations-intro
  type: hard
builds-toward:
- frequency-response-magnitude-phase-basics
- bode-plot-magnitude-asymptotes-rules
tags:
- transfer-functions
- laplace
- differential-equations
stage: advanced
status: draft
---

# Deriving Transfer Functions from Differential Equations

## Core Idea
The transfer function is obtained by applying the Laplace transform to a linear differential equation with zero initial conditions. G(s) = Y(s)/U(s) represents the input-output relationship in the s-domain. This transformation converts convolution operations into algebraic relationships, enabling system analysis and design.

## Questions

```yaml
- question: "A control engineer derives a transfer function G(s) for a motor system, but the motor starts from rest with a non-zero initial velocity. Why can't G(s) alone be used to predict the full response?"
  type: multiple-choice
  options:
    - "The transfer function only applies to nonlinear systems"
    - "G(s) assumes zero initial conditions, so it captures only the forced response; the free response from stored initial energy must be added separately"
    - "The Laplace transform cannot be applied to systems with initial velocity"
    - "G(s) requires the input to be a unit step function"
  answer: 1
  explanation: "The transfer function is derived by applying the Laplace transform and invoking zero initial conditions, which allows d^n y/dt^n to simplify to s^n Y(s) with no extra boundary terms. If initial conditions are non-zero, extra terms appear that break the clean G(s) = Y(s)/U(s) form. The transfer function describes forced response only; free response from initial energy must be computed separately and added."

- question: "What does the pole-zero structure of a transfer function G(s) tell you about a system's stability?"
  type: multiple-choice
  options:
    - "Stability is determined by the zeros of the numerator polynomial"
    - "A system is stable if and only if all zeros of G(s) lie in the left half of the s-plane"
    - "A system is stable if and only if all poles of G(s) lie in the left half of the s-plane"
    - "Stability requires that the number of poles equals the number of zeros"
  answer: 2
  explanation: "Poles — the roots of the denominator polynomial — determine the natural (unforced) behavior of a system. A pole at s = −a produces a decaying exponential e^{−at}; poles with positive real parts produce growing exponentials, i.e., instability. Stability requires all poles to be in the left half of the s-plane (negative real parts). Zeros affect how the system responds to particular inputs but do not determine stability."

- question: "The transfer function G(s) = Y(s)/U(s) fully describes the complete response of a system, including how it responds to stored initial energy."
  type: true-false
  answer: false
  explanation: "G(s) is derived under the assumption of zero initial conditions. It captures only the input-output (forced) response to an applied input U(s). If the system has stored energy at t=0 — such as initial velocity or initial capacitor charge — the resulting free response is not captured by G(s)·U(s). Complete response requires the forced and free contributions to be calculated and summed separately."

- question: "Cascading two LTI systems in series is equivalent to multiplying their individual transfer functions."
  type: true-false
  answer: true
  explanation: "One of the key advantages of transfer functions is that convolution in the time domain becomes multiplication in the s-domain. If Y(s) = G₁(s)·U(s) and Z(s) = G₂(s)·Y(s), then Z(s) = G₂(s)·G₁(s)·U(s) — the cascaded transfer function is simply the product. This algebraic property is why transfer functions make system design tractable: cascading, feedback, and parallel combinations all reduce to rational arithmetic."

- question: "Why must zero initial conditions be assumed when deriving a transfer function, and what physical interpretation does this assumption carry?"
  type: short-answer
  answer: "Zero initial conditions ensure that the Laplace transform of d^n y/dt^n reduces cleanly to s^n Y(s), with no boundary terms. Physically, this means the system starts with no stored energy — no initial voltage on a capacitor, no initial velocity of a mass. The transfer function then captures only the system's response to the applied input, not to pre-existing internal state. It characterizes the system itself (its poles, zeros, and gain) rather than a particular run of the system from a specific starting state."
  explanation: "If initial conditions were non-zero, the transformed equations would include extra terms that depend on the specific starting conditions, preventing formation of the clean Y(s)/U(s) ratio. The zero-initial-conditions assumption is therefore not a limitation of the technique but a deliberate choice to isolate the system's inherent input-output character — the same character regardless of how the system was set up before the input arrived."
```

## Explainer

Think about how a mechanical spring-mass-damper or an electrical RC circuit behaves: its governing physics is a differential equation connecting input forces (or voltages) to output positions (or currents). In the time domain that equation is hard to manipulate — differentiating and integrating compound in complicated ways. The Laplace transform is the escape hatch. It converts differentiation into multiplication by *s*, turning the differential equation into an algebraic equation you can solve with ordinary arithmetic.

The procedure is mechanical but worth internalizing step by step. Take any linear, constant-coefficient ODE describing a system, apply the Laplace transform term by term, and invoke zero initial conditions. The "zero initial conditions" assumption is what allows the Laplace transform of a derivative d^n y/dt^n to simplify cleanly to s^n Y(s) — no boundary terms survive. Rearrange to isolate Y(s) on one side and U(s) on the other. The ratio G(s) = Y(s)/U(s) is the **transfer function**: a compact algebraic expression encoding the system's complete input-output behavior.

From your LTI systems prerequisite you know that LTI systems are fully characterized by their impulse response h(t). The transfer function G(s) is precisely the Laplace transform of h(t). This means G(s) holds the same information as h(t) but in a domain where convolution in time becomes multiplication: Y(s) = G(s) · U(s). This algebraic product is why transfer functions are so powerful — cascading two systems just means multiplying their transfer functions, and feedback loops produce rational expressions rather than integral equations.

The structure of G(s) — a ratio of polynomials in *s* — reveals the system's character. The roots of the numerator polynomial are the **zeros** of the system; the roots of the denominator are the **poles**. Poles determine natural behavior: a pole at s = −a (negative real) produces exponential decay e^{−at} in the step response, while poles with imaginary parts produce oscillation. When all poles are in the left half of the s-plane (negative real parts), the system is stable. This pole-zero geometry, read directly from the transfer function, is the gateway to Bode plots, root locus, and frequency-domain design — all of which build directly on the representation you derive here.

A common stumbling point is forgetting that the transfer function assumes zero initial conditions. If a system starts with stored energy (non-zero initial capacitor voltage, non-zero initial velocity), the Laplace transform generates extra terms that break the clean G(s) = Y(s)/U(s) form. The transfer function describes how the system responds to *inputs*, not to initial conditions. For complete response with non-zero initial conditions, the two contributions — forced response via G(s)·U(s) and free response from initial conditions — must be added separately. In control design this is usually not a concern because we design around the steady-state input-output relationship, but it is worth understanding where the assumption lives.
