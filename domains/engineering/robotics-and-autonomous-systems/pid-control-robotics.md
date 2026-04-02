---
id: pid-control-robotics
title: PID Control for Robot Actuators
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: feedback-control-fundamentals
  type: hard
- id: trajectory-planning
  type: soft
builds-toward:
- dynamics-robot-manipulators
- actuators-and-sensors-robotics
tags:
- pid-control
- proportional
- integral
- derivative
- servo-control
- joint-control
stage: advanced
status: validated
---

# PID Control for Robot Actuators

## Core Idea
Each joint of a robot arm is controlled independently using a PID (Proportional-Integral-Derivative) controller that drives the actual joint angle toward a desired angle (the trajectory setpoint). The proportional term responds to current error, the integral term accumulates persistent error, and the derivative term anticipates future error. Proper tuning of the three gains (K_p, K_i, K_d) ensures fast, stable response without overshoot or oscillation. Anti-windup logic prevents integrator saturation during large transients.

## How It's Best Learned
Implement a simple PID controller in simulation for one joint of a robot. Start with K_i = K_d = 0 (proportional-only), observe steady-state error. Add integral gain K_i to eliminate steady-state error. Add derivative gain K_d to reduce overshoot and stabilize the response. Use a step input (sudden joint angle setpoint change) and observe the step response. Experiment with tuning methods like Ziegler-Nichols to find good starting gains. Move to real hardware if available and retune based on actual response.

## Common Misconceptions
- A PID controller with larger gains is always better (gives faster response); excessively large gains cause overshoot, oscillation, and instability.
- PID tuning is a one-time task; in practice, tuning changes with operating point, load, and wear—real systems require regular re-tuning.
- Derivative action always improves stability; in noisy systems, derivative action amplifies measurement noise and can cause control jitter.
- If a joint doesn't reach its setpoint with tuned PID, you must increase proportional gain; the issue may actually be integral saturation or command saturation.

## Questions

```yaml
- question: "A PID-controlled robot joint with well-tuned gains (K_p = 10, K_i = 0.5, K_d = 1) reaches its setpoint accurately for small setpoint changes but oscillates severely and overshoots for large step changes. The most likely cause is:"
  type: multiple-choice
  options:
    - "The proportional gain K_p is too high"
    - "The derivative gain K_d is not large enough to damp the oscillation"
    - "The actuator saturates during large transients, causing integrator windup that keeps the joint overshooting even after reaching the setpoint"
    - "The control loop frequency is too low to handle large transients"
  answer: 2
  explanation: "Ziegler-Nichols is valuable because it relates the tuning gains to the plant's actual behavior (its critical frequency and gain), not arbitrary parameters. The resulting PID controller is typically slightly underdamped (some overshoot) but stable, providing a good baseline for manual fine-tuning. Variations like Ziegler-Nichols for no overshoot (K_p = 0.2·K_u) or quarter-amplitude damping (K_p = 0.45·K_u) offer different trade-offs between speed and overshoot."
```

## Explainer

A robot arm's motion, commanded by a trajectory planner, must be executed by physical actuators (motors, hydraulic cylinders). The difference between the desired joint angle (from the trajectory) and the actual measured joint angle (from encoders or potentiometers) is the error. A control system must continuously adjust the actuator's command (torque or voltage) to drive this error to zero. This is the job of the PID controller.

The **proportional (P) term** is the simplest: τ_p = K_p · (θ_d - θ). The control output is proportional to the current error. Large error produces large control effort; small error produces small effort. However, proportional control alone cannot eliminate steady-state error. If there is a small persistent error, proportional action outputs a steady (but small) correction that exactly balances the error. The system settles with nonzero error.

The **integral (I) term** accumulates error over time: τ_i = K_i · ∫(θ_d - θ) dt. As long as error persists, the integral grows, and the control output increases. At steady state with constant error, the integral term builds up until it outputs just enough correction to cancel the error, bringing steady-state error to zero. This is why integrator action is essential for accurate control. However, the integrator has a drawback: during large transients (e.g., a large setpoint step), the integral accumulates so much that the control signal saturates (hits the actuator's maximum), yet the integrator keeps growing. This is **integrator windup**: after the setpoint is reached, the integrator has wound up to an enormous value, so the control signal stays saturated and drives the joint past the target. Anti-windup logic (conditional integration or feedback of saturation error) prevents this.

The **derivative (D) term** anticipates future error: τ_d = K_d · d(θ_d - θ)/dt. If the error is decreasing rapidly, derivative action opposes the motion, damping oscillations and reducing overshoot. Derivative action is not required for stability but improves the transient response. However, in real systems with noisy measurements, computing the derivative amplifies high-frequency noise, causing chattering. The solution is to low-pass filter the measurement before differentiating, trading a small amount of phase lag for noise rejection.

The **combined PID law** is:

τ = K_p · e(t) + K_i · ∫e(t) dt + K_d · de(t)/dt

where e(t) = θ_d(t) - θ(t) is the error.

**Tuning** a PID controller means choosing the three gains K_p, K_i, K_d. Excessive gains cause overshoot and oscillation. Insufficient gains cause sluggish response and steady-state error. The Ziegler-Nichols method is a simple empirical approach: increase K_p until the system oscillates (marginally unstable), then compute K_i and K_d from the critical gain and oscillation frequency. This provides a good starting point; manual fine-tuning typically follows based on observed step response.

In practice, each joint of a robot arm has its own PID controller. The trajectory planner specifies the desired joint angles and velocities at each time step. The PID controller for each joint converts this reference into a command signal (voltage or current) to the actuator, continuously correcting for any deviations. The independent control of each joint is possible when cross-coupling between joints is negligible (a reasonable assumption for most robots). More sophisticated approaches (computed torque control, nonlinear control) account for the dynamic coupling between joints, but PID remains the workhorse of industrial robot control due to its simplicity and robustness.
