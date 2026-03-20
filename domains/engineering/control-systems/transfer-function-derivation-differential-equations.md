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

## Explainer

Think about how a mechanical spring-mass-damper or an electrical RC circuit behaves: its governing physics is a differential equation connecting input forces (or voltages) to output positions (or currents). In the time domain that equation is hard to manipulate — differentiating and integrating compound in complicated ways. The Laplace transform is the escape hatch. It converts differentiation into multiplication by *s*, turning the differential equation into an algebraic equation you can solve with ordinary arithmetic.

The procedure is mechanical but worth internalizing step by step. Take any linear, constant-coefficient ODE describing a system, apply the Laplace transform term by term, and invoke zero initial conditions. The "zero initial conditions" assumption is what allows the Laplace transform of a derivative d^n y/dt^n to simplify cleanly to s^n Y(s) — no boundary terms survive. Rearrange to isolate Y(s) on one side and U(s) on the other. The ratio G(s) = Y(s)/U(s) is the **transfer function**: a compact algebraic expression encoding the system's complete input-output behavior.

From your LTI systems prerequisite you know that LTI systems are fully characterized by their impulse response h(t). The transfer function G(s) is precisely the Laplace transform of h(t). This means G(s) holds the same information as h(t) but in a domain where convolution in time becomes multiplication: Y(s) = G(s) · U(s). This algebraic product is why transfer functions are so powerful — cascading two systems just means multiplying their transfer functions, and feedback loops produce rational expressions rather than integral equations.

The structure of G(s) — a ratio of polynomials in *s* — reveals the system's character. The roots of the numerator polynomial are the **zeros** of the system; the roots of the denominator are the **poles**. Poles determine natural behavior: a pole at s = −a (negative real) produces exponential decay e^{−at} in the step response, while poles with imaginary parts produce oscillation. When all poles are in the left half of the s-plane (negative real parts), the system is stable. This pole-zero geometry, read directly from the transfer function, is the gateway to Bode plots, root locus, and frequency-domain design — all of which build directly on the representation you derive here.

A common stumbling point is forgetting that the transfer function assumes zero initial conditions. If a system starts with stored energy (non-zero initial capacitor voltage, non-zero initial velocity), the Laplace transform generates extra terms that break the clean G(s) = Y(s)/U(s) form. The transfer function describes how the system responds to *inputs*, not to initial conditions. For complete response with non-zero initial conditions, the two contributions — forced response via G(s)·U(s) and free response from initial conditions — must be added separately. In control design this is usually not a concern because we design around the steady-state input-output relationship, but it is worth understanding where the assumption lives.
