---
id: rotational-motion-fixed-axis
title: Rotational Motion About a Fixed Axis
domain: physics
course: classical-mechanics
prerequisites:
- id: rotational-kinematics
  type: hard
- id: rotational-dynamics
  type: hard
- id: converting-degrees-and-radians
  type: soft
builds-toward:
- torque-angular-acceleration
- rolling-motion-equations
tags:
- rotation
- fixed-axis
- dynamics
stage: formal-systems
status: draft
---

# Rotational Motion About a Fixed Axis

## Core Idea
When a rigid body rotates about a fixed axis, all points follow circular paths with the same angular velocity ω and angular acceleration α. The moment of inertia I plays the role of mass in τ = Iα.

## Questions

```yaml
- question: "A solid disk of radius 0.5 m rotates at 10 rad/s about its center. What are the linear speeds of a point at the rim (r = 0.5 m) and a point halfway to the rim (r = 0.25 m)?"
  type: multiple-choice
  options:
    - "Both move at 10 m/s — all points share the same angular velocity, so they have the same linear speed"
    - "Rim: 5 m/s; inner point: 2.5 m/s — linear speed is proportional to distance from the axis"
    - "Rim: 0.5 m/s; inner point: 0.25 m/s — linear speed equals the radius at that angular velocity"
    - "The inner point moves faster because it has a shorter arc to complete per revolution"
  answer: 1
  explanation: "Linear speed v = rω. For the rim: v = 0.5 × 10 = 5 m/s. For the inner point: v = 0.25 × 10 = 2.5 m/s. All points on a rigidly rotating body share the same angular velocity ω — this is the defining property of fixed-axis rigid rotation. But their linear speeds differ because they travel different arc lengths per radian: a rim point covers a longer path per revolution. Option A is the classic error: shared ω does not imply shared v. Only the angular quantities are uniform across the body; the linear quantities vary with r."

- question: "Two cylinders have identical total mass M and radius R. Cylinder A is solid; Cylinder B is a hollow thin ring with all mass at the rim. The same torque is applied to each. Which angularly accelerates more quickly?"
  type: multiple-choice
  options:
    - "Cylinder B — hollow objects are lighter at the center and therefore easier to spin"
    - "Both equally — they have the same total mass, so they have the same rotational inertia"
    - "Cylinder A — its mass is distributed closer to the axis on average, giving a smaller moment of inertia (I = ½MR² vs I = MR²)"
    - "Cylinder B — the hollow ring concentrates mass at large radius, increasing the torque arm"
  answer: 2
  explanation: "From τ = Iα, for the same torque, smaller I means larger α. The solid cylinder has I = ½MR², while the hollow ring has I = MR² — twice as large, even with the same total mass. This is because I = Σmᵢrᵢ²: the ring has all its mass at radius R (contributing maximum r² per unit mass), while the solid cylinder's mass spans all radii 0 to R, averaging to a smaller effective r². Mass close to the axis barely resists rotation; mass far from the axis resists strongly. Moment of inertia depends on mass distribution, not just total mass."

- question: "When a rigid body rotates about a fixed axis, all particles in the body share the same angular velocity and therefore also share the same linear velocity."
  type: true-false
  answer: false
  explanation: "All particles in a rigidly rotating body do share the same angular velocity ω — this is the defining feature of rigid-body rotation about a fixed axis. But linear speed v = rω depends on both ω and the particle's distance r from the axis. Particles farther from the axis have larger r and therefore larger linear speed. Only the angular quantities (ω, α) are uniform throughout the body; the linear quantities (v, tangential acceleration) vary with distance from the axis. A rim point and a hub point on the same wheel have the same ω but very different v."

- question: "Redistributing a rotating body's mass farther from the rotation axis — while keeping total mass constant — increases its moment of inertia and makes it harder to change its rotational speed."
  type: true-false
  answer: true
  explanation: "Moment of inertia I = Σmᵢrᵢ² has an r² weighting: a particle at radius 2r contributes four times as much to I as the same particle at radius r. Moving mass farther from the axis therefore increases I substantially. From τ = Iα, a larger I means a given torque produces less angular acceleration — the body is harder to spin up or slow down. This is why flywheels are designed with mass concentrated at the rim (high I, resistant to speed changes), and why a figure skater who extends their arms rotates more slowly."

- question: "A figure skater spins with arms outstretched, then pulls them tightly to their body and immediately spins faster. Explain this using moment of inertia and angular momentum."
  type: short-answer
  answer: "Angular momentum L = Iω is conserved when no external torque acts (friction from the ice is negligible). When the skater pulls their arms inward, mass moves closer to the rotation axis, decreasing moment of inertia I (since I = Σmᵢrᵢ², smaller r means smaller I). Because L = Iω must remain constant, a decrease in I requires a proportional increase in ω: the skater spins faster. This is a direct consequence of I depending on mass distribution — the same total mass in a compact configuration (small r, small I) spins much faster than when spread out."
  explanation: "The three key ideas: (1) I = Σmᵢrᵢ² — decreasing r decreases I; (2) conservation of angular momentum L = Iω — with no external torque, L is constant; (3) therefore ω must increase when I decreases. The figure skater is a canonical demonstration because the acceleration is immediately felt, making the abstract r² dependence of moment of inertia viscerally intuitive. It also connects fixed-axis rotation to the broader principle of angular momentum conservation."
```

## Explainer

You have already studied rotational kinematics (positions, velocities, and accelerations in angular terms) and rotational dynamics (torques and how they cause angular acceleration). Rotational motion about a fixed axis is where these threads come together into a coherent mechanical framework — the precise rotational analog of linear dynamics, with every concept mapping onto its translational counterpart.

The analogy is exact and worth making explicit. In linear mechanics: force F causes acceleration a in a body of mass m, according to F = ma. Mass is the resistance to change in linear velocity. In rotational mechanics: **torque** τ causes angular acceleration α in a body with **moment of inertia** I, according to τ = Iα. Moment of inertia is the resistance to change in rotational velocity. The deeper point is why I depends on the *distribution* of mass, not just the total mass. A mass far from the rotation axis requires more torque to accelerate rotationally than the same mass close to the axis — because it travels a longer arc for the same angular displacement and therefore requires greater linear acceleration at its location. This is why a figure skater pulls in their arms to spin faster: with mass moved closer to the axis, I decreases, and to conserve angular momentum L = Iω, ω must increase.

When a rigid body rotates about a **fixed axis**, a powerful simplification applies: all particles in the body share the same angular velocity ω and angular acceleration α. They do *not* share the same linear velocity or linear acceleration — a point at radius r has linear speed v = rω, so points farther from the axis move faster. This is the defining geometry of rigid rotation: the body rotates as one unit, with the angular quantities uniform throughout even though the linear quantities vary by distance from the axis.

The moment of inertia I = Σmᵢrᵢ² (or its integral form for continuous bodies) is the central quantity to calculate for any given object and axis. Familiar results — I = ½mr² for a solid disk, I = ⅖mr² for a solid sphere, I = mr² for a thin ring — are not arbitrary; they reflect how mass is distributed relative to the axis. The **parallel axis theorem** extends these results to any axis parallel to one through the center of mass: I = I_cm + md², where d is the distance between the axes. This is essential for applied problems where the rotation axis is not through the center of mass — a door hinge, a rod pivoting at one end, a physical pendulum swinging about a support point. Mastering fixed-axis rotation prepares you for rolling motion (where translational and rotational dynamics combine) and for angular momentum conservation in systems where external torques are absent.
