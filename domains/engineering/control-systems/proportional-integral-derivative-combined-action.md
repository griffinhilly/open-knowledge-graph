---
id: proportional-integral-derivative-combined-action
title: 'Proportional-Integral-Derivative Control: Combined Action'
domain: engineering
course: control-systems
prerequisites:
- id: pid-control
  type: hard
- id: internal-model-principle-integral-action
  type: soft
builds-toward:
- process-model-identification-relay-autotuning
tags:
- pid-controller
- proportional-action
- integral-action
- derivative-action
- tuning
stage: expert
status: validated
---
# Proportional-Integral-Derivative Control: Combined Action

## Core Idea
PID control law u(t) = Kₚ e(t) + Kᵢ ∫e(τ)dτ + Kd de/dt combines three actions: proportional provides immediate response; integral eliminates steady-state error but can destabilize; derivative improves stability and damping by responding to error rate.

## Questions

```yaml
- question: "A temperature controller uses only proportional control (P-only) with gain Kₚ. The system reaches steady state with a constant 3°C error (offset) below the setpoint. What is the most direct way to eliminate this offset without changing Kₚ?"
  type: multiple-choice
  options:
    - "Increase the setpoint by 3°C to compensate for the expected offset"
    - "Add integral action, which accumulates the error over time until the output eliminates it"
    - "Add derivative action, which detects the persistent error and adds corrective force"
    - "Double Kₚ, which will halve the offset and eventually reduce it to zero"
  answer: 1
  explanation: "Pure proportional control requires a nonzero error to produce any output — it can only apply corrective force proportional to what error currently exists. A constant load disturbance requires a constant corrective force, and the only way P-only control generates that force is by maintaining a nonzero steady-state error (offset). Increasing Kₚ reduces the offset but cannot eliminate it without becoming infinite. Integral action solves this by accumulating the error: even a tiny persistent offset causes the integral term to grow until the output increases enough to eliminate the error entirely. Derivative action responds to the rate of error change, not accumulated error, so it cannot eliminate steady-state offset."

- question: "During a large setpoint step in a PID-controlled process, the actuator fully saturates at its maximum position for an extended period. What is the likely consequence if no anti-windup scheme is implemented?"
  type: multiple-choice
  options:
    - "The derivative term will saturate and become zero, leaving only P+I control active"
    - "The integral term keeps accumulating error even though the actuator cannot respond, causing a large overshoot when the actuator finally desaturates"
    - "The proportional term will dominate and the loop will become oscillatory at its natural frequency"
    - "The controller will switch to pure proportional control until saturation ends"
  answer: 1
  explanation: "Integrator windup occurs when the actuator is saturated and cannot produce additional output, but the integral term keeps accumulating error as if it could. When the process variable finally approaches the setpoint and the actuator desaturates, the integral has accumulated a large value that continues to drive the actuator in the same direction, causing significant overshoot. Anti-windup schemes — such as clamping the integral when saturation is detected — prevent this by stopping or unwinding the integral accumulation during saturation."

- question: "Derivative action in a PID controller contributes phase lead to the open-loop transfer function, which improves phase margin and damps oscillatory responses."
  type: true-false
  answer: true
  explanation: "A derivative term contributes phase lead in the frequency domain, counteracting the phase lag introduced by the plant and other loop elements. This improves phase margin and moves the closed-loop poles away from the imaginary axis. In the time domain, derivative action provides 'anticipatory braking' — if the error is large but shrinking rapidly, the derivative term reduces the control effort before the error reaches zero, preventing overshoot and damping oscillations. This is why derivative action is sometimes called 'rate action' or 'anticipatory control.'"

- question: "Increasing the integral gain Kᵢ generally improves control performance by eliminating steady-state error faster."
  type: true-false
  answer: false
  explanation: "Integral action adds a pole at the origin in the open-loop transfer function, which introduces phase lag. Increasing Kᵢ increases the integral action's contribution across frequencies, adding more phase lag and reducing phase margin. At some point, the reduced phase margin destabilizes the loop, causing oscillation or even instability. There is an optimal range for Kᵢ: enough to eliminate steady-state error at an acceptable rate without destabilizing the loop. Large Kᵢ also increases susceptibility to integrator windup during actuator saturation. Faster error elimination is not always better — Kᵢ must be tuned against process dynamics."

- question: "Explain why pure proportional control cannot eliminate steady-state error in the presence of a constant load disturbance, even with very high proportional gain."
  type: short-answer
  answer: "Pure proportional control generates output u(t) = Kₚ·e(t). For the controller to produce any output at all, there must be a nonzero error e(t). A constant load disturbance requires a constant nonzero control output to counteract it. Therefore, the proportional controller must maintain a constant nonzero error at steady state — this residual error (offset) is what sustains the corrective force. Increasing Kₚ makes the required offset smaller (the same corrective force is generated by a smaller error), but offset can never be zero unless Kₚ is infinite, which would destabilize the loop. Eliminating offset requires integral action, which accumulates past error and can provide the needed constant force even as current error approaches zero."
  explanation: "A proportional controller lacks memory — it only knows the current error, not what it has been. To generate a sustained output, it needs a sustained input (error). An integrator, by contrast, accumulates past error and can maintain a nonzero output even when current error is zero. This is why the integrator is called 'reset action': it resets the steady-state operating point until offset is eliminated."
```

## Explainer

From your study of PID control, you know each of the three actions individually. The challenge now is understanding how they interact when combined — why each action is insufficient on its own, what each contributes to the combined controller, and how the interplay between them creates the tuning tradeoffs that define PID design in practice.

**Proportional action** alone is direct and intuitive: apply a correction proportional to the current error. The larger the error, the harder the controller pushes. But pure proportional control has a fundamental limitation: for it to produce any output at all, there must be a nonzero error. In a system with constant load disturbances, the controller must maintain a nonzero error (called **steady-state error** or **offset**) to produce the constant corrective force needed to counteract the disturbance. Increasing K_p reduces the offset but doesn't eliminate it — and large K_p tends to make the system oscillatory, since a high-gain loop amplifies disturbances and can overshoot.

**Integral action** solves the offset problem by accumulating error over time. If any steady-state error persists — even a tiny one — the integral term grows without bound until the controller output increases enough to eliminate it. Mathematically, the integrator adds a pole at the origin in the open-loop transfer function, which guarantees zero steady-state error to constant inputs. The cost: the integrator adds phase lag, which reduces phase margin and can cause **integrator windup** when the actuator saturates (the integral keeps growing even when nothing can be done, leading to large overshoots when the saturation clears). Anti-windup schemes are essential in real implementations for exactly this reason.

**Derivative action** addresses the dynamic problem: P and I controllers only react to error that has already accumulated. The derivative term looks at *how fast* the error is changing — if the error is large but rapidly decreasing (meaning the system is already heading toward the setpoint), derivative action reduces the control effort to prevent overshoot. Think of it as anticipatory braking: you don't maintain full braking force until you've already stopped; you ease off as you approach the target. Derivative action improves phase margin (it contributes phase lead) and damps oscillations. The downside: derivatives amplify high-frequency noise, since small rapid fluctuations in the measured variable produce large derivative spikes. This is why practical derivative implementations include a low-pass filter, and why derivative action is often omitted for noisy measurements.

The combined PID controller is a tool whose three gains K_p, K_i, K_d interact: increasing K_p speeds response but risks oscillation; K_i eliminates steady-state error but reduces phase margin; K_d adds damping but amplifies noise. Tuning PID is the art of finding the combination that meets speed, stability, and disturbance-rejection requirements simultaneously. Systematic methods — Ziegler-Nichols, relay autotuning — provide starting-point recipes, but all ultimately require iteration against the real plant.
