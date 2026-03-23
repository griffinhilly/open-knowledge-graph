---
id: rolling-without-slipping
title: Rolling Without Slipping
domain: physics
course: classical-mechanics
prerequisites:
- id: rotational-kinematics
  type: hard
- id: circular-motion-kinematics
  type: soft
builds-toward:
- rotational-kinetic-energy
tags:
- rolling
- kinematics
- constraints
stage: formal-systems
status: validated
---

# Rolling Without Slipping

## Core Idea
Rolling without slipping enforces the kinematic constraint v_CM = R ω: the center-of-mass velocity equals radius times angular velocity. This couples translation and rotation, reducing degrees of freedom. In energy analysis, rolling objects combine translational KE (½ m v²) and rotational KE (½ I ω²); the fraction going to each depends on the moment of inertia (e.g., 1/3 rotational for a solid cylinder, 2/5 for a solid sphere).

## Questions

```yaml
- question: "A solid sphere and a hollow spherical shell of equal mass and radius are released from rest at the top of an inclined ramp. Assuming rolling without slipping, which reaches the bottom first?"
  type: multiple-choice
  options:
    - "The hollow shell, because its mass is concentrated at the rim, giving it more rotational momentum"
    - "The solid sphere, because its smaller moment of inertia means less energy goes into rotation and more into translation"
    - "They arrive simultaneously, because they have the same mass and experience the same gravitational force"
    - "The result depends on the ramp angle, not on the shape of the object"
  answer: 1
  explanation: "By energy conservation, both objects convert the same initial potential energy into total kinetic energy (½mv² + ½Iω²). Using the rolling constraint v = Rω, total KE = ½mv²(1 + I/mR²). The object with larger I/mR² puts more energy into rotation and less into translation, arriving with lower v_CM. For a solid sphere, I/mR² = 2/5; for a hollow shell, I/mR² = 2/3. The sphere's smaller rotational fraction means more translational speed — it arrives first. Same mass is irrelevant; the I/mR² ratio is what matters."

- question: "A wheel rolls without slipping on a flat surface. How much work does the static friction force at the contact point do?"
  type: multiple-choice
  options:
    - "Positive work, because friction is what enables rolling and provides energy to the system"
    - "Negative work, because friction always opposes motion"
    - "Zero work, because the contact point has zero instantaneous velocity — the force acts on a point that isn't moving"
    - "Zero work, but only because rolling friction is negligible on flat surfaces"
  answer: 2
  explanation: "Work = force × displacement of the point of application. During rolling without slipping, the contact point has zero instantaneous velocity relative to the ground — it is momentarily stationary, not sliding. Therefore the static friction force acts on a point with zero velocity, doing zero work. This is not an approximation; it is exact for ideal rolling without slipping. However, friction is still essential — it provides the torque that causes angular acceleration. A force can be mechanically necessary without doing work."

- question: "During rolling without slipping, the contact point of the wheel has zero instantaneous velocity relative to the ground."
  type: true-false
  answer: true
  explanation: "This is the physical meaning of 'no slipping' and the foundation of the rolling constraint. The contact point's velocity has two contributions: the translational velocity v_CM (forward) and the tangential rim velocity Rω (backward at the contact point due to rotation). For rolling without slipping, these exactly cancel: v_contact = v_CM − Rω = 0. This is why static, not kinetic, friction acts at the contact point — the surfaces are not sliding relative to each other."

- question: "If a round object is placed on a frictionless surface, it will still roll without slipping because its shape ensures the contact point stays stationary."
  type: true-false
  answer: false
  explanation: "Friction is essential for rolling without slipping — it is the torque-generating mechanism that couples translational and rotational motion. On a frictionless surface, a force applied to a round object's center accelerates it translationally but does not create a torque, so rotation lags behind. The object slides rather than rolls, and the rolling constraint v_CM = Rω is violated. Without friction, there is no mechanism to enforce the coupling between translation and rotation."

- question: "Derive the rolling constraint v_CM = Rω by explaining what physical condition at the contact point it expresses."
  type: short-answer
  answer: "The condition is zero relative velocity at the contact point. The contact point's velocity has two contributions: the translational velocity v_CM of the wheel's center (forward), and the tangential velocity Rω due to rotation (backward at the bottom of the wheel). For no slipping, these must cancel exactly: v_CM − Rω = 0, which gives v_CM = Rω. This single equation couples the two degrees of freedom (translation and rotation) into one, so knowing either v_CM or ω immediately determines the other."
  explanation: "Understanding why the constraint takes this form — rather than just memorizing the equation — makes it straightforward to handle inclined planes, curved surfaces, and other rolling geometries. The contact-point velocity condition is the physical fact; v_CM = Rω is just that fact expressed mathematically."
```

## Explainer

From rotational kinematics, you know that rotating objects have angular velocity ω (how fast they spin) and that points on a rotating body have tangential speeds that depend on their distance from the axis. Rolling without slipping takes this further by linking rotation and translation: when a wheel rolls on a surface without slipping, every point on the rim has zero velocity *relative to the ground* at the instant it contacts the surface. This is the physical meaning of "no slipping" — the contact point is momentarily stationary.

From that contact condition, the **rolling constraint** v_CM = Rω follows directly. The center of the wheel moves forward at speed v_CM. The contact point's velocity has two contributions: the translational velocity of the whole wheel (v_CM, forward) and the tangential velocity of the rim due to rotation (Rω, backward at the contact point). For zero slip, these must cancel: v_CM = Rω. This single equation couples the two degrees of freedom (translation and rotation) into one. Once you know v_CM, you know ω, and vice versa.

This constraint transforms energy problems. A sliding block on a frictionless surface converts all potential energy to translational KE: ½mv². A rolling object splits energy between translation and rotation. The total kinetic energy is ½mv² + ½Iω². Using v = Rω to eliminate ω gives KE = ½mv²(1 + I/mR²). The factor (1 + I/mR²) tells you the penalty for being a rolling object: a hoop (I = mR²) has twice the KE of a sliding point mass at the same speed, because half its energy is rotational. A solid sphere (I = 2mR²/5) has a factor of 7/5. This is why a solid sphere rolls down a ramp faster than a hollow shell of the same mass and radius — the shell must put more energy into rotation.

A common point of confusion: the static friction force at the contact point does no work during rolling without slipping (because the contact point has zero instantaneous velocity), but it is still essential — it is what creates the torque that accelerates the rotation. Remove friction (ice, for example) and the wheel can spin without rolling, or slide without spinning, because the constraint is broken. This is why rolling problems always specify whether the surface is rough enough to maintain rolling without slipping, and why that condition determines whether you can use v = Rω to link translational and rotational quantities.
