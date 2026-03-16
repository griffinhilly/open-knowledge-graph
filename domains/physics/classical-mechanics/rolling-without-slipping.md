---
id: rolling-without-slipping
title: Rolling Without Slipping
domain: physics
course: classical-mechanics
prerequisites:
- id: rotational-kinematics
  type: hard
- id: circular-motion-kinematics
  type: soft
builds-toward:
- rotational-kinetic-energy
tags:
- rolling
- kinematics
- constraints
stage: formal-systems
status: draft
---

# Rolling Without Slipping

## Core Idea
Rolling without slipping enforces the kinematic constraint v_CM = R ω: the center-of-mass velocity equals radius times angular velocity. This couples translation and rotation, reducing degrees of freedom. In energy analysis, rolling objects combine translational KE (½ m v²) and rotational KE (½ I ω²); the fraction going to each depends on the moment of inertia (e.g., 1/3 rotational for a solid cylinder, 2/5 for a solid sphere).

## Explainer

From rotational kinematics, you know that rotating objects have angular velocity ω (how fast they spin) and that points on a rotating body have tangential speeds that depend on their distance from the axis. Rolling without slipping takes this further by linking rotation and translation: when a wheel rolls on a surface without slipping, every point on the rim has zero velocity *relative to the ground* at the instant it contacts the surface. This is the physical meaning of "no slipping" — the contact point is momentarily stationary.

From that contact condition, the **rolling constraint** v_CM = Rω follows directly. The center of the wheel moves forward at speed v_CM. The contact point's velocity has two contributions: the translational velocity of the whole wheel (v_CM, forward) and the tangential velocity of the rim due to rotation (Rω, backward at the contact point). For zero slip, these must cancel: v_CM = Rω. This single equation couples the two degrees of freedom (translation and rotation) into one. Once you know v_CM, you know ω, and vice versa.

This constraint transforms energy problems. A sliding block on a frictionless surface converts all potential energy to translational KE: ½mv². A rolling object splits energy between translation and rotation. The total kinetic energy is ½mv² + ½Iω². Using v = Rω to eliminate ω gives KE = ½mv²(1 + I/mR²). The factor (1 + I/mR²) tells you the penalty for being a rolling object: a hoop (I = mR²) has twice the KE of a sliding point mass at the same speed, because half its energy is rotational. A solid sphere (I = 2mR²/5) has a factor of 7/5. This is why a solid sphere rolls down a ramp faster than a hollow shell of the same mass and radius — the shell must put more energy into rotation.

A common point of confusion: the static friction force at the contact point does no work during rolling without slipping (because the contact point has zero instantaneous velocity), but it is still essential — it is what creates the torque that accelerates the rotation. Remove friction (ice, for example) and the wheel can spin without rolling, or slide without spinning, because the constraint is broken. This is why rolling problems always specify whether the surface is rough enough to maintain rolling without slipping, and why that condition determines whether you can use v = Rω to link translational and rotational quantities.
