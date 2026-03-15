---
id: feedback-control-fundamentals
title: Feedback Control Fundamentals
domain: engineering
course: control-systems
prerequisites:
- id: differential-equations-intro-separable
  type: hard
- id: first-order-transient-circuits
  type: soft
- id: second-order-transient-circuits
  type: soft
- id: differential-equations-intro
  type: soft
builds-toward:
- laplace-transform-control
- transfer-functions-control
tags:
- feedback
- closed-loop
- open-loop
- control
- error-signal
stage: advanced
status: validated
---

# Feedback Control Fundamentals

## Core Idea
Feedback control uses the difference between a desired output (setpoint) and the actual output (error signal) to drive a system toward its goal. Open-loop systems apply input without measuring output, while closed-loop systems continuously correct based on feedback. The block diagram of a closed-loop system includes the plant (process being controlled), the controller, sensors, and the feedback path. Key performance goals include stability, accuracy, and speed of response.

## How It's Best Learned
Start by analyzing simple thermostats or cruise control systems as physical intuitions for feedback before formalizing with math. Draw block diagrams of everyday control systems and compare open-loop vs. closed-loop responses to understand why feedback matters.

## Common Misconceptions
- More feedback gain is not always better — too much gain causes oscillation or instability.
- Open-loop control is not always inferior; it is appropriate when the plant is well-characterized and disturbances are minimal.
- The 'negative' in negative feedback refers to the subtraction operation at the summing junction, not a negative system outcome.
