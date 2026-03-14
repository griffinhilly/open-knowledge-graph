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
