---
id: rigid-body-plane-motion-analysis
title: General Plane Motion of Rigid Bodies
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: rigid-body-kinematics-general-motion
  type: hard
- id: rotation-fixed-axis-dynamics
  type: hard
builds-toward:
- instantaneous-center-of-rotation-method
tags:
- plane-motion
- translation
- rotation
- general
stage: formal-systems
status: draft
---

# General Plane Motion of Rigid Bodies

## Core Idea
General plane motion combines translation of the center of mass and rotation about the center of mass. The velocity of any point is v = v_cm + ω × r. Kinetic energy is KE = ½m v_cm² + ½I_cm ω². The equations of motion are ΣF = m a_cm and ΣM_cm = I_cm α, which decouple translation and rotation.

## Explainer

You've already analyzed rotation about a fixed axis and the kinematics of general rigid body motion. **General plane motion** is the synthesis: a body that simultaneously translates and rotates, with no axis fixed in space. Think of a wheel rolling down a ramp, a connecting rod in an engine, or a football tumbling through the air. The key insight is that no matter how complicated the motion looks, you can always decompose it into two independent parts: the translation of the center of mass, and the rotation about the center of mass.

This decomposition is what makes the equations of motion so clean. The net external force vector equals m times the acceleration of the center of mass — full stop. It does not matter how the body is rotating; translational dynamics depends only on where the CM is accelerating. Similarly, the net external moment about the center of mass equals I_cm times the angular acceleration α — and this is true regardless of how the CM is translating. The two equations ΣF = m·a_cm and ΣM_cm = I_cm·α are independent of each other. This is why you always sum moments about the center of mass (or about another strategically chosen point) — it uncouples the problem.

The kinetic energy formula KE = ½m·v_cm² + ½I_cm·ω² reflects the same decomposition. The first term is the energy of a point mass moving with the CM; the second is the energy of spinning about the CM. For a rolling wheel, both terms contribute — it has translational KE from its moving center and rotational KE from spinning. For a sliding hockey puck (no rotation), only the first term contributes. Understanding which modes carry energy matters for problems involving collisions, energy conservation, and designing systems that need to absorb or store energy efficiently.

When solving a plane motion problem, the standard approach is: (1) identify all external forces and moments, (2) write ΣF_x = m·a_cx, ΣF_y = m·a_cy for the translational equations, (3) write ΣM_cm = I_cm·α for the rotational equation, and (4) use kinematic constraints — like the rolling constraint v_cm = ω·R for a wheel — to reduce the number of unknowns. The kinematic constraint is often what connects the translational and rotational variables, turning three equations and three unknowns into a solvable system. Getting comfortable with identifying and writing that constraint is the central skill the method requires.
