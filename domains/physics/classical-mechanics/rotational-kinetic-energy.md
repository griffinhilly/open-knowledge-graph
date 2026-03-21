---
id: rotational-kinetic-energy
title: Rotational Kinetic Energy
domain: physics
course: classical-mechanics
prerequisites:
- id: kinetic-energy
  type: hard
- id: moment-of-inertia
  type: hard
- id: rotational-kinematics
  type: hard
builds-toward: []
tags:
- kinetic-energy
- rotation
- energy
stage: formal-systems
status: draft
---
# Rotational Kinetic Energy

## Core Idea
A rotating object has kinetic energy KE_rot = ½ I ω², where I is the moment of inertia about the rotation axis and ω is angular velocity. This is the rotational analog of KE = ½ m v². For an object both rotating and translating, total KE = ½ m v_CM² + ½ I_CM ω², where both terms contribute to the energy.

## Questions

```yaml
- question: "A hollow cylinder and a solid sphere of the same mass and radius are released from rest at the top of the same ramp. Which reaches the bottom first, and why?"
  type: multiple-choice
  options:
    - "The hollow cylinder, because its mass is concentrated at the rim, giving it more rotational momentum"
    - "They arrive simultaneously, since they have the same mass and radius and start from the same height"
    - "The solid sphere, because its moment of inertia is smaller (2/5 MR² vs. MR²), so less of the available potential energy goes into rotation and more into translational speed"
    - "The hollow cylinder, because a larger moment of inertia means more total kinetic energy at the bottom"
  answer: 2
  explanation: "Both objects start with the same gravitational potential energy (mgh). At the bottom, that energy is split between translational KE (½mv²) and rotational KE (½Iω²). The hollow cylinder has I = MR² (all mass at the rim); the solid sphere has I = 2/5 MR². The larger I of the hollow cylinder means more energy is channeled into rotation and less into translation — so the cylinder moves along the ramp more slowly. The sphere wins because its mass distribution puts less emphasis on rotation."

- question: "For a ball rolling without slipping down a ramp, which equation correctly expresses the total kinetic energy at any point?"
  type: multiple-choice
  options:
    - "KE = ½Iω², since rolling is purely rotational"
    - "KE = ½mv², since the relevant velocity is the center-of-mass velocity"
    - "KE = ½mv_CM² + ½I_CM ω², where both translational and rotational terms contribute"
    - "KE = mv_CM² because the factor of ½ cancels when both terms are combined"
  answer: 2
  explanation: "A rolling object simultaneously translates (center of mass moves) and rotates (spins about the center of mass). Both motions store kinetic energy. The total is the sum: translational KE of the center of mass plus rotational KE about the center of mass. The rolling-without-slipping constraint v_CM = Rω links these terms, but they are distinct contributions to the total energy. Treating rolling as purely translational or purely rotational both give wrong answers."

- question: "For a rigid object rolling without slipping, the total kinetic energy equals the translational kinetic energy of the center of mass plus the rotational kinetic energy about the center of mass."
  type: true-false
  answer: true
  explanation: "This additive decomposition is exact for rigid bodies. Rolling without slipping means the object simultaneously translates at v_CM and rotates at ω = v_CM/R. The translational term ½mv_CM² captures the motion of the center of mass through space; the rotational term ½I_CM ω² captures the spin about the center of mass. The two terms are funded by the same energy source (gravity when rolling downhill) and add linearly."

- question: "A hollow hoop (I = MR²) and a solid disk (I = ½MR²) of the same mass and radius, both rolling without slipping, will reach the same translational speed at the bottom of any ramp."
  type: true-false
  answer: false
  explanation: "They will not. Because both start with the same potential energy (mgh), and that energy splits between translation and rotation, the disk — with the smaller I — puts less energy into rotation and more into translation, arriving faster. The hoop concentrates all mass at the rim (maximum I), so it puts proportionally more energy into rotation, leaving less for translational speed. The final translational speed depends on the moment of inertia, not just the mass and radius."

- question: "Explain why a hollow cylinder rolls slower down a ramp than a solid sphere of the same mass and radius, using rotational kinetic energy and moment of inertia."
  type: short-answer
  answer: "Both objects start with the same gravitational potential energy, which converts entirely to kinetic energy at the bottom. For each, total KE = ½mv² + ½Iω². The rolling constraint v = Rω lets us write this as KE = ½mv²(1 + I/MR²). A larger I means a larger fraction of total KE goes into rotation and a smaller fraction goes into translational speed. The hollow cylinder has I = MR² (all mass at radius R), giving a factor of (1 + 1) = 2. The solid sphere has I = 2/5 MR², giving a factor of (1 + 2/5) = 7/5. The sphere's smaller factor means more of the energy is translational — so it moves faster along the ramp."
  explanation: "This is the power of the energy method: without computing torques, angular acceleration, or friction forces, a single energy equation explains why shape matters for rolling. The moment of inertia summarizes how mass is distributed relative to the rotation axis, and that distribution directly controls how the available energy partitions between rotation and translation."
```

## Explainer

You already know kinetic energy for a point mass: KE = ½mv². You know moment of inertia I as the rotational analog of mass — a measure of how hard it is to change rotational motion, reflecting both the amount of mass and how far that mass is distributed from the rotation axis. You know angular velocity ω as the rotational analog of linear velocity v. **Rotational kinetic energy** follows directly from substituting these analogs: KE_rot = ½Iω².

The analogy runs deep and is worth tracing explicitly. In translation, kinetic energy depends on inertia (m) and the square of velocity (v²). In rotation, kinetic energy depends on rotational inertia (I) and the square of angular velocity (ω²). The factor ½ arises for the same mathematical reason in both cases — it comes from integrating the work done to accelerate the object from rest. If you can calculate I for a rigid body about its axis (and you learned standard results: ½MR² for a solid disk, MR² for a hoop, 2/5 MR² for a solid sphere), computing rotational kinetic energy reduces to a straightforward substitution once ω is known.

The real power emerges when an object both rotates and translates simultaneously — like a wheel rolling down a ramp or a ball rolling across a floor. The **total kinetic energy** has two additive terms: translational KE of the center of mass moving through space (½mv_CM²) plus rotational KE about the center of mass (½I_CM ω²). Both terms are funded by the same source of energy — gravitational potential energy when rolling down an incline. This is why a hollow cylinder rolls slower to the bottom of a ramp than a solid sphere of the same mass and radius: the hollow cylinder concentrates its mass at large radius, giving it a larger I, so a greater fraction of the available potential energy is channeled into rotation and less into translational speed.

Energy methods using this framework are extremely efficient. For a rolling object on a frictionless incline, you can write the energy equation at two points: (½mv² + ½Iω² + mgh)_initial = (½mv² + ½Iω² + mgh)_final. The rolling-without-slipping constraint v_CM = Rω links the translational and rotational terms, making the equation solvable for the final speed without ever computing torques or angular accelerations step by step. This single equation replaces what would otherwise require separate translational and rotational Newton's laws and a careful treatment of the static friction force that sustains rolling.
