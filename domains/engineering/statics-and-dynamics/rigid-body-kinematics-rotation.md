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

## Questions

```yaml
- question: "A wheel spins at a constant angular velocity (α = 0). What is the acceleration of a point on the rim?"
  type: multiple-choice
  options:
    - "Zero — since angular acceleration is zero, no linear acceleration exists"
    - "Only tangential acceleration, directed along the rim, because the speed is changing"
    - "Only centripetal acceleration, directed toward the rotation axis, with magnitude ω²r"
    - "Both centripetal and tangential acceleration, because the velocity vector is always changing"
  answer: 2
  explanation: "At constant angular velocity, α = 0, so tangential acceleration a_t = αr = 0. However, the point is moving in a circle — its velocity direction is constantly changing even though its speed is constant. This change in direction requires centripetal (normal) acceleration a_n = ω²r, directed radially inward toward the axis. This is the most common misconception: students assume 'constant speed' means 'no acceleration,' forgetting that acceleration is a vector and that changing direction counts. A point on a spinning wheel at constant ω has nonzero centripetal acceleration at every instant."

- question: "A point P is located at radius r = 0.4 m on a rotating disk with ω = 5 rad/s and α = 3 rad/s². The tangential and centripetal (normal) accelerations of P are:"
  type: multiple-choice
  options:
    - "a_t = 3 m/s², a_n = 5 m/s² — using a = αr and a = ωr directly"
    - "a_t = 1.2 m/s², a_n = 10 m/s² — using a_t = αr and a_n = ω²r"
    - "a_t = 0.6 m/s², a_n = 2 m/s² — dividing ω and α by r"
    - "a_t = 1.2 m/s², a_n = 5 m/s² — using a_t = αr and a_n = ωr"
  answer: 1
  explanation: "Tangential acceleration a_t = αr = 3 × 0.4 = 1.2 m/s². Centripetal acceleration a_n = ω²r = 25 × 0.4 = 10 m/s². Note that centripetal acceleration uses ω² (not ω) multiplied by r. Option D is a common error: using ωr for centripetal acceleration instead of ω²r. Option A uses α and ω directly without multiplying by r. The total acceleration magnitude is √(a_t² + a_n²) = √(1.44 + 100) ≈ 10.1 m/s², showing that centripetal acceleration dominates at moderate angular speeds."

- question: "A rigid body rotating at constant angular velocity (α = 0) has zero acceleration at every point."
  type: true-false
  answer: false
  explanation: "Every point on a rotating body (except points on the axis itself) has centripetal acceleration a_n = ω²r directed toward the rotation axis, regardless of whether angular acceleration is zero. Constant angular velocity means zero tangential acceleration (a_t = αr = 0) — the speed of each point is not changing — but the direction of the velocity vector is continuously changing as the point travels in a circle. This change in direction is centripetal acceleration. Only when ω = 0 (body not rotating) does a_n also vanish. This is a critical point: 'no angular acceleration' ≠ 'no linear acceleration.'"

- question: "The centripetal acceleration of a point P at radius r on a rotating rigid body is directed toward the rotation axis and has magnitude ω²r."
  type: true-false
  answer: true
  explanation: "This is the correct formula and direction for centripetal acceleration in fixed-axis rotation. The centripetal acceleration keeps point P moving in a circle by continuously redirecting its velocity vector toward the center (the rotation axis). Its magnitude is ω²r — note it depends on ω squared, so even modest angular speeds produce significant centripetal accelerations, especially at large r. This is distinct from tangential acceleration a_t = αr, which changes the speed and points along the arc (tangent to the circle). Both components are always perpendicular to each other."

- question: "Why does a point on a spinning wheel have centripetal acceleration even when the wheel rotates at constant speed? What causes this acceleration, and in what direction does it point?"
  type: short-answer
  answer: "Centripetal acceleration arises because the velocity of a point on the rim is constantly changing direction, even when its magnitude (speed) is constant. Velocity is a vector — any change in direction constitutes acceleration, even without a change in speed. As the point travels in a circle, its velocity vector must continuously rotate to remain tangent to the circular path. The rate of change of that velocity vector points radially inward, toward the rotation axis, with magnitude ω²r. This inward acceleration is centripetal acceleration — it is the acceleration required to maintain circular motion, not a consequence of speeding up."
  explanation: "A common intuition failure is equating 'acceleration' with 'speeding up or slowing down.' In rectilinear motion, acceleration does change speed. But in circular motion, even at constant speed, the direction of motion changes at every instant, and Newton's second law requires a net force (and therefore acceleration) to produce any change in velocity, including a change in direction. The centripetal acceleration a_n = ω²r is the vector pointing from point P toward the axis that accounts for this continuous direction change. Forgetting this component leads to errors in any dynamics problem involving rotating components."
```

## Explainer

In particle kinematics you described motion along a straight line using position s, velocity v = ds/dt, and acceleration a = dv/dt. Fixed-axis rotation is the direct rotational analogue: replace the linear coordinates with angular coordinates. **Angular position** θ (radians) locates the body, **angular velocity** ω = dθ/dt describes how fast it spins, and **angular acceleration** α = dω/dt describes how that spin rate changes. Every kinematic equation from rectilinear motion has an identical twin in rotation — just swap s → θ, v → ω, a → α. If α is constant, the constant-acceleration equations apply: ω = ω₀ + αt, θ = θ₀ + ω₀t + ½αt², and ω² = ω₀² + 2α(θ − θ₀). This one-to-one correspondence means you already know half of rotational kinematics — you just need to translate.

The connection between the rotation of the body and the motion of any specific **point P** on that body is where radial distance r enters. Every point traces a circular arc, so its speed is tangential: v = ωr. This is not an approximation — for a rigid body, the entire body rotates as one unit, so a point twice as far from the axis moves twice as fast. The acceleration of point P has two components. The **tangential acceleration** a_t = αr points along the arc direction and changes the speed. The **centripetal (normal) acceleration** a_n = ω²r points radially inward toward the rotation axis and arises purely from the changing direction of the velocity vector. Crucially, a_n is present whenever ω ≠ 0, even if α = 0 — a spinning body at constant speed still requires centripetal acceleration at every point on it.

When dealing with connected rotating parts — a motor shaft driving a gear, which drives a belt, which drives another shaft — you translate between components using the constraint that belt speed or contact speed must match at the interface. If gear A (radius r_A) meshes with gear B (radius r_B), then their contact speeds are equal: ω_A·r_A = ω_B·r_B. This relationship governs all gear trains, belt-pulley systems, and chain drives. Write this constraint first, use it to express all angular velocities in terms of one unknown, then apply whatever kinematics equation the problem requires.

When α is not constant, you cannot use the constant-α formulas. Instead, you must integrate. If α is given as a function of time, integrate once to get ω(t) and again for θ(t). If α is given as a function of θ, use the identity α·dθ = ω·dω (obtained by writing α = dω/dt = (dω/dθ)(dθ/dt) = ω·dω/dθ) and integrate to find ω as a function of θ directly. Recognizing which form of α you have — time-dependent or position-dependent — determines which integration strategy to apply, and choosing the wrong one is a common source of algebraic dead-ends.


