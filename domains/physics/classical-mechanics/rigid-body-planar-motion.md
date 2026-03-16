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

## Explainer

From center-of-mass motion, you know that a system of particles can be treated as a point mass M located at the center of mass, with its motion governed by the net external force: F_net = Ma_cm. From torque and angular acceleration, you know that rotational motion obeys τ = Iα, where τ is the net torque about an axis, I is the moment of inertia about that axis, and α is the angular acceleration. Rigid body planar motion combines both of these results into a unified description.

The central insight is the **decomposition theorem**: any planar motion of a rigid body can be exactly decomposed into (1) translation of the center of mass, and (2) rotation about the center of mass. These two components are independent in the equations of motion but both contribute to the total kinetic energy. This means that when you analyze a rolling disk, a falling rod, or a sliding-and-spinning puck on a frictionless surface, you need two separate equations: ΣF = Ma_cm for the translational part, and Στ_cm = I_cm · α for the rotational part about the center of mass. The forces and torques are not independent — the same force (say, friction) can contribute to both equations — but the equations themselves capture different aspects of the motion.

The **kinetic energy** formula KE = ½Mv_cm² + ½I_cm ω² reflects this decomposition directly. The first term is the translational kinetic energy of the whole mass moving at the center-of-mass speed; the second is the rotational kinetic energy of the body spinning about its own center of mass. This is useful for energy methods: if a rigid body rolls down an incline, you can use energy conservation, but you must account for both terms. A hoop and a disk of equal mass and radius released from the same height will not reach the bottom at the same speed — the hoop has a larger moment of inertia (more mass at the rim), so more energy goes into rotation and less into translation.

The constraint that connects these two terms in rolling-without-slipping is v_cm = Rω. This geometric condition ties the translational and rotational speeds together, reducing the degrees of freedom by one and making the system solvable with fewer equations. When slipping occurs, the constraint breaks and you must treat translational and rotational motion fully separately, using kinetic friction to link the force equation to the torque equation. Recognizing whether rolling-without-slipping holds — by checking whether static friction is within its maximum value — is the key judgment call in planar rigid body problems.
