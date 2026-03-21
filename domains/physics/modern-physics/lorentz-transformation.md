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

## Questions

```yaml
- question: "Two firecrackers explode simultaneously (same t) but at different locations x₁ and x₂ in frame S. What does the Lorentz transformation predict about these events in frame S′, moving at velocity v relative to S?"
  type: multiple-choice
  options:
    - "They are simultaneous in S′ as well, since simultaneity is a physical fact independent of reference frame"
    - "They are generally not simultaneous in S′, because t′ = γ(t − vx/c²) depends on x as well as t"
    - "They are not simultaneous in S′ only if v > 0.5c"
    - "They are not simultaneous in S′ only if the events are causally connected"
  answer: 1
  explanation: "The key non-Galilean feature is that t′ depends on both t and x. For two events with equal t but different x, the t′ values differ: t′₁ = γ(t − vx₁/c²) ≠ γ(t − vx₂/c²) = t′₂ unless x₁ = x₂. This is relativity of simultaneity — a direct physical consequence of the x-term in the time transformation. In the Galilean transformation, t′ = t for all events regardless of position, so simultaneity is absolute. The Lorentz transformation replaces this with frame-dependent simultaneity at all nonzero velocities."

- question: "A student applies t′ = γt to compute the time interval between two events at locations x₁ = 0 and x₂ = 100 m in frame S. What error has the student made?"
  type: multiple-choice
  options:
    - "No error — t′ = γt is the correct Lorentz time transformation"
    - "The student dropped the vx/c² term: the full transformation is t′ = γ(t − vx/c²), and setting x = 0 is only valid when both events occur at the same location in S"
    - "The student should have used the inverse transformation t = γ(t′ + vx′/c²) instead"
    - "The error is using γ rather than 1/γ for time dilation"
  answer: 1
  explanation: "The simplified formula t′ = γt is valid only when x = 0 — that is, when both events occur at the same spatial location in frame S (like two ticks of a clock at rest in S). For events at different locations, the full form t′ = γ(t − vx/c²) must be used, and the x-dependent term is the relativity-of-simultaneity correction. Applying the simplified formula to spatially separated events conflates time dilation (a clock-rate effect) with the full Lorentz transformation and gives a wrong answer. This is one of the most common errors in special relativity calculations."

- question: "The Lorentz transformation predicts that the spacetime interval s² = c²t² − x² takes the same numerical value in all inertial frames."
  type: true-false
  answer: true
  explanation: "The invariant interval is the spacetime analog of Euclidean distance: just as r² = x² + y² is unchanged by spatial rotations, s² = c²t² − x² is unchanged by Lorentz transformations. This is verifiable by direct substitution of the transformation equations. The invariance means that while individual coordinates (t, x) are frame-dependent, their combination s² is an objective, frame-independent property of any pair of events. The minus sign (unlike the plus sign in Euclidean distance) is what gives spacetime its hyperbolic geometry and prevents motion faster than light."

- question: "In the Lorentz transformation, the time coordinate in one frame depends only on the time coordinate in the other frame, not on spatial position."
  type: true-false
  answer: false
  explanation: "This is precisely the common misconception to avoid. The Lorentz time transformation is t′ = γ(t − vx/c²), which explicitly includes the spatial position x. This mixing of space into the time coordinate — absent in the Galilean t′ = t — is the mathematical expression of relativity of simultaneity. Two events at the same time but different locations in S are NOT at the same time in S′. The vx/c² term is not a small correction; it is the central non-Newtonian content of special relativity."

- question: "Why is the fact that t′ depends on x in the Lorentz transformation a genuine physical statement and not merely a mathematical coordinate convention?"
  type: short-answer
  answer: "In Newtonian mechanics, t′ = t: all observers agree on when events happen, regardless of where they are. The Lorentz transformation replaces this with t′ = γ(t − vx/c²): the time of an event in frame S′ depends on both its time and its location in frame S. Two events at the same t but different x have different t′ — they are not simultaneous in S′. This is not a convention about how we label events; it is a physical disagreement between inertial observers about which events happened at the same time. Experiments confirm this: moving clocks lose synchronization in ways that depend on their spatial separation, not just their relative velocity. Relativity of simultaneity has measurable consequences in particle physics and GPS timing corrections."
  explanation: "The contrast with Galilean relativity is the key. The Galilean transformation also changes spatial coordinates between frames, but time is untouched — every observer agrees on the time order and simultaneity of events. The Lorentz transformation breaks this by coupling time to space, producing a fundamentally different causal structure. The invariance of the spacetime interval (rather than time alone or distance alone) is the new invariant that replaces Newtonian absolute time."
```

## Explainer

You already know two relativistic effects from direct analysis: moving clocks run slow (time dilation) and moving rulers contract (length contraction). The Lorentz transformation is not a new piece of physics — it is the single transformation that contains both results and generates all other relativistic kinematic effects from one unified formula. Think of it as the master equation of special relativity kinematics.

The starting point is a comparison with the familiar **Galilean transformation**: x′ = x − vt, t′ = t. This says that frame S′ (moving at velocity v relative to S) just shifts the x-coordinate, and time is universal. This works perfectly for everyday speeds. Special relativity replaces it with x′ = γ(x − vt), t′ = γ(t − vx/c²), where γ = 1/√(1 − v²/c²). Two things are different. First, there is a factor γ stretching the spatial term — that is the origin of length contraction. Second, and most importantly, **time is mixed with space**: t′ depends on both t and x. This is the heart of relativity. Two events that happen at the same time (t₁ = t₂) but different places (x₁ ≠ x₂) in frame S are generally *not* simultaneous in frame S′. Simultaneity is relative.

To see how the known effects emerge: for time dilation, consider a clock at rest at x = 0 in S (so x = 0 for both events — "tick" and "tock"). Then t′ = γt, so the time interval is longer in S′ — moving clocks run slow. For length contraction, consider a rod at rest in S′. Its two endpoints must be measured simultaneously in S (t fixed, x₁ and x₂ measured at the same t). Using x = γ(x′ + vt′), the length in S works out to L₀/γ — the rod is shorter in the frame where it is moving.

The **invariant spacetime interval** s² = c²t² − x² is preserved under Lorentz transformations: it takes the same value in all inertial frames. This is the spacetime analog of the Euclidean distance r² = x² + y² being preserved under spatial rotations. In fact, the Lorentz transformation is precisely a "rotation" in spacetime — but with a hyperbolic geometry (the minus sign in s²) rather than Euclidean. The parameter that plays the role of angle is the **rapidity** φ = tanh⁻¹(v/c). Writing the transformation in terms of rapidity (x′ = x cosh φ − ct sinh φ, ct′ = ct cosh φ − x sinh φ) makes the analogy with spatial rotations exact, and reveals why relativistic velocity addition looks like adding rapidities rather than velocities: φ_total = φ₁ + φ₂, which is why you can never exceed c no matter how many boosts you stack.
