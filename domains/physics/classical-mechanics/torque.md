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
builds-toward:
- rotational-dynamics
- angular-momentum
- moment-of-inertia
tags:
- torque
- rotation
- moment-arm
- lever
stage: formal-systems
status: draft
---

# Torque

## Core Idea
Torque is the rotational analog of force: τ = r × F, with magnitude τ = rF sinθ, where r is the distance from the pivot (moment arm) and θ is the angle between r and F. Torque causes angular acceleration. The moment arm is the perpendicular distance from the pivot to the line of action of the force. A larger moment arm produces more torque for the same force magnitude.

## How It's Best Learned
Practice computing torques for forces applied at various angles to a lever arm. Use the sign convention: counter-clockwise torques are positive, clockwise are negative. Solve static equilibrium problems where Στ = 0 and ΣF = 0 simultaneously.

## Common Misconceptions
- Using r (distance to point of application) instead of the perpendicular moment arm when the force is not perpendicular to r.
- Forgetting that torque depends on the choice of pivot point — always specify the axis of rotation.
