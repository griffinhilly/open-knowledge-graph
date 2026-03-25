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
- id: normal-modes-oscillations
  type: soft
- id: phase-and-amplitude-forced-oscillations
  type: soft
builds-toward:
- small-angle-approximation
tags:
- oscillations
- rotation
- pendulum
stage: formal-systems
status: validated
---
# Physical Pendulum and Rotational Oscillations

## Core Idea
A physical pendulum is an extended rigid body pivoted at a point. Its restoring torque is proportional to sin(θ), and for small angles it undergoes simple harmonic motion with period T = 2π√(I/(mgd)), where I is moment of inertia and d is distance to center of mass.

## Questions

```yaml
- question: "A uniform rod of mass m and length L is pivoted at one end and swings as a physical pendulum. How does its period compare to a simple pendulum of the same length L?"
  type: multiple-choice
  options:
    - "Same period: T = 2π√(L/g), because the total length is the same"
    - "Longer period, because the distributed mass increases the effective pendulum length"
    - "Shorter period, because the effective length is L_eq = I/(md) = (2/3)L, which is less than L"
    - "Shorter period, because the moment of inertia mL²/3 is smaller than mL²"
  answer: 2
  explanation: "For a uniform rod pivoted at one end: I = mL²/3 and d = L/2 (center of mass is at the midpoint). The equivalent length is L_eq = I/(md) = (mL²/3)/(m·L/2) = 2L/3 < L. Since T = 2π√(L_eq/g), the rod swings faster (shorter period) than a simple pendulum of the same total length. The mass distribution places the effective center of oscillation closer to the pivot than if all mass were at the tip."

- question: "In the physical pendulum period formula T = 2π√(I/(mgd)), what does d represent?"
  type: multiple-choice
  options:
    - "The total length of the pendulum arm from pivot to the lowest point of the body"
    - "The distance from the pivot point to the center of mass of the rigid body"
    - "The radius of gyration of the body about its center of mass"
    - "The distance from the center of mass to the lowest point of the body"
  answer: 1
  explanation: "d is the distance from the pivot point P to the center of mass of the rigid body. It appears because the restoring torque is τ = −mgd sin(θ) — gravity acts at the center of mass, and d is the moment arm for that force. This is distinct from the total length of the object, and it's also distinct from the radius of gyration. Confusing d with the total length L is the most common error when applying this formula."

- question: "A physical pendulum's period depends on the moment of inertia about the pivot point, not about the center of mass."
  type: true-false
  answer: true
  explanation: "The equation of motion is Iα = −mgd sin(θ), where I must be computed about the pivot point P (the actual axis of rotation), not about the center of mass. When applying the formula, you often need the parallel-axis theorem: I_pivot = I_cm + md². Using I_cm instead of I_pivot is a common error that gives the wrong period."

- question: "The period of a physical pendulum can be calculated using T = 2π√(L/g) as long as L is taken to be the total physical length of the object."
  type: true-false
  answer: false
  explanation: "T = 2π√(L/g) applies only to the simple pendulum, where all mass is concentrated at a single point at distance L from the pivot. For a physical pendulum, the correct formula is T = 2π√(I/(mgd)). This reduces to the simple pendulum result only when I = mL² and d = L (all mass at the tip), which is not the case for any real extended object."

- question: "Explain why a uniform rod pivoted at one end swings faster than a simple pendulum of the same total length, using the concept of equivalent length."
  type: short-answer
  answer: "The equivalent length of a physical pendulum is L_eq = I/(md). For a uniform rod pivoted at one end, I = mL²/3 and d = L/2, so L_eq = (mL²/3)/(m·L/2) = 2L/3. Since T = 2π√(L_eq/g), and 2L/3 < L, the rod has a shorter period than a simple pendulum of the same length. Physically, the mass is distributed along the rod with much of it closer to the pivot than the tip, so the rod's effective oscillation length is shorter than its total length."
  explanation: "The equivalent length concept lets you map any physical pendulum to a simple pendulum for the purpose of calculating period. The 'effective length' is always less than the total length for uniform objects (center of mass is inside the object), which is why distributed-mass pendulums swing faster than point-mass pendulums of the same size."
```

## Explainer

Your prerequisite on the simple pendulum gave you the archetypal oscillator: a point mass on a massless string, with period T = 2π√(L/g). That derivation relied on a simplification — all the mass is concentrated at one point. The **physical pendulum** removes that simplification and asks: what happens when the swinging object is a real extended body? A bat, a door, a swinging leg, a compound pendulum in a clock — these are all physical pendulums. Analyzing them requires combining your knowledge of the simple pendulum with your prerequisites on **torque** and **moment of inertia**.

The setup: a rigid body of mass m pivots about a fixed point P. The body's center of mass is a distance d from the pivot. When the body is displaced by angle θ from equilibrium, gravity acts on the center of mass and creates a **restoring torque** τ = −mgd sin(θ). This is the rotational analogue of the restoring force in the simple pendulum. Newton's second law for rotation says τ = Iα, where I is the **moment of inertia** about the pivot point P (not about the center of mass — use the parallel-axis theorem: I = I_cm + md²). Combining these gives the equation of motion: Iα = −mgd sin(θ), or equivalently θ̈ = −(mgd/I) sin(θ).

This is structurally identical to the simple pendulum's equation — it's a nonlinear differential equation with a sin(θ) term. For small angles, sin(θ) ≈ θ, which linearizes the equation to θ̈ = −(mgd/I)θ. This is **simple harmonic motion** with angular frequency ω = √(mgd/I) and period T = 2π√(I/(mgd)). Notice how this generalizes the simple pendulum result: if all the mass were at the end of a string of length L, then I = mL² and d = L, so T = 2π√(mL²/mgL) = 2π√(L/g), recovering the simple result. The physical pendulum formula is the parent formula; the simple pendulum is the special case.

The power of this framework shows up in real applications. A uniform rod of mass m and length L pivoted at one end has I = mL²/3 (not mL²) and d = L/2, giving T = 2π√(2L/3g) — a rod swings *faster* than a simple pendulum of the same length. This makes intuitive sense: the mass is distributed along the rod, so its "effective" length is shorter than L. You can also find a physical pendulum's moment of inertia experimentally by measuring its period and using the formula in reverse — an important technique in experimental mechanics. The concept of **equivalent length** L_eq = I/(md) lets you map any physical pendulum back to an equivalent simple pendulum, providing a clean mental model: however complicated the shape, the period depends on just two numbers — how hard it is to rotate (I) and how far the center of mass is from the pivot (d).
