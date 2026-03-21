---
id: rotation-fixed-axis-dynamics
title: 'Rotation about a Fixed Axis: Kinematics and Kinetics'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: kinematics-rigid-body-rotation
  type: hard
- id: moment-of-inertia-about-centroid
  type: hard
builds-toward:
- rigid-body-plane-motion-analysis
tags:
- fixed-axis
- rotation
- angular-acceleration
- torque
stage: formal-systems
status: draft
---

# Rotation about a Fixed Axis: Kinematics and Kinetics

## Core Idea
For a rigid body rotating about a fixed axis, angular kinematics parallels linear kinematics: ω = dθ/dt, α = dω/dt. The kinetic equation is ΣM = I α, where M is the net torque and I is the moment of inertia about the axis. Kinetic energy is KE = ½I ω². These equations fully describe the rotational motion of wheels, rotors, and other rotating machinery.

## Questions

```yaml
- question: "A solid disk (moment of inertia I) and a thin ring (moment of inertia 2I, same outer radius) are each subjected to the same constant net torque M about their central axis. What is the ratio of their angular accelerations (disk : ring)?"
  type: multiple-choice
  options:
    - "1:1 — same torque means same angular acceleration by Newton's second law"
    - "2:1 — the disk has half the moment of inertia, so ΣM = Iα gives twice the acceleration"
    - "1:2 — the ring has more mass near the rim, giving it a mechanical advantage"
    - "Cannot be determined without knowing the mass"
  answer: 1
  explanation: "From ΣM = Iα, angular acceleration is α = ΣM / I. Same torque M applied to I gives α_disk = M/I; applied to 2I gives α_ring = M/(2I). Ratio = 2:1. The analogy is exact: doubling mass halves linear acceleration for the same force; doubling moment of inertia halves angular acceleration for the same torque. Option A is the common misconception — students forget that I, not mass alone, determines rotational response."

- question: "A wheel (moment of inertia I) starts from rest and reaches angular velocity ω after rotating through angle θ under a constant net torque M. Using the work-energy method, which expression gives I?"
  type: multiple-choice
  options:
    - "I = Mθ / ω"
    - "I = 2Mθ / ω²"
    - "I = Mω / (2θ)"
    - "I = Mθω²"
  answer: 1
  explanation: "Work done by a constant torque through angle θ is W = Mθ. By the work-energy theorem, W = ΔKE = ½Iω² − 0. Setting Mθ = ½Iω² and solving: I = 2Mθ/ω². This mirrors the linear case: ½mv² = Fd → m = 2Fd/v². The work-energy approach avoids integrating the equation of motion and is often faster when the question asks for speed at a given angle rather than acceleration at an instant."

- question: "For a rigid body rotating about a fixed axis, the kinetic energy is ½mv², where v is the speed of the body's center of mass."
  type: true-false
  answer: false
  explanation: "For pure rotation about a fixed axis, the kinetic energy is ½Iω², where I is the mass moment of inertia about that axis. The formula ½mv² applies to translational motion of a point mass. A rotating body's kinetic energy depends on how its mass is distributed (captured by I) and its angular velocity ω, not on the linear speed of a single point. Using ½mv_cm² instead of ½Iω² would give the wrong answer for any mass distribution other than a particle."

- question: "The equation ΣM = Iα for fixed-axis rotation is valid only when the axis of rotation does not translate."
  type: true-false
  answer: true
  explanation: "ΣM = Iα applies when the axis is truly fixed in space — like a wheel on an axle. When the axis itself accelerates (a rolling wheel on a moving surface, a swinging pendulum with a moving pivot), you are in general plane motion, which requires both a translational equation (ΣF = ma_cm) and a rotational equation (ΣM_cm = I_cm·α). Using ΣM = Iα for a non-fixed axis is a common error that gives incorrect results."

- question: "Describe the rotational analogue of Newton's second law for fixed-axis rotation: what quantity plays the role of force, mass, and acceleration, and why does a larger moment of inertia mean a slower rotational response to the same torque?"
  type: short-answer
  answer: "Net torque ΣM plays the role of force, moment of inertia I plays the role of mass, and angular acceleration α plays the role of linear acceleration. The governing equation is ΣM = Iα (compare to ΣF = ma). A larger I means mass is distributed farther from the axis; that mass resists rotational acceleration more because accelerating it requires more force at a greater radius. Same torque on larger I yields smaller α, just as same force on larger mass yields smaller linear acceleration."
  explanation: "Moment of inertia is not just mass — it is a measure of how far from the axis that mass sits. A hollow cylinder and a solid cylinder of equal mass have different moments of inertia because the hollow one has all its mass at the maximum radius, giving it the maximum possible rotational inertia. This is why figure skaters pull in their arms to spin faster — redistributing mass closer to the rotation axis reduces I, and since angular momentum Iω is conserved, ω must increase."
```

## Explainer

From rigid-body kinematics you know how to describe the geometry of rotation: angular position θ, velocity ω = dθ/dt, and acceleration α = dω/dt are related by the same calculus as linear position, velocity, and acceleration. From moment of inertia, you know how mass distributed around an axis resists rotational acceleration. Fixed-axis dynamics brings these threads together: it answers the question of *what causes* the angular acceleration you've been describing kinematically.

The governing equation is ΣM = Iα, where ΣM is the net moment (torque) of all forces about the fixed axis, I is the mass moment of inertia about that axis, and α is the resulting angular acceleration. This is the rotational form of Newton's second law, with moment replacing force, moment of inertia replacing mass, and angular acceleration replacing linear acceleration. The analogy is exact: doubling the torque doubles the acceleration, and doubling the moment of inertia halves it. A heavy flywheel (large I) resists changes in rotation; a lightweight spool (small I) responds quickly to applied torques.

The kinetic energy of a rotating rigid body is KE = ½Iω², perfectly mirroring the translational ½mv². This means you can apply energy methods — work-energy theorem — to rotational problems directly. The net work done by all torques equals the change in ½Iω². For a wheel accelerating from rest under a constant applied torque M, the kinetic energy after rotating through angle θ is simply W = Mθ, and you can solve for the final ω without integrating the equation of motion. This work-energy approach is often faster than the ΣM = Iα approach when the question asks about speed at a given position rather than acceleration at a given instant.

To solve fixed-axis dynamics problems, the standard procedure is: (1) identify the fixed axis and compute I about it using the parallel-axis theorem if needed; (2) draw a free-body diagram and identify all forces and their moment arms about the fixed axis; (3) compute ΣM and divide by I to find α; (4) integrate kinematically if time or angle information is needed. For problems involving a rope unwinding from a pulley, or a disk rolling without slip on a fixed axle, this procedure gives the complete solution. The key constraint is that the axis truly does not translate — when it does, you're in the more complex territory of general plane motion, where both translation and rotation must be tracked simultaneously.
