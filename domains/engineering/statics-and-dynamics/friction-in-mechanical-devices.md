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

## Explainer

From your study of static friction equilibrium, you know that the friction force available at a surface is F ≤ μN, where N is the normal force. In simple block-on-surface problems that relationship stands alone. In mechanical devices, the key insight is that geometry multiplies and redirects friction, making it either a useful force amplifier or an efficient energy lock. Understanding each device type is a matter of identifying what angle the surfaces make and how that angle concentrates or leverages the friction forces.

A **wedge** converts a small applied horizontal force into a large vertical lifting force by using a shallow taper — but it requires overcoming friction on two contact surfaces simultaneously. The ratio of load to applied force depends on the wedge angle and the friction angle (φ = arctan μ). **Self-locking** occurs when the wedge angle is less than the friction angle: the wedge will not slide out even when the applied force is removed, because friction on the back surface pins it in place. The same logic governs **power screws**: a screw thread is geometrically equivalent to a wedge wrapped around a cylinder. When the lead angle (the helix angle of the thread) is smaller than the friction angle, the screw is self-locking — the load cannot unscrew it, which is why you do not need to hold a jack handle to keep a car lifted.

**Belt drives and band brakes** apply the exponential capstan relationship (T_tight / T_slack = e^(μβ)) to transmit torque or resist motion. The tight side tensions the belt or brake band, and friction at the contact surface amplifies that tension exponentially with wrap angle. A band brake can clamp a rotating drum with an enormous resisting torque using modest input force, simply by increasing the wrap angle. In brakes, the goal is dissipating kinetic energy; in belt drives, the goal is transmitting power without slip.

The unifying theme across all these devices is the **friction angle** and the condition for self-locking: when geometry forces the reaction force into the friction cone, the device locks without external input. When geometry places the reaction outside the friction cone, motion occurs regardless of friction. Engineers exploit self-locking to hold loads (jacks, clamps, turnbuckles) and deliberately avoid it when back-drivability is needed (lead screws on adjustable instruments). Every friction device analysis starts by identifying which face is active, what normal force the geometry generates, and whether the friction angle criterion is satisfied.
