---
id: center-of-mass
title: Center of Mass
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-second-law
  type: hard
- id: vectors-in-two-dimensions
  type: soft
- id: definite-integral-definition
  type: soft
- id: applications-integrals-area-mass
  type: hard
- id: triple-integrals
  type: soft
builds-toward:
- conservation-of-momentum
- rotational-dynamics
- moment-of-inertia
tags:
- center-of-mass
- mass-distribution
- reference-point
stage: formal-systems
status: validated
---

# Center of Mass

## Core Idea
The center of mass (CM) of a system of particles is the mass-weighted average position: r_cm = (Σmᵢrᵢ)/(Σmᵢ). For continuous bodies, r_cm = (∫r dm)/M. Newton's second law for a system states that the net external force equals total mass times the acceleration of the CM: F_net = M·a_cm. Internal forces between parts of the system do not affect the CM motion, making the center of mass the natural reference point for dynamics.

## How It's Best Learned
Compute CM positions for simple discrete systems (two masses on a rod) and verify by balancing the rod at the computed point. Then extend to uniform 2D shapes using symmetry and integration.

## Common Misconceptions
- Thinking the CM must be located inside the object: for a ring or hollow shell, the CM lies at the geometric center where there is no material.
- Confusing the CM (weighted by mass) with the geometric centroid (weighted by volume) when density is nonuniform.
