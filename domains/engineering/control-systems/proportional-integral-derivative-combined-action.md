---
id: proportional-integral-derivative-combined-action
title: 'Proportional-Integral-Derivative Control: Combined Action'
domain: engineering
course: control-systems
prerequisites:
- id: pid-control
  type: hard
builds-toward:
- process-model-identification-relay-autotuning
tags:
- pid-controller
- proportional-action
- integral-action
- derivative-action
- tuning
stage: advanced
status: draft
---

# Proportional-Integral-Derivative Control: Combined Action

## Core Idea
PID control law u(t) = Kₚ e(t) + Kᵢ ∫e(τ)dτ + Kd de/dt combines three actions: proportional provides immediate response; integral eliminates steady-state error but can destabilize; derivative improves stability and damping by responding to error rate.

## Explainer

From your study of PID control, you know each of the three actions individually. The challenge now is understanding how they interact when combined — why each action is insufficient on its own, what each contributes to the combined controller, and how the interplay between them creates the tuning tradeoffs that define PID design in practice.

**Proportional action** alone is direct and intuitive: apply a correction proportional to the current error. The larger the error, the harder the controller pushes. But pure proportional control has a fundamental limitation: for it to produce any output at all, there must be a nonzero error. In a system with constant load disturbances, the controller must maintain a nonzero error (called **steady-state error** or **offset**) to produce the constant corrective force needed to counteract the disturbance. Increasing K_p reduces the offset but doesn't eliminate it — and large K_p tends to make the system oscillatory, since a high-gain loop amplifies disturbances and can overshoot.

**Integral action** solves the offset problem by accumulating error over time. If any steady-state error persists — even a tiny one — the integral term grows without bound until the controller output increases enough to eliminate it. Mathematically, the integrator adds a pole at the origin in the open-loop transfer function, which guarantees zero steady-state error to constant inputs. The cost: the integrator adds phase lag, which reduces phase margin and can cause **integrator windup** when the actuator saturates (the integral keeps growing even when nothing can be done, leading to large overshoots when the saturation clears). Anti-windup schemes are essential in real implementations for exactly this reason.

**Derivative action** addresses the dynamic problem: P and I controllers only react to error that has already accumulated. The derivative term looks at *how fast* the error is changing — if the error is large but rapidly decreasing (meaning the system is already heading toward the setpoint), derivative action reduces the control effort to prevent overshoot. Think of it as anticipatory braking: you don't maintain full braking force until you've already stopped; you ease off as you approach the target. Derivative action improves phase margin (it contributes phase lead) and damps oscillations. The downside: derivatives amplify high-frequency noise, since small rapid fluctuations in the measured variable produce large derivative spikes. This is why practical derivative implementations include a low-pass filter, and why derivative action is often omitted for noisy measurements.

The combined PID controller is a tool whose three gains K_p, K_i, K_d interact: increasing K_p speeds response but risks oscillation; K_i eliminates steady-state error but reduces phase margin; K_d adds damping but amplifies noise. Tuning PID is the art of finding the combination that meets speed, stability, and disturbance-rejection requirements simultaneously. Systematic methods — Ziegler-Nichols, relay autotuning — provide starting-point recipes, but all ultimately require iteration against the real plant.
