---
id: angular-momentum-of-rigid-body
title: Angular Momentum of Rigid Body
domain: physics
course: classical-mechanics
prerequisites:
- id: angular-momentum
  type: hard
- id: moment-of-inertia
  type: hard
- id: cross-product-3d
  type: hard
- id: matrices-intro
  type: soft
builds-toward:
- conservation-of-angular-momentum
tags:
- angular-momentum
- rotation
- dynamics
stage: formal-systems
status: draft
---

# Angular Momentum of Rigid Body

## Core Idea
For a rigid body rotating about a fixed axis, angular momentum L = I ω, where I is the moment of inertia about that axis. The rotational equation of motion τ_net = I α = dL/dt shows that torque changes angular momentum, exactly as force changes linear momentum. When no external torque acts, L is conserved.

## Explainer

You already know that for a point particle, **angular momentum** is **L** = **r** × **p** — a vector pointing perpendicular to the plane of rotation, with magnitude L = mvr for circular motion. A rigid body is simply a collection of particles all constrained to move together. Its total angular momentum is the sum of the angular momenta of every constituent particle. For rotation about a fixed axis, this sum collapses elegantly: each particle contributes m_i v_i r_i = m_i r_i² ω, and summing over all particles gives L = (Σ m_i r_i²) ω = **I ω**, where I is the **moment of inertia** — the rotational analog of mass, measuring how mass is distributed relative to the rotation axis.

The analogy with linear dynamics is exact and worth internalizing. Newton's second law says F_net = dp/dt: net force equals the rate of change of linear momentum. The rotational counterpart is **τ_net = dL/dt**: net torque equals the rate of change of angular momentum. For a rigid body with fixed axis and constant I, this becomes τ_net = I α, the rotational analog of F = ma. The **cross product** you studied lets you compute torque precisely: **τ** = **r** × **F**, so only the force component perpendicular to the moment arm produces torque, and the direction of **τ** (and thus the change in **L**) is given by the right-hand rule.

The most powerful consequence is **conservation of angular momentum**: when τ_net = 0, L = Iω is constant. A spinning ice skater pulling in her arms decreases I (mass moves closer to the axis), so ω must increase to keep L fixed — she spins faster. A gyroscope resists reorientation because a torque applied to it changes the direction of **L** without reducing its magnitude, causing **precession** rather than tipping over. Both effects follow from the same equation: dL/dt = τ_net. If that torque is zero in magnitude, L is constant in both magnitude and direction.

For rotation about an arbitrary axis (not necessarily a symmetry axis), the full picture requires the **inertia tensor** — a 3×3 matrix relating the angular velocity vector **ω** to the angular momentum vector **L** via **L** = **I** **ω**. The surprising result is that **L** and **ω** are not generally parallel: a body can spin in one direction while its angular momentum points in another. This is why wobbling occurs when an asymmetric object is thrown. Along special axes called **principal axes**, however, **L** and **ω** are parallel and the motion is stable — these are the eigenvectors of the inertia tensor. Understanding this connects the mechanics you've learned to matrix algebra and shows why rigid body dynamics is richer and more complex than the fixed-axis case that the formula L = Iω summarizes.
