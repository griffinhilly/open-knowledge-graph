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

## Explainer

You've studied steady-state error analysis, which tells you how much a feedback system misses its target in the long run, and second-order step response, which characterizes overshoot, damping, and settling. PID control is the standard tool for shaping both simultaneously. The acronym stands for **Proportional-Integral-Derivative**, and each term addresses a distinct aspect of control performance.

The **proportional term** K_p·e(t) is the most intuitive: apply control effort in direct proportion to the current error. If the output is far from the setpoint, apply a large corrective signal; if it's close, apply a small one. P control drives the system toward the target but almost always leaves a **steady-state error** — a persistent offset. This is because at steady state, error is constant (not growing), so the P term produces a fixed control output, which must balance the plant's steady-state input requirement. If the required control output is nonzero, error must be nonzero too. Increasing K_p reduces the error but increases the tendency toward oscillation and instability: the system becomes "jumpy" and eventually goes unstable at high enough gain.

The **integral term** K_i·∫e(t)dt accumulates past errors over time. As long as any error persists, the integral grows, increasing control effort until the error is driven to zero. This is why integral action **eliminates steady-state error** unconditionally — it is mathematically equivalent to adding a pole at the origin in the open-loop transfer function, making the closed-loop system Type 1. The cost of this guaranteed zero error is dynamic: the accumulated integral can overshoot the setpoint, causing ringing, and if the actuator saturates (reaches its physical limit), the integral keeps growing even though it can't do any work — **integrator windup**. Anti-windup schemes conditionally stop integrating when saturation is detected. The integral term is the essential addition when pure P control leaves unacceptable offset.

The **derivative term** K_d·de/dt reacts to the *rate of change* of error rather than its current value. If the error is decreasing rapidly (the system is heading toward the setpoint quickly), the derivative term applies a braking force to prevent overshoot. If error is increasing rapidly (the system is diverging), the derivative term adds a large corrective kick. Think of it as prediction: by looking at the slope of the error, the derivative term anticipates where the system is heading and acts ahead of time. The practical problem is that real sensor signals contain noise, and differentiation amplifies high-frequency noise dramatically. Pure derivative action is almost never implemented; instead, a filtered derivative is used — a derivative in series with a first-order low-pass filter — which gives the benefit of rate feedback while rejecting noise above a chosen frequency. Tuning methods like **Ziegler-Nichols** provide empirical starting points by measuring the plant's ultimate gain (the K_p at which sustained oscillation occurs) and the oscillation period, then computing K_p, K_i, K_d from those measurements. These starting points are rarely optimal but reduce the search space for manual refinement.


