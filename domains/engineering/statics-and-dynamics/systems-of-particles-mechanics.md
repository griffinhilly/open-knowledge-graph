---
id: systems-of-particles-mechanics
title: 'Systems of Particles: Center of Mass and Internal Forces'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: center-of-mass-vs-centroid
  type: hard
- id: conservation-of-linear-momentum
  type: hard
builds-toward:
- rigid-body-kinetics-force-acceleration
tags:
- systems
- center-of-mass
- particle-systems
stage: formal-systems
status: draft
---

# Systems of Particles: Center of Mass and Internal Forces

## Core Idea
A system of particles behaves as though all its mass were concentrated at the center of mass, which accelerates according to the net external force (internal forces cancel by Newton's third law). This decomposition separates translational motion from internal dynamics, simplifying analysis of complex multi-body systems including rigid bodies.

## Questions

```yaml
- question: "A gymnast in mid-air performs a backflip, vigorously moving her arms and legs throughout. What path does her center of mass follow during the flip?"
  type: multiple-choice
  options:
    - "A curved path that shifts unpredictably as she moves her limbs, since redistributing mass changes the center of mass trajectory"
    - "A parabolic arc determined only by gravity and her initial velocity at takeoff — unaffected by any limb movements"
    - "A horizontal path because her rotational motion cancels the effect of gravitational pull"
    - "An unpredictable path because internal forces from muscle contractions complicate the dynamics"
  answer: 1
  explanation: "Her limb movements are internal forces within the gymnast-as-system. By Newton's third law, every muscle force has an equal and opposite reaction within the same system — internal forces cancel when summed. Only external forces (gravity, air resistance) govern the center of mass. Gravity accelerates it downward at g, combined with her initial horizontal velocity at takeoff, producing a perfect parabola. Her internal acrobatics can change her rotation and limb positions but cannot alter the trajectory of the center of mass."

- question: "Two ice skaters (masses 60 kg and 90 kg) stand still on frictionless ice and push off each other. After the push, what happens to the center of mass of the two-skater system?"
  type: multiple-choice
  options:
    - "The heavier skater stays at rest and the lighter skater moves backward"
    - "Both skaters move in opposite directions such that total momentum remains zero and the center of mass stays stationary"
    - "The center of mass moves in the direction the lighter skater travels, since lighter objects move faster after a push"
    - "The push creates net external forces that accelerate the entire system's center of mass"
  answer: 1
  explanation: "The push forces are internal to the two-skater system — equal and opposite by Newton's third law, so they cancel in the system sum. With no external horizontal forces (frictionless ice), ΣF_ext = 0, so M·a_cm = 0 and the center of mass remains stationary. Both skaters gain equal and opposite momenta (60 kg × v₁ = 90 kg × v₂ in opposite directions), consistent with zero total momentum. Option A is a common misconception — both skaters move, not just the lighter one."

- question: "Internal forces within a system of particles can change the system's total linear momentum."
  type: true-false
  answer: false
  explanation: "By Newton's third law, every internal force has an equal and opposite counterpart within the system. When you sum all forces across all particles, every internal pair contributes +F and -F, which cancel to zero. Only external forces (those from outside the system boundary) can change total momentum. This is why ΣF_ext = M·a_cm — internal forces, regardless of their magnitude or complexity, are irrelevant to the center of mass motion."

- question: "The equation ΣF_ext = M·a_cm holds only for systems of exactly two particles, not for larger or more complex systems."
  type: true-false
  answer: false
  explanation: "This equation holds for any system of particles — two, a thousand, or infinitely many (as in a rigid body). The derivation only requires that internal forces come in action-reaction pairs (Newton's third law), which is always true. A rigid body is technically a system of infinitely many particles, and ΣF_ext = Ma_cm still governs its translational motion. The separation into translational (ΣF_ext = Ma_cm) and rotational (ΣM = Iα) equations is exactly what makes rigid body dynamics tractable."

- question: "Why does choosing the system boundary — deciding what is 'inside' versus 'outside' — matter so much when analyzing multi-body mechanics problems?"
  type: short-answer
  answer: "The system boundary determines which forces are internal (cancel by Newton's third law and don't appear in ΣF_ext = Ma_cm) and which are external (must be computed and summed). A force that is external if you analyze one object becomes internal — and disappears from the equation — if you expand the system to include both objects. For example, treating two colliding balls as a single system makes the collision forces internal, letting you analyze center-of-mass motion without ever knowing the collision force's magnitude. A thoughtful system boundary can eliminate entire categories of forces from the analysis, dramatically simplifying the problem."
  explanation: "This is the practical art of systems mechanics: the physics is the same regardless of boundary choice, but the algebra differs enormously. Collision analysis, rocket propulsion, and chain dynamics all become tractable when you choose a system boundary that makes the complicated forces internal and focuses attention on the simpler external forces."
```

## Explainer

You already know that the **center of mass** is the mass-weighted average position of a body, and that **linear momentum** is conserved when no external forces act. The system-of-particles result ties these together into a single principle with broad reach. When multiple particles interact — through springs, contact, tension, or any internal mechanism — the internal forces always come in action-reaction pairs (Newton's third law). Summing over all particles, every internal force has an equal and opposite counterpart within the system, and they cancel exactly. Internal forces cannot change the system's total momentum or accelerate the system's center of mass.

What remains is clean: **ΣF_ext = M · a_cm**, where M is total mass and a_cm is the acceleration of the center of mass. This is Newton's second law applied to the entire system, with internal forces gone. The center of mass moves exactly as though all the system's mass were concentrated there, subject only to external forces. A spinning wrench thrown across a room, a cluster of colliding billiard balls, a rocket expelling exhaust — in every case, the center of mass follows the trajectory dictated by external forces alone, no matter how complicated the internal dynamics.

This separation is what makes rigid body dynamics tractable. A rigid body is a system of infinitely many particles with internal stresses maintaining fixed relative positions. By the particle-system result, translational motion of the center of mass is governed by ΣF_ext = Ma_cm (external forces only), and rotational motion about the center of mass is governed by ΣM_cm = Iα (external torques only). The two equations decouple — you do not need to know the internal stresses to analyze gross translational and rotational motion.

The practical power is clearest in collision analysis. If you take two colliding objects as your system, the collision forces are internal and cancel. During the brief collision interval, external forces (gravity, friction) are small relative to the impulsive collision forces and can often be neglected. In that approximation, total system momentum is conserved — not because forces vanish, but because internal forces cancel and external impulses are negligible. The boundary you draw around the system determines what counts as internal, so choosing the system thoughtfully is the analytical skill at the heart of every multi-body problem.
