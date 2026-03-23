---
id: linear-momentum-impulse-systems
title: Linear Momentum and Impulse in Systems
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: particle-dynamics-accelerated-motion
  type: hard
- id: impulse-momentum-particles
  type: soft
builds-toward:
- collision-energy-analysis
tags:
- momentum
- impulse
- conservation
- impact
- force-time
- collisions
stage: formal-systems
status: validated
---

# Linear Momentum and Impulse in Systems

## Core Idea
Linear momentum p = mv is conserved when external forces are zero, and changes by impulse (force integrated over time): Δp = ∫F dt. This principle is especially useful for collision analysis, explosions, and impact problems where forces are large but contact time is short, making impulse-momentum methods more practical than detailed force-acceleration analysis.

## Questions

```yaml
- question: "Two ice skaters push off each other from rest. The internal push forces between them are enormous. What is the total linear momentum of the two-skater system immediately after they separate?"
  type: multiple-choice
  options:
    - "Large and positive, because large forces were applied during the push"
    - "Proportional to the impulse each skater received from the other"
    - "Zero, because internal forces cancel in Newton's third law pairs"
    - "Depends on which skater pushed harder during the interaction"
  answer: 2
  explanation: "When two skaters push on each other, those are *internal* forces within the system. By Newton's third law, Skater A pushes B with force F while B pushes A with -F. These cancel exactly when summing across the system. Starting from rest (total P = 0) with no external horizontal forces, total momentum remains zero — the skaters move in opposite directions with equal and opposite momenta. No matter how hard they push, the total system momentum is conserved. The individual impulses are large; the *net* external impulse is zero."

- question: "During a collision lasting 0.002 seconds, the contact forces are too brief and complex to measure. You can measure velocities before and after. Which method finds the impulse delivered to one object?"
  type: multiple-choice
  options:
    - "Work-energy theorem: impulse equals the change in kinetic energy"
    - "Impulse-momentum theorem: J = ΔP = m·Δv, computed directly from measured velocities"
    - "You cannot find impulse without knowing the detailed force-time profile"
    - "Newton's second law applied as J = F·a, where a is measured acceleration"
  answer: 1
  explanation: "The impulse-momentum theorem states J = ΔP = m·Δv. If you know the mass and initial and final velocities, you can compute the impulse without knowing the force-time history. This is the practical power of the approach: ∫F dt = ΔP relates impulse to measurable quantities even when the force profile is unknown. Option A confuses work (force over displacement) with impulse (force over time) — these are fundamentally different quantities connected to different conserved quantities (energy vs. momentum)."

- question: "For an isolated system with no external forces, total linear momentum is conserved regardless of how large the internal forces between particles are."
  type: true-false
  answer: true
  explanation: "Internal forces always come in Newton's third law pairs: if particle A exerts F on particle B, then B exerts -F on A. When summing all forces across the system to compute dP/dt, every internal force is exactly canceled by its reaction partner. The net result is F_ext = dP/dt. If F_ext = 0, then dP/dt = 0 and total momentum P is constant. The magnitude of internal forces is completely irrelevant — even enormous internal forces (like those in an explosion) leave total system momentum unchanged."

- question: "Impulse is defined as force multiplied by displacement."
  type: true-false
  answer: false
  explanation: "Impulse is force multiplied by *time* — or more precisely, the integral of force over time: J = ∫F dt. Force multiplied by displacement is *work*, which relates to changes in kinetic energy via the work-energy theorem. Impulse and work are both integrals of force, but over different variables (time vs. displacement), and each connects to a different conserved quantity (momentum vs. energy). Confusing the two leads to applying the wrong framework when choosing between impulse-momentum and work-energy methods."

- question: "In a system of particles, why do internal forces not contribute to changes in total linear momentum? State the physical principle and explain its consequence for collision analysis."
  type: short-answer
  answer: "Internal forces come in Newton's third law pairs: if particle A exerts force F on particle B, then B simultaneously exerts -F on A. When summing all forces across the entire system, every internal force is canceled by its equal and opposite reaction. Only external forces remain, giving F_ext = dP/dt. If external forces are zero (or negligible over a brief collision), total momentum is conserved. For collision analysis, this means you can equate total momentum before and after the collision without knowing anything about the contact forces during it."
  explanation: "This is Newton's third law applied at the system level. It's why an isolated system's momentum is conserved: every internal push is matched by an equal and opposite push. In collision problems, internal contact forces are typically far larger than any external forces over the brief contact duration — so external impulse is negligible and total momentum is conserved. The framework replaces 'what were the forces?' with 'what were the velocities before and after?' — a powerful simplification that works precisely because internal forces cancel."
```

## Explainer

From your work on particle dynamics, you know that F = ma describes how a single particle responds to a net force. Momentum reformulates this as p = mv, and Newton's second law becomes F = dp/dt — force is the rate of change of momentum. This reframing is subtle but powerful: it generalizes naturally from a single particle to a system of particles, and it opens a different path to solving problems where you do not know the internal forces.

The key idea for a system is to separate internal forces (which particles in the system exert on each other) from external forces (which come from outside the system). Internal forces always occur in Newton's-third-law pairs: if particle A pushes particle B with force F, then B pushes A with −F. When you sum up all forces across the entire system, internal forces cancel in pairs. What remains is the **net external force**. This gives the system momentum principle: F_ext = dP/dt, where P = Σm_i*v_i is the total linear momentum of the system. If the net external force is zero, P is constant — **conservation of linear momentum**.

The **impulse-momentum theorem** follows directly: ∫F dt = ΔP, where the left side is the **impulse** J, a force integrated over time. This form is most useful during collisions and impacts, where the contact forces are extremely large, the contact duration Δt is extremely short, but the product F·Δt (the impulse) is finite and measurable. In these situations, you cannot integrate F(t) directly because you do not know the detailed force-time profile inside the contact. But if you can measure initial and final velocities, you know ΔP and therefore J without needing that detail. Explosions work the same way: the internal blast forces are immense and brief, but if external impulse is negligible over that short interval, momentum is conserved across the event.

A useful analogy: impulse is to momentum what work is to kinetic energy. Work (∫F·dx) tells you how much a force changes the energy of a particle as it moves through space. Impulse (∫F dt) tells you how much a force changes the momentum of a particle as time passes. Both are integrals of force, but over different independent variables, and each connects to a different conserved quantity. When you have a collision problem, momentum methods are natural; when you have a path-dependent problem, energy methods may be cleaner. Choosing between work-energy and impulse-momentum is a skill that develops with practice — look for what is conserved (or what can be calculated) with the given information, and choose the framework that eliminates the unknowns you cannot measure.
