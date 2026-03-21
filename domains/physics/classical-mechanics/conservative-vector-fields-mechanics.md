---
id: conservative-vector-fields-mechanics
title: Conservative Force Fields and Potential Energy
domain: physics
course: classical-mechanics
prerequisites:
- id: work-and-energy
  type: hard
- id: potential-energy
  type: hard
- id: conservative-fields-potential
  type: hard
builds-toward:
- total-mechanical-energy-conservation
- effective-potential-central-forces
tags:
- forces
- fields
- energy
stage: formal-systems
status: draft
---

# Conservative Force Fields and Potential Energy

## Core Idea
A conservative force field has the property that work done is path-independent and can be written as the negative gradient of a potential energy function: F = −∇U. Line integrals around closed loops vanish, and mechanical energy is conserved.

## Questions

```yaml
- question: "A ball moves from point A (potential energy U = 10 J) to point B (potential energy U = 6 J) under only a conservative force. How much work does the conservative force do?"
  type: multiple-choice
  options:
    - "−4 J — the force opposes the motion since potential energy decreased"
    - "+4 J — work equals the decrease in potential energy"
    - "+6 J — work equals the potential energy at the destination"
    - "0 J — conservative forces do no net work over any path"
  answer: 1
  explanation: "The work-energy theorem for conservative forces gives W = −ΔU = −(U_B − U_A) = −(6 − 10) = +4 J. The force does positive work when the particle moves to lower potential energy — the force 'pushes downhill,' doing work on the particle. Option A gets the sign wrong: the force points in the direction of decreasing U (that's what F = −∇U means), so it does positive work when U decreases. Option D is wrong: conservative forces do zero net work around a *closed loop*, not along every path."

- question: "Which of the following is NOT a property of a conservative force field?"
  type: multiple-choice
  options:
    - "The work done between two points is path-independent"
    - "The line integral around any closed loop is zero"
    - "The work done increases with the length of the path taken"
    - "The force can be written as F = −∇U for some scalar potential U"
  answer: 2
  explanation: "Option C describes a non-conservative force like friction. For a conservative force, the work done between two endpoints is the same regardless of which path connects them — a defining property. This path-independence is mathematically equivalent to the closed-loop integral being zero (option A) and to the existence of a potential energy function whose negative gradient gives the force (option D). Friction's work does depend on path length, which is precisely why friction is non-conservative and cannot be described by a potential energy function."

- question: "If only conservative forces act on a particle and the particle returns to its exact starting position, the net work done by those forces is zero."
  type: true-false
  answer: true
  explanation: "This is the closed-loop property: the line integral of a conservative force around any closed path is zero. Returning to the starting point means the starting and ending potential energies are identical, so ΔU = 0, and therefore W = −ΔU = 0. This is not a coincidence but the defining mathematical property of conservative fields. Gravity, the spring force, and electrostatic forces all satisfy this; friction does not — a longer circular path always dissipates more energy via friction."

- question: "When a ball thrown upward loses kinetic energy as it rises, that energy simply disappears because gravity has done negative work on it."
  type: true-false
  answer: false
  explanation: "Energy is not destroyed — it is converted. Gravity is a conservative force, so the work it does is W = −ΔU. When gravity does negative work on the rising ball (W < 0), the ball's potential energy increases by exactly the same amount: the lost kinetic energy is stored as gravitational potential energy. This is energy conservation: K + U = constant (when only conservative forces act). The energy can be fully recovered — the stored potential energy converts back to kinetic energy as the ball falls. Non-conservative forces like friction are different: they convert mechanical energy into heat, which cannot be recovered as kinetic energy."

- question: "Why does the negative sign in F = −∇U make physical sense? What does it tell you about the direction of a conservative force relative to potential energy?"
  type: short-answer
  answer: "The negative sign encodes that conservative forces push objects toward lower potential energy. The gradient ∇U points in the direction of steepest increase of U; the negative sign reverses this, so F points in the direction of steepest decrease — 'downhill' in potential energy. Gravity is the clearest example: gravitational potential energy increases with height, and gravity pulls downward (toward lower U). A spring compressed more has higher elastic potential energy, and the spring force pushes toward the equilibrium (lower U). In every case, the force acts to reduce potential energy, and the negative sign in F = −∇U captures this universally."
  explanation: "This connection between the sign convention and physical intuition is what makes the formula F = −∇U more than just notation. It tells you immediately which direction a force acts for any potential energy landscape: particles roll toward potential energy minima, just as a ball rolls downhill. It also explains why stable equilibrium occurs at a minimum of potential energy — small displacements from a minimum are opposed by the conservative force, which pushes back toward the minimum. Understanding the negative sign as 'force points downhill in U-space' is the key conceptual handle for working with potential energy in any context."
```

## Explainer

From your work on potential energy and work-energy, you know that potential energy U stores the capacity to do work, and that work done by a force changes kinetic energy. Conservative fields formalize exactly which forces can be described this way. The defining property is **path independence**: the work done by a conservative force moving a particle between two points depends only on those endpoints, not on which route is taken. Gravity is the canonical example — carrying a book from the floor to a shelf does the same work against gravity whether you take the stairs or a spiral path. Friction, by contrast, is non-conservative: a longer, winding path dissipates more energy.

Path independence has an equivalent geometric formulation: the line integral of a conservative force around any closed loop is zero. Take a particle on any journey that returns to its starting point — gravity does exactly zero net work. This is not an accident but a fundamental constraint: it means the force cannot systematically add or remove energy from a particle traveling in circles. Mathematically, a force field **F** is conservative if and only if it can be written as the **negative gradient** of a scalar field: **F** = −∇U. The gradient ∇U points in the direction of steepest increase of U; the negative sign means the force points *downhill* in potential energy, just as gravity pulls objects toward lower gravitational potential.

Why the negative sign matters is worth dwelling on. Potential energy is defined to be highest where the force pushes against you most. A ball at height h has high gravitational potential energy — gravity is trying to pull it lower, toward decreasing U. The force points in the direction of decreasing U, so **F** = −∇U encodes "force points downhill." This also tells you immediately how to find forces from potential energy functions and vice versa. In one dimension, F = −dU/dx: if potential energy rises steeply, the force pushing back is large.

The payoff is energy conservation. When only conservative forces act, the work-energy theorem W = ΔK becomes −ΔU = ΔK, which rearranges to ΔK + ΔU = 0, or K + U = constant. This is total mechanical energy conservation, your next topic. Conservative fields are precisely the forces for which this bookkeeping works — kinetic energy lost is stored as potential energy and can be fully recovered. Non-conservative forces like friction convert mechanical energy irreversibly into heat, breaking the conservation. Identifying which forces in a problem are conservative is therefore the first step in any energy-conservation analysis.
