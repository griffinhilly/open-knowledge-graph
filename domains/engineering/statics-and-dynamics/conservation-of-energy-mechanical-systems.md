---
id: conservation-of-energy-mechanical-systems
title: Conservation of Mechanical Energy in Systems
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: work-energy-theorem-rigorous
  type: hard
- id: potential-energy-conservative-forces
  type: hard
- id: energy-conservation-applications
  type: hard
builds-toward:
- lagrangian-mechanics-overview
tags:
- energy
- conservation-laws
- mechanical-systems
stage: formal-systems
status: validated
---

# Conservation of Mechanical Energy in Systems

## Core Idea
When only conservative forces act on a mechanical system, total mechanical energy E = T + V (kinetic plus potential) remains constant. This scalar conservation law is often more useful than Newton's laws for solving complex problems, particularly when motion is constrained and constraint forces are unknown or irrelevant to the energy analysis.

## Questions

```yaml
- question: "A bead slides without friction along a curved wire from rest at a height of 2 m down to ground level. What is its speed at the bottom, given g = 9.8 m/s²?"
  type: multiple-choice
  options:
    - "It depends on the wire's shape — a steeper path accelerates the bead more and produces higher speed"
    - "v = √(2gh) ≈ 6.3 m/s, determined entirely by the height difference via energy conservation"
    - "v = √(gh) ≈ 4.4 m/s, since kinetic energy equals mgh/2"
    - "The speed cannot be determined without knowing the normal force the wire exerts"
  answer: 1
  explanation: "Energy conservation: mgh = ½mv², so v = √(2gh) = √(2·9.8·2) ≈ 6.3 m/s. The wire's shape is irrelevant because the normal force is always perpendicular to the bead's motion — it does no work and never appears in the energy equation. This is the power of energy methods: constraint forces vanish entirely. Option D represents the Newtonian burden — you'd need the normal force to apply F = ma, but energy conservation sidesteps it."

- question: "Why does the conservation of mechanical energy fail when a block slides down a ramp with significant friction?"
  type: multiple-choice
  options:
    - "Friction is a constraint force that doesn't do work, so it shouldn't affect energy conservation"
    - "Friction is a non-conservative force that converts mechanical energy to heat, so T + V decreases rather than remaining constant"
    - "Friction only affects the direction of motion, not the speed, so energy is conserved but momentum is not"
    - "Friction changes the block's mass, violating the assumption that m is constant"
  answer: 1
  explanation: "Conservation of mechanical energy (T + V = constant) holds only when all forces doing work are conservative — meaning their work depends only on position, not path. Friction is non-conservative: it always opposes motion, does negative work equal to friction force times distance traveled, and converts mechanical energy into heat. The correct equation becomes T₁ + V₁ + W_friction = T₂ + V₂, where W_friction is negative. Option A is wrong: friction acts parallel to motion (along the surface), so it does do work — unlike normal forces, which act perpendicular."

- question: "Conservation of mechanical energy (T + V = constant) applies to a pendulum because the string tension does work on the bob as it swings."
  type: true-false
  answer: false
  explanation: "The string tension acts centripetally — always directed toward the pivot, perpendicular to the bob's velocity (which is tangential). Since force and velocity are perpendicular at every instant, the tension does zero work. Therefore the only force doing work is gravity (conservative), and T + V is conserved. The statement has the causal logic inverted: energy is conserved precisely because the tension does NO work — not because it does work."

- question: "The energy conservation approach is more powerful than Newton's second law for constrained mechanical systems because it produces a scalar equation that never requires computing constraint forces."
  type: true-false
  answer: true
  explanation: "Newton's second law gives vector equations — often three coupled differential equations per body — and requires identifying all forces, including constraint forces (normal forces, string tensions) that do no work. Energy conservation produces a single scalar equation T₁ + V₁ = T₂ + V₂ in which constraint forces never appear. For a bead on a wire or a ball on a ramp, the Newtonian approach carries these irrelevant forces through the calculation; energy methods skip them entirely. This is why energy methods are said to be more powerful for constrained systems."

- question: "Explain why conservation of mechanical energy is described as a scalar conservation law, and why this matters for solving mechanics problems."
  type: short-answer
  answer: "Energy is a scalar — it has magnitude but no direction. Kinetic energy T = ½mv² and potential energy V = mgh are both scalars, so T + V = constant is a single algebraic equation with no directional components. Newton's second law F = ma is a vector equation giving one equation per spatial dimension — three coupled differential equations in 3D. Scalar energy methods collapse multi-dimensional dynamics into a single equation, eliminating component resolution and often making the problem solvable by algebra rather than integration."
  explanation: "The scalar nature is both a strength and a limitation. Energy conservation tells you the speed at any configuration but not the trajectory — you don't get position as a function of time. For many engineering problems, that speed information is exactly what you need (e.g., how fast does a roller coaster reach the bottom?). For others, you need the full trajectory, requiring Newton's laws or the Lagrangian. The Lagrangian formalism, which you'll meet next, extends this scalar approach to derive the full equations of motion from energy alone."
```

## Explainer

From your work with the work-energy theorem and potential energy, you already know that a conservative force is one where the work it does depends only on start and end position, not on the path taken — gravity and springs are the canonical examples. The energy conservation law in mechanics is the direct consequence: if every force doing work on a system is conservative, then whatever kinetic energy is lost as an object slows down must be stored as potential energy, and vice versa. The sum E = T + V never changes. This is not a new physical principle; it is a special case of the work-energy theorem when all work comes from conservative forces.

The power of this scalar law becomes clearest when you compare it to Newton's second law approach. Newton's laws give you vector equations — often three coupled differential equations — and to use them you must track every force including constraint forces like normal forces and tension. In many problems, those constraint forces do no work (they act perpendicular to motion), so you do not care what they are, yet you still have to carry them through Newton's equations. Energy conservation skips all of that. You write the energy at one instant equal to the energy at another instant: T₁ + V₁ = T₂ + V₂. The constraint forces never appear. A bead constrained to slide on a frictionless wire, a pendulum swinging on a massless rod, a ball rolling down a curved surface — all of these yield to a single scalar equation that Newton's approach would make far more laborious.

The critical word is **conservative**: this law fails the moment friction, air resistance, or any non-conservative force does work on the system. When those forces are present, energy is lost from the mechanical system (converted to heat), and T + V is no longer constant. In that case, you must return to the work-energy theorem and account for the work done by non-conservative forces: T₁ + V₁ + W_{nc} = T₂ + V₂. Conservation of mechanical energy is the zero-non-conservative-work special case of this more general statement.

Building toward Lagrangian mechanics, which is your next topic, it helps to see conservation of energy as the first hint of a deeper truth: the equations of motion for a mechanical system can be derived entirely from its energy, without ever writing force vectors. The **Lagrangian** L = T − V encodes all the dynamics, and the Euler-Lagrange equations extract them. Conservation of mechanical energy is the gateway to that more powerful formulation — and the physical intuition is the same: describe a system by how its energies trade off, and the motion follows.
