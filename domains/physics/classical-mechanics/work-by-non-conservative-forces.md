---
id: work-by-non-conservative-forces
title: Work by Non-Conservative Forces
domain: physics
course: classical-mechanics
prerequisites:
- id: work-energy-theorem
  type: hard
- id: friction-forces
  type: hard
builds-toward:
- mechanical-energy-and-non-conservative-forces
tags:
- work
- energy
- friction
- dissipation
stage: formal-systems
status: draft
---

# Work by Non-Conservative Forces

## Core Idea
Non-conservative forces (friction, air resistance) do path-dependent work and dissipate mechanical energy into heat. The work-energy theorem still holds—W_total = ΔKE—but you must explicitly include W_friction and other non-conservative work. Mechanical energy (KE + PE) decreases by an amount equal to the magnitude of work done by these forces.

## Questions

```yaml
- question: "A box slides from rest down a rough incline. Compared to an identical frictionless incline, what is true about the box's kinetic energy at the bottom?"
  type: multiple-choice
  options:
    - "It is the same — total energy is conserved in both cases"
    - "It is greater — friction converts potential energy more efficiently to kinetic energy"
    - "It is less — friction converts some mechanical energy to heat, reducing the final KE"
    - "It is less — friction increases the normal force, reducing the net work done by gravity"
  answer: 2
  explanation: "Friction does negative work (opposing motion), so W_total = W_gravity + W_friction, and W_friction < 0. By the work-energy theorem, ΔKE = W_total, so the final KE is less than it would be without friction. The missing mechanical energy is not destroyed — it becomes thermal energy in the surfaces. Total energy is conserved; only mechanical energy (KE + PE) is degraded. Option A confuses 'total energy conservation' with 'mechanical energy conservation' — a persistent error when non-conservative forces are present."

- question: "A block is dragged from point A to point B along a rough surface via two different routes: one short and direct, one long and winding. Friction does more negative work along the longer route."
  type: true-false
  answer: true
  explanation: "This is the defining property of non-conservative forces: the work they do depends on the path, not just the endpoints. W_friction = −μₖ·N·d, where d is the path length. A longer path means larger d, so friction does more negative work and removes more mechanical energy. This contrasts with conservative forces like gravity, where the work done depends only on the height difference regardless of path. Path-dependence is exactly what makes friction non-conservative."

- question: "When friction acts on a sliding object, the total energy of the system (mechanical + thermal) decreases."
  type: true-false
  answer: false
  explanation: "Total energy is always conserved. Friction converts mechanical energy into thermal energy — it does not destroy energy. The mechanical energy of the object decreases (W_friction < 0 means ΔE_mechanical < 0), but this is exactly offset by an equal increase in the thermal energy of the contacting surfaces. The statement 'friction dissipates energy' refers specifically to mechanical energy; the total energy budget is unchanged. This preview of thermodynamics — mechanical energy degraded to heat — is one of the conceptual payoffs of this topic."

- question: "Why can't we define a potential energy function for friction, the way we define gravitational potential energy?"
  type: short-answer
  answer: "Potential energy is defined for conservative forces because their work depends only on position (start and end points), not on path. Gravitational PE works because gravity does the same work between any two heights regardless of route — PE = mgh captures this path-independence. Friction's work depends on path length: drag an object in a complete circle and friction does negative work the entire time, even though you return to the starting position. There is no function of position whose change equals the work done by friction, so no potential energy can be defined for it."
  explanation: "The roundtrip test is the clearest diagnostic: a conservative force does zero net work on a closed loop (all PE is recovered). Friction always does negative work, accumulating energy loss on any loop. This path-dependence is precisely why PE cannot be defined and why mechanical energy is not conserved when friction is present."

- question: "A block of mass 5 kg slides down a 3-meter rough ramp (30° incline, μₖ = 0.3), starting from rest. Which expression correctly gives the block's final kinetic energy?"
  type: multiple-choice
  options:
    - "KE = mgh, using only gravity since friction is internal"
    - "KE = mgh − μₖ·mg·cos(30°)·d, where d = 3 m is the ramp length"
    - "KE = mgh + μₖ·mg·cos(30°)·d, because friction assists downward motion"
    - "KE = 0, because friction converts all kinetic energy to heat on any slope"
  answer: 1
  explanation: "W_friction = −μₖ·N·d = −μₖ·mg·cos(30°)·(3 m), and W_gravity = mgh where h = 3·sin(30°) = 1.5 m. By the work-energy theorem: KE_f = W_gravity + W_friction = mgh − μₖ·mg·cos(30°)·d. Option A ignores friction (valid only on a frictionless surface). Option C has the wrong sign — friction opposes motion and removes energy. Option D would only hold if friction were enormous enough to prevent motion, which is not stated."
```

## Explainer

You know from the work-energy theorem that the net work done on an object equals its change in kinetic energy: W_net = ΔKE. You also know from studying friction that friction forces oppose motion, are proportional to the normal force, and depend on the surfaces involved. This topic brings these together and explains what happens to mechanical energy — the sum of kinetic and potential energy — when friction is present.

The key distinction is between **conservative forces** and **non-conservative forces**. A conservative force (gravity, springs) does work that depends only on the starting and ending positions, never on the path taken. Because of this, you can define a potential energy associated with conservative forces, and the work they do equals the decrease in that potential energy. When only conservative forces act, mechanical energy is conserved: KE + PE = constant. **Non-conservative forces** like friction and air resistance do work that *does* depend on the path: a block sliding from A to B on a rough surface loses more energy to friction if you take a longer route. There is no potential energy you can define for friction because the work it does isn't recoverable — it's converted to thermal energy.

The modified energy equation follows directly from the work-energy theorem. W_net = ΔKE; W_net = W_conservative + W_non-conservative; W_conservative = -ΔPE. Substituting: -ΔPE + W_non-conservative = ΔKE, which rearranges to W_non-conservative = ΔKE + ΔPE = ΔE_mechanical. Since friction does negative work (it opposes motion), W_friction < 0, meaning ΔE_mechanical < 0: mechanical energy decreases. The amount of mechanical energy lost equals exactly the magnitude of work done by friction, which equals the heat generated. The total energy (mechanical + thermal) is still conserved — energy is never destroyed, just converted.

A concrete example clarifies the bookkeeping. A box of mass m slides 4 m down a ramp inclined at 30°, starting from rest, with kinetic friction coefficient μ_k = 0.2. Gravity does positive work (lowering the box), friction does negative work (opposing motion along the ramp). The box's final kinetic energy equals the work by gravity minus the magnitude of work by friction: KE_f = mgh - μ_k·N·d, where h is the vertical drop and d = 4 m is the path length. You cannot avoid the friction term by choosing a different path or reference point — that's what path-dependence means.

The broader point is that **real mechanical systems always involve non-conservative forces**, so pure conservation of mechanical energy is an idealization. Whenever a problem says "ignore friction" or "ignore air resistance," it's granting you permission to use the simpler conservation law. When those forces are present, you must account for them explicitly using W_nc = ΔE_mechanical, or equivalently, track all work terms in the full work-energy theorem. This framework also previews thermodynamics: the mechanical energy that friction "destroys" doesn't vanish — it increases the internal energy of the surfaces. Conservation of energy holds globally; it's only mechanical energy that non-conservative forces degrade.

