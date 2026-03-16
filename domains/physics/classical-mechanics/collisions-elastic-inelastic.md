---
id: collisions-elastic-inelastic
title: Elastic and Inelastic Collisions
domain: physics
course: classical-mechanics
prerequisites:
- id: conservation-of-momentum
  type: hard
- id: conservation-of-energy
  type: soft
tags:
- collisions
- elastic
- inelastic
- perfectly-inelastic
stage: abstract-reasoning
status: validated
---

# Elastic and Inelastic Collisions

## Core Idea
In elastic collisions, both momentum and kinetic energy are conserved (e.g., billiard balls at low speed). In perfectly inelastic collisions, objects stick together, momentum is conserved, but kinetic energy is not. In between are partially inelastic collisions. The coefficient of restitution e (ratio of relative speeds after to before) characterizes a collision: e = 1 (elastic), 0 < e < 1 (partially inelastic), e = 0 (perfectly inelastic).

## How It's Best Learned
Solve elastic collisions in 1D using both conservation equations simultaneously. For perfectly inelastic collisions, use a single momentum equation since the objects share a final velocity. Check: can kinetic energy increase in a collision? (No — a coefficient e > 1 would require an explosive.)

## Common Misconceptions
- Thinking elastic means the objects bounce 'hard' — elastic strictly means kinetic energy is conserved, not how hard the impact looks.
- Trying to apply both conservation laws to an inelastic collision: kinetic energy is not conserved, so only momentum conservation applies.

## Explainer

You already know that **momentum is conserved** whenever no net external force acts on a system, and that **kinetic energy is conserved** in isolated systems with only conservative forces. Collisions let you see these two principles operating together — or separately — depending on what happens at the moment of impact.

The key distinction is what happens to kinetic energy *during* the collision. In an **elastic collision**, the objects deform and rebound without any permanent deformation or heat generation — the internal forces are perfectly conservative, so kinetic energy is restored when the objects separate. Billiard balls and atomic collisions approximate this well. In an **inelastic collision**, some kinetic energy is converted into internal energy — heat, sound, deformation — during the collision. That energy doesn't disappear (total energy is always conserved), but it leaves the kinetic budget. In a **perfectly inelastic collision**, the objects stick together and move as one, maximizing the loss of kinetic energy consistent with momentum conservation.

For a **1D elastic collision** between two objects, you have two conservation equations: Σp_before = Σp_after, and ΣKE_before = ΣKE_after. Writing these out: m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂', and ½m₁v₁² + ½m₂v₂² = ½m₁v₁'² + ½m₂v₂'². Two equations, two unknowns (v₁' and v₂'). The kinetic energy equation is quadratic, but it factors conveniently — you can rewrite it as m₁(v₁ - v₁')(v₁ + v₁') = m₂(v₂' - v₂)(v₂' + v₂'), then combine with the momentum equation to get the elegant result: the **relative speed of approach equals the relative speed of separation**, (v₁ - v₂) = -(v₁' - v₂'). This is the elastic collision's signature, and it makes the algebra tractable.

The **coefficient of restitution** *e* generalizes this: it is the ratio of the relative speed after to the relative speed before, *e* = |v₂' - v₁'| / |v₁ - v₂|. For elastic collisions e = 1, for perfectly inelastic e = 0, and real collisions fall in between. Notice that e > 1 would mean the objects speed up during collision — impossible without an internal energy source like an explosion. The coefficient of restitution is the single parameter that characterizes where a real collision sits on the spectrum, and it is directly measurable by dropping a ball and seeing how high it bounces. This is why e is useful in engineering: it captures the collision behavior without requiring you to model all the internal energy losses in detail.
