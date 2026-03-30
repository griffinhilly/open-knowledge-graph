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
status: validated
---

# Reference Tracking and Servo System Design

## Core Idea
Servo systems track time-varying reference inputs (not just constants). Tracking error is the difference between reference and output; zero steady-state tracking requires sufficient loop gain and type. Transient tracking performance (rise time to follow step changes, overshoot) is decoupled from steady-state error only if the controller is properly designed. Servo performance requires careful specification of both steady-state and transient metrics.

## Questions

```yaml
- question: "A type-1 servo system (one integrator in the open loop) is commanded to track a ramp reference (constant-velocity input). What is the steady-state tracking behavior?"
  type: multiple-choice
  options:
    - "Zero steady-state error — one integrator is sufficient to track any reference signal asymptotically"
    - "A finite, nonzero constant tracking error that persists indefinitely as the ramp continues"
    - "Unstable behavior — a type-1 system cannot handle ramp inputs without going unstable"
    - "Zero steady-state error only if the loop gain is sufficiently high"
  answer: 1
  explanation: "System type determines which reference classes can be tracked with zero steady-state error. A type-1 system (one open-loop integrator) achieves zero steady-state error to a step reference and finite constant error to a ramp reference. To track a ramp with zero steady-state error, you need at least type-2 (two integrators). The finite ramp error is called the velocity error constant, and it depends on the loop gain — higher gain reduces it but cannot eliminate it without adding another integrator. Option A confuses type-1 sufficiency for steps with sufficiency for ramps."

- question: "A servo designer increases loop gain to improve steady-state accuracy. What is the most likely consequence for transient tracking performance?"
  type: multiple-choice
  options:
    - "Transient performance improves proportionally — higher gain makes the system respond faster with less overshoot"
    - "Transient performance is unchanged because steady-state error and transient response are independent"
    - "Phase margin decreases, leading to increased overshoot, longer settling time, and potential instability"
    - "Rise time increases because the higher gain slows the initial response to reference changes"
  answer: 2
  explanation: "This is the fundamental tension in servo design. Increasing loop gain improves steady-state accuracy by raising the error constants, but it also reduces phase margin — the phase buffer before instability. Lower phase margin means more oscillatory step responses, greater overshoot, longer settling times, and at the extreme, instability. The gain that zeroes steady-state error for a given reference class may produce intolerable oscillations in the transient response. Good servo design uses integral action to raise system type (for steady-state accuracy) and lead compensation or filters to preserve phase margin (for transient performance)."

- question: "A servo system that achieves zero steady-state error to a step reference input will automatically also achieve zero steady-state error to a ramp reference input."
  type: true-false
  answer: false
  explanation: "Steady-state tracking error depends on system type, not just gain. Zero steady-state error to a step requires at least type-1 (one open-loop integrator). Zero steady-state error to a ramp requires at least type-2 (two open-loop integrators). A type-1 system tracks steps perfectly but produces a finite, persistent error to ramp inputs. Knowing the error to one class of reference tells you nothing about error to a higher-order class — you must match system type to the most demanding signal your application requires."

- question: "The system type — the number of open-loop integrators — determines whether steady-state tracking error to a given class of reference signal can be driven to zero."
  type: true-false
  answer: true
  explanation: "System type is the key structural property for steady-state performance. Type-0: constant error to step, unbounded error to ramp. Type-1: zero error to step, finite constant error to ramp, unbounded error to parabola. Type-2: zero error to both step and ramp, finite error to parabolic input. This hierarchy follows from the internal model principle: to track a reference with zero steady-state error, the controller must contain a model of the reference signal's dynamics — hence integrators for steps and ramps. Loop gain affects the magnitude of finite errors but cannot change the fundamental type classification."

- question: "Explain the fundamental tension between steady-state accuracy and transient tracking performance in servo design, and how a well-designed controller addresses both simultaneously."
  type: short-answer
  answer: "Steady-state accuracy requires sufficient system type (integrators) and loop gain. But adding integrators reduces phase margin, and increasing gain further reduces it — both tend to make the closed-loop response oscillatory, increasing overshoot and settling time (poor transient performance). The tension is that the tools for eliminating steady-state error degrade transient behavior. A well-designed servo controller separates these concerns: integral action raises the system type to meet steady-state requirements, while lead compensation or bandwidth-limiting filters are added to restore phase margin and shape the transient response to meet rise time, overshoot, and settling time specifications."
  explanation: "The practical approach starts by specifying both requirement classes independently before choosing a controller structure. Steady-state specs determine minimum system type and low-frequency gain. Transient specs determine required bandwidth and phase margin. A controller (often a PI or PID with lead compensation) must be designed to satisfy both simultaneously. When they genuinely conflict, the engineer faces a deliberate design tradeoff and must document which requirement was relaxed and why — rather than discovering the conflict after the fact during testing."
```

## Explainer

A regulator holds a constant setpoint against disturbances. A **servo system** does something harder: it tracks a reference that is itself moving over time. Think of a radar antenna following an aircraft across the sky, a robot arm tracing a welding path, or a disk drive head seeking a specific track while the disk spins. The controller must not only eliminate static error but must also follow dynamic trajectories — and how quickly and accurately it does so, and how much it overshoots, all matter to the application.

**Tracking error** e(t) = r(t) − y(t) is the moment-to-moment difference between the desired reference and the actual output. Your prerequisite on steady-state error analysis established the key result: the **system type** — the number of pure integrators (poles at s = 0) in the open-loop transfer function — determines which classes of reference input can be tracked with zero steady-state error. A type-0 system has constant steady-state error to a step reference. A type-1 system (one integrator in the loop) eliminates steady-state error to a step and achieves finite but nonzero error to a ramp. A type-2 system tracks ramps with zero steady-state error. For servo applications, you must match the system type to the most demanding signal your reference will generate — if the reference is a ramp (constant velocity), you need at least type-1 to have any hope of tracking it asymptotically.

But eliminating steady-state error is only half the specification. **Transient tracking performance** — how quickly and smoothly the output follows reference changes — is equally important and often more demanding. A servo that eventually catches up to a ramp but takes several seconds to settle is useless for fast positioning. Rise time, settling time, and overshoot (from your time-domain performance specifications) describe the transient response to step changes in the reference. These are not independent of steady-state behavior: increasing loop gain improves steady-state accuracy but typically degrades transient performance by reducing phase margin, increasing overshoot, and exciting resonances. The fundamental tension in servo design is that the tools for reducing steady-state error often conflict with the tools for controlling transient behavior.

Good servo design separates these concerns by specifying both classes of requirement explicitly before selecting a controller. Steady-state accuracy requirements determine the minimum system type and low-frequency loop gain. Transient performance requirements determine bandwidth, damping targets, and phase margin. A well-designed servo controller — often using **integral action** to raise the system type and **lead compensation** or bandwidth-limiting filters to preserve phase margin and manage the transient — must satisfy both sets of requirements simultaneously. When they conflict, the design engineer must make a deliberate tradeoff, and understanding that tradeoff quantitatively is what distinguishes principled servo design from trial-and-error tuning.
