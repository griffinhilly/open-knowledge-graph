---
id: euler-equations-rigid-body-rotation
title: Euler's Equations for Rigid Body Rotation
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: rotation-about-arbitrary-axis
  type: hard
- id: conservation-of-angular-momentum-mechanics
  type: soft
builds-toward:
- gyroscopic-motion-and-stability
tags:
- euler-equations
- rigid-bodies
- dynamics
stage: formal-systems
status: draft
---

# Euler's Equations for Rigid Body Rotation

## Core Idea
Euler's equations (τ = Iα + ω × Iω) describe how torques cause angular acceleration and precession in a rotating rigid body. In the body's principal axis frame, these three decoupled equations reveal that rotation about the maximum and minimum inertia axes is stable, while rotation about the intermediate axis is unstable.

## Explainer

From your study of rotation about an arbitrary axis, you know that angular momentum **L** = **I**ω, where **I** is the inertia tensor. What makes rigid body dynamics subtle is that **I** is attached to the body: as the body rotates, the inertia tensor rotates with it. This means that even if angular momentum is constant (no torque), the angular velocity vector **ω** can still change direction — because the body's moment of inertia about any fixed axis changes as it spins. Euler's equations are the mathematical consequence of accounting for this rotating frame.

The key step is switching from an inertial frame to the **body-fixed frame** — the frame that rotates with the object. In that frame, the inertia tensor **I** is constant (no rotating entries to track), which makes equations of motion far simpler. The price you pay is that Newton's law acquires an extra term from the frame's rotation. Taking the time derivative of **L** in the rotating frame introduces a **ω × L** cross product, yielding **τ** = **I**(dω/dt) + **ω** × (**I**ω). Written along the three **principal axes** (the axes that diagonalize **I**), this expands to the three scalar Euler equations: τ₁ = I₁(dω₁/dt) − (I₂−I₃)ω₂ω₃, and cyclically for the other two axes.

The coupling terms like (I₂−I₃)ω₂ω₃ are the physical signature of **gyroscopic effects**. Even in torque-free motion (τ = 0), if the body spins about a direction that is *not* a principal axis, the ω components interact and drive each other — this is precession. Throw a book spinning imperfectly about any axis and watch it wobble: that wobble is Euler's equations in action. The stability analysis is striking: a body freely rotating about its maximum or minimum inertia axis is stable (small perturbations lead to small wobbles), but rotation about the **intermediate axis** is unstable — perturbations grow. This is the **tennis racket theorem**, or intermediate axis theorem, observable with any roughly rectangular object.

In practical engineering problems — gyroscopes, satellites, spinning turbines — Euler's equations must be integrated numerically or analyzed for special cases. One important special case is **torque-free axisymmetric motion** (two equal principal moments of inertia, like a symmetric top). Here the equations decouple partially, and angular velocity traces a cone around the symmetry axis — called **body-cone and space-cone precession**. Another special case is **steady precession** under gravity, the classical gyroscope solution: a rapidly spinning top precesses slowly around the vertical instead of falling, because the gravitational torque goes into changing the direction of **L**, not its magnitude.

Your prerequisite on angular momentum conservation sets up the conservation law (τ = dL/dt in the inertial frame). Euler's equations translate that law into coordinates that rotate with the body, making it tractable for real three-dimensional shapes. The next step — gyroscopic motion and stability — will use Euler's equations directly to analyze more complex precession and nutation behavior in engineering devices like gyroscopes and attitude control systems.
