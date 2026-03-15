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
