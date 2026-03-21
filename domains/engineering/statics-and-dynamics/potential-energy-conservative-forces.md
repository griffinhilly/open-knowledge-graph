---
id: potential-energy-conservative-forces
title: Potential Energy and Conservative Forces
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: work-power-energy-fundamentals
  type: hard
- id: rigid-body-work-energy
  type: soft
builds-toward:
- energy-conservation-methods
- vibrations-simple-harmonic
tags:
- potential-energy
- conservative
- gravity
- springs
stage: formal-systems
status: draft
---

# Potential Energy and Conservative Forces

## Core Idea
A conservative force is one where work done is independent of the path; it can be represented by a potential energy function: F = -∇U. Gravitational potential energy is mgh and elastic potential energy is ½kx². For conservative forces, mechanical energy E = KE + PE is conserved: E = constant along the motion.

## Questions

```yaml
- question: "A 1 kg ball is dropped straight down from height h = 5 m. A second 1 kg ball rolls down a curved frictionless ramp from the same height. Which ball has more kinetic energy at the bottom?"
  type: multiple-choice
  options:
    - "The dropped ball — it takes a shorter, more direct path and therefore does less work against gravity"
    - "The rolled ball — the curved path allows gravity to act over a longer distance, generating more energy"
    - "Both have equal kinetic energy — gravity is a conservative force and only the height difference determines the work done"
    - "It depends on the exact shape of the ramp curve"
  answer: 2
  explanation: "Gravity is a conservative force: the work it does depends only on the vertical displacement, not on the path taken. Both balls fall the same height h, so gravity does the same work mgh on each, giving both the same final kinetic energy. This is the defining feature of conservative forces — path independence. Options A and B both incorrectly assume that path length or shape affects the energy gained; this would be true for non-conservative forces like friction, but not for gravity."

- question: "Which of the following forces is NOT conservative?"
  type: multiple-choice
  options:
    - "Gravity near Earth's surface"
    - "Spring restoring force (F = -kx)"
    - "Kinetic friction"
    - "Electrostatic force between fixed charges"
  answer: 2
  explanation: "Kinetic friction is not conservative — the work it does depends on the path length, not just the endpoints. Sliding an object back and forth across a surface dissipates more energy the longer the path, so there is no potential energy function for friction. Gravity, spring forces, and electrostatic forces are all conservative: their work depends only on starting and ending positions, and each has a corresponding potential energy function (U = mgh, U = ½kx², and U = kq₁q₂/r, respectively)."

- question: "The work done by a conservative force depends on the length of the path traveled between two points."
  type: true-false
  answer: false
  explanation: "False — this is the definition of a non-conservative force. A conservative force does work that depends only on the starting and ending positions, not on the path connecting them. This path-independence is what allows us to define a potential energy function: because the work is the same no matter how you travel between two points, we can assign a unique potential energy to each position. If work depended on path length, no such function could exist."

- question: "When friction acts on a system alongside gravity, the total mechanical energy (KE + PE) is no longer conserved, and the work done by friction must be accounted for separately."
  type: true-false
  answer: true
  explanation: "True. Conservation of mechanical energy (KE + PE = constant) only holds when all forces doing work are conservative. Friction is non-conservative: it converts mechanical energy into heat, reducing the total. The corrected energy equation is ΔE_mechanical = W_non-conservative, where W_non-conservative is negative for friction (energy is lost). Conservative forces still contribute through changes in potential energy; friction appears on the right-hand side as an explicit energy loss. This is why a sliding block doesn't reach the same height on the way back up as it started — friction has dissipated some of the initial mechanical energy."

- question: "Explain what it means for a force to be conservative, and describe how the relationship F = -dU/dx connects the force to its potential energy function."
  type: short-answer
  answer: "A force is conservative if the work it does between any two points is independent of the path taken — equivalently, the work done around any closed loop is zero. This property allows us to assign a unique potential energy value U to every position. The connection F = -dU/dx (or F = -∇U in 3D) encodes the physical intuition that force points toward lower potential energy: the negative sign means the force pushes in the direction of decreasing U, just as a ball rolls downhill. For gravity, U = mgh, so F = -d(mgh)/dh = -mg (pointing downward, consistent with gravity). For a spring, U = ½kx², so F = -kx (pointing back toward equilibrium)."
  explanation: "The negative sign is critical and often missed. It means conservative forces are 'restoring' in the sense that they drive systems toward lower energy states. This also ensures that potential energy and kinetic energy trade off correctly: as U decreases (ball falls), KE increases by the same amount, keeping E = KE + PE constant."
```

## Explainer

From the work-energy theorem you already know, the net work done on a body equals its change in kinetic energy: W_net = ΔKE. This is always true. But for certain forces — gravity, spring forces — something special holds: the work they do depends only on the starting and ending position, not on the path traveled between them. A ball dropped straight down and a ball rolled down a curved ramp gain the same kinetic energy from gravity if they fall the same height. These are **conservative forces**, and recognizing them unlocks a far more powerful method of analysis.

The key is the **potential energy function** U, defined so that F = -dU/dx in one dimension (or F = -∇U in three). The negative sign encodes the physical intuition: force points toward decreasing potential energy, just as a ball rolls downhill. For gravity near Earth's surface, U = mgh, and F = -d(mgh)/dh = -mg, consistent with gravity pulling downward. For a spring, U = ½kx², and F = -kx, consistent with the restoring force toward equilibrium. These potential energy expressions are not definitions to memorize independently — they follow from integrating the forces you already know.

The payoff is **conservation of mechanical energy**: when only conservative forces do work on a system, the total mechanical energy E = KE + PE is constant throughout the motion. Writing E_initial = E_final lets you solve for any unknown state without tracing the path. A roller coaster descending from rest at height h reaches speed v = √(2gh) at the bottom, regardless of the track's shape — you don't integrate work along the curve, you simply equate energy. A mass on a spring oscillates indefinitely, converting kinetic energy to elastic potential and back, with the total unchanged.

The contrast with non-conservative forces defines the method's scope. Friction, drag, and externally applied forces that lack a potential energy function do work that depends on path length — they convert mechanical energy to heat or inject energy from external sources. When these are present, use the general form: ΔE_mechanical = W_non-conservative. Conservative forces still contribute through ΔPE, but non-conservative work appears explicitly on the right. Identifying which forces are conservative is always the first step: segregate the forces, handle conservative ones through potential energy, and account for the rest through path-dependent work.
