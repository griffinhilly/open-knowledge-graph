---
id: rigid-body-planar-motion
title: 'Rigid Body Planar Motion: Translation and Rotation'
domain: physics
course: classical-mechanics
prerequisites:
- id: center-of-mass-motion
  type: hard
- id: torque-angular-acceleration
  type: hard
- id: work-power-rotation
  type: soft
builds-toward:
- rolling-motion-equations
tags:
- rigid-body
- motion
- translation-rotation
stage: formal-systems
status: draft
---

# Rigid Body Planar Motion: Translation and Rotation

## Core Idea
A rigid body in 2D undergoes both translational and rotational motion. Its motion can be analyzed as motion of the center of mass plus rotation about the center of mass: total KE = ½Mv_cm² + ½Iω².

## Questions

```yaml
- question: "A solid disk and a hoop of equal mass M and equal radius R are released from rest at the top of an inclined plane. Which reaches the bottom first?"
  type: multiple-choice
  options:
    - "The hoop, because its mass concentrated at the rim gives it greater rotational momentum"
    - "The disk, because its smaller moment of inertia means less energy goes into rotation and more into translational speed"
    - "They arrive at the same time, because they have identical mass and radius"
    - "The disk, because static friction acts more strongly on the hoop"
  answer: 1
  explanation: "Both start with the same potential energy Mgh, which must be split between translational KE (½Mv_cm²) and rotational KE (½Iω²). The disk (I = MR²/2) has a smaller moment of inertia than the hoop (I = MR²), so less energy goes into rotation and more into translation — the disk arrives faster. Equal mass and radius do not imply equal speed; the distribution of mass (captured by I) is what determines how energy is partitioned."

- question: "A rigid body rolls without slipping down an incline from height h. How does its final translational speed compare to a point mass sliding frictionlessly down the same incline?"
  type: multiple-choice
  options:
    - "Equal to √(2gh) — rolling objects reach the same speed as sliding point masses"
    - "Less than √(2gh) — energy is split between translation and rotation, leaving less for translational speed"
    - "Greater than √(2gh) — rotation adds kinetic energy to the system"
    - "The comparison depends on the object's shape but not its mass"
  answer: 1
  explanation: "A frictionlessly sliding point mass converts all potential energy to translational KE: ½Mv² = Mgh, giving v = √(2gh). A rolling rigid body must also supply rotational KE (½Iω²), so less energy is available for translation. With v_cm = Rω, both kinetic energy terms depend on v_cm, and conservation of energy gives v_cm = √(2gh / (1 + I/MR²)) < √(2gh). The shape (via I/MR²) determines exactly how much slower it is."

- question: "For a rigid body in planar motion, the translational equation ΣF = Ma_cm and the rotational equation Στ_cm = I_cm α are fully independent — a single applied force can contribute to at most one of these equations."
  type: true-false
  answer: false
  explanation: "This is a key misconception. The same force can simultaneously contribute to both equations. Friction on a rolling body, for example, appears in ΣF = Ma_cm as a translational force and in Στ_cm = I_cm α as a torque (since it acts at the contact point, at distance R from the center of mass). The equations are independent in structure but not in the forces they share — this coupling is what makes rigid body problems solvable."

- question: "The rolling-without-slipping constraint v_cm = Rω links translational and rotational motion, reducing the number of independent variables needed to describe the motion."
  type: true-false
  answer: true
  explanation: "Without rolling-without-slipping, a rigid body has two independent degrees of freedom: translational (described by v_cm) and rotational (described by ω). The geometric constraint v_cm = Rω ties these together, reducing to one independent variable. This means you need one fewer equation to solve the problem. When slipping occurs, the constraint breaks, and you must treat both equations fully independently, using kinetic friction as the link between the translational and rotational dynamics."

- question: "Explain the decomposition theorem for planar rigid body motion and why it means you need two separate equations (not one) to fully describe the motion."
  type: short-answer
  answer: "Any planar rigid body motion can be decomposed exactly into (1) translation of the center of mass, governed by ΣF = Ma_cm, and (2) rotation about the center of mass, governed by Στ_cm = I_cm α. These are two separate physical processes that happen simultaneously — the same forces appear in both equations but describe different aspects of the motion. One equation cannot capture both: Newton's second law for a point mass describes translation, but says nothing about how the body spins."
  explanation: "The decomposition is what makes rigid body analysis tractable. Rather than tracking every particle in the body, you track two quantities: where the center of mass goes (translation) and how the body rotates about it. The kinetic energy formula KE = ½Mv_cm² + ½I_cm ω² reflects this same decomposition — two additive terms, one for each mode of motion."
```

## Explainer

From center-of-mass motion, you know that a system of particles can be treated as a point mass M located at the center of mass, with its motion governed by the net external force: F_net = Ma_cm. From torque and angular acceleration, you know that rotational motion obeys τ = Iα, where τ is the net torque about an axis, I is the moment of inertia about that axis, and α is the angular acceleration. Rigid body planar motion combines both of these results into a unified description.

The central insight is the **decomposition theorem**: any planar motion of a rigid body can be exactly decomposed into (1) translation of the center of mass, and (2) rotation about the center of mass. These two components are independent in the equations of motion but both contribute to the total kinetic energy. This means that when you analyze a rolling disk, a falling rod, or a sliding-and-spinning puck on a frictionless surface, you need two separate equations: ΣF = Ma_cm for the translational part, and Στ_cm = I_cm · α for the rotational part about the center of mass. The forces and torques are not independent — the same force (say, friction) can contribute to both equations — but the equations themselves capture different aspects of the motion.

The **kinetic energy** formula KE = ½Mv_cm² + ½I_cm ω² reflects this decomposition directly. The first term is the translational kinetic energy of the whole mass moving at the center-of-mass speed; the second is the rotational kinetic energy of the body spinning about its own center of mass. This is useful for energy methods: if a rigid body rolls down an incline, you can use energy conservation, but you must account for both terms. A hoop and a disk of equal mass and radius released from the same height will not reach the bottom at the same speed — the hoop has a larger moment of inertia (more mass at the rim), so more energy goes into rotation and less into translation.

The constraint that connects these two terms in rolling-without-slipping is v_cm = Rω. This geometric condition ties the translational and rotational speeds together, reducing the degrees of freedom by one and making the system solvable with fewer equations. When slipping occurs, the constraint breaks and you must treat translational and rotational motion fully separately, using kinetic friction to link the force equation to the torque equation. Recognizing whether rolling-without-slipping holds — by checking whether static friction is within its maximum value — is the key judgment call in planar rigid body problems.
