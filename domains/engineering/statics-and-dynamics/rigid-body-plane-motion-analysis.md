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
status: validated
---

# General Plane Motion of Rigid Bodies

## Core Idea
General plane motion combines translation of the center of mass and rotation about the center of mass. The velocity of any point is v = v_cm + ω × r. Kinetic energy is KE = ½m v_cm² + ½I_cm ω². The equations of motion are ΣF = m a_cm and ΣM_cm = I_cm α, which decouple translation and rotation.

## Questions

```yaml
- question: "A solid disk rolls without slipping down a ramp. Which set of equations fully describes its motion?"
  type: multiple-choice
  options:
    - "ΣF = m·a_cm alone — rolling is a single constraint that eliminates the rotational equation"
    - "ΣF_x = m·a_cx, ΣF_y = m·a_cy, ΣM_cm = I_cm·α, plus the rolling constraint a_cm = α·R"
    - "The rotational equation is unnecessary because rolling motion is fully determined by Newton's second law for translation"
    - "Only ΣM about the contact point is needed, since rolling makes all other equations redundant"
  answer: 1
  explanation: "General plane motion requires three scalar equations (two translational, one rotational), plus any kinematic constraints. For a rolling disk, the no-slip constraint a_cm = α·R connects the translational and rotational variables, turning the system into something solvable. Option C is wrong — without the rotational equation there is no way to find angular acceleration independently. Option D is a valid computational shortcut for some problems but does not replace the full equation set; it works by eliminating friction from the moment equation, not by making other equations 'redundant.'"

- question: "Two objects with equal mass roll from rest down a ramp: a solid cylinder (I_cm = ½mR²) and a hollow cylinder (I_cm = mR²). Which reaches the bottom first?"
  type: multiple-choice
  options:
    - "The solid cylinder, because it has lower rotational inertia so more energy goes to translational motion"
    - "The hollow cylinder, because all its mass is at the rim, giving it greater angular speed"
    - "They tie, because they have the same mass and gravitational force"
    - "The hollow cylinder, because its larger moment of inertia stores more energy efficiently"
  answer: 0
  explanation: "Using energy conservation with the rolling constraint, the translational speed at the bottom satisfies ½v²(m + I_cm/R²) = mgh. The solid cylinder needs ½v²(m + ½m) = ¾mv² to reach height h; the hollow cylinder needs ½v²(m + m) = mv². For the same h, the solid cylinder achieves higher v_cm because a smaller fraction of the available energy goes into rotation. Higher rotational inertia stores more energy in spin, leaving less for forward motion."

- question: "The equation ΣM_cm = I_cm · α applies only when the body's center of mass is not accelerating."
  type: true-false
  answer: false
  explanation: "ΣM_cm = I_cm · α applies universally for rigid body plane motion regardless of whether the CM is accelerating. This is precisely the power of the decomposition: the translational equation ΣF = m·a_cm and the rotational equation ΣM_cm = I_cm·α are independent of each other. The rotational equation depends only on moments about the CM and angular acceleration — the translational state of the CM does not appear in it."

- question: "For a wheel rolling without slipping on a flat surface, the contact point between the wheel and the ground is instantaneously at rest."
  type: true-false
  answer: true
  explanation: "For rolling without slipping, the velocity at the contact point is zero instantaneously. The contact point has the CM's forward velocity v_cm plus the velocity from rotation, which points backward at magnitude ω·R = v_cm. These cancel exactly, giving zero velocity. This is the defining condition of rolling without slipping and is why the contact point serves as the instantaneous center of rotation for a rolling body."

- question: "Why does the decomposition of general plane motion into CM translation plus rotation about the CM make the equations of motion simpler, and what goes wrong if you sum moments about a point other than the CM?"
  type: short-answer
  answer: "Summing moments about the CM decouples the translational and rotational equations. ΣF = m·a_cm depends only on net force and CM acceleration. ΣM_cm = I_cm·α depends only on moments and angular acceleration. If you sum moments about an arbitrary point P instead, you get an extra coupling term: ΣM_P = I_cm·α + r_{P→cm} × m·a_cm. This mixes translational and rotational unknowns and complicates the algebra. The CM is the one reference point where this coupling term vanishes, making the equations independent."
  explanation: "The physics behind this is the decomposition theorem: the total angular momentum about any point decomposes into spin about the CM plus orbital angular momentum of the CM about that point. Only when you choose the CM as reference does the orbital term not introduce extra coupling — because the CM's position relative to itself is zero."
```

## Explainer

You've already analyzed rotation about a fixed axis and the kinematics of general rigid body motion. **General plane motion** is the synthesis: a body that simultaneously translates and rotates, with no axis fixed in space. Think of a wheel rolling down a ramp, a connecting rod in an engine, or a football tumbling through the air. The key insight is that no matter how complicated the motion looks, you can always decompose it into two independent parts: the translation of the center of mass, and the rotation about the center of mass.

This decomposition is what makes the equations of motion so clean. The net external force vector equals m times the acceleration of the center of mass — full stop. It does not matter how the body is rotating; translational dynamics depends only on where the CM is accelerating. Similarly, the net external moment about the center of mass equals I_cm times the angular acceleration α — and this is true regardless of how the CM is translating. The two equations ΣF = m·a_cm and ΣM_cm = I_cm·α are independent of each other. This is why you always sum moments about the center of mass (or about another strategically chosen point) — it uncouples the problem.

The kinetic energy formula KE = ½m·v_cm² + ½I_cm·ω² reflects the same decomposition. The first term is the energy of a point mass moving with the CM; the second is the energy of spinning about the CM. For a rolling wheel, both terms contribute — it has translational KE from its moving center and rotational KE from spinning. For a sliding hockey puck (no rotation), only the first term contributes. Understanding which modes carry energy matters for problems involving collisions, energy conservation, and designing systems that need to absorb or store energy efficiently.

When solving a plane motion problem, the standard approach is: (1) identify all external forces and moments, (2) write ΣF_x = m·a_cx, ΣF_y = m·a_cy for the translational equations, (3) write ΣM_cm = I_cm·α for the rotational equation, and (4) use kinematic constraints — like the rolling constraint v_cm = ω·R for a wheel — to reduce the number of unknowns. The kinematic constraint is often what connects the translational and rotational variables, turning three equations and three unknowns into a solvable system. Getting comfortable with identifying and writing that constraint is the central skill the method requires.
