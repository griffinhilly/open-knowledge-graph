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

## Explainer

In particle kinematics you described motion along a straight line using position s, velocity v = ds/dt, and acceleration a = dv/dt. Fixed-axis rotation is the direct rotational analogue: replace the linear coordinates with angular coordinates. **Angular position** θ (radians) locates the body, **angular velocity** ω = dθ/dt describes how fast it spins, and **angular acceleration** α = dω/dt describes how that spin rate changes. Every kinematic equation from rectilinear motion has an identical twin in rotation — just swap s → θ, v → ω, a → α. If α is constant, the constant-acceleration equations apply: ω = ω₀ + αt, θ = θ₀ + ω₀t + ½αt², and ω² = ω₀² + 2α(θ − θ₀). This one-to-one correspondence means you already know half of rotational kinematics — you just need to translate.

The connection between the rotation of the body and the motion of any specific **point P** on that body is where radial distance r enters. Every point traces a circular arc, so its speed is tangential: v = ωr. This is not an approximation — for a rigid body, the entire body rotates as one unit, so a point twice as far from the axis moves twice as fast. The acceleration of point P has two components. The **tangential acceleration** a_t = αr points along the arc direction and changes the speed. The **centripetal (normal) acceleration** a_n = ω²r points radially inward toward the rotation axis and arises purely from the changing direction of the velocity vector. Crucially, a_n is present whenever ω ≠ 0, even if α = 0 — a spinning body at constant speed still requires centripetal acceleration at every point on it.

When dealing with connected rotating parts — a motor shaft driving a gear, which drives a belt, which drives another shaft — you translate between components using the constraint that belt speed or contact speed must match at the interface. If gear A (radius r_A) meshes with gear B (radius r_B), then their contact speeds are equal: ω_A·r_A = ω_B·r_B. This relationship governs all gear trains, belt-pulley systems, and chain drives. Write this constraint first, use it to express all angular velocities in terms of one unknown, then apply whatever kinematics equation the problem requires.

When α is not constant, you cannot use the constant-α formulas. Instead, you must integrate. If α is given as a function of time, integrate once to get ω(t) and again for θ(t). If α is given as a function of θ, use the identity α·dθ = ω·dω (obtained by writing α = dω/dt = (dω/dθ)(dθ/dt) = ω·dω/dθ) and integrate to find ω as a function of θ directly. Recognizing which form of α you have — time-dependent or position-dependent — determines which integration strategy to apply, and choosing the wrong one is a common source of algebraic dead-ends.


