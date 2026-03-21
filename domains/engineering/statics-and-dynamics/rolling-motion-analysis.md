---
id: rolling-motion-analysis
title: 'Rolling Without Slipping: Kinematics and Dynamics'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: holonomic-and-nonholonomic-constraints
  type: hard
- id: rigid-body-rotation-theory
  type: hard
builds-toward:
- systems-of-particles-mechanics
tags:
- rolling
- constraints
- contact-mechanics
stage: formal-systems
status: draft
---

# Rolling Without Slipping: Kinematics and Dynamics

## Core Idea
Rolling without slipping (v = ωr) is a nonholonomic constraint that couples translational and rotational motion. The no-slip condition at the contact point relates acceleration (a = αr) and, through energy analysis, reveals that rolling motion distributes kinetic energy between translation and rotation—the rolling object accelerates slower than one sliding freely.

## Questions

```yaml
- question: "A solid disk (I = ½mr²) and a thin ring (I = mr²) of the same mass and radius are released from rest at the top of the same ramp. Which reaches the bottom first?"
  type: multiple-choice
  options:
    - "The ring — it has more rotational inertia, which propels it faster"
    - "The solid disk — it has a lower I/mr² ratio, so less energy goes into rotation and more into translation"
    - "They tie — both have the same mass, so gravitational force is identical"
    - "The disk — because the ring's larger moment of inertia causes it to slip"
  answer: 1
  explanation: "Rolling kinetic energy is KE = ½mv²(1 + I/mr²). For a solid disk, I/mr² = ½, giving KE = ¾mv². For a ring, I/mr² = 1, giving KE = mv². At the same height, both start with the same potential energy mgh. The ring must 'spend' more of that energy on rotation, leaving less for translation — so its center moves slower. The disk wins every time, regardless of mass, because the ratio I/mr² depends only on geometry. The common error is thinking mass determines the winner."

- question: "A disk of radius r rolls without slipping with its center moving at speed v. What is the velocity of the topmost point of the disk?"
  type: multiple-choice
  options:
    - "v — all points on a rolling disk move at the same speed as the center"
    - "0 — all points rotate around the center, so the top and bottom cancel out"
    - "2v — the top point's translational and rotational velocities add together"
    - "½v — the topmost point is moving against the direction of travel"
  answer: 2
  explanation: "Every point on a rolling object has two components of velocity: the translational velocity v of the center (same for all points), plus a rotational velocity relative to the center. At the top, the rotational velocity is +ωr = +v in the same direction as the translation, giving 2v total. At the contact point, the rotational velocity is -ωr = -v, exactly canceling the translational +v, giving zero — which is required by the no-slip condition. This geometry (contact at rest, top at 2v) is a direct consequence of the instantaneous center of rotation being at the contact point."

- question: "A rolling object always reaches the bottom of a frictionless ramp more slowly than an identical sliding block, regardless of the object's mass."
  type: true-false
  answer: true
  explanation: "The rolling constraint forces the object to distribute its kinetic energy between translational and rotational motion: KE_total = ½mv²(1 + I/mr²). A sliding block on a frictionless ramp converts all potential energy to translational KE = ½mv². Since the rolling object must also spin, less energy is available for translation at any given height, so it moves slower. Mass cancels from both sides of the energy equation (mgh = ½mv²(1 + I/mr²)), confirming that mass does not affect the outcome — only the shape ratio I/mr² matters."

- question: "Two rolling objects of different masses but the same geometric shape will reach the bottom of a ramp at different times because the heavier object has more gravitational force acting on it."
  type: true-false
  answer: false
  explanation: "Mass cancels completely in the rolling-down-a-ramp problem. From energy conservation: mgh = ½mv²(1 + I/mr²). Dividing both sides by m, the descent speed v depends only on gh and I/mr² — neither of which involves mass. A heavy solid disk and a light solid disk released together will reach the bottom at exactly the same time. This is the rotational analog of Galileo's finding that all objects fall at the same rate in free fall. What determines arrival time is the geometry of the object (I/mr²), not its mass."

- question: "Why does the no-slip condition (v = ωr) mean that a rolling object has effectively higher inertia than a sliding block of the same mass?"
  type: short-answer
  answer: "The no-slip constraint couples translational and rotational motion into a single degree of freedom. Any force that accelerates the center (producing a = αr) must also simultaneously angularly accelerate the spinning — it cannot do one without the other. The energy that goes into spinning (½Iω² = ½I(v/r)²) is unavailable for translational acceleration. Effectively, the object resists acceleration from both its translational mass m and its rotational inertia I/r². The total effective inertia is m(1 + I/mr²), always greater than m alone. This is why rolling objects accelerate more slowly than sliding ones under the same net force."
  explanation: "The physical picture is: a net horizontal force on a sliding block on a frictionless surface accelerates only the center of mass. The same force on a rolling object must also cause rotation — friction at the contact point creates a torque. Some of the applied force's effect goes into spinning, less into translating. The coupling via v = ωr means you cannot speed up the center without also speeding up the rotation, so the 'effective mass' seen by any accelerating force is larger than the actual mass. This insight generalizes to all constrained mechanical systems: constraints redistribute inertia."
```

## Explainer

You've studied rigid body rotation and the constraints that govern mechanical systems. Rolling without slipping is the most important constrained rigid-body motion in engineering, appearing in wheels, gears, planetary rollers, and ball bearings. The "without slipping" condition is a constraint that links translational and rotational motion in a precise way — and understanding that link transforms what seems like a complex problem into a tractable one.

The **no-slip condition** at the contact point is the foundation. When a disk of radius r rolls without slipping on a flat surface, the contact point is instantaneously at rest relative to the ground. This means the velocity of the center must equal the arc length swept per unit time: **v = ωr**, where v is the translational speed of the center and ω is the angular velocity. Differentiating gives **a = αr**, linking translational and angular accelerations. These two equations are the complete statement of the rolling constraint — they eliminate one degree of freedom, reducing the system from two independent motions to one. If you know ω, you know v; if you know α, you know a.

The instantaneous contact point being at rest has a useful geometric interpretation: it acts as an **instantaneous center of rotation**. All points on the rolling object rotate about this contact point at each instant, even as that center itself moves along the ground. The topmost point of the disk therefore moves at twice the center's velocity (2v), the center moves at v, and the contact point moves at zero. This is verifiable by adding translational and rotational velocity vectors at each point, and it has a practical consequence: a wheel spinning in place with a locked axle has its contact point moving at maximum speed, while a properly rolling wheel has its contact point momentarily still. The constraint is what converts rotary drive into net translation.

Energy analysis reveals a profound consequence of rolling: the total kinetic energy is KE = ½mv² + ½Iω². Using v = ωr to eliminate ω, this becomes KE = ½mv²(1 + I/mr²). Compare this to a frictionless sliding object of the same mass, which has only ½mv². The rolling object effectively carries higher inertia — part of its energy budget goes to spinning, leaving less available for translational acceleration. A solid disk (I = ½mr²) rolling down a ramp will always arrive at the bottom slower than a frictionless sliding block, regardless of mass. Two objects of different mass but the same shape will tie — what matters is the dimensionless ratio I/mr², which depends only on geometry. A thin ring (I = mr²) rolls even more slowly than a solid disk; a sphere (I = 2mr²/5) rolls faster than a disk. This geometry-dependence is a clean consequence of the rolling constraint and serves as an elegant experimental test of rotational inertia.
