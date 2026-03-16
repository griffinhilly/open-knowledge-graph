---
id: galilean-relativity-classical
title: Galilean Relativity and Classical Reference Frames
domain: physics
course: modern-physics
prerequisites:
- id: newtons-first-law
  type: hard
- id: newtons-second-law
  type: hard
builds-toward:
- relativity-of-simultaneity
tags:
- relativity
- reference-frames
- mechanics
stage: abstract-reasoning
status: draft
---

# Galilean Relativity and Classical Reference Frames

## Core Idea
In classical mechanics, the laws of physics appear identical in all inertial reference frames moving at constant velocity relative to each other. This Galilean invariance means that mechanical experiments give equivalent results when velocities are transformed between frames. However, electromagnetic phenomena and light propagation revealed that this classical framework is incomplete.

## Explainer

From Newton's first and second laws, you know that force equals mass times acceleration, and that objects with no net force move at constant velocity. But these laws implicitly assume you can measure position and velocity — and that requires specifying *relative to what*. An **inertial reference frame** is a coordinate system in which Newton's first law holds: an object with no net force moves in a straight line at constant speed. Any frame moving at constant velocity relative to an inertial frame is itself inertial. Galilean relativity is the classical statement that all inertial frames are equivalent for mechanics — no mechanical experiment can distinguish "truly moving" from "truly at rest."

The mathematical expression of this is the **Galilean transformation**. If frame S′ moves at constant velocity v relative to frame S along the x-axis, positions transform as x′ = x − vt, while time is absolute: t′ = t. Velocities transform as u′ = u − v — a ball moving at u in S is seen moving at u − v in S′. Accelerations are unchanged: a′ = a, since differentiating u′ = u − v with respect to t gives zero additional terms when v is constant. Because F = ma and acceleration is the same in both frames, the force law takes identical form in S and S′. This is **Galilean invariance**: Newton's laws are unchanged by the transformation.

The intuitive content is deeply familiar. On a smoothly cruising train, you cannot tell (with eyes closed) whether you are moving or stationary. A ball thrown straight up falls straight back down; objects do not drift toward the back of the car. Mechanical laws work just as they do on the ground. What you *can* detect is acceleration: when the train brakes, you feel a lurch, because the braking frame is non-inertial — Newton's laws no longer hold without adding fictitious forces. The distinction between inertial and non-inertial frames is physically real; the distinction between different inertial frames is not. Galilean relativity says there is no preferred "rest" frame for mechanics.

For over two centuries, Galilean relativity went unchallenged. Then Maxwell's equations revealed a crisis: they predict that electromagnetic waves travel at speed c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s — a specific number with no reference frame built into it. Under Galilean velocity addition, an observer moving at v toward a light source should measure light at c + v; moving away, at c − v. But experiments (most famously the Michelson-Morley experiment of 1887) showed no such dependence: light's speed is c regardless of the observer's motion. This is logically incompatible with Galilean relativity. Einstein resolved the contradiction in 1905 by abandoning the assumption that time is absolute — the step that leads to special relativity, where simultaneity is relative and the speed of light is the same in every inertial frame by postulate, not by accident.
