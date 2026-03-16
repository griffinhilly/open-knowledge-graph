---
id: lorentz-transformation
title: Lorentz Transformation
domain: physics
course: modern-physics
prerequisites:
- id: time-dilation
  type: hard
- id: length-contraction
  type: hard
- id: operations-with-radicals
  type: soft
- id: linear-transformations
  type: soft
- id: linear-transformations-definition
  type: soft
- id: matrix-operations
  type: soft
builds-toward:
- relativistic-velocity-addition
- relativistic-momentum-energy
tags:
- relativity
- coordinates
- spacetime
- transformation
stage: advanced
status: validated
---

# Lorentz Transformation

## Core Idea
The Lorentz transformation gives the precise relationship between the spacetime coordinates (t, x, y, z) assigned to an event in one inertial frame and those assigned in another frame moving with velocity v along the x-axis: x′ = γ(x − vt), t′ = γ(t − vx/c²), with y′ = y and z′ = z. These replace the Galilean transformation of Newtonian mechanics and reduce to it when v ≪ c. The invariant spacetime interval s² = c²t² − x² − y² − z² is preserved under Lorentz transformations, playing the role that Euclidean distance plays in ordinary rotations.

## How It's Best Learned
Verify that the transformation preserves the invariant interval algebraically. Rederive time dilation and length contraction as special cases. Practice applying the transformation to concrete events — e.g., a firecracker exploding at specific coordinates.

## Common Misconceptions
- The Lorentz transformation is just a coordinate change with no physical meaning — it encodes genuine physical differences in what events are simultaneous.
- t′ depends only on t — the mixing of space and time (t′ depends on x) is precisely the non-Galilean content.

## Explainer

You already know two relativistic effects from direct analysis: moving clocks run slow (time dilation) and moving rulers contract (length contraction). The Lorentz transformation is not a new piece of physics — it is the single transformation that contains both results and generates all other relativistic kinematic effects from one unified formula. Think of it as the master equation of special relativity kinematics.

The starting point is a comparison with the familiar **Galilean transformation**: x′ = x − vt, t′ = t. This says that frame S′ (moving at velocity v relative to S) just shifts the x-coordinate, and time is universal. This works perfectly for everyday speeds. Special relativity replaces it with x′ = γ(x − vt), t′ = γ(t − vx/c²), where γ = 1/√(1 − v²/c²). Two things are different. First, there is a factor γ stretching the spatial term — that is the origin of length contraction. Second, and most importantly, **time is mixed with space**: t′ depends on both t and x. This is the heart of relativity. Two events that happen at the same time (t₁ = t₂) but different places (x₁ ≠ x₂) in frame S are generally *not* simultaneous in frame S′. Simultaneity is relative.

To see how the known effects emerge: for time dilation, consider a clock at rest at x = 0 in S (so x = 0 for both events — "tick" and "tock"). Then t′ = γt, so the time interval is longer in S′ — moving clocks run slow. For length contraction, consider a rod at rest in S′. Its two endpoints must be measured simultaneously in S (t fixed, x₁ and x₂ measured at the same t). Using x = γ(x′ + vt′), the length in S works out to L₀/γ — the rod is shorter in the frame where it is moving.

The **invariant spacetime interval** s² = c²t² − x² is preserved under Lorentz transformations: it takes the same value in all inertial frames. This is the spacetime analog of the Euclidean distance r² = x² + y² being preserved under spatial rotations. In fact, the Lorentz transformation is precisely a "rotation" in spacetime — but with a hyperbolic geometry (the minus sign in s²) rather than Euclidean. The parameter that plays the role of angle is the **rapidity** φ = tanh⁻¹(v/c). Writing the transformation in terms of rapidity (x′ = x cosh φ − ct sinh φ, ct′ = ct cosh φ − x sinh φ) makes the analogy with spatial rotations exact, and reveals why relativistic velocity addition looks like adding rapidities rather than velocities: φ_total = φ₁ + φ₂, which is why you can never exceed c no matter how many boosts you stack.
