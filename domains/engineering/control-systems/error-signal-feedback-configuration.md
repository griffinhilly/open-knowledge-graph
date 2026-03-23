---
id: error-signal-feedback-configuration
title: Error Signal and Feedback Topology
domain: engineering
course: control-systems
prerequisites:
- id: open-loop-vs-closed-loop-fundamentals
  type: hard
- id: transfer-functions-control
  type: hard
builds-toward:
- steady-state-error-system-type
- disturbance-rejection-and-feedforward
tags:
- feedback
- error
- topology
- architecture
stage: expert
status: validated
---

# Error Signal and Feedback Topology

## Core Idea
The error signal is the difference between desired reference and actual output, which drives the controller. Feedback topology determines how signals flow and combine: unity feedback, non-unity feedback, and cascaded loops each affect steady-state error and stability differently. Proper configuration of the feedback path is critical because the error computation and loop structure determines what disturbances the system can reject.

## How It's Best Learned
Draw block diagrams and trace signal paths. Derive transfer functions for different feedback topologies (unity feedback vs sensor with gain) and compare their steady-state errors to step inputs.

## Common Misconceptions
- The error is always measured directly; sensor dynamics and non-unity feedback complicate error computation.
- More negative feedback always improves performance; excessive feedback gain causes instability and noise amplification.
- Feedback configuration doesn't affect which disturbances can be rejected; disturbance location relative to feedback path is critical.

## Questions

```yaml
- question: "A control system uses a sensor with gain H = 0.5 (non-unity feedback) to measure a temperature output. The reference is set to R = 200°C. After the loop reaches steady state with zero error signal (E → 0), what is the actual temperature output?"
  type: multiple-choice
  options:
    - "200°C — the system tracks the reference exactly in all well-designed closed-loop systems"
    - "100°C — because with H = 0.5, the sensor reads half the actual temperature, so the system drives the actual output to 400°C to make the sensor reading match R"
    - "400°C — the non-unity feedback gain scales up the actual temperature, so E = R − H·Y → 0 means Y = R/H = 400°C"
    - "100°C — the sensor attenuates the signal, so the controller only corrects half the error and settles at 100°C"
  answer: 2
  explanation: "In non-unity feedback, the error is E = R − H·Y. At steady state, E → 0, so H·Y = R, meaning Y = R/H = 200/0.5 = 400°C. The controller drives the loop until the *sensed* output H·Y matches R — it has no way to distinguish between R and H·Y independently. This is why non-unity feedback changes steady-state behavior: the system tracks R/H, not R. Option A (200°C) assumes unity feedback. Understanding this prevents errors when designing systems with sensors that have their own gain."

- question: "Two disturbances affect a feedback control system: D₁ enters at the plant input (before the plant, inside the feedback loop), and D₂ enters at the plant output (after the plant, outside the forward path). Which disturbance can the feedback controller attenuate, and why?"
  type: multiple-choice
  options:
    - "D₂ only — output disturbances are directly subtracted from the reference in the error computation"
    - "Both D₁ and D₂ equally — feedback attenuates all disturbances regardless of where they enter"
    - "D₁ only — it enters inside the feedback loop, so its effect propagates to the output and is measured; the controller corrects for it. D₂ enters after the measurement point and is not visible to the controller"
    - "Neither — disturbance rejection requires separate feedforward controllers in both cases"
  answer: 2
  explanation: "A disturbance that enters *inside* the feedback loop (before or within the forward path) affects the output, which the sensor measures. The controller sees the deviation from reference and generates corrective action. A disturbance at the output (after the plant, outside the loop) adds directly to the measured signal but bypasses the correction path — the controller sees the disturbed output but cannot distinguish disturbance from true output. Worse, high feedback gain amplifies output-side disturbances like sensor noise. The topology of where disturbances enter relative to the measurement point is critical to predicting what can be rejected."

- question: "Increasing feedback gain always improves both tracking accuracy and system stability simultaneously."
  type: true-false
  answer: false
  explanation: "This is a common misconception. While higher loop gain generally reduces steady-state error (improving tracking), it simultaneously reduces phase margin and can push closed-loop poles into the right half-plane, causing instability. Additionally, high gain amplifies sensor noise at the plant input. There is a fundamental tradeoff in feedback design: performance (tight tracking, fast disturbance rejection) versus robustness (stability margins). Every practical controller design must balance these — unlimited gain is not the answer."

- question: "In non-unity feedback, the error signal is computed as the difference between the reference R(s) and the sensed output H(s)·Y(s), not the actual plant output Y(s) directly."
  type: true-false
  answer: true
  explanation: "This is the definition of non-unity feedback. The summing junction computes E(s) = R(s) − H(s)·Y(s), where H(s) represents the sensor or feedback element dynamics. In unity feedback (H = 1), E = R − Y and the error directly reflects the tracking error. In non-unity feedback, the controller sees and responds to the *sensor's* representation of the output, which may differ from the true output in gain and phase. This affects both steady-state values and the closed-loop transfer function."

- question: "Why does the location of a disturbance — before versus after the plant — determine whether the feedback controller can reject it?"
  type: short-answer
  answer: "Feedback works by measuring the output, comparing it to the reference, and generating a corrective signal. A disturbance entering *before* the plant (at the plant input) passes through the plant before reaching the output sensor. The sensor detects the resulting deviation from the reference, the controller generates a corrective input, and the loop works to cancel the disturbance's effect. A disturbance entering *after* the plant — or equivalently, corrupting the sensor measurement — is already past the point where the controller can introduce a physical correction. The controller cannot distinguish it from a legitimate output change, so it responds by driving the plant harder, which can amplify the disturbance rather than cancel it."
  explanation: "This is why sensor noise is treated differently from input disturbances in control design. Sensor noise is an output-side disturbance: high loop gain makes the controller respond aggressively to noise, injecting large control signals for small measurement errors. Input disturbances (wind gusts on a drone, load changes on a motor) can be attenuated by the loop. Feedforward control is often added to handle disturbances that enter outside the feedback path and are known or measurable ahead of time."
```

## Explainer

From your study of open-loop versus closed-loop systems and transfer functions, you know that feedback means measuring the output and using that measurement to adjust the input. The bridge between those two ideas is the **error signal**: the difference between what you want (the **reference** or setpoint) and what you have (the actual output). The controller acts on this error, and the entire feedback architecture is organized around computing and responding to it.

In the standard **unity-feedback** block diagram, the error is E(s) = R(s) − Y(s). The controller C(s) receives E(s) and produces the control input U(s) = C(s)·E(s). The plant G(s) converts control input to output: Y(s) = G(s)·U(s). Substituting, the closed-loop transfer function is Y(s)/R(s) = G(s)C(s) / [1 + G(s)C(s)]. The denominator 1 + G(s)C(s) is the **characteristic polynomial** — its roots are the closed-loop poles, and they determine stability and transient response. Every performance and stability result in control theory flows from this one expression. Designing a controller is, at its core, choosing C(s) to place these poles in acceptable locations.

**Non-unity feedback** arises whenever the sensor measuring the output has its own dynamics or gain scaling H(s) ≠ 1. The error computation becomes E(s) = R(s) − H(s)·Y(s), and the closed-loop transfer function changes to G(s)C(s) / [1 + G(s)C(s)H(s)]. This seemingly small change has real consequences: the system now tracks R(s) scaled by H(s), not R(s) directly, and steady-state errors change accordingly. Unity feedback is a design choice that simplifies analysis, not a physical given — any time a sensor has gain or dynamics, you are implicitly working with non-unity feedback.

The topology of the feedback path also determines which disturbances the system can reject. A disturbance entering the loop *before* the plant — say, an external force on a robot arm or an input torque disturbance — is inside the feedback loop. The controller "sees" its effect through the output measurement and can counteract it. A disturbance entering *after* the plant — sensor noise, for instance — is outside the forward path and is not attenuated by loop gain; in fact, high loop gain can amplify sensor noise at the input. Understanding where each disturbance enters relative to the feedback path is essential for predicting what the system can and cannot reject, and for deciding whether feedforward augmentation is needed.
