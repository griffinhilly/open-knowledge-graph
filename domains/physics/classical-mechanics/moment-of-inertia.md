---
id: moment-of-inertia
title: Moment of Inertia
domain: physics
course: classical-mechanics
prerequisites:
- id: torque
  type: hard
- id: definite-integral-definition
  type: soft
- id: center-of-mass
  type: soft
builds-toward:
- rotational-dynamics
- angular-momentum
tags:
- moment-of-inertia
- rotational-inertia
- mass-distribution
stage: formal-systems
status: validated
---
# Moment of Inertia

## Core Idea
The moment of inertia I = Σmᵢrᵢ² (or ∫r² dm for continuous bodies) is the rotational analog of mass — it measures resistance to angular acceleration. Unlike mass, I depends on how mass is distributed relative to the rotation axis: mass farther from the axis contributes more. Standard results include: I = MR² (ring), I = ½MR² (solid disk), I = ⅔MR² (solid sphere shell), I = ⅖MR² (solid sphere). The parallel axis theorem I = I_cm + Md² allows computing I about any axis.

## How It's Best Learned
Memorize key moments of inertia for standard shapes, then apply the parallel axis theorem for off-center axes. Develop physical intuition: a hollow cylinder has greater I than a solid one of the same mass because its mass is farther from the axis.

## Common Misconceptions
- Thinking moment of inertia is a fixed property of an object — it depends entirely on the chosen rotation axis.
- Applying parallel axis theorem with d measured from the wrong axis: d must be measured from the center-of-mass axis.
