---
id: torque
title: Torque
domain: physics
course: classical-mechanics
prerequisites:
- id: free-body-diagrams
  type: hard
- id: rotational-kinematics
  type: hard
- id: cross-product
  type: soft
- id: vectors-in-two-dimensions
  type: soft
- id: cross-product-3d
  type: soft
builds-toward:
- rotational-dynamics
- angular-momentum
- moment-of-inertia
tags:
- torque
- rotation
- moment-arm
- lever
stage: abstract-reasoning
status: validated
---

# Torque

## Core Idea
Torque is the rotational analog of force: τ = r × F, with magnitude τ = rF sinθ, where r is the distance from the pivot (moment arm) and θ is the angle between r and F. Torque causes angular acceleration. The moment arm is the perpendicular distance from the pivot to the line of action of the force. A larger moment arm produces more torque for the same force magnitude.

## How It's Best Learned
Practice computing torques for forces applied at various angles to a lever arm. Use the sign convention: counter-clockwise torques are positive, clockwise are negative. Solve static equilibrium problems where Στ = 0 and ΣF = 0 simultaneously.

## Common Misconceptions
- Using r (distance to point of application) instead of the perpendicular moment arm when the force is not perpendicular to r.
- Forgetting that torque depends on the choice of pivot point — always specify the axis of rotation.

## Questions

```yaml
- question: "A 4 N force is applied to a 0.5 m lever arm at an angle of 30° from the lever. What is the torque about the pivot?"
  type: multiple-choice
  options: ["2.0 N·m", "1.0 N·m", "1.73 N·m", "0.5 N·m"]
  answer: 1
  explanation: "τ = rF sinθ = (0.5)(4) sin(30°) = 2 × 0.5 = 1.0 N·m. The sin(30°) = 0.5 factor accounts for the fact that only the component of force perpendicular to the lever arm contributes to rotation."

- question: "The torque produced by a force on an object depends on where you choose the pivot point."
  type: true-false
  answer: true
  explanation: "Torque is always calculated relative to a specific axis of rotation. The same force can produce different torque values depending on which pivot you choose, because the moment arm (perpendicular distance from pivot to the line of action) changes. This is why problems always require you to specify the axis."

- question: "A force is applied exactly along the length of a lever arm (θ = 0°). What torque does it produce, and why?"
  type: short-answer
  answer: "Zero torque, because sin(0°) = 0. A force directed straight through the pivot creates no tendency to rotate the object."
  explanation: "τ = rF sinθ. When the force is parallel to the moment arm, its entire effect is to push along the lever — none of it acts perpendicular to produce rotation. The perpendicular component of the force is what causes angular acceleration, and that component is zero at θ = 0°."
```

## Explainer

You already know from rotational kinematics how to describe rotation — angular velocity, angular acceleration, and so on. But what *causes* angular acceleration? Just as a net force causes linear acceleration (F = ma), a net torque causes angular acceleration. Torque is the rotational analog of force.

The core formula is τ = rF sinθ, where r is the distance from the pivot to the point where the force is applied, F is the force magnitude, and θ is the angle between the force vector and the lever arm. The key quantity is the **moment arm** — the perpendicular distance from the pivot to the *line of action* of the force. If you extend the force vector infinitely in both directions, the moment arm is the shortest distance from the pivot to that line. Mathematically this is just r sinθ, so τ = F × (moment arm).

This geometry explains two important things. First, applying a force perpendicular to the lever (θ = 90°) produces the maximum torque — all of the force contributes to rotation. A force applied along the lever (θ = 0° or 180°) produces zero torque — it just pushes toward or away from the pivot. Second, the farther from the pivot you apply the force, the greater the torque. This is why door handles are placed at the edge of the door, not near the hinges, and why a longer wrench makes it easier to loosen a bolt.

For sign convention, counter-clockwise torques are typically positive and clockwise are negative. In static equilibrium problems (where nothing rotates), you need both ΣF = 0 (no net linear force) and Στ = 0 (no net torque). This second condition is what lets you solve for unknown forces in structures like beams, bridges, and seesaws.

One critical pitfall: torque is always defined relative to a chosen pivot. The same force can produce a large torque about one axis and zero torque about another. In a problem, always state which pivot you're using before computing. Often you can choose the pivot strategically — placing it at the location of an unknown force eliminates that force from the torque equation, simplifying the algebra.
