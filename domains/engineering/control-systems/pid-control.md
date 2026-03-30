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

## Questions

```yaml
- question: "A temperature controller uses only proportional control (Kp only, no I or D). After a step change in setpoint, the system settles. What behavior should you expect at steady state?"
  type: multiple-choice
  options:
    - "The output oscillates indefinitely around the setpoint at constant amplitude"
    - "The output reaches exactly the setpoint with zero steady-state error"
    - "The output stabilizes at a value slightly offset from the setpoint — a persistent steady-state error"
    - "The output overshoots and then drifts toward the setpoint over a very long time"
  answer: 2
  explanation: "P-only control almost always leaves a steady-state error. At steady state, the error is constant, so the proportional term produces a fixed control output. If the plant requires a nonzero input to maintain its output at setpoint, then error must remain nonzero to sustain that input. Only by increasing Kp can you reduce the error — but not eliminate it — and high Kp risks instability. The integral term is needed to drive steady-state error to zero."

- question: "A PID controller's actuator saturates at its maximum value during a large setpoint change. While saturated, the integral term keeps accumulating error. When the actuator finally comes out of saturation, what happens?"
  type: multiple-choice
  options:
    - "The controller instantly drives to the correct setpoint because all that accumulated error becomes useful"
    - "Integrator windup causes a large overshoot — the swollen integral drives the output well past the setpoint before it can be corrected"
    - "The proportional term compensates for the accumulated integral, preventing overshoot"
    - "The derivative term detects the rapid change and brakes effectively, preventing windup effects"
  answer: 1
  explanation: "Integrator windup occurs when the actuator is saturated and cannot respond to control commands, but the integral term continues summing error as if it could. When saturation ends, the controller has a massively inflated integral that drives the output far past the setpoint before the integral can be 'unwound.' Anti-windup schemes conditionally stop integrating during saturation to prevent this. This is one of the most important practical issues in real PID implementations."

- question: "Adding derivative action to a PID controller usually improves closed-loop performance by predicting future error and allowing earlier corrective action."
  type: true-false
  answer: false
  explanation: "Derivative action amplifies high-frequency noise — differentiation multiplies noise power proportionally to frequency squared. Pure derivative action is almost never implemented in practice; a filtered derivative (D term in series with a first-order low-pass filter) is standard. Furthermore, on plants with large time delays or noisy sensors, derivative action can degrade rather than improve performance. It is a useful tool when sensor noise is manageable, not a universally beneficial addition."

- question: "Integral action eliminates steady-state error because it is mathematically equivalent to adding a pole at the origin in the open-loop transfer function, making the closed-loop system Type 1."
  type: true-false
  answer: true
  explanation: "The integral of error ∫e(t)dt has a Laplace transform of E(s)/s — dividing by s is equivalent to adding a pole at s = 0 (the origin) in the open-loop transfer function. A Type 1 system (one pole at the origin) has zero steady-state error for a step input by the final value theorem. This is why integral action unconditionally eliminates steady-state error for constant setpoints — it is a structural property of the loop, not just an empirical tuning effect."

- question: "Why does proportional-only control almost always leave a steady-state error, and what does the integral term do — mechanically — to eliminate it?"
  type: short-answer
  answer: "P-only control requires nonzero error to generate nonzero control output. At steady state, the plant needs a fixed input to hold its output — so error must remain nonzero to produce that input. The integral term accumulates error over time: as long as any error persists, the integral grows, continuously increasing control effort. This continues until the error is driven to exactly zero, at which point the accumulated integral holds the control effort at the required steady-state level without needing any ongoing error signal."
  explanation: "The key insight is that the integral 'remembers' past errors — it can maintain a control output even when current error is zero, because the history of errors is encoded in its accumulated value. This is exactly what P-only control lacks: a mechanism to sustain control effort without sustained error."
```

## Explainer

You've studied steady-state error analysis, which tells you how much a feedback system misses its target in the long run, and second-order step response, which characterizes overshoot, damping, and settling. PID control is the standard tool for shaping both simultaneously. The acronym stands for **Proportional-Integral-Derivative**, and each term addresses a distinct aspect of control performance.

The **proportional term** K_p·e(t) is the most intuitive: apply control effort in direct proportion to the current error. If the output is far from the setpoint, apply a large corrective signal; if it's close, apply a small one. P control drives the system toward the target but almost always leaves a **steady-state error** — a persistent offset. This is because at steady state, error is constant (not growing), so the P term produces a fixed control output, which must balance the plant's steady-state input requirement. If the required control output is nonzero, error must be nonzero too. Increasing K_p reduces the error but increases the tendency toward oscillation and instability: the system becomes "jumpy" and eventually goes unstable at high enough gain.

The **integral term** K_i·∫e(t)dt accumulates past errors over time. As long as any error persists, the integral grows, increasing control effort until the error is driven to zero. This is why integral action **eliminates steady-state error** unconditionally — it is mathematically equivalent to adding a pole at the origin in the open-loop transfer function, making the closed-loop system Type 1. The cost of this guaranteed zero error is dynamic: the accumulated integral can overshoot the setpoint, causing ringing, and if the actuator saturates (reaches its physical limit), the integral keeps growing even though it can't do any work — **integrator windup**. Anti-windup schemes conditionally stop integrating when saturation is detected. The integral term is the essential addition when pure P control leaves unacceptable offset.

The **derivative term** K_d·de/dt reacts to the *rate of change* of error rather than its current value. If the error is decreasing rapidly (the system is heading toward the setpoint quickly), the derivative term applies a braking force to prevent overshoot. If error is increasing rapidly (the system is diverging), the derivative term adds a large corrective kick. Think of it as prediction: by looking at the slope of the error, the derivative term anticipates where the system is heading and acts ahead of time. The practical problem is that real sensor signals contain noise, and differentiation amplifies high-frequency noise dramatically. Pure derivative action is almost never implemented; instead, a filtered derivative is used — a derivative in series with a first-order low-pass filter — which gives the benefit of rate feedback while rejecting noise above a chosen frequency. Tuning methods like **Ziegler-Nichols** provide empirical starting points by measuring the plant's ultimate gain (the K_p at which sustained oscillation occurs) and the oscillation period, then computing K_p, K_i, K_d from those measurements. These starting points are rarely optimal but reduce the search space for manual refinement.


