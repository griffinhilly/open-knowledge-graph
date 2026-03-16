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

## Explainer

You know from moment of inertia that I = Σmᵢrᵢ² (or ∫r² dm for continuous objects) measures how mass is distributed relative to a rotation axis — the further the mass, the larger its contribution, and the harder the object is to spin. But the moment of inertia depends critically on *which axis you choose*. A solid cylinder spun about its central axis has a very different I than the same cylinder spun about an axis along its rim. Do you have to redo the full integral every time? The parallel axis theorem says no, as long as the new axis is parallel to one you've already computed.

The theorem states: **I = I_CM + Md²**, where I_CM is the moment of inertia about an axis through the center of mass, M is the total mass, and d is the perpendicular distance from the center of mass axis to the new axis. The proof follows directly from expanding the definition of I with shifted coordinates — it's a straightforward application of the identity that Σmᵢ(rᵢ - d)² = Σmᵢrᵢ² - 2d·Σmᵢrᵢ + Md², and the middle term vanishes because the center of mass is at the origin by definition. The Md² term represents the additional rotational inertia you pick up by displacing all the mass by distance d from the axis — every bit of mass is now at least d away.

The physical intuition is this: when you shift the rotation axis away from the center of mass, two things happen. First, the mass distribution relative to the new axis is more spread out overall (I_CM remains the same, since it measures internal distribution). Second, even if all the mass were concentrated at the center of mass, it would now be at distance d from the axis and contribute Md². The theorem says the total effect is simply the sum. Importantly, I_CM is the *minimum* moment of inertia among all parallel axes — any other parallel axis gives a strictly larger value, because Md² ≥ 0.

In practice, you will use this theorem constantly. Look up or compute the moment of inertia of a standard shape about its center of mass (there are tables for disks, rods, spheres, cylinders), then apply I = I_CM + Md² for whatever axis the problem needs. For example: a solid disk of mass M and radius R has I_CM = ½MR² about its central axis. About an axis at its rim (d = R), the theorem gives I = ½MR² + MR² = (3/2)MR². You do not need to redo the integral — you just shift the axis. This is the theorem's practical power.

The theorem also has a companion — the **perpendicular axis theorem** for flat (planar) objects, which relates moments about two in-plane axes to the moment about the axis perpendicular to the plane. Together, they give you a complete toolkit for rotating objects about any axis without integration, as long as you know the standard center-of-mass moments. As you move into rotational dynamics, these will be your standard computational tools.

