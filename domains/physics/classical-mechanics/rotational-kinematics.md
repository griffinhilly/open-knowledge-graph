---
id: rotational-kinematics
title: Rotational Kinematics
domain: physics
course: classical-mechanics
prerequisites:
- id: kinematics-1d
  type: hard
- id: circular-motion-kinematics
  type: soft
- id: derivative-as-slope-of-tangent
  type: soft
- id: trigonometric-ratios-review
  type: soft
- id: converting-degrees-and-radians
  type: hard
- id: trigonometric-functions-and-graphs
  type: soft
builds-toward:
- torque
- rotational-dynamics
- angular-momentum
tags:
- rotational-kinematics
- angular-velocity
- angular-acceleration
- rotation
stage: formal-systems
status: validated
---

# Rotational Kinematics

## Core Idea
Rotational kinematics describes angular motion using angular displacement θ, angular velocity ω = dθ/dt, and angular acceleration α = dω/dt. These exactly parallel linear kinematics: θ ↔ x, ω ↔ v, α ↔ a. For constant angular acceleration, the same four kinematic equations apply with angular substitutions. Linear and angular quantities are related by arc-length relations: s = rθ, v = rω, a_t = rα.

## How It's Best Learned
Solve rotational kinematics problems by direct analogy to linear problems. Always verify which quantities are given as angular vs. linear and convert using r before applying equations.

## Common Misconceptions
- Confusing angular velocity ω (rad/s) with tangential speed v (m/s): a point on the rim and a point halfway from the center have the same ω but different v.
- Forgetting that the constant-acceleration kinematic equations apply only when α is constant.

## Questions

```yaml
- question: "A disk is rotating at constant angular velocity. Point A is on the rim; Point B is halfway between the center and the rim. Which statement is true?"
  type: multiple-choice
  options: ["A and B have the same tangential speed", "A and B have the same angular velocity", "A has a smaller angular velocity than B", "B has a greater tangential speed than A"]
  answer: 1
  explanation: "Angular velocity ω describes how fast the angle is changing — every point on a rigid rotating body sweeps through the same angle per second, so ω is the same for all points. Tangential speed, however, depends on radius: v = rω, so point A on the rim (larger r) moves faster through space than point B closer to the center."

- question: "The kinematic equation ω = ω₀ + αt can be applied to any spinning object as long as you know its initial angular velocity."
  type: true-false
  answer: false
  explanation: "This equation — and all four constant-acceleration kinematic equations — require that the angular acceleration α is constant throughout the motion. If α varies (for example, as torque changes), these equations give incorrect results. This is the direct rotational analogue of the linear restriction: v = v₀ + at only holds when acceleration is constant."

- question: "A point on the rim of a wheel of radius r is moving at tangential speed v. What is the wheel's angular velocity ω, and what are its units?"
  type: short-answer
  answer: "ω = v/r, in radians per second (rad/s)"
  explanation: "The arc-length relationship v = rω can be rearranged to ω = v/r. Angular velocity is measured in rad/s because radians are dimensionless (arc length divided by radius), leaving units of inverse seconds. This relationship is the bridge between the rotational and linear descriptions of the same physical motion."
```

## Explainer

Rotational kinematics is not a new topic — it is linear kinematics rewritten for spinning objects. Every quantity you already know has a rotational counterpart: displacement x becomes angular displacement θ (in radians), velocity v becomes angular velocity ω (rad/s), and acceleration a becomes angular acceleration α (rad/s²). The four kinematic equations you used for straight-line motion work identically for rotation, just with these swapped symbols. If you can solve a linear kinematics problem, you can solve a rotational one by analogy.

The reason radians matter here is that they make the connection between linear and rotational quantities clean. The arc length traveled by a point at radius r after an angular displacement θ is simply s = rθ — no conversion factor needed. Differentiate both sides and you get v = rω; differentiate again and you get the tangential acceleration a_t = rα. These three equations are your bridge: if you know the angular quantities and the radius, you can always find the corresponding linear quantities for any point on the rotating object.

The most common confusion is between angular velocity and tangential speed. When a rigid disk spins, every point rotates through the same angle in the same time — so every point shares the same ω. But a point on the rim traces a much larger circle than a point near the center, so it must be moving faster through space. Its tangential speed v = rω is larger because r is larger. Think of two ants on a spinning record: the one on the outer edge covers far more distance per revolution than the one near the label, even though they complete each revolution in the same time.

Finally, remember that the constant-α kinematic equations apply only when angular acceleration is uniform, just as the linear equations require constant a. Many introductory problems assume constant α (a motor spinning up uniformly, a wheel decelerating due to constant friction), and in those cases the analogy is perfect. When you move on to torque and rotational dynamics, you will learn what causes angular acceleration — the rotational analogue of Newton's second law — which will make the full picture clear.
