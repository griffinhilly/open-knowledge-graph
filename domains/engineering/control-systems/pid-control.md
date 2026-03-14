---
id: pid-control
title: PID Controllers
domain: engineering
course: control-systems
prerequisites:
- id: steady-state-error-analysis
  type: hard
- id: time-domain-response-second-order
  type: hard
- id: gain-and-phase-margins
  type: soft
builds-toward:
- lead-lag-compensators
tags:
- pid
- proportional
- integral
- derivative
- tuning
- ziegler-nichols
stage: advanced
status: validated
---

# PID Controllers

## Core Idea
A PID controller computes control output as u(t) = Kp·e(t) + Ki·∫e(t)dt + Kd·de/dt, where e(t) is the error between setpoint and measured output. Proportional action provides immediate response proportional to current error; integral action eliminates steady-state error by accumulating past errors (adding a pole at the origin, making the system Type 1); derivative action provides damping by reacting to the rate of error change. PID controllers are the dominant control structure in industrial practice, governing temperature regulators, robotic joints, and process control loops. Tuning methods include Ziegler-Nichols ultimate gain method, Cohen-Coon, and model-based IMC tuning.

## How It's Best Learned
Implement a PID controller in simulation on a second-order plant and manually tune Kp, Ki, Kd while observing step responses. Use Ziegler-Nichols as a starting point and refine iteratively, observing how each term affects the response independently before combining them.

## Common Misconceptions
- Adding integral action always eliminates steady-state error but can cause integrator windup during actuator saturation — anti-windup measures are essential in practical implementations.
- Derivative action amplifies high-frequency noise; the practical implementation uses a filtered derivative (D term with first-order low-pass filter), not pure differentiation.
- PID may not be suitable for plants with large time delays or non-minimum-phase behavior — model-based controllers or Smith predictors are preferred in such cases.
