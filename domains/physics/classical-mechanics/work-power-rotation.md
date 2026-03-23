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
status: validated
---

# Work and Power in Rotational Motion

## Core Idea
Work done by a torque is W = ∫τ dθ, and instantaneous power is P = τω. The work-energy theorem states that work equals the change in rotational kinetic energy, W = ½I(ω_f² − ω_i²).

## Questions

```yaml
- question: "A motor applies a constant torque of 50 N·m to a shaft. The shaft turns through 4π radians. How much work does the motor do?"
  type: multiple-choice
  options:
    - "50π J ≈ 157 J"
    - "200π J ≈ 628 J"
    - "200 J"
    - "The work cannot be determined without knowing the angular velocity"
  answer: 1
  explanation: "W = τθ = 50 N·m × 4π rad = 200π J ≈ 628 J. Radians are dimensionless, so N·m × rad = N·m = J. Option A (50π) would arise from mistakenly using θ = π. Option C (200 J) omits the π factor. Option D confuses work with power — power requires angular velocity, but work requires only torque and angular displacement, which are both given here."

- question: "A flywheel with moment of inertia I = 2 kg·m² is spinning at ω = 10 rad/s and is then brought to rest by friction. How much work did friction do on the flywheel?"
  type: multiple-choice
  options:
    - "+100 J (friction added rotational energy to slow it down)"
    - "−20 J (W = ½Iω = ½ × 2 × 10 = 10, times sign)"
    - "−100 J (W = ½Iω_f² − ½Iω_i² = 0 − ½(2)(10²) = −100 J)"
    - "−200 J (W = Iω_f² − Iω_i² = 0 − 2 × 100 = −200 J, omitting the ½)"
  answer: 2
  explanation: "By the work-energy theorem for rotation: W_net = ½Iω_f² − ½Iω_i² = ½(2)(0²) − ½(2)(10²) = 0 − 100 = −100 J. The negative sign reflects that friction removes energy from the flywheel. Option A has the wrong sign (friction doesn't add energy here). Option B forgets to square ω. Option D omits the ½ factor. The rotational work-energy theorem is structurally identical to the linear version — just substitute I for m and ω for v."

- question: "The instantaneous power delivered to a rotating body is P = τω, the direct rotational analog of P = Fv in linear mechanics."
  type: true-false
  answer: true
  explanation: "The analogy holds exactly: force F corresponds to torque τ, and linear velocity v corresponds to angular velocity ω. Since P = Fv (linear) and the substitution F→τ, v→ω is consistent throughout rotational mechanics, P = τω follows. Both express power as the product of the effort quantity and the rate of displacement. This is also consistent dimensionally: τ (N·m) × ω (rad/s) = N·m/s = W, since radians are dimensionless."

- question: "Because angular displacement is measured in radians, which are dimensionless, the product of torque (N·m) and angular displacement (rad) does not have units of joules."
  type: true-false
  answer: false
  explanation: "Radians are dimensionless — they are a ratio of arc length to radius, both in meters, so the meters cancel. Therefore torque (N·m) × angular displacement (rad) = N·m × (dimensionless) = N·m = J. Radians being dimensionless is precisely what makes the rotational formulas W = τθ and P = τω dimensionally consistent with their linear counterparts. The units work out correctly, and the product has units of joules."

- question: "A car engine delivers constant power P. Using P = τω, explain why a low gear (high torque, low wheel angular velocity) and a high gear (low torque, high wheel angular velocity) can both transmit the same engine power to the wheels."
  type: short-answer
  answer: "Power is the product of torque and angular velocity: P = τω. At constant P, increasing one factor requires decreasing the other. In a low gear, the transmission multiplies torque (τ is large) at the cost of wheel angular velocity (ω is small) — useful for acceleration. In a high gear, wheel angular velocity is high (ω is large) but torque is reduced (τ is small) — useful for cruising speed. Since P = τω is constant in both cases, both gears can transmit the same engine power while trading off between torque and speed."
  explanation: "This is the fundamental tradeoff in mechanical power transmission. The gear ratio determines how torque and angular velocity are exchanged, but their product (power) is conserved (ignoring friction losses). This principle applies to all mechanical systems: bicycle gears, electric motors, turbines, and flywheels all exploit the τω = constant relationship at fixed power."
```

## Explainer

Every concept in rotational dynamics has a direct linear analog, and this topic completes the translation. You already know that in linear motion, work is W = F·d (force times displacement) and power is P = Fv (force times velocity). Now substitute the rotational analogs: torque τ replaces force F, and angular displacement θ replaces linear displacement d. The result is W = τθ for constant torque, or W = ∫τ dθ for varying torque. Similarly, since v = rω links linear and angular speed, multiplying through by force gives P = τω. The structure is identical — only the variables change names.

The **work-energy theorem for rotation** follows the same logic as its linear counterpart. In linear mechanics, net work equals the change in kinetic energy: W_net = ΔKE = ½mv_f² − ½mv_i². Rotational kinetic energy is ½Iω², so the rotational version is simply W_net = ½Iω_f² − ½Iω_i². This is not a new principle — it is the same work-energy theorem, expressed in the language of rotation. If you spin up a flywheel by applying a torque through some angular displacement, the work you do equals the rotational kinetic energy you have added to the system.

Consider a motor shaft rotating under a constant torque of 20 N·m at 100 rad/s. The power output is P = τω = 2000 W — exactly two kilowatts. If the torque is applied while the shaft turns through π radians (half a revolution), the work done is W = τθ = 20 × π ≈ 63 J. Notice that large power can come from large torque at low speed, or small torque at high speed — the same tradeoff you know from gears. A car in a low gear produces high torque but low angular velocity at the wheels; a high gear produces lower torque but higher angular velocity for the same engine power.

The key check on any rotational energy problem is unit consistency: radians are dimensionless, so τ (in N·m) times θ (in rad) gives joules. Angular velocity in rad/s times torque in N·m gives watts. If your numbers don't carry the right units at each step, the analogy has broken down somewhere. Once this translation is fluent, problems involving rotating drums, motors, turbines, and flywheels reduce to familiar energy bookkeeping — the rotational wrapper is thin.
