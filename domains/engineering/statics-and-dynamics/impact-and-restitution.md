---
id: impact-and-restitution
title: Impact and Coefficient of Restitution
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: impulse-momentum-particles
  type: hard
- id: collisions-elastic-inelastic
  type: soft
tags:
- dynamics
- impact
- collision
- coefficient of restitution
- energy loss
stage: formal-systems
status: validated
---

# Impact and Coefficient of Restitution

## Core Idea
Impact between two particles is analyzed using the coefficient of restitution e, defined as e = (v'_B − v'_A) / (v_A − v_B) along the line of impact (common normal at contact). For perfectly elastic impact e = 1 (no kinetic energy loss); for perfectly plastic impact e = 0 (maximum energy loss, particles stick together). Combined with conservation of linear momentum along the line of impact, the two equations determine post-impact velocities. For oblique impacts, tangential velocity components of smooth spheres are unchanged, and restitution applies only along the line of impact.

## How It's Best Learned
Always identify the line of impact first (direction of common normal at contact). Write conservation of momentum and the restitution equation as a two-equation system and solve simultaneously. Verify that kinetic energy is not gained.

## Common Misconceptions
- Applying the restitution equation in the tangential direction instead of along the line of impact.
- Confusing e = 1 (elastic, no energy loss) with a special case requiring equal masses.
- In oblique impacts, incorrectly changing the tangential velocity components of smooth particles during contact.

## Explainer

From your work with impulse-momentum and collisions, you know that a collision is a brief, high-force interaction and that linear momentum is conserved across it. The problem with stopping there is that momentum conservation alone gives you one equation and two unknowns (the two post-impact velocities along the line of contact). You need a second equation — and that is where the **coefficient of restitution** e comes in.

The coefficient of restitution is defined along the **line of impact** (the common normal at the contact point, which is the line connecting the centers of two spheres or the normal to a flat surface): e = (v'_B − v'_A) / (v_A − v_B). Read it as a ratio of separation speed to approach speed. When e = 1, the particles separate exactly as fast as they approached — no kinetic energy is lost, which is the **perfectly elastic** case. When e = 0, v'_A = v'_B — the particles stick together and move as one, which is the **perfectly plastic** case with maximum energy loss. All real impacts fall somewhere between 0 and 1; a rubber ball on concrete might have e ≈ 0.8, a lump of clay on steel might have e ≈ 0.1.

With these two equations — conservation of momentum and the restitution relationship — you can always solve for both post-impact velocities along the line of impact. The procedure is: (1) identify the line of impact, (2) write the scalar momentum equation m_A*v_A + m_B*v_B = m_A*v'_A + m_B*v'_B, (3) write the restitution equation, (4) solve the system. You should always check that kinetic energy does not increase in the result — that would violate physics.

Oblique impacts add a layer of geometry but no new physics. When two smooth spheres collide at an angle, the contact force acts only along the line of impact (the normal direction) — there is no friction force in the tangential direction. This means the momentum equation and restitution equation apply only in the normal direction, and the tangential velocity components of each particle are completely unchanged by the impact. The key move is to decompose each particle's velocity into normal and tangential components at the start, apply impact analysis in the normal direction only, and then reassemble the post-impact velocity from the new normal component and the unchanged tangential component. Many students forget this decomposition and incorrectly try to apply restitution in the tangential direction, producing nonsensical results.
