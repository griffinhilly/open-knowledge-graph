---
id: parallel-axis-theorem
title: Parallel Axis Theorem
domain: physics
course: classical-mechanics
prerequisites:
- id: moment-of-inertia
  type: hard
- id: triple-integrals
  type: soft
builds-toward:
- rotational-dynamics
tags:
- moment-of-inertia
- rotation
- theorem
stage: formal-systems
status: draft
---

# Parallel Axis Theorem

## Core Idea
The moment of inertia about any axis equals the moment about a parallel axis through the center of mass plus M·d², where d is the distance between the axes: I = I_CM + M·d². This theorem eliminates the need to integrate for every possible axis; compute I_CM once, then use the simple formula for any parallel axis.
