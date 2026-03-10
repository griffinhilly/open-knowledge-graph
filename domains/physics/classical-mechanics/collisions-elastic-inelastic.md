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
stage: formal-systems
status: draft
---

# Elastic and Inelastic Collisions

## Core Idea
In elastic collisions, both momentum and kinetic energy are conserved (e.g., billiard balls at low speed). In perfectly inelastic collisions, objects stick together, momentum is conserved, but kinetic energy is not. In between are partially inelastic collisions. The coefficient of restitution e (ratio of relative speeds after to before) characterizes a collision: e = 1 (elastic), 0 < e < 1 (partially inelastic), e = 0 (perfectly inelastic).

## How It's Best Learned
Solve elastic collisions in 1D using both conservation equations simultaneously. For perfectly inelastic collisions, use a single momentum equation since the objects share a final velocity. Check: can kinetic energy increase in a collision? (No — a coefficient e > 1 would require an explosive.)

## Common Misconceptions
- Thinking elastic means the objects bounce 'hard' — elastic strictly means kinetic energy is conserved, not how hard the impact looks.
- Trying to apply both conservation laws to an inelastic collision: kinetic energy is not conserved, so only momentum conservation applies.
