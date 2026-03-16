---
id: reference-tracking-servo-systems
title: Reference Tracking and Servo System Design
domain: engineering
course: control-systems
prerequisites:
- id: steady-state-error-analysis
  type: hard
- id: time-domain-performance-specifications
  type: hard
builds-toward:
- sensitivity-and-robustness-functions
tags:
- reference-tracking
- servo
- tracking-error
- design
stage: advanced
status: draft
---

# Reference Tracking and Servo System Design

## Core Idea
Servo systems track time-varying reference inputs (not just constants). Tracking error is the difference between reference and output; zero steady-state tracking requires sufficient loop gain and type. Transient tracking performance (rise time to follow step changes, overshoot) is decoupled from steady-state error only if the controller is properly designed. Servo performance requires careful specification of both steady-state and transient metrics.

## Explainer

A regulator holds a constant setpoint against disturbances. A **servo system** does something harder: it tracks a reference that is itself moving over time. Think of a radar antenna following an aircraft across the sky, a robot arm tracing a welding path, or a disk drive head seeking a specific track while the disk spins. The controller must not only eliminate static error but must also follow dynamic trajectories — and how quickly and accurately it does so, and how much it overshoots, all matter to the application.

**Tracking error** e(t) = r(t) − y(t) is the moment-to-moment difference between the desired reference and the actual output. Your prerequisite on steady-state error analysis established the key result: the **system type** — the number of pure integrators (poles at s = 0) in the open-loop transfer function — determines which classes of reference input can be tracked with zero steady-state error. A type-0 system has constant steady-state error to a step reference. A type-1 system (one integrator in the loop) eliminates steady-state error to a step and achieves finite but nonzero error to a ramp. A type-2 system tracks ramps with zero steady-state error. For servo applications, you must match the system type to the most demanding signal your reference will generate — if the reference is a ramp (constant velocity), you need at least type-1 to have any hope of tracking it asymptotically.

But eliminating steady-state error is only half the specification. **Transient tracking performance** — how quickly and smoothly the output follows reference changes — is equally important and often more demanding. A servo that eventually catches up to a ramp but takes several seconds to settle is useless for fast positioning. Rise time, settling time, and overshoot (from your time-domain performance specifications) describe the transient response to step changes in the reference. These are not independent of steady-state behavior: increasing loop gain improves steady-state accuracy but typically degrades transient performance by reducing phase margin, increasing overshoot, and exciting resonances. The fundamental tension in servo design is that the tools for reducing steady-state error often conflict with the tools for controlling transient behavior.

Good servo design separates these concerns by specifying both classes of requirement explicitly before selecting a controller. Steady-state accuracy requirements determine the minimum system type and low-frequency loop gain. Transient performance requirements determine bandwidth, damping targets, and phase margin. A well-designed servo controller — often using **integral action** to raise the system type and **lead compensation** or bandwidth-limiting filters to preserve phase margin and manage the transient — must satisfy both sets of requirements simultaneously. When they conflict, the design engineer must make a deliberate tradeoff, and understanding that tradeoff quantitatively is what distinguishes principled servo design from trial-and-error tuning.
