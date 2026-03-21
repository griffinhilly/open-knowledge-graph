---
id: rotational-dynamics
title: 'Rotational Dynamics: Newton''s Second Law for Rotation'
domain: physics
course: classical-mechanics
prerequisites:
- id: torque
  type: hard
- id: moment-of-inertia
  type: hard
- id: rotational-kinematics
  type: hard
- id: center-of-mass
  type: soft
- id: circular-motion-dynamics
  type: soft
- id: static-equilibrium
  type: soft
- id: cross-product
  type: hard
- id: converting-degrees-and-radians
  type: soft
builds-toward:
- angular-momentum
- conservation-of-angular-momentum
tags:
- rotational-dynamics
- torque
- moment-of-inertia
- angular-acceleration
stage: formal-systems
status: validated
---
# Rotational Dynamics: Newton's Second Law for Rotation

## Core Idea
The rotational analog of Newton's second law is Στ = Iα: the net torque on a rigid body about a fixed axis equals its moment of inertia times its angular acceleration. This equation governs all rotational dynamics, from spinning tops to rolling cylinders. For rolling-without-slipping problems, linear and rotational equations couple through the constraint a = αr.

## How It's Best Learned
Draw a free-body diagram, compute all torques about the rotation axis, set Στ = Iα. For rolling objects, write both ΣF = ma (linear) and Στ = Iα (rotational) and connect them via the no-slip condition a = αr.

## Common Misconceptions
- Applying rotational dynamics without computing torques — net torque, not net force, drives angular acceleration.
- Using the wrong axis for computing I and τ — they must be computed about the same axis.

## Questions

```yaml
- question: "A solid cylinder and a hollow cylinder of the same mass and radius are released from rest at the top of an identical ramp. Which reaches the bottom first?"
  type: multiple-choice
  options:
    - "The hollow cylinder, because it has more mass concentrated at the rim, generating more torque"
    - "The solid cylinder, because its moment of inertia is smaller (I = ½mr²), so less of its energy is locked in rotation"
    - "They tie — both experience the same gravitational force and normal force"
    - "The hollow cylinder, because the angular velocity is higher when all mass is at the edge"
  answer: 1
  explanation: "For a rolling object, total energy is split between translational (½mv²) and rotational (½Iω²) kinetic energy. The hollow cylinder has I = mr², the solid cylinder has I = ½mr². Using the no-slip constraint v = ωr and energy conservation, the solid cylinder reaches the bottom faster because a smaller fraction of its energy is tied up in rotation — more is available for translational speed. The gravitational force is the same for both, but I determines how the energy is distributed between the two motion types."

- question: "A mechanic applies force F to a wrench in a direction pointing directly toward the bolt (i.e., the force vector points straight at the rotation axis). What torque does this force produce?"
  type: multiple-choice
  options:
    - "Torque = Fr, where r is the length of the wrench"
    - "Torque = Fr sin(0°) = 0 — a force aimed at the axis produces no torque"
    - "Torque = F/r, since the lever arm is inverted when the force aims inward"
    - "Torque = Fr cos(0°) = Fr — the full force contributes because the angle is zero"
  answer: 1
  explanation: "Torque is τ = r × F with magnitude τ = rF sin θ, where θ is the angle between the position vector r and the force F. When the force is aimed directly at the rotation axis, θ = 0°, so sin(0°) = 0 and the torque is zero. Intuitively, this force has no 'twisting' component — it pushes along the wrench rather than perpendicular to it. Maximum torque occurs when the force is perpendicular to the lever arm (θ = 90°), which is why you push perpendicular to a wrench handle."

- question: "When applying Στ = Iα to a rotating rigid body, the moment of inertia I and all torques τ must be computed about the same axis."
  type: true-false
  answer: true
  explanation: "This is a fundamental consistency requirement. Both I (the distribution of mass relative to an axis) and τ (the rotational effect of each force) are axis-dependent quantities. If you compute I about the center of mass but compute a torque about a different point, the equation Στ = Iα becomes invalid. This is one of the most common errors in rotational dynamics problems — it's the rotational analog of mixing coordinate systems in linear mechanics."

- question: "Applying a larger net force to a rigid body always produces a larger angular acceleration."
  type: true-false
  answer: false
  explanation: "Angular acceleration is governed by Στ = Iα — it depends on net TORQUE, not net force. A large force applied very close to or directly through the rotation axis produces little or no torque and thus little or no angular acceleration. A smaller force applied farther from the axis can produce a much larger torque. Additionally, I (moment of inertia) matters: the same torque produces a larger angular acceleration in a body with smaller I. The correct relationship is α = Στ/I, not α = ΣF/I."

- question: "Why does a hollow cylinder roll more slowly down a ramp than a solid cylinder of the same mass and radius, even though gravity exerts the same force on both?"
  type: short-answer
  answer: "Both cylinders have the same gravitational potential energy at the top of the ramp, but they distribute that energy differently between translational and rotational motion when rolling. The hollow cylinder (I = mr²) has a larger moment of inertia than the solid cylinder (I = ½mr²) because all of its mass is at the rim, far from the axis. By the no-slip constraint a = αr, more rotational inertia means more energy must go into spinning before any additional translational speed is gained. So the hollow cylinder reaches the bottom with the same total energy, but more of it is rotational — meaning less translational speed and a slower descent."
  explanation: "This problem illustrates a key feature of Στ = Iα: the same torque produces less angular acceleration when I is large. Since friction provides the torque that angularly accelerates the rolling cylinder, a larger I means friction must 'fight harder' to spin up the mass. The coupling constraint a = αr then limits the translational acceleration. The solid cylinder's mass is distributed closer to the axis (lower I), making it easier to spin and thus able to translate faster for the same energy input."
```

## Explainer

Newton's second law for linear motion is the central equation of classical mechanics: the net force on an object equals its mass times its linear acceleration (ΣF = ma). You've now built all the ingredients to write the exact rotational analog. Your study of torque established that torque is the rotational cause of angular acceleration — it's the "twisting force" that depends on both the force applied and how far from the axis it acts. Your study of moment of inertia established that I is the rotational analog of mass — it measures how a body's mass is distributed relative to the rotation axis, and therefore how resistant the body is to changes in its rotational motion. Put these together: **Στ = Iα**. Net torque drives angular acceleration, with moment of inertia as the proportionality constant.

The analogy table is worth internalizing explicitly: force F ↔ torque τ; mass m ↔ moment of inertia I; linear acceleration a ↔ angular acceleration α; linear momentum p = mv ↔ angular momentum L = Iω. Every theorem you know about linear dynamics has a rotational counterpart with this substitution. The equation Στ = Iα is not a new law — it is the rotational expression of the same underlying physics as F = ma. This is why your work on rotational kinematics (relating θ, ω, α) maps exactly onto the kinematic equations for linear motion.

The **cross product** (from your prerequisites) reveals why torque is a vector. Torque τ = r × F depends not just on the magnitudes of the position vector r and the force F, but on the angle between them: τ = rF sin θ. A force applied directly toward or away from the rotation axis (θ = 0° or 180°) produces zero torque — it cannot cause rotation. A force applied perpendicular to r (θ = 90°) produces maximum torque. The direction of τ = r × F, given by the right-hand rule, tells you which axis the torque rotates around and in which sense. For 2D problems — a disk spinning in a plane, a door opening — you only need the magnitude, but the vector nature of torque is essential for 3D problems like gyroscopes and precession.

**Rolling without slipping** is the signature problem that combines linear and rotational dynamics. When a cylinder rolls down a ramp, friction at the contact point produces a torque that angularly accelerates the cylinder as it linearly accelerates down the slope. Write two equations: ΣF = ma (net linear force = mass × linear acceleration) and Στ = Iα (net torque about the center = moment of inertia × angular acceleration). The no-slip constraint connects them: a = αr, meaning the linear acceleration of the center equals the angular acceleration times the radius. Together, these three relationships uniquely determine both a and α. The fraction of total kinetic energy stored in rotation depends on I — which depends on how mass is distributed. A hollow cylinder (all mass at radius r, so I = mr²) stores more energy in rotation than a solid cylinder (I = ½mr²), which is why the solid cylinder reaches the bottom of a ramp faster: less of its energy is "tied up" in spinning.
