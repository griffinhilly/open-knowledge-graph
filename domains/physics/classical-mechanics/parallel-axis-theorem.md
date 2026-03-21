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

## Questions

```yaml
- question: "A solid disk of mass M and radius R has I_CM = ½MR² about its central axis. What is its moment of inertia about an axis tangent to its rim, parallel to the central axis?"
  type: multiple-choice
  options:
    - "½MR²  — the same as the center-of-mass value, since the mass distribution doesn't change"
    - "MR²  — just the Md² term, since d = R"
    - "(3/2)MR²  — applying I = I_CM + Md² with d = R gives ½MR² + MR²"
    - "2MR²  — you double I_CM when moving to the rim"
  answer: 2
  explanation: "The parallel axis theorem gives I = I_CM + Md². The axis at the rim is parallel to the central axis and displaced by d = R. So I = ½MR² + M(R²) = (3/2)MR². Option A forgets the Md² term — a common error from not realizing that displacing the axis always adds inertia. Option B forgets I_CM. Option D has no derivation; doubling is incorrect. The extra MR² represents the additional inertia from the fact that all the mass is now at least distance R from the new axis."

- question: "Why does the parallel axis theorem include a Md² term?"
  type: multiple-choice
  options:
    - "It corrects for rotational friction at the new axis location"
    - "Even if all the mass were concentrated at the center of mass, it would now be at distance d from the new axis — this additional contribution is exactly Md², and the theorem's proof shows the cross-term vanishes"
    - "It reduces I_CM to account for mass that is now closer to the new axis than to the old one"
    - "It converts from the center-of-mass reference frame to an inertial lab frame"
  answer: 1
  explanation: "The proof of the theorem expands I = Σmᵢ(rᵢ − d)² = Σmᵢrᵢ² − 2d·Σmᵢrᵢ + Md². The first term is I_CM, the middle term vanishes because the center of mass is at the origin by definition (Σmᵢrᵢ = 0 in the CM frame), and the last term Md² remains. Physically: when you shift the axis by d, even a point mass at the center of mass is now at distance d from the axis, contributing Md² to the total moment of inertia. The spread of mass around the CM (I_CM) is unchanged; you've simply added the inertia of the CM's own displacement."

- question: "Among all axes parallel to a given direction, the axis through the center of mass gives the smallest moment of inertia."
  type: true-false
  answer: true
  explanation: "This follows directly from I = I_CM + Md². Since M > 0 and d² ≥ 0, we have I ≥ I_CM for every parallel axis, with equality only when d = 0 (i.e., the axis passes through the center of mass). Any displacement strictly increases the moment of inertia. This makes the center-of-mass axis special: it is the axis of minimum rotational inertia among all parallel axes, which has physical consequences for natural rotation and the design of rotating machinery."

- question: "The parallel axis theorem can be applied to find the moment of inertia about any new axis, whether or not it is parallel to the original axis through the center of mass."
  type: true-false
  answer: false
  explanation: "The parallel axis theorem applies only to parallel axes — axes that have the same orientation in space, differing only in their location (perpendicular displacement d). The formula I = I_CM + Md² does not apply when the new axis is tilted relative to the center-of-mass axis, because the derivation assumes the coordinate shift is purely perpendicular. For axes in different orientations, you need the full inertia tensor and the general transformation rules."

- question: "Why does the parallel axis theorem make physical sense? What does the Md² term represent, and why does the I_CM term remain unchanged?"
  type: short-answer
  answer: "When the rotation axis is displaced from the center of mass by distance d, two contributions add independently. First, I_CM captures how the mass is internally distributed around the center of mass — this doesn't change when you shift the axis, because the relative positions of all the mass elements to each other are unchanged. Second, Md² captures what would happen even if all the mass were concentrated at the center of mass: a point mass M at distance d from the axis contributes Md² to rotational inertia. The theorem says the total effect is the sum of these two independent contributions, because the cross-term in the algebraic expansion vanishes when you work in the center-of-mass frame."
  explanation: "The physical intuition is cleanest this way: shifting the axis has two effects that can be computed separately — the internal distribution (unchanged, so I_CM) and the displacement of the whole mass distribution's center (adding Md²). The vanishing cross-term is the mathematical expression of the fact that the center of mass is exactly the 'balance point' — there is no net first moment around it."
```

## Explainer

You know from moment of inertia that I = Σmᵢrᵢ² (or ∫r² dm for continuous objects) measures how mass is distributed relative to a rotation axis — the further the mass, the larger its contribution, and the harder the object is to spin. But the moment of inertia depends critically on *which axis you choose*. A solid cylinder spun about its central axis has a very different I than the same cylinder spun about an axis along its rim. Do you have to redo the full integral every time? The parallel axis theorem says no, as long as the new axis is parallel to one you've already computed.

The theorem states: **I = I_CM + Md²**, where I_CM is the moment of inertia about an axis through the center of mass, M is the total mass, and d is the perpendicular distance from the center of mass axis to the new axis. The proof follows directly from expanding the definition of I with shifted coordinates — it's a straightforward application of the identity that Σmᵢ(rᵢ - d)² = Σmᵢrᵢ² - 2d·Σmᵢrᵢ + Md², and the middle term vanishes because the center of mass is at the origin by definition. The Md² term represents the additional rotational inertia you pick up by displacing all the mass by distance d from the axis — every bit of mass is now at least d away.

The physical intuition is this: when you shift the rotation axis away from the center of mass, two things happen. First, the mass distribution relative to the new axis is more spread out overall (I_CM remains the same, since it measures internal distribution). Second, even if all the mass were concentrated at the center of mass, it would now be at distance d from the axis and contribute Md². The theorem says the total effect is simply the sum. Importantly, I_CM is the *minimum* moment of inertia among all parallel axes — any other parallel axis gives a strictly larger value, because Md² ≥ 0.

In practice, you will use this theorem constantly. Look up or compute the moment of inertia of a standard shape about its center of mass (there are tables for disks, rods, spheres, cylinders), then apply I = I_CM + Md² for whatever axis the problem needs. For example: a solid disk of mass M and radius R has I_CM = ½MR² about its central axis. About an axis at its rim (d = R), the theorem gives I = ½MR² + MR² = (3/2)MR². You do not need to redo the integral — you just shift the axis. This is the theorem's practical power.

The theorem also has a companion — the **perpendicular axis theorem** for flat (planar) objects, which relates moments about two in-plane axes to the moment about the axis perpendicular to the plane. Together, they give you a complete toolkit for rotating objects about any axis without integration, as long as you know the standard center-of-mass moments. As you move into rotational dynamics, these will be your standard computational tools.

