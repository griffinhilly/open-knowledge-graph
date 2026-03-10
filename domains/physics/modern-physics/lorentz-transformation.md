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
builds-toward:
- relativistic-velocity-addition
- relativistic-momentum-energy
tags:
- relativity
- coordinates
- spacetime
- transformation
stage: advanced
status: draft
---

# Lorentz Transformation

## Core Idea
The Lorentz transformation gives the precise relationship between the spacetime coordinates (t, x, y, z) assigned to an event in one inertial frame and those assigned in another frame moving with velocity v along the x-axis: x′ = γ(x − vt), t′ = γ(t − vx/c²), with y′ = y and z′ = z. These replace the Galilean transformation of Newtonian mechanics and reduce to it when v ≪ c. The invariant spacetime interval s² = c²t² − x² − y² − z² is preserved under Lorentz transformations, playing the role that Euclidean distance plays in ordinary rotations.

## How It's Best Learned
Verify that the transformation preserves the invariant interval algebraically. Rederive time dilation and length contraction as special cases. Practice applying the transformation to concrete events — e.g., a firecracker exploding at specific coordinates.

## Common Misconceptions
- The Lorentz transformation is just a coordinate change with no physical meaning — it encodes genuine physical differences in what events are simultaneous.
- t′ depends only on t — the mixing of space and time (t′ depends on x) is precisely the non-Galilean content.
