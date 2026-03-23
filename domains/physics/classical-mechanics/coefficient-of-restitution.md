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
status: validated
---

# Coefficient of Restitution

## Core Idea
The coefficient of restitution e is the ratio of relative velocity of separation to relative velocity of approach in a collision. It ranges from 0 (perfectly inelastic) to 1 (perfectly elastic), characterizing how much the collision bounces.

## How It's Best Learned
Measure e experimentally by dropping balls and measuring rebound heights. Use e to solve collision problems as an alternative to energy conservation, which fails for inelastic collisions.

## Questions

```yaml
- question: "Object A (mass m) moves at 10 m/s toward stationary object B (also mass m). After the collision, A moves at 2 m/s and B moves at 8 m/s in the same direction. What is the coefficient of restitution?"
  type: multiple-choice
  options:
    - "e = (2 + 8)/10 = 1.0 — this is a perfectly elastic collision"
    - "e = (8 − 2)/(10 − 0) = 0.6"
    - "e = 10/(8 + 2) = 1.0 — same result, confirming elastic collision"
    - "e cannot be calculated without knowing the actual masses"
  answer: 1
  explanation: "The coefficient of restitution is e = (relative speed of separation)/(relative speed of approach). Before: A approaches B at 10 − 0 = 10 m/s relative speed. After: B moves away from A at 8 − 2 = 6 m/s relative speed. So e = 6/10 = 0.6. Option A sums the final speeds instead of taking their difference — a common error that conflates momentum with relative velocity. Momentum conservation checks out (10m = 2m + 8m ✓), confirming these are valid post-collision velocities. Note e = 0.6 < 1, consistent with a real (not perfectly elastic) collision."

- question: "A student claims that for a collision with known e = 0.7, momentum conservation alone is sufficient to find both final velocities. Why is this incorrect, and what additional equation is needed?"
  type: multiple-choice
  options:
    - "Momentum is not conserved in inelastic collisions; you need energy conservation instead"
    - "Momentum conservation gives one equation for two unknowns; the restitution equation e = (relative separation speed)/(relative approach speed) provides the necessary second equation"
    - "For e < 1, the standard collision equations don't apply — you need a separate energy-loss formula"
    - "The student is correct — momentum conservation is sufficient for any collision problem"
  answer: 1
  explanation: "For a collision between two objects, there are two unknown final velocities. Momentum conservation gives exactly one equation linking them. Without a second independent equation, the system is underdetermined — infinitely many pairs of final velocities conserve momentum. The restitution equation e = v_rel,after / v_rel,before is that second equation. Together they form a solvable 2×2 linear system. This is precisely why the coefficient of restitution is useful: energy conservation fails for inelastic collisions (the energy lost is unknown), but e is a given material property that provides the needed constraint."

- question: "A ball dropped from height h rebounds to height h'. The coefficient of restitution for this ball-floor collision equals h'/h."
  type: true-false
  answer: false
  explanation: "e = √(h'/h), not h'/h. Height is proportional to kinetic energy (h ~ v²), so the impact speed is proportional to √h and the rebound speed to √h'. The coefficient of restitution is the ratio of speeds, not energies: e = √h'/√h = √(h'/h). Equivalently, e² = h'/h. A ball with e = 0.9 rebounds to h' = e²h = 0.81h, not 0.9h. This is a common error that confuses the ratio of heights (which gives e²) with the ratio of speeds (which gives e)."

- question: "The coefficient of restitution is a property of a single material — a rubber ball has the same e regardless of what surface it bounces against."
  type: true-false
  answer: false
  explanation: "The coefficient of restitution characterizes the pair of materials in contact, not a single material alone. A rubber ball bouncing on hardwood, concrete, carpet, or another rubber ball will have different e values because the energy loss during impact depends on how both surfaces deform and interact. Specifying e requires specifying both surfaces. This is why engineering specifications for e always name both materials, and why a ball may bounce very differently on different surfaces even though the ball itself hasn't changed."

- question: "Why is the coefficient of restitution useful specifically for solving inelastic collision problems, when energy conservation cannot be used?"
  type: short-answer
  answer: "In any collision that is not perfectly elastic, kinetic energy is lost — converted to heat, sound, and deformation. The amount lost is not known in advance, so energy conservation cannot be written as a useful equation (it would introduce the unknown energy loss as a third variable). The coefficient of restitution sidesteps this problem: e is a known material property, and the equation e = (relative separation speed)/(relative approach speed) provides a second independent equation alongside momentum conservation. Two equations for two unknown final velocities makes the system exactly solvable without needing to know how much energy was lost."
  explanation: "This is the conceptual core of why e is introduced as a concept. For perfectly elastic collisions, energy conservation provides the second equation. For perfectly inelastic collisions, the objects stick together, so there is only one unknown final velocity and momentum alone suffices. For all intermediate cases — the vast majority of real collisions — neither energy conservation nor the sticking condition applies, and e fills the gap."
```

## Explainer

From your study of elastic and inelastic collisions, you know the two extremes: in a **perfectly elastic collision** kinetic energy is conserved and objects bounce as if made of ideal springs; in a **perfectly inelastic collision** the maximum kinetic energy is lost and objects stick together. Real collisions fall somewhere between these extremes. The **coefficient of restitution** *e* is a single dimensionless number that locates any given collision on this spectrum.

The definition is precise: *e* equals the ratio of the **relative speed of separation** after the collision to the **relative speed of approach** before it. If two objects approach each other at a combined closing speed of 10 m/s and separate at 7 m/s, then *e* = 0.7. When *e* = 1, objects separate at the same relative speed they approached — perfectly elastic. When *e* = 0, they do not separate at all — perfectly inelastic. All real materials produce *e* values strictly between 0 and 1, because some kinetic energy is always converted to heat, sound, and permanent deformation.

The coefficient of restitution is practically important because it provides a second equation for collision problems, complementing conservation of momentum. For inelastic collisions, you cannot use energy conservation — you don't know how much energy was lost. But you *can* apply both momentum conservation and the *e* equation simultaneously to determine both final velocities. In one dimension, this system of two equations (momentum and restitution) is exactly sufficient to solve for two unknowns given a known *e*, making it the standard approach for any collision that is neither perfectly elastic nor perfectly inelastic.

An intuitive way to measure *e* for a bouncing ball is to drop it from height *h* and measure the rebound height *h'*. Because the ball approaches the floor with speed proportional to √*h* and rebounds with speed proportional to √*h'*, the coefficient of restitution equals √(*h'*/*h*). A superball with *e* ≈ 0.9 rebounds to about 81% of its drop height; a clay ball with *e* ≈ 0.1 barely bounces. This reveals that *e* is a property of the *pair* of materials in contact — it depends on both surfaces — and in reality it also varies with impact speed, temperature, and geometry, which is why the simple model works well for introductory problems but must be refined for engineering applications.
