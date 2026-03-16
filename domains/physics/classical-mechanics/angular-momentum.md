---
id: angular-momentum
title: Angular Momentum
domain: physics
course: classical-mechanics
prerequisites:
- id: rotational-dynamics
  type: hard
- id: momentum-and-impulse
  type: soft
- id: cross-product
  type: soft
- id: cross-product-3d
  type: soft
builds-toward:
- conservation-of-angular-momentum
tags:
- angular-momentum
- rotation
- spin
stage: formal-systems
status: validated
---

# Angular Momentum

## Core Idea
Angular momentum is the rotational analog of linear momentum. For a rigid body rotating about a fixed axis, L = Iω. For a point mass, L = r × p = mvr sinθ. The net torque equals the rate of change of angular momentum: Στ = dL/dt, exactly as F = dp/dt. Angular momentum is a vector (direction from right-hand rule) and is measured in kg·m²/s.

## How It's Best Learned
Connect L = Iω to ordinary momentum: if you double ω (spin faster), L doubles just as p doubles when v doubles. Practice computing L for point masses moving in curves and for spinning rigid bodies.

## Common Misconceptions
- Thinking angular momentum only applies to spinning objects: any object moving in a curved path (or even in a straight line offset from the origin) has angular momentum relative to some axis.
- Forgetting the direction of L: it is along the axis of rotation (perpendicular to the plane of rotation).

## Questions

```yaml
- question: "A figure skater spinning with arms outstretched pulls her arms in tightly. Assuming no external torque acts, what happens to her angular speed?"
  type: multiple-choice
  options:
    - "It decreases, because she has less rotational inertia."
    - "It stays the same, because no external torque acts."
    - "It increases, because angular momentum is conserved and her moment of inertia decreases."
    - "It increases, because pulling her arms in applies an internal torque."
  answer: 2
  explanation: "With no external torque, angular momentum L = Iω is conserved. Pulling arms inward reduces moment of inertia I. Since L = Iω must stay constant, ω must increase. This is why skaters spin faster when they pull in — not because of any external force, but because L is fixed and I shrinks."

- question: "A hockey puck sliding in a straight line across frictionless ice has zero angular momentum with respect to any reference point you choose."
  type: true-false
  answer: false
  explanation: "Angular momentum L = r × p depends on the reference point chosen. For a puck with momentum p moving in a straight line, if you choose a reference point that is NOT on the line of motion, then r has a nonzero perpendicular component, giving L = mvr⊥ ≠ 0. Only if the reference point lies exactly on the line of motion is L zero. This illustrates that angular momentum is not exclusive to spinning or curved-path motion."

- question: "In what sense is angular momentum the rotational analog of linear momentum? Identify one equation that makes this analogy precise."
  type: short-answer
  answer: "Just as F = dp/dt relates net force to the rate of change of linear momentum, the equation Στ = dL/dt relates net torque to the rate of change of angular momentum. L = Iω parallels p = mv, with moment of inertia I playing the role of mass and angular velocity ω playing the role of linear velocity."
  explanation: "The analogy runs deep: mass ↔ moment of inertia, velocity ↔ angular velocity, force ↔ torque, linear momentum ↔ angular momentum. Every theorem about linear momentum has a rotational counterpart. Recognizing this parallel dramatically reduces what you need to memorize — you can derive rotational results from linear ones by substitution."
```

## Explainer

Angular momentum is the rotational world's answer to linear momentum. You already know that a moving object has momentum p = mv, and that forces change momentum via F = dp/dt. The rotational picture is completely parallel: a rotating object has angular momentum L = Iω, and torques change angular momentum via Στ = dL/dt. Once you see this analogy, angular momentum stops being a new concept and becomes a familiar one wearing different clothes.

For a rigid body spinning about a fixed axis, L = Iω is all you need. The moment of inertia I is the rotational analog of mass — it measures how hard it is to change rotational motion, and it depends not just on how much mass an object has but on where that mass is relative to the axis. A hollow cylinder and a solid cylinder of equal mass and radius have different moments of inertia because the hollow one has all its mass at maximum distance from the axis. For a point mass moving along any curved (or even straight) path, L = r × p = mvr sinθ, where r is the position vector from the reference point to the mass and θ is the angle between r and p. This cross-product definition is more general and covers the surprising case where even straight-line motion can carry angular momentum.

The direction of L is where many students get tripped up. L is a vector, and it points along the axis of rotation — perpendicular to the plane in which the rotation happens — with its sense given by the right-hand rule: curl the fingers of your right hand in the direction of rotation and your thumb points along L. This means that for a wheel spinning counterclockwise when viewed from the front, L points toward you. Changing L's direction (not just its magnitude) requires a torque, which is why gyroscopes resist being tipped — changing their orientation means changing the direction of L, and that requires sustained torque.

The practical power of angular momentum shows up most clearly in problems where external torque is absent. If Στ = 0, then dL/dt = 0, so L is conserved. The figure skater pulling in her arms is the classic case: no external torque acts (ice friction is negligible at the blade), so Iω stays constant. As I decreases (arms closer to axis), ω must increase. This is not a special fact about skaters — it is a consequence of Στ = dL/dt applied to an isolated system, the same equation you use for torques in general.

Connect this back to torque (Στ = Iα) and rotational dynamics: angular momentum gives you the conserved quantity that torque changes, exactly as linear momentum is the conserved quantity that force changes. Whenever you set up a rotational problem, ask first whether any external torque acts. If not, conservation of angular momentum is your most powerful tool.
