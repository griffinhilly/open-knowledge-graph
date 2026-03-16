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

## Explainer

The center of mass is the single most useful simplification in the mechanics of multi-part systems. When you have a complex object — a rigid body, a collection of particles, a system of interacting masses — you often don't need to track every individual part. From your prerequisite in **Newton's second law**, you know that F = ma for a single particle. The center-of-mass theorem extends this: **F_net = M · a_cm**, where F_net is the total *external* force, M is the total mass, and a_cm is the acceleration of the center of mass. Every internal force — the molecular bonds holding a baseball together, the mutual gravitational attraction between Earth and Moon — cancels out in pairs by Newton's third law. Only what the *outside* does to the system matters for CM motion.

To build intuition for the formula r_cm = (Σmᵢrᵢ)/M, think of it as a mass-weighted average — a tug-of-war where each particle pulls the average toward itself in proportion to its mass. Place a 1 kg mass at x = 0 and a 3 kg mass at x = 4 m: the CM sits at (1·0 + 3·4)/4 = 3 m, three-quarters of the way toward the heavier mass. The heavier particle dominates. For a continuous body, the integral r_cm = (∫r dm)/M does the same thing for infinitely many infinitesimal mass elements — your prerequisite in **integration for area and mass** gives you the tools to evaluate this directly by setting up dm = ρ dV and integrating over the body.

The most striking implication concerns trajectory independence from internal motion. Throw a wrench through the air: it tumbles and rotates, but its CM traces a perfect parabolic arc exactly as a single point-mass would. The tumbling is internal redistribution of mass; it does not appear in F_net = M · a_cm because the internal forces sum to zero. Similarly, if an artillery shell explodes mid-flight, the fragments scatter in all directions, but the CM of all the fragments continues along the same parabolic path the intact shell was on — because the explosion is internal. External forces alone (gravity, air resistance) change the CM trajectory.

The CM concept directly sets up everything that follows in this course. **Conservation of momentum** is just F_net = M · a_cm with F_net = 0: if no net external force acts, the CM moves at constant velocity, meaning the total momentum M · v_cm is conserved. When you move to **rotational dynamics** and **moment of inertia**, the CM becomes the natural reference point — an object rotating about its own CM has the simplest equations of motion, and the parallel-axis theorem lets you shift to any parallel axis. Mastering the CM now means you already understand the architecture of multi-body dynamics before you have learned any of its detailed techniques.
