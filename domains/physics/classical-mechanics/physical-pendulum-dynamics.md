---
id: physical-pendulum-dynamics
title: Physical Pendulum and Rotational Oscillations
domain: physics
course: classical-mechanics
prerequisites:
- id: simple-pendulum
  type: hard
- id: moment-of-inertia
  type: hard
- id: torque
  type: hard
builds-toward:
- small-angle-approximation
tags:
- oscillations
- rotation
- pendulum
stage: formal-systems
status: draft
---

# Physical Pendulum and Rotational Oscillations

## Core Idea
A physical pendulum is an extended rigid body pivoted at a point. Its restoring torque is proportional to sin(θ), and for small angles it undergoes simple harmonic motion with period T = 2π√(I/(mgd)), where I is moment of inertia and d is distance to center of mass.

## Explainer

Your prerequisite on the simple pendulum gave you the archetypal oscillator: a point mass on a massless string, with period T = 2π√(L/g). That derivation relied on a simplification — all the mass is concentrated at one point. The **physical pendulum** removes that simplification and asks: what happens when the swinging object is a real extended body? A bat, a door, a swinging leg, a compound pendulum in a clock — these are all physical pendulums. Analyzing them requires combining your knowledge of the simple pendulum with your prerequisites on **torque** and **moment of inertia**.

The setup: a rigid body of mass m pivots about a fixed point P. The body's center of mass is a distance d from the pivot. When the body is displaced by angle θ from equilibrium, gravity acts on the center of mass and creates a **restoring torque** τ = −mgd sin(θ). This is the rotational analogue of the restoring force in the simple pendulum. Newton's second law for rotation says τ = Iα, where I is the **moment of inertia** about the pivot point P (not about the center of mass — use the parallel-axis theorem: I = I_cm + md²). Combining these gives the equation of motion: Iα = −mgd sin(θ), or equivalently θ̈ = −(mgd/I) sin(θ).

This is structurally identical to the simple pendulum's equation — it's a nonlinear differential equation with a sin(θ) term. For small angles, sin(θ) ≈ θ, which linearizes the equation to θ̈ = −(mgd/I)θ. This is **simple harmonic motion** with angular frequency ω = √(mgd/I) and period T = 2π√(I/(mgd)). Notice how this generalizes the simple pendulum result: if all the mass were at the end of a string of length L, then I = mL² and d = L, so T = 2π√(mL²/mgL) = 2π√(L/g), recovering the simple result. The physical pendulum formula is the parent formula; the simple pendulum is the special case.

The power of this framework shows up in real applications. A uniform rod of mass m and length L pivoted at one end has I = mL²/3 (not mL²) and d = L/2, giving T = 2π√(2L/3g) — a rod swings *faster* than a simple pendulum of the same length. This makes intuitive sense: the mass is distributed along the rod, so its "effective" length is shorter than L. You can also find a physical pendulum's moment of inertia experimentally by measuring its period and using the formula in reverse — an important technique in experimental mechanics. The concept of **equivalent length** L_eq = I/(md) lets you map any physical pendulum back to an equivalent simple pendulum, providing a clean mental model: however complicated the shape, the period depends on just two numbers — how hard it is to rotate (I) and how far the center of mass is from the pivot (d).
