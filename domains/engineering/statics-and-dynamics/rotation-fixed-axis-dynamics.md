---
id: rotation-fixed-axis-dynamics
title: 'Rotation about a Fixed Axis: Kinematics and Kinetics'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: kinematics-rigid-body-rotation
  type: hard
- id: moment-of-inertia-about-centroid
  type: hard
builds-toward:
- rigid-body-plane-motion-analysis
tags:
- fixed-axis
- rotation
- angular-acceleration
- torque
stage: formal-systems
status: draft
---

# Rotation about a Fixed Axis: Kinematics and Kinetics

## Core Idea
For a rigid body rotating about a fixed axis, angular kinematics parallels linear kinematics: ω = dθ/dt, α = dω/dt. The kinetic equation is ΣM = I α, where M is the net torque and I is the moment of inertia about the axis. Kinetic energy is KE = ½I ω². These equations fully describe the rotational motion of wheels, rotors, and other rotating machinery.

## Explainer

From rigid-body kinematics you know how to describe the geometry of rotation: angular position θ, velocity ω = dθ/dt, and acceleration α = dω/dt are related by the same calculus as linear position, velocity, and acceleration. From moment of inertia, you know how mass distributed around an axis resists rotational acceleration. Fixed-axis dynamics brings these threads together: it answers the question of *what causes* the angular acceleration you've been describing kinematically.

The governing equation is ΣM = Iα, where ΣM is the net moment (torque) of all forces about the fixed axis, I is the mass moment of inertia about that axis, and α is the resulting angular acceleration. This is the rotational form of Newton's second law, with moment replacing force, moment of inertia replacing mass, and angular acceleration replacing linear acceleration. The analogy is exact: doubling the torque doubles the acceleration, and doubling the moment of inertia halves it. A heavy flywheel (large I) resists changes in rotation; a lightweight spool (small I) responds quickly to applied torques.

The kinetic energy of a rotating rigid body is KE = ½Iω², perfectly mirroring the translational ½mv². This means you can apply energy methods — work-energy theorem — to rotational problems directly. The net work done by all torques equals the change in ½Iω². For a wheel accelerating from rest under a constant applied torque M, the kinetic energy after rotating through angle θ is simply W = Mθ, and you can solve for the final ω without integrating the equation of motion. This work-energy approach is often faster than the ΣM = Iα approach when the question asks about speed at a given position rather than acceleration at a given instant.

To solve fixed-axis dynamics problems, the standard procedure is: (1) identify the fixed axis and compute I about it using the parallel-axis theorem if needed; (2) draw a free-body diagram and identify all forces and their moment arms about the fixed axis; (3) compute ΣM and divide by I to find α; (4) integrate kinematically if time or angle information is needed. For problems involving a rope unwinding from a pulley, or a disk rolling without slip on a fixed axle, this procedure gives the complete solution. The key constraint is that the axis truly does not translate — when it does, you're in the more complex territory of general plane motion, where both translation and rotation must be tracked simultaneously.
