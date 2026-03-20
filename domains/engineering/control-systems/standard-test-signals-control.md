---
id: standard-test-signals-control
title: Standard Test Signals and Input-Output Analysis
domain: engineering
course: control-systems
prerequisites:
- id: transfer-function-derivation-differential-equations
  type: hard
- id: laplace-transform-properties-inverse
  type: soft
builds-toward:
- impulse-response-and-convolution-control
- response-specifications-performance-metrics
- first-order-system-transient-response
tags:
- test-signals
- impulse
- step
- ramp
- input
stage: advanced
status: draft
---

# Standard Test Signals and Input-Output Analysis

## Core Idea
Standard test signals (impulse, step, ramp, parabolic, sinusoid) are used to characterize system response. The impulse response h(t) defines the system completely; step response shows tracking ability; ramp response reveals steady-state accuracy. These signals reveal different aspects of system performance.

## Explainer

To analyze a system you need a known input. Rather than testing with arbitrary real-world signals that are hard to reproduce or compare, control engineers use a small family of mathematically precise test signals. Each one probes a different aspect of system behavior, and together they build a complete picture of performance. You already know transfer functions — the test signal vocabulary is the natural companion: it is the set of inputs you plug into a transfer function to extract meaningful answers.

The five standard signals form a hierarchy related by integration. The **impulse** δ(t) is the most fundamental: an infinitely tall, infinitely narrow spike with unit area. Because a general input can be decomposed into a continuum of scaled, shifted impulses (this is what your prerequisites on convolution formalize), the **impulse response** h(t) completely characterizes a linear time-invariant system. Integrate the impulse and you get the **unit step** u(t), which tests how the system responds to a sudden sustained change — the most practically common disturbance. Integrate the step and you get the **ramp** r(t) = t·u(t), which tests whether the system can track a constantly changing reference. Integrate again and you get the **parabolic** signal, which probes the ability to track accelerating inputs. The **sinusoid** stands apart: it tests frequency-domain behavior, revealing how the system amplifies or attenuates signals at each frequency.

Why does this hierarchy matter? It directly connects to steady-state error. A system driven by a step must eventually match a constant reference; whether it does depends on the number of integrators in its open-loop transfer function (the **system type**). A type-0 system has a finite constant error to a step input. A type-1 system (with one integrator) eliminates step error but has finite error to a ramp. A type-2 system eliminates ramp error but still has finite error to a parabola. Choosing which test signal to use is really asking: "How ambitious is the tracking requirement for this application?"

In practice, the step response is the workhorse diagnostic. Apply a step and measure the rise time, overshoot, settling time, and steady-state error — these **time-domain performance specifications** are the most intuitive way to judge a controller. The impulse response is more theoretical but more powerful: in the Laplace domain it is simply H(s) = Y(s)/X(s) with X(s) = 1, so the impulse response is the inverse Laplace transform of the transfer function itself. This is why the impulse and step responses are linked: the step response is the integral of the impulse response, and you can differentiate a measured step response to estimate the impulse response. Together, these signals give you a practical diagnostic language for every stage of control system design.
