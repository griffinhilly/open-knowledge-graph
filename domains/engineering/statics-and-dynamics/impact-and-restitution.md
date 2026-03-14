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
