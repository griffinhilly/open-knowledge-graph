---
id: collision-energy-analysis
title: Collision Analysis and Energy
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: linear-momentum-impulse-systems
  type: hard
- id: impact-and-restitution
  type: soft
tags:
- collision
- restitution
- elastic
- inelastic
- energy dissipation
- impact velocity
stage: formal-systems
status: draft
---

# Collision Analysis and Energy

## Core Idea
Collisions are classified by the coefficient of restitution e, which relates relative velocities before and after impact: e = (v₂' - v₁') / (v₁ - v₂). Elastic collisions (e = 1) conserve kinetic energy; inelastic collisions (0 ≤ e < 1) dissipate energy through deformation and heat. Momentum is always conserved, enabling calculation of post-impact velocities and energy loss.

## Explainer

From your prerequisite study of linear momentum and impulse, you know that the total momentum of a system is conserved whenever the net external impulse is zero. In a collision, the internal forces between the colliding objects are enormous but exactly equal and opposite — they contribute zero net impulse to the system. External forces like gravity act during the collision too, but the collision duration is so short that their impulse is negligible. The result: **momentum conservation is exact** for all collisions, regardless of how violent or how much energy is lost.

Momentum conservation alone gives you one equation for two unknowns (the two post-collision velocities). To close the problem you need a second equation — and this is where the **coefficient of restitution** e comes in. The coefficient of restitution relates the relative velocity of separation after impact to the relative velocity of approach before impact: e = (v₂' − v₁')/(v₁ − v₂). It is a material property that captures how much the contact surfaces elastically "bounce back." A perfectly elastic collision has e = 1, meaning the objects separate with exactly the same relative speed they approached. A perfectly inelastic collision has e = 0, meaning the objects end up moving together (zero relative velocity after impact) — maximum deformation, maximum energy loss. Real collisions fall somewhere between: a tennis ball on concrete might have e ≈ 0.75, while a lead ball might have e ≈ 0.2.

With momentum conservation and the restitution equation, you have two equations and two unknowns. Solving them gives both post-impact velocities. The **kinetic energy lost** can then be computed directly: ΔKE = ½m₁v₁² + ½m₂v₂² − ½m₁v₁'² − ½m₂v₂'². For an elastic collision (e = 1) this is zero by construction — you can verify algebraically. For an inelastic collision, the lost kinetic energy has gone into deformation, heat, sound, and vibration. A useful result: for two masses with a perfectly inelastic collision (e = 0), the energy loss depends only on the reduced mass and the relative velocity of approach — larger mass ratio means more energy survives.

The hardest conceptual step for most students is accepting that momentum is always conserved while energy is not. Momentum is a vector quantity tied to a symmetry law (spatial translation invariance) and always conserved in an isolated system. Kinetic energy is not separately conserved in inelastic collisions because energy transforms into other forms — but total energy is still conserved. The coefficient of restitution is the bridge: it tells you exactly how much relative velocity survives the collision, from which you can quantify exactly how much kinetic energy was converted into other forms.
