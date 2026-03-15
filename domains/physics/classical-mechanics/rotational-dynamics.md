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
