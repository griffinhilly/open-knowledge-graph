---
id: relativistic-momentum-definition
title: Relativistic Momentum and Inertia
domain: physics
course: modern-physics
prerequisites:
- id: special-relativity-postulates
  type: hard
- id: momentum-and-impulse
  type: hard
builds-toward:
- relativistic-kinetic-energy
tags:
- special-relativity
- momentum
- dynamics
stage: advanced
status: draft
---

# Relativistic Momentum and Inertia

## Core Idea
Relativistic momentum is defined as p = γmv, where γ is the Lorentz factor (1/√(1−v²/c²)). Unlike classical momentum, relativistic momentum approaches infinity as velocity approaches light speed, preventing any massive object from reaching c. This modification preserves momentum conservation in all inertial frames.

## Explainer

From your study of classical momentum, you know that p = mv and that applying a constant force to an object produces a constant acceleration — doubling the force doubles the rate of velocity change. Special relativity breaks this simple picture. Once you accept the two postulates — that the laws of physics are the same in all inertial frames, and that the speed of light c is the same for all observers — a contradiction emerges: classical momentum is not conserved under Lorentz transformations. The fix requires redefining momentum in a way that respects Lorentz symmetry.

The **Lorentz factor** γ = 1/√(1−v²/c²) is the key object. At everyday speeds (v ≪ c), γ ≈ 1 and p = γmv ≈ mv — classical mechanics is recovered, which is why Newton's laws work so well for cars and baseballs. But as v approaches c, γ grows without bound. At 99% of c, γ ≈ 7; at 99.9%, γ ≈ 22. The relativistic momentum p = γmv therefore also grows without bound as v → c, even though v itself is bounded. This is the mechanism that makes c a speed limit: to accelerate a massive object to c would require infinite momentum, and thus infinite energy.

A useful way to build intuition is to think about **effective inertia**. In classical mechanics, inertia (resistance to acceleration) is simply the rest mass m. In relativity, the resistance to further acceleration grows as γm — an object already moving at 0.99c is about 7 times harder to accelerate than the same object at rest. The faster it moves, the more energy you must supply to gain each additional increment of speed, and the increments of speed you gain keep shrinking. This is not because the mass literally increases (the invariant rest mass m is constant), but because the relationship between force, acceleration, and velocity is fundamentally different.

**Momentum conservation** is the deeper reason for this definition. Consider a symmetric collision viewed from two different inertial frames. With classical momentum, the collision appears to violate conservation in one of the frames after a Lorentz boost. With relativistic momentum p = γmv, conservation holds in every inertial frame simultaneously. This is what singles out γmv as the correct definition — it is the quantity that transforms consistently under the Lorentz transformations you already know. The relativistic momentum also forms part of the **four-momentum** (E/c, p), a Lorentz four-vector, which is why relativistic energy and momentum are naturally unified — a connection you will develop next in relativistic kinetic energy.
