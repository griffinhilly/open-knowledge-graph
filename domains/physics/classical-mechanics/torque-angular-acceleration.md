---
id: torque-angular-acceleration
title: Torque and Angular Acceleration Relations
domain: physics
course: classical-mechanics
prerequisites:
- id: torque
  type: hard
- id: rotational-motion-fixed-axis
  type: hard
- id: cross-product-3d
  type: soft
builds-toward:
- work-power-rotation
- rigid-body-planar-motion
tags:
- torque
- angular-dynamics
- mechanics
stage: formal-systems
status: draft
---

# Torque and Angular Acceleration Relations

## Core Idea
The net torque equals the moment of inertia times angular acceleration: τ_net = Iα. This is the rotational analog of Newton's second law and applies to both rigid bodies and systems of particles.

## Explainer

You already know that **torque** is the rotational effectiveness of a force — τ = r × F — and that **rotational motion about a fixed axis** is described by angular displacement θ, angular velocity ω, and angular acceleration α, with the same kinematic relationships as linear motion. The equation τ_net = Iα ties these together exactly as F_net = ma ties force to linear acceleration, and the parallel structure is worth exploiting fully.

In linear dynamics, **mass** measures resistance to changes in translational motion — a large mass requires a large force to accelerate. In rotational dynamics, the **moment of inertia** I plays the same role for angular acceleration. But I is not just a number intrinsic to the object; it depends on how the mass is *distributed relative to the axis of rotation*. A mass element dm at distance r from the axis contributes r² dm to the moment of inertia, so mass far from the axis counts for much more than mass near it. This is why a figure skater pulls in their arms to spin faster — reducing r reduces I, and since angular momentum Iω is conserved, ω must increase. The r² dependence means even modest redistributions of mass have large rotational effects.

To apply τ_net = Iα, the procedure mirrors F = ma: identify all forces acting on the body, compute the torque each exerts about the rotation axis (τ = r F sin θ, where θ is the angle between r and F), sum them with signs (choose a positive direction for rotation), look up or calculate I for the body and axis, then solve for α. The force-torque analogy runs deep: a force tangential to the rotation path produces torque most efficiently (sin θ = 1); a force directed through the axis produces zero torque (r = 0 or sin θ = 0). This is the rotational equivalent of recognizing that only the component of force along the direction of motion does work.

The most common application is a **pulley or wheel with mass**. In an introductory problem, a massless pulley simply changes the direction of a string tension. Once the pulley has mass, the tension on the two sides of the rope need not be equal — the net torque from the tension difference is what causes the pulley to accelerate angularly. Writing τ_net = Iα for the pulley alongside F = ma for each hanging mass yields a system of equations. The coupling condition is the kinematic constraint: the rope's linear acceleration a equals the pulley rim's tangential acceleration, a = αR. This constraint links the linear and rotational dynamics and allows you to solve for all accelerations and the true tensions. Notice that a massive pulley always results in a *smaller* linear acceleration than the massless case — some of the driving force goes into spinning up the pulley rather than accelerating the masses.
