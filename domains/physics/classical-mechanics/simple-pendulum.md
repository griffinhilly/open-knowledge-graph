---
id: simple-pendulum
title: The Simple Pendulum
domain: physics
course: classical-mechanics
prerequisites:
- id: simple-harmonic-motion
  type: hard
- id: circular-motion-kinematics
  type: soft
- id: trigonometric-ratios-review
  type: soft
tags:
- pendulum
- SHM
- oscillation
- gravity
stage: abstract-reasoning
status: validated
---

# The Simple Pendulum

## Core Idea
A simple pendulum (point mass on a massless string of length L) undergoes approximate SHM for small angles (θ < ~15°), with angular frequency ω = √(g/L) and period T = 2π√(L/g). The restoring force is the tangential component of gravity: F_t = −mg sinθ ≈ −mgθ (small angle). The period depends on L and g, but not on mass or amplitude (for small oscillations).

## How It's Best Learned
Measure pendulum period for various lengths and verify the T ∝ √L relationship. Also test the small-angle approximation by comparing measured periods at 5°, 20°, and 45° amplitude — the approximation degrades at large angles.

## Common Misconceptions
- Thinking heavier pendulums oscillate faster: period is mass-independent.
- Applying T = 2π√(L/g) for large swings: it overestimates period because sin θ < θ only for small θ.
- Confusing the pendulum length L (measured to the center of mass) with the string length when using a physical bob of nonnegligible size.
