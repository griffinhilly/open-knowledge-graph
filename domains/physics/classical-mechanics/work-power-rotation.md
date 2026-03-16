---
id: work-power-rotation
title: Work and Power in Rotational Motion
domain: physics
course: classical-mechanics
prerequisites:
- id: torque-angular-acceleration
  type: hard
- id: work-and-energy
  type: hard
builds-toward:
- rigid-body-planar-motion
tags:
- work
- power
- rotation
stage: formal-systems
status: draft
---

# Work and Power in Rotational Motion

## Core Idea
Work done by a torque is W = ∫τ dθ, and instantaneous power is P = τω. The work-energy theorem states that work equals the change in rotational kinetic energy, W = ½I(ω_f² − ω_i²).

## Explainer

Every concept in rotational dynamics has a direct linear analog, and this topic completes the translation. You already know that in linear motion, work is W = F·d (force times displacement) and power is P = Fv (force times velocity). Now substitute the rotational analogs: torque τ replaces force F, and angular displacement θ replaces linear displacement d. The result is W = τθ for constant torque, or W = ∫τ dθ for varying torque. Similarly, since v = rω links linear and angular speed, multiplying through by force gives P = τω. The structure is identical — only the variables change names.

The **work-energy theorem for rotation** follows the same logic as its linear counterpart. In linear mechanics, net work equals the change in kinetic energy: W_net = ΔKE = ½mv_f² − ½mv_i². Rotational kinetic energy is ½Iω², so the rotational version is simply W_net = ½Iω_f² − ½Iω_i². This is not a new principle — it is the same work-energy theorem, expressed in the language of rotation. If you spin up a flywheel by applying a torque through some angular displacement, the work you do equals the rotational kinetic energy you have added to the system.

Consider a motor shaft rotating under a constant torque of 20 N·m at 100 rad/s. The power output is P = τω = 2000 W — exactly two kilowatts. If the torque is applied while the shaft turns through π radians (half a revolution), the work done is W = τθ = 20 × π ≈ 63 J. Notice that large power can come from large torque at low speed, or small torque at high speed — the same tradeoff you know from gears. A car in a low gear produces high torque but low angular velocity at the wheels; a high gear produces lower torque but higher angular velocity for the same engine power.

The key check on any rotational energy problem is unit consistency: radians are dimensionless, so τ (in N·m) times θ (in rad) gives joules. Angular velocity in rad/s times torque in N·m gives watts. If your numbers don't carry the right units at each step, the analogy has broken down somewhere. Once this translation is fluent, problems involving rotating drums, motors, turbines, and flywheels reduce to familiar energy bookkeeping — the rotational wrapper is thin.
