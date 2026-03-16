---
id: rotational-kinetic-energy
title: Rotational Kinetic Energy
domain: physics
course: classical-mechanics
prerequisites:
- id: kinetic-energy
  type: hard
- id: moment-of-inertia
  type: hard
- id: rotational-kinematics
  type: hard
builds-toward:
- rolling-without-slipping
tags:
- kinetic-energy
- rotation
- energy
stage: formal-systems
status: draft
---

# Rotational Kinetic Energy

## Core Idea
A rotating object has kinetic energy KE_rot = ½ I ω², where I is the moment of inertia about the rotation axis and ω is angular velocity. This is the rotational analog of KE = ½ m v². For an object both rotating and translating, total KE = ½ m v_CM² + ½ I_CM ω², where both terms contribute to the energy.

## Explainer

You already know kinetic energy for a point mass: KE = ½mv². You know moment of inertia I as the rotational analog of mass — a measure of how hard it is to change rotational motion, reflecting both the amount of mass and how far that mass is distributed from the rotation axis. You know angular velocity ω as the rotational analog of linear velocity v. **Rotational kinetic energy** follows directly from substituting these analogs: KE_rot = ½Iω².

The analogy runs deep and is worth tracing explicitly. In translation, kinetic energy depends on inertia (m) and the square of velocity (v²). In rotation, kinetic energy depends on rotational inertia (I) and the square of angular velocity (ω²). The factor ½ arises for the same mathematical reason in both cases — it comes from integrating the work done to accelerate the object from rest. If you can calculate I for a rigid body about its axis (and you learned standard results: ½MR² for a solid disk, MR² for a hoop, 2/5 MR² for a solid sphere), computing rotational kinetic energy reduces to a straightforward substitution once ω is known.

The real power emerges when an object both rotates and translates simultaneously — like a wheel rolling down a ramp or a ball rolling across a floor. The **total kinetic energy** has two additive terms: translational KE of the center of mass moving through space (½mv_CM²) plus rotational KE about the center of mass (½I_CM ω²). Both terms are funded by the same source of energy — gravitational potential energy when rolling down an incline. This is why a hollow cylinder rolls slower to the bottom of a ramp than a solid sphere of the same mass and radius: the hollow cylinder concentrates its mass at large radius, giving it a larger I, so a greater fraction of the available potential energy is channeled into rotation and less into translational speed.

Energy methods using this framework are extremely efficient. For a rolling object on a frictionless incline, you can write the energy equation at two points: (½mv² + ½Iω² + mgh)_initial = (½mv² + ½Iω² + mgh)_final. The rolling-without-slipping constraint v_CM = Rω links the translational and rotational terms, making the equation solvable for the final speed without ever computing torques or angular accelerations step by step. This single equation replaces what would otherwise require separate translational and rotational Newton's laws and a careful treatment of the static friction force that sustains rolling.
