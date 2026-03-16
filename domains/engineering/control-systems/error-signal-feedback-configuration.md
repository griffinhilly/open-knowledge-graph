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
stage: advanced
status: draft
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

## Explainer

From your study of open-loop versus closed-loop systems and transfer functions, you know that feedback means measuring the output and using that measurement to adjust the input. The bridge between those two ideas is the **error signal**: the difference between what you want (the **reference** or setpoint) and what you have (the actual output). The controller acts on this error, and the entire feedback architecture is organized around computing and responding to it.

In the standard **unity-feedback** block diagram, the error is E(s) = R(s) − Y(s). The controller C(s) receives E(s) and produces the control input U(s) = C(s)·E(s). The plant G(s) converts control input to output: Y(s) = G(s)·U(s). Substituting, the closed-loop transfer function is Y(s)/R(s) = G(s)C(s) / [1 + G(s)C(s)]. The denominator 1 + G(s)C(s) is the **characteristic polynomial** — its roots are the closed-loop poles, and they determine stability and transient response. Every performance and stability result in control theory flows from this one expression. Designing a controller is, at its core, choosing C(s) to place these poles in acceptable locations.

**Non-unity feedback** arises whenever the sensor measuring the output has its own dynamics or gain scaling H(s) ≠ 1. The error computation becomes E(s) = R(s) − H(s)·Y(s), and the closed-loop transfer function changes to G(s)C(s) / [1 + G(s)C(s)H(s)]. This seemingly small change has real consequences: the system now tracks R(s) scaled by H(s), not R(s) directly, and steady-state errors change accordingly. Unity feedback is a design choice that simplifies analysis, not a physical given — any time a sensor has gain or dynamics, you are implicitly working with non-unity feedback.

The topology of the feedback path also determines which disturbances the system can reject. A disturbance entering the loop *before* the plant — say, an external force on a robot arm or an input torque disturbance — is inside the feedback loop. The controller "sees" its effect through the output measurement and can counteract it. A disturbance entering *after* the plant — sensor noise, for instance — is outside the forward path and is not attenuated by loop gain; in fact, high loop gain can amplify sensor noise at the input. Understanding where each disturbance enters relative to the feedback path is essential for predicting what the system can and cannot reject, and for deciding whether feedforward augmentation is needed.
