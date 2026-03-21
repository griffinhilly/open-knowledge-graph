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

## Questions

```yaml
- question: "A control engineer applies a unit step to a system and observes a non-zero steady-state error. She concludes the system will perform adequately for ramp-input tracking. What is the flaw in her reasoning?"
  type: multiple-choice
  options:
    - "Step response cannot reveal steady-state error — only the frequency response can"
    - "A non-zero steady-state error to a step indicates a type-0 system, which will have infinite steady-state error to a ramp input"
    - "Ramp and step tracking performance are independent — non-zero step error says nothing about ramp performance"
    - "Steady-state error to a step is always zero for any stable closed-loop system"
  answer: 1
  explanation: "System type determines which inputs can be tracked with zero steady-state error. A type-0 system (no open-loop integrators) has finite, non-zero error to a step — and infinite error to a ramp, meaning the output falls further and further behind a linearly increasing reference. Non-zero step error immediately disqualifies the system from ramp tracking. The test signals form a hierarchy of increasing tracking ambition: passing the step test is a prerequisite for even attempting ramp tracking."

- question: "A type-1 system (with one integrator in the open-loop transfer function) is driven by a unit step input. The steady-state error is:"
  type: multiple-choice
  options:
    - "Infinite, because integrators cause output runaway under constant inputs"
    - "Equal to 1, since the unit step has amplitude 1 by definition"
    - "Zero, because the integrator ensures the output eventually matches any constant reference"
    - "Non-zero and finite, equal to 1/(1 + Kp) where Kp is the position constant"
  answer: 2
  explanation: "A type-1 system contains one integrator in its open-loop transfer function. The integrator continuously adjusts its output until the error driving it reaches zero — for a constant (step) input, this means the steady-state error is driven to zero. Answer D describes a type-0 system (with no integrator). The position constant Kp → ∞ for a type-1 system, giving e_ss = 1/(1 + ∞) = 0. However, a type-1 system still has finite error to a ramp, and infinite error to a parabolic input."

- question: "The impulse response h(t) completely characterizes a linear time-invariant system because any input signal can be expressed as a sum of scaled, shifted impulses, and superposition applies."
  type: true-false
  answer: true
  explanation: "This is the mathematical foundation for convolution. An arbitrary input x(t) can be written as an integral of shifted, weighted impulses (by the sifting property of the delta function). Since the system is linear and time-invariant, the response to each shifted impulse is a shifted, scaled copy of h(t). The total output is the convolution y(t) = x(t) * h(t). Knowing h(t) is sufficient to compute the output to any input — the impulse response is a complete description of the system's input-output behavior."

- question: "The step response and impulse response of a system contain independent information — neither can be derived from the other."
  type: true-false
  answer: false
  explanation: "The step response is the integral of the impulse response, and equivalently, the impulse response is the derivative of the step response. This relationship follows directly from the fact that the unit step is the integral of the unit impulse. In the Laplace domain, the step response is H(s)/s (the transfer function divided by s, since the step's transform is 1/s) while the impulse response is simply H(s). Both encode identical information; the choice between them is practical — the step is easier to apply experimentally, while the impulse is theoretically cleaner."

- question: "Why does choosing which standard test signal to apply to a system amount to specifying the ambition of the tracking requirement?"
  type: short-answer
  answer: "The standard signals form a hierarchy related by integration: impulse → step → ramp → parabolic. Each represents a more demanding tracking task, and whether a system can track with zero steady-state error depends on its type (the number of open-loop integrators). A type-0 system eliminates error only for an impulse (trivially) and has finite error to a step. A type-1 system eliminates step error but has finite error to a ramp. A type-2 system eliminates ramp error but still fails for a parabolic input. When choosing which signal to test with, the engineer is asking: 'How demanding is the intended application?' A servomotor tracking a constantly moving target needs ramp-tracking capability (type-1 minimum). A thermostat holding a fixed setpoint only needs step-tracking (type-0 sufficient). The test signal defines which performance dimension to interrogate."
  explanation: "This connection between test signals and system type is what makes the signal hierarchy practically useful rather than just mathematically convenient. It gives engineers a principled language for specifying requirements — not 'the system should work well' but 'the system must track a ramp with zero steady-state error,' which immediately translates to a structural requirement on the open-loop transfer function."
```

## Explainer

To analyze a system you need a known input. Rather than testing with arbitrary real-world signals that are hard to reproduce or compare, control engineers use a small family of mathematically precise test signals. Each one probes a different aspect of system behavior, and together they build a complete picture of performance. You already know transfer functions — the test signal vocabulary is the natural companion: it is the set of inputs you plug into a transfer function to extract meaningful answers.

The five standard signals form a hierarchy related by integration. The **impulse** δ(t) is the most fundamental: an infinitely tall, infinitely narrow spike with unit area. Because a general input can be decomposed into a continuum of scaled, shifted impulses (this is what your prerequisites on convolution formalize), the **impulse response** h(t) completely characterizes a linear time-invariant system. Integrate the impulse and you get the **unit step** u(t), which tests how the system responds to a sudden sustained change — the most practically common disturbance. Integrate the step and you get the **ramp** r(t) = t·u(t), which tests whether the system can track a constantly changing reference. Integrate again and you get the **parabolic** signal, which probes the ability to track accelerating inputs. The **sinusoid** stands apart: it tests frequency-domain behavior, revealing how the system amplifies or attenuates signals at each frequency.

Why does this hierarchy matter? It directly connects to steady-state error. A system driven by a step must eventually match a constant reference; whether it does depends on the number of integrators in its open-loop transfer function (the **system type**). A type-0 system has a finite constant error to a step input. A type-1 system (with one integrator) eliminates step error but has finite error to a ramp. A type-2 system eliminates ramp error but still has finite error to a parabola. Choosing which test signal to use is really asking: "How ambitious is the tracking requirement for this application?"

In practice, the step response is the workhorse diagnostic. Apply a step and measure the rise time, overshoot, settling time, and steady-state error — these **time-domain performance specifications** are the most intuitive way to judge a controller. The impulse response is more theoretical but more powerful: in the Laplace domain it is simply H(s) = Y(s)/X(s) with X(s) = 1, so the impulse response is the inverse Laplace transform of the transfer function itself. This is why the impulse and step responses are linked: the step response is the integral of the impulse response, and you can differentiate a measured step response to estimate the impulse response. Together, these signals give you a practical diagnostic language for every stage of control system design.
