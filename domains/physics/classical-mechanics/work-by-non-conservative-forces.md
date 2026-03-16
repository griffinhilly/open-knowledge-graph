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

## Explainer

You know from the work-energy theorem that the net work done on an object equals its change in kinetic energy: W_net = ΔKE. You also know from studying friction that friction forces oppose motion, are proportional to the normal force, and depend on the surfaces involved. This topic brings these together and explains what happens to mechanical energy — the sum of kinetic and potential energy — when friction is present.

The key distinction is between **conservative forces** and **non-conservative forces**. A conservative force (gravity, springs) does work that depends only on the starting and ending positions, never on the path taken. Because of this, you can define a potential energy associated with conservative forces, and the work they do equals the decrease in that potential energy. When only conservative forces act, mechanical energy is conserved: KE + PE = constant. **Non-conservative forces** like friction and air resistance do work that *does* depend on the path: a block sliding from A to B on a rough surface loses more energy to friction if you take a longer route. There is no potential energy you can define for friction because the work it does isn't recoverable — it's converted to thermal energy.

The modified energy equation follows directly from the work-energy theorem. W_net = ΔKE; W_net = W_conservative + W_non-conservative; W_conservative = -ΔPE. Substituting: -ΔPE + W_non-conservative = ΔKE, which rearranges to W_non-conservative = ΔKE + ΔPE = ΔE_mechanical. Since friction does negative work (it opposes motion), W_friction < 0, meaning ΔE_mechanical < 0: mechanical energy decreases. The amount of mechanical energy lost equals exactly the magnitude of work done by friction, which equals the heat generated. The total energy (mechanical + thermal) is still conserved — energy is never destroyed, just converted.

A concrete example clarifies the bookkeeping. A box of mass m slides 4 m down a ramp inclined at 30°, starting from rest, with kinetic friction coefficient μ_k = 0.2. Gravity does positive work (lowering the box), friction does negative work (opposing motion along the ramp). The box's final kinetic energy equals the work by gravity minus the magnitude of work by friction: KE_f = mgh - μ_k·N·d, where h is the vertical drop and d = 4 m is the path length. You cannot avoid the friction term by choosing a different path or reference point — that's what path-dependence means.

The broader point is that **real mechanical systems always involve non-conservative forces**, so pure conservation of mechanical energy is an idealization. Whenever a problem says "ignore friction" or "ignore air resistance," it's granting you permission to use the simpler conservation law. When those forces are present, you must account for them explicitly using W_nc = ΔE_mechanical, or equivalently, track all work terms in the full work-energy theorem. This framework also previews thermodynamics: the mechanical energy that friction "destroys" doesn't vanish — it increases the internal energy of the surfaces. Conservation of energy holds globally; it's only mechanical energy that non-conservative forces degrade.

