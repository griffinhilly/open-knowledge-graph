---
id: conservation-of-linear-momentum
title: Conservation of Linear Momentum in Systems
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: linear-momentum-impulse-systems
  type: hard
- id: newtons-three-laws-mechanics
  type: soft
builds-toward:
- systems-of-particles-mechanics
tags:
- momentum
- conservation-laws
- systems
stage: formal-systems
status: draft
---

# Conservation of Linear Momentum in Systems

## Core Idea
When no external forces act on a system (or sum to zero), total linear momentum remains constant. This conservation law follows directly from Newton's third law and is far more powerful than tracking individual particle motions—it solves collision and explosion problems without knowing details of internal forces.

## Explainer

From your work with impulse and momentum, you know that the change in a single particle's momentum equals the net impulse applied to it: ΔL = ∫F_net dt. Now extend that thinking to a **system** of particles. Any two particles within the system exert forces on each other — but Newton's third law guarantees those internal forces are equal in magnitude and opposite in direction. When you add up all the momenta changes across the entire system, the internal forces cancel in pairs. Only the **external forces** — forces from outside the system boundary — can change the total momentum. If the external forces sum to zero (or if the time interval is so short that their impulse is negligible), the total momentum before equals the total momentum after.

This is powerful because it lets you bypass the internal force details entirely. In a collision between two billiard balls, enormous contact forces act for a few milliseconds — forces that are difficult to measure or model. You never need to know them. You only need to identify the system (both balls), confirm that external impulses are negligible during the collision (gravity acts, but the collision is so brief that mg·Δt ≈ 0), and then write **m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'**. The same logic applies to explosions run in reverse: a stationary artillery shell that bursts into fragments must have zero total momentum after the explosion because it had zero momentum before.

Conservation is **directional**: it applies independently in x, y, and z. A hockey puck sliding across frictionless ice and struck by a glancing blow conserves momentum in the direction perpendicular to the impulse, even if it does not conserve momentum in the direction of the impulse. This independence is frequently the key to solving two-dimensional collision problems: one direction may be constrained (a ball bouncing off a wall can only leave horizontally), giving you an equation that pins down one component of the unknown velocity.

Watch the system boundary carefully. Include all objects that interact internally; exclude everything whose forces you want to ignore as external. If friction is present and acts for a nontrivial time, it is an external impulse and momentum is not conserved. If the problem asks you to analyze only part of the collision — say, one of the two colliding objects — then the contact force between them is external to that subsystem and must be included. The beauty of conservation is that it rewards choosing the right system: pick the boundary where external impulses vanish, and a complicated interaction collapses into a simple bookkeeping equation.


