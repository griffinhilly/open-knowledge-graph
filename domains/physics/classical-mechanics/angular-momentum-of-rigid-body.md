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
- id: cross-product
  type: hard
builds-toward:
- conservation-of-angular-momentum
tags:
- angular-momentum
- rotation
- dynamics
stage: formal-systems
status: validated
---

# Angular Momentum of Rigid Body

## Core Idea
For a rigid body rotating about a fixed axis, angular momentum L = I ω, where I is the moment of inertia about that axis. The rotational equation of motion τ_net = I α = dL/dt shows that torque changes angular momentum, exactly as force changes linear momentum. When no external torque acts, L is conserved.

## Questions

```yaml
- question: "An ice skater spins with arms extended, then pulls her arms tightly to her body. A student argues: 'Her moment of inertia decreases, so her angular velocity stays the same and her angular momentum decreases.' What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing is wrong — a more compact body does rotate with less angular momentum."
    - "When no external torque acts, L = Iω is conserved. Decreasing I requires ω to increase proportionally — she spins faster, not at the same rate. Angular momentum does not decrease."
    - "The student is right that ω stays constant, but wrong about angular momentum — it stays the same, not decreases."
    - "The student is right that angular momentum decreases, but wrong about ω — it also decreases."
  answer: 1
  explanation: "In the absence of external torque (friction with the ice is negligible), angular momentum L = Iω is conserved. If the skater reduces her moment of inertia I by pulling her arms in, ω must increase so that the product Iω remains constant. This is the classic demonstration of conservation of angular momentum: the same total rotational quantity is now distributed over a body with lower rotational inertia, so it spins faster. The student confused 'more compact' with 'less momentum,' but L is conserved — its redistribution between I and ω is the whole point."

- question: "The rotational equation τ_net = dL/dt is described as the exact rotational analog of Newton's second law. Which pairing best captures this analogy?"
  type: multiple-choice
  options:
    - "Force ↔ torque, mass ↔ angular velocity, linear acceleration ↔ moment of inertia."
    - "Force ↔ torque, mass ↔ moment of inertia, linear momentum ↔ angular momentum."
    - "Work ↔ torque, kinetic energy ↔ angular momentum, power ↔ angular velocity."
    - "Force ↔ angular velocity, mass ↔ moment of inertia, linear acceleration ↔ angular acceleration."
  answer: 1
  explanation: "Newton's second law: F_net = dp/dt, where p = mv (mass × velocity). The rotational analog: τ_net = dL/dt, where L = Iω (moment of inertia × angular velocity). The correspondence is: force ↔ torque (causes change), mass ↔ moment of inertia (resistance to change), linear momentum ↔ angular momentum (quantity of motion). For constant I, this becomes τ = Iα, mirroring F = ma with I playing the role of m and α playing the role of a."

- question: "If no external torque acts on a spinning rigid body, its angular momentum remains constant in both magnitude and direction."
  type: true-false
  answer: true
  explanation: "τ_net = dL/dt implies that when τ_net = 0, L is constant — not just its magnitude but the entire vector, including direction. This is why a gyroscope resists tipping: applying a torque changes the direction of L (causing precession) rather than reducing its magnitude, but without any torque, both the spin rate and the spin axis remain fixed. Conservation of angular momentum is a direct consequence of zero net external torque."

- question: "For any rotating rigid body, the angular momentum vector L generally points in the same direction as the angular velocity vector ω."
  type: true-false
  answer: false
  explanation: "L ∥ ω only when the rotation is about a principal axis (an eigenvector of the inertia tensor). For rotation about an arbitrary axis, L = Iω where I is the full 3×3 inertia tensor matrix, and the matrix multiplication generally produces a vector not parallel to ω. This misalignment is why an asymmetric object thrown in the air wobbles: ω and L point in different directions, and ω precesses around L. Stable, non-wobbling rotation occurs only about the principal axes."

- question: "Why does a spinning ice skater spin faster when she pulls her arms in? Name the physical principle and explain the mechanism."
  type: short-answer
  answer: "Conservation of angular momentum. When no external torque acts on the skater, L = Iω is constant. Pulling her arms inward brings mass closer to the rotation axis, reducing her moment of inertia I. Since L must remain fixed, ω = L/I must increase proportionally — the same total angular momentum is now carried by a body with lower rotational inertia, so it rotates faster. The mechanism is the direct trade-off between I and ω enforced by the conservation law."
  explanation: "This is the clearest everyday demonstration of angular momentum conservation. The same principle explains why a collapsing protostellar cloud spins up into a rapidly rotating star, and why a diver pulls into a tuck to spin faster before unfolding for entry."
```

## Explainer

You already know that for a point particle, **angular momentum** is **L** = **r** × **p** — a vector pointing perpendicular to the plane of rotation, with magnitude L = mvr for circular motion. A rigid body is simply a collection of particles all constrained to move together. Its total angular momentum is the sum of the angular momenta of every constituent particle. For rotation about a fixed axis, this sum collapses elegantly: each particle contributes m_i v_i r_i = m_i r_i² ω, and summing over all particles gives L = (Σ m_i r_i²) ω = **I ω**, where I is the **moment of inertia** — the rotational analog of mass, measuring how mass is distributed relative to the rotation axis.

The analogy with linear dynamics is exact and worth internalizing. Newton's second law says F_net = dp/dt: net force equals the rate of change of linear momentum. The rotational counterpart is **τ_net = dL/dt**: net torque equals the rate of change of angular momentum. For a rigid body with fixed axis and constant I, this becomes τ_net = I α, the rotational analog of F = ma. The **cross product** you studied lets you compute torque precisely: **τ** = **r** × **F**, so only the force component perpendicular to the moment arm produces torque, and the direction of **τ** (and thus the change in **L**) is given by the right-hand rule.

The most powerful consequence is **conservation of angular momentum**: when τ_net = 0, L = Iω is constant. A spinning ice skater pulling in her arms decreases I (mass moves closer to the axis), so ω must increase to keep L fixed — she spins faster. A gyroscope resists reorientation because a torque applied to it changes the direction of **L** without reducing its magnitude, causing **precession** rather than tipping over. Both effects follow from the same equation: dL/dt = τ_net. If that torque is zero in magnitude, L is constant in both magnitude and direction.

For rotation about an arbitrary axis (not necessarily a symmetry axis), the full picture requires the **inertia tensor** — a 3×3 matrix relating the angular velocity vector **ω** to the angular momentum vector **L** via **L** = **I** **ω**. The surprising result is that **L** and **ω** are not generally parallel: a body can spin in one direction while its angular momentum points in another. This is why wobbling occurs when an asymmetric object is thrown. Along special axes called **principal axes**, however, **L** and **ω** are parallel and the motion is stable — these are the eigenvectors of the inertia tensor. Understanding this connects the mechanics you've learned to matrix algebra and shows why rigid body dynamics is richer and more complex than the fixed-axis case that the formula L = Iω summarizes.
