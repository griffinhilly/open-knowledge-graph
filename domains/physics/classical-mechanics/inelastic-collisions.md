---
id: inelastic-collisions
title: Inelastic Collisions
domain: physics
course: classical-mechanics
prerequisites:
- id: conservation-of-momentum
  type: hard
- id: elastic-collisions-mechanics
  type: soft
builds-toward:
- collision-analysis-applications
- energy-dissipation-and-irreversibility
tags:
- collisions
- energy
- dissipation
stage: formal-systems
status: draft
---

# Inelastic Collisions

## Core Idea
In an inelastic collision, momentum is conserved but kinetic energy is not—some energy is converted into heat, sound, or deformation. A perfectly inelastic collision occurs when objects stick together afterward.

## How It's Best Learned
Compare momentum before and after with kinetic energy before and after. Calculate energy loss explicitly. Explore the special case of perfectly inelastic collisions where relative velocity becomes zero.

## Common Misconceptions
Momentum is conserved in all collisions if no external forces act. The term 'inelastic' does not mean the objects are damaged; it only describes energy loss during the collision.

## Explainer

From conservation of momentum, you know the central rule: the total momentum of a closed system does not change when no net external force acts. This holds for every collision — elastic, inelastic, and everything in between. What distinguishes collision types is what happens to **kinetic energy**. In an elastic collision (your soft prerequisite), kinetic energy is also conserved: the total KE before equals the total KE after. Real-world collisions are almost never elastic. When two cars crash, metal deforms, heat is generated, and sound propagates outward. Kinetic energy has been converted into other forms. These are **inelastic collisions**.

The key calculation is a before-and-after accounting. For two objects with masses m₁ and m₂ and initial velocities v₁ and v₂, momentum conservation gives: m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'. This equation always holds (assuming no external forces). The kinetic energy before is ½m₁v₁² + ½m₂v₂², and the kinetic energy after is ½m₁v₁'² + ½m₂v₂'². In an inelastic collision, KE_after < KE_before. The difference ΔKE is the energy that went into deformation, heat, and sound — the **energy dissipated** by the collision. Calculating this explicitly is the central skill: momentum conservation tells you how velocities change; energy accounting tells you how much energy was lost and reinforces that the outcome is physically consistent.

The special case worth mastering is the **perfectly inelastic collision**: the two objects stick together and move as one mass afterward. This is the maximum-energy-loss scenario consistent with momentum conservation. After the collision, the combined object has velocity v_f = (m₁v₁ + m₂v₂)/(m₁ + m₂) — just total momentum divided by total mass. You can show that the kinetic energy lost in a perfectly inelastic collision is always positive (it is ½μΔv², where μ is the reduced mass and Δv is the relative velocity before impact). The energy always goes somewhere; it just leaves the mechanical energy budget.

A common conceptual stumble: students sometimes wonder why we can't just use energy conservation to solve all collision problems. The answer is that kinetic energy conservation is a special condition that only applies to idealized elastic collisions, while momentum conservation is a universal consequence of Newton's third law and applies always. In problems where you are not told whether a collision is elastic, you cannot assume KE is conserved — you must use momentum conservation, which holds regardless. The ability to distinguish which quantities are conserved in a given physical situation — and why — is the core skill this topic builds.
