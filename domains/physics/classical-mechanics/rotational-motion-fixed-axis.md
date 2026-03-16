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

## Explainer

You have already studied rotational kinematics (positions, velocities, and accelerations in angular terms) and rotational dynamics (torques and how they cause angular acceleration). Rotational motion about a fixed axis is where these threads come together into a coherent mechanical framework — the precise rotational analog of linear dynamics, with every concept mapping onto its translational counterpart.

The analogy is exact and worth making explicit. In linear mechanics: force F causes acceleration a in a body of mass m, according to F = ma. Mass is the resistance to change in linear velocity. In rotational mechanics: **torque** τ causes angular acceleration α in a body with **moment of inertia** I, according to τ = Iα. Moment of inertia is the resistance to change in rotational velocity. The deeper point is why I depends on the *distribution* of mass, not just the total mass. A mass far from the rotation axis requires more torque to accelerate rotationally than the same mass close to the axis — because it travels a longer arc for the same angular displacement and therefore requires greater linear acceleration at its location. This is why a figure skater pulls in their arms to spin faster: with mass moved closer to the axis, I decreases, and to conserve angular momentum L = Iω, ω must increase.

When a rigid body rotates about a **fixed axis**, a powerful simplification applies: all particles in the body share the same angular velocity ω and angular acceleration α. They do *not* share the same linear velocity or linear acceleration — a point at radius r has linear speed v = rω, so points farther from the axis move faster. This is the defining geometry of rigid rotation: the body rotates as one unit, with the angular quantities uniform throughout even though the linear quantities vary by distance from the axis.

The moment of inertia I = Σmᵢrᵢ² (or its integral form for continuous bodies) is the central quantity to calculate for any given object and axis. Familiar results — I = ½mr² for a solid disk, I = ⅖mr² for a solid sphere, I = mr² for a thin ring — are not arbitrary; they reflect how mass is distributed relative to the axis. The **parallel axis theorem** extends these results to any axis parallel to one through the center of mass: I = I_cm + md², where d is the distance between the axes. This is essential for applied problems where the rotation axis is not through the center of mass — a door hinge, a rod pivoting at one end, a physical pendulum swinging about a support point. Mastering fixed-axis rotation prepares you for rolling motion (where translational and rotational dynamics combine) and for angular momentum conservation in systems where external torques are absent.
