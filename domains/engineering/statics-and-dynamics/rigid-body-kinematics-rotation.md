---
id: rigid-body-kinematics-rotation
title: Rigid Body Kinematics — Fixed-Axis Rotation
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: kinematics-particles-rectilinear
  type: hard
- id: angular-momentum
  type: soft
builds-toward:
- rigid-body-kinematics-general-motion
- rigid-body-kinetics-force-acceleration
tags:
- dynamics
- kinematics
- rotation
- angular velocity
- angular acceleration
- fixed-axis rotation
stage: formal-systems
status: draft
---

# Rigid Body Kinematics — Fixed-Axis Rotation

## Core Idea
Fixed-axis rotation describes the motion of a rigid body that rotates about a stationary axis. Every point in the body moves in a circular arc centered on the axis, so the kinematics of any point can be expressed in terms of the angular quantities: angular position theta, angular velocity omega = d(theta)/dt, and angular acceleration alpha = d(omega)/dt. The relationships mirror rectilinear particle kinematics: alpha = d(omega)/dt, omega = d(theta)/dt, and alpha*d(theta) = omega*d(omega). For constant angular acceleration, the familiar constant-acceleration equations apply with theta, omega, and alpha replacing s, v, and a. The velocity and acceleration of any point P at radial distance r from the axis are v = omega*r (tangential), a_t = alpha*r (tangential acceleration), and a_n = omega^2*r (centripetal acceleration directed toward the axis).

## How It's Best Learned
Draw the analogy to rectilinear kinematics explicitly: theta <-> s, omega <-> v, alpha <-> a. Solve constant angular acceleration problems using the rotational kinematic equations first, then find the linear velocity and acceleration of specific points using the r-omega and r-alpha relationships. Work problems that combine angular kinematics with gear or belt connections between rotating bodies.

## Common Misconceptions
- Forgetting the centripetal (normal) acceleration component a_n = omega^2*r for a point on the rotating body — even if angular acceleration is zero, points still have centripetal acceleration whenever omega is nonzero.
- Using diameter instead of radius when computing v = omega*r or a_t = alpha*r.
- Applying the constant angular acceleration equations when alpha varies with time or position, which requires integration instead.
