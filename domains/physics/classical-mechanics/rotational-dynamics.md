---
id: rotational-dynamics
title: 'Rotational Dynamics: Newton''s Second Law for Rotation'
domain: physics
course: classical-mechanics
prerequisites:
- id: torque
  type: hard
- id: moment-of-inertia
  type: hard
- id: rotational-kinematics
  type: hard
- id: center-of-mass
  type: soft
- id: circular-motion-dynamics
  type: soft
- id: static-equilibrium
  type: soft
- id: cross-product
  type: hard
- id: converting-degrees-and-radians
  type: soft
builds-toward:
- angular-momentum
- conservation-of-angular-momentum
tags:
- rotational-dynamics
- torque
- moment-of-inertia
- angular-acceleration
stage: formal-systems
status: validated
---
# Rotational Dynamics: Newton's Second Law for Rotation

## Core Idea
The rotational analog of Newton's second law is Στ = Iα: the net torque on a rigid body about a fixed axis equals its moment of inertia times its angular acceleration. This equation governs all rotational dynamics, from spinning tops to rolling cylinders. For rolling-without-slipping problems, linear and rotational equations couple through the constraint a = αr.

## How It's Best Learned
Draw a free-body diagram, compute all torques about the rotation axis, set Στ = Iα. For rolling objects, write both ΣF = ma (linear) and Στ = Iα (rotational) and connect them via the no-slip condition a = αr.

## Common Misconceptions
- Applying rotational dynamics without computing torques — net torque, not net force, drives angular acceleration.
- Using the wrong axis for computing I and τ — they must be computed about the same axis.

## Explainer

Newton's second law for linear motion is the central equation of classical mechanics: the net force on an object equals its mass times its linear acceleration (ΣF = ma). You've now built all the ingredients to write the exact rotational analog. Your study of torque established that torque is the rotational cause of angular acceleration — it's the "twisting force" that depends on both the force applied and how far from the axis it acts. Your study of moment of inertia established that I is the rotational analog of mass — it measures how a body's mass is distributed relative to the rotation axis, and therefore how resistant the body is to changes in its rotational motion. Put these together: **Στ = Iα**. Net torque drives angular acceleration, with moment of inertia as the proportionality constant.

The analogy table is worth internalizing explicitly: force F ↔ torque τ; mass m ↔ moment of inertia I; linear acceleration a ↔ angular acceleration α; linear momentum p = mv ↔ angular momentum L = Iω. Every theorem you know about linear dynamics has a rotational counterpart with this substitution. The equation Στ = Iα is not a new law — it is the rotational expression of the same underlying physics as F = ma. This is why your work on rotational kinematics (relating θ, ω, α) maps exactly onto the kinematic equations for linear motion.

The **cross product** (from your prerequisites) reveals why torque is a vector. Torque τ = r × F depends not just on the magnitudes of the position vector r and the force F, but on the angle between them: τ = rF sin θ. A force applied directly toward or away from the rotation axis (θ = 0° or 180°) produces zero torque — it cannot cause rotation. A force applied perpendicular to r (θ = 90°) produces maximum torque. The direction of τ = r × F, given by the right-hand rule, tells you which axis the torque rotates around and in which sense. For 2D problems — a disk spinning in a plane, a door opening — you only need the magnitude, but the vector nature of torque is essential for 3D problems like gyroscopes and precession.

**Rolling without slipping** is the signature problem that combines linear and rotational dynamics. When a cylinder rolls down a ramp, friction at the contact point produces a torque that angularly accelerates the cylinder as it linearly accelerates down the slope. Write two equations: ΣF = ma (net linear force = mass × linear acceleration) and Στ = Iα (net torque about the center = moment of inertia × angular acceleration). The no-slip constraint connects them: a = αr, meaning the linear acceleration of the center equals the angular acceleration times the radius. Together, these three relationships uniquely determine both a and α. The fraction of total kinetic energy stored in rotation depends on I — which depends on how mass is distributed. A hollow cylinder (all mass at radius r, so I = mr²) stores more energy in rotation than a solid cylinder (I = ½mr²), which is why the solid cylinder reaches the bottom of a ramp faster: less of its energy is "tied up" in spinning.
