---
id: coefficient-of-restitution
title: Coefficient of Restitution
domain: physics
course: classical-mechanics
prerequisites:
- id: elastic-collisions-mechanics
  type: hard
- id: inelastic-collisions
  type: hard
builds-toward:
- collision-analysis-applications
tags:
- collisions
- parameters
stage: formal-systems
status: draft
---

# Coefficient of Restitution

## Core Idea
The coefficient of restitution e is the ratio of relative velocity of separation to relative velocity of approach in a collision. It ranges from 0 (perfectly inelastic) to 1 (perfectly elastic), characterizing how much the collision bounces.

## How It's Best Learned
Measure e experimentally by dropping balls and measuring rebound heights. Use e to solve collision problems as an alternative to energy conservation, which fails for inelastic collisions.

## Explainer

From your study of elastic and inelastic collisions, you know the two extremes: in a **perfectly elastic collision** kinetic energy is conserved and objects bounce as if made of ideal springs; in a **perfectly inelastic collision** the maximum kinetic energy is lost and objects stick together. Real collisions fall somewhere between these extremes. The **coefficient of restitution** *e* is a single dimensionless number that locates any given collision on this spectrum.

The definition is precise: *e* equals the ratio of the **relative speed of separation** after the collision to the **relative speed of approach** before it. If two objects approach each other at a combined closing speed of 10 m/s and separate at 7 m/s, then *e* = 0.7. When *e* = 1, objects separate at the same relative speed they approached — perfectly elastic. When *e* = 0, they do not separate at all — perfectly inelastic. All real materials produce *e* values strictly between 0 and 1, because some kinetic energy is always converted to heat, sound, and permanent deformation.

The coefficient of restitution is practically important because it provides a second equation for collision problems, complementing conservation of momentum. For inelastic collisions, you cannot use energy conservation — you don't know how much energy was lost. But you *can* apply both momentum conservation and the *e* equation simultaneously to determine both final velocities. In one dimension, this system of two equations (momentum and restitution) is exactly sufficient to solve for two unknowns given a known *e*, making it the standard approach for any collision that is neither perfectly elastic nor perfectly inelastic.

An intuitive way to measure *e* for a bouncing ball is to drop it from height *h* and measure the rebound height *h'*. Because the ball approaches the floor with speed proportional to √*h* and rebounds with speed proportional to √*h'*, the coefficient of restitution equals √(*h'*/*h*). A superball with *e* ≈ 0.9 rebounds to about 81% of its drop height; a clay ball with *e* ≈ 0.1 barely bounces. This reveals that *e* is a property of the *pair* of materials in contact — it depends on both surfaces — and in reality it also varies with impact speed, temperature, and geometry, which is why the simple model works well for introductory problems but must be refined for engineering applications.
