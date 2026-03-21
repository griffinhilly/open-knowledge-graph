---
id: friction-in-mechanical-devices
title: Friction in Mechanical Devices
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: static-friction-equilibrium
  type: hard
- id: friction-wedges-screws-belts
  type: soft
tags:
- friction
- screws
- wedges
- belt drives
- brakes
- self-locking
stage: formal-systems
status: draft
---

# Friction in Mechanical Devices

## Core Idea
Friction plays a critical role in screws, wedges, belt drives, and brakes. Analysis includes determining when sliding begins, calculating forces required to prevent motion or achieve desired speed, and understanding self-locking behavior when friction is high enough to hold loads indefinitely. Friction enables mechanism function and can dissipate unwanted energy.

## Questions

```yaml
- question: "A power screw has a lead angle of 3° and a friction angle of 12°. An engineer redesigns the thread to increase the lead angle to 15°. What changes about the screw's behavior?"
  type: multiple-choice
  options:
    - "The screw becomes more self-locking because a larger lead angle traps more friction force"
    - "The screw loses self-locking — the load can now back-drive the screw because the lead angle exceeds the friction angle"
    - "The screw lifts loads faster but retains self-locking because the friction coefficient is unchanged"
    - "Nothing changes — self-locking depends only on the friction coefficient, not the thread geometry"
  answer: 1
  explanation: "Self-locking requires that the lead angle be less than the friction angle (φ = arctan μ). At 3° < 12°, the screw is self-locking: friction holds the load without external input. At 15° > 12°, the geometry places the reaction force outside the friction cone, so the load can back-drive the thread — the screw is no longer self-locking. This design tradeoff is critical: a car jack must be self-locking (you need to leave it holding the car), while a lead screw on an adjustable instrument may need to be back-drivable."

- question: "A band brake wraps around a drum with wrap angle β = π radians and friction coefficient μ = 0.3. The slack side tension is 50 N. What is the approximate tight side tension? (Use e^(0.3π) ≈ 2.57)"
  type: multiple-choice
  options:
    - "50 N — friction makes no difference at the wrap angle used"
    - "65 N — tension scales linearly with wrap angle: T = T_slack × (1 + μβ)"
    - "128 N — exponential capstan equation: T_tight = 50 × e^(0.3π)"
    - "500 N — the tight side is always ten times the slack side in standard brakes"
  answer: 2
  explanation: "The capstan equation T_tight/T_slack = e^(μβ) is exponential, not linear. Each infinitesimal element of the belt adds a friction contribution proportional to the current tension, so the contributions compound multiplicatively around the wrap. With μ = 0.3 and β = π: T_tight = 50 × e^(0.942) ≈ 50 × 2.57 ≈ 128 N. Option B represents the common mistake of assuming linear scaling. The exponential nature is what makes a few wraps of rope around a post capable of holding a very large load with modest input force."

- question: "A wedge is self-locking when its wedge angle is greater than the friction angle."
  type: true-false
  answer: false
  explanation: "Self-locking occurs when the wedge angle is *less than* the friction angle. When the wedge angle < φ (friction angle), the geometry forces the reaction force inside the friction cone, so friction is always sufficient to prevent sliding regardless of the applied load. When the wedge angle > φ, the reaction force falls outside the friction cone and the wedge slides under load. The self-locking criterion — angle < friction angle — is the same for wedges, power screws, and any device where inclined surfaces interact."

- question: "A power screw thread is geometrically equivalent to a wedge wrapped around a cylinder, so the self-locking criterion (lead angle vs. friction angle) applies to both."
  type: true-false
  answer: true
  explanation: "The analogy is direct: unrolling a screw thread produces an inclined plane (wedge) whose slope is the lead angle. The same self-locking condition applies: if the helix (lead) angle is less than the friction angle, the load cannot unscrew the thread — the screw self-locks. This is why a car jack keeps a vehicle raised without holding the handle, and why highly-efficient ball-screw actuators (with very low friction angles) are deliberately not self-locking and require a brake to hold position."

- question: "Explain the self-locking criterion for a wedge or power screw. Why does a car jack not require you to hold the handle to keep the car raised?"
  type: short-answer
  answer: "Self-locking occurs when the lead (or wedge) angle is less than the friction angle φ = arctan(μ). When this condition holds, any load trying to back-drive the device creates a reaction force that falls within the friction cone — friction can always generate enough force to resist motion, so the device stays put without external input. A car jack is designed with a thread whose lead angle is below the friction angle, so the weight of the car cannot unscrew the jack; the geometry locks it in place."
  explanation: "The friction angle is the maximum angle at which the reaction force can be directed away from the normal while friction still holds. When the device geometry forces the reaction force to stay within this cone, no sliding is possible regardless of load magnitude — this is self-locking. Engineers exploit this in jacks, clamps, and turnbuckles while deliberately choosing lead angles above the friction angle when back-drivability is needed (adjustable instruments, certain actuators)."
```

## Explainer

From your study of static friction equilibrium, you know that the friction force available at a surface is F ≤ μN, where N is the normal force. In simple block-on-surface problems that relationship stands alone. In mechanical devices, the key insight is that geometry multiplies and redirects friction, making it either a useful force amplifier or an efficient energy lock. Understanding each device type is a matter of identifying what angle the surfaces make and how that angle concentrates or leverages the friction forces.

A **wedge** converts a small applied horizontal force into a large vertical lifting force by using a shallow taper — but it requires overcoming friction on two contact surfaces simultaneously. The ratio of load to applied force depends on the wedge angle and the friction angle (φ = arctan μ). **Self-locking** occurs when the wedge angle is less than the friction angle: the wedge will not slide out even when the applied force is removed, because friction on the back surface pins it in place. The same logic governs **power screws**: a screw thread is geometrically equivalent to a wedge wrapped around a cylinder. When the lead angle (the helix angle of the thread) is smaller than the friction angle, the screw is self-locking — the load cannot unscrew it, which is why you do not need to hold a jack handle to keep a car lifted.

**Belt drives and band brakes** apply the exponential capstan relationship (T_tight / T_slack = e^(μβ)) to transmit torque or resist motion. The tight side tensions the belt or brake band, and friction at the contact surface amplifies that tension exponentially with wrap angle. A band brake can clamp a rotating drum with an enormous resisting torque using modest input force, simply by increasing the wrap angle. In brakes, the goal is dissipating kinetic energy; in belt drives, the goal is transmitting power without slip.

The unifying theme across all these devices is the **friction angle** and the condition for self-locking: when geometry forces the reaction force into the friction cone, the device locks without external input. When geometry places the reaction outside the friction cone, motion occurs regardless of friction. Engineers exploit self-locking to hold loads (jacks, clamps, turnbuckles) and deliberately avoid it when back-drivability is needed (lead screws on adjustable instruments). Every friction device analysis starts by identifying which face is active, what normal force the geometry generates, and whether the friction angle criterion is satisfied.
