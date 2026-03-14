---
id: cascade-and-feedforward-control
title: Cascade and Feedforward Control
domain: engineering
course: control-systems
prerequisites:
- id: feedback-control-fundamentals
  type: hard
- id: pid-control
  type: hard
tags:
- cascade-control
- feedforward-control
- disturbance-rejection
- multi-loop
- inner-loop
- outer-loop
stage: advanced
status: draft
---

# Cascade and Feedforward Control

## Core Idea
Cascade control uses two nested feedback loops to improve disturbance rejection and response speed: an inner (secondary) loop with a fast sensor controls an intermediate variable, while an outer (primary) loop sets the inner loop's setpoint based on the primary controlled variable. The inner loop rejects disturbances entering the secondary process before they propagate to the primary output, and it linearizes the inner process dynamics as seen by the outer controller. For cascade control to be effective, the inner loop must be significantly faster than the outer loop (typically 3-5 times faster) so the outer controller can treat the inner loop as approximately unity gain. Feedforward control takes a fundamentally different approach: it measures a disturbance directly and applies a corrective control action before the disturbance affects the output, using a feedforward transfer function G_ff = −G_d/G_p (where G_d is the disturbance-to-output path and G_p is the control-to-output path). Perfect feedforward cancellation requires exact knowledge of G_d and G_p, which is never available in practice, so feedforward is almost always combined with feedback to handle modeling errors and unmeasured disturbances. Combined cascade-feedforward architectures are common in process control, where the feedforward signal adjusts the inner loop setpoint while the outer loop corrects for residual errors.

## How It's Best Learned
Simulate a heat exchanger or tank-level process with a measurable disturbance (e.g., inlet temperature or flow). First implement single-loop PID control and observe the disturbance response. Then add an inner cascade loop around the fast actuator dynamics and compare. Finally, add feedforward from the measured disturbance and observe the incremental improvement. This layered comparison makes the value of each architecture tangible.

## Common Misconceptions
- Cascade control does not require two different physical variables — it requires two measurements at different time scales, but in some applications the inner and outer measurements are the same variable at different points in the process.
- Feedforward control cannot work alone in practice because it provides zero correction for unmeasured disturbances, model uncertainty, and sensor drift — it is a complement to feedback, not a replacement.
- The inner loop in a cascade must be tuned first with the outer loop open; tuning both loops simultaneously couples their dynamics and typically leads to oscillatory or unstable behavior.
