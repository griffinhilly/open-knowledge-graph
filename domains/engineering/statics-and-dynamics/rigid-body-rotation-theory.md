---
id: rigid-body-rotation-theory
title: 'Rigid Body Rotation: Angular Velocity and Acceleration'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: rotation-fixed-axis-dynamics
  type: hard
builds-toward:
- principal-moments-of-inertia
- euler-equations-rigid-body-rotation
tags:
- rotation
- rigid-bodies
- kinematics
stage: formal-systems
status: draft
---

# Rigid Body Rotation: Angular Velocity and Acceleration

## Core Idea
A rigid body rotating about a fixed axis has all points moving in circles with the same angular velocity ω and angular acceleration α. The velocity and acceleration of any point depend on its distance from the axis; this kinematic relationship v = ωr is the foundation for analyzing rotational dynamics and energy.

## Explainer

When you studied rotation about a fixed axis, you learned that **angular velocity** ω describes how fast a body is spinning and **angular acceleration** α describes how that spin is changing. The key insight extending this to a full rigid body is that every point in the body shares the same ω and α — that is precisely what makes it *rigid*. The body rotates as one piece; no point can spin faster than another.

Yet even though ω is the same for all points, the *linear* velocity varies dramatically with distance from the axis. A point at radius r has speed v = ωr; a point twice as far from the axis moves twice as fast. This is why the tip of a helicopter rotor blade moves near the speed of sound while its root barely moves at all. Similarly, the tangential acceleration (due to changing speed) is aₜ = αr, and the centripetal (normal) acceleration pointing toward the axis is aₙ = ω²r. These two acceleration components are perpendicular: aₜ changes the speed, aₙ changes the direction of velocity. Both grow with radius, so points far from the axis experience much larger total accelerations.

The angular quantities ω and α behave exactly like their linear counterparts v and a, just mapped to rotation. The kinematic equations for constant angular acceleration are direct analogues of the constant-acceleration linear equations: θ = θ₀ + ω₀t + ½αt² mirrors x = x₀ + v₀t + ½at², and ω² = ω₀² + 2αΔθ mirrors v² = v₀² + 2aΔx. This analogy is not coincidental — both sets of equations come from the same calculus of integration under constant derivatives.

Understanding these kinematics sets up the dynamics: torque, moment of inertia, and the rotational form of Newton's second law (τ = Iα) are the rotational equivalents of force, mass, and F = ma. The relationship v = ωr also connects the translational and rotational energy of rolling objects, and it underpins how gears, pulleys, and transmissions convert between torques and speeds. Any time you need to relate linear motion of a point to the rotation of the body it belongs to, v = ωr and aₜ = αr are your starting equations.
