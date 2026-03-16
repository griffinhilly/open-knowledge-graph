---
id: conservation-of-angular-momentum-mechanics
title: Conservation of Angular Momentum
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: angular-impulse-momentum
  type: hard
- id: torque-angular-acceleration
  type: soft
- id: conservation-of-angular-momentum
  type: hard
builds-toward:
- rigid-body-rotation-theory
- gyroscopic-motion-and-stability
tags:
- angular-momentum
- conservation-laws
- torque
stage: formal-systems
status: draft
---

# Conservation of Angular Momentum

## Core Idea
Angular momentum L = r × p (or L = Iω for rotation) is conserved in systems with zero net external torque. This explains why spinning ice skaters accelerate when pulling in their arms, and why rotating systems exhibit remarkable stability—it is the rotational analog of linear momentum conservation and equally fundamental.

## Explainer

You already know from angular impulse-momentum that net torque causes angular momentum to change: ΣM = dL/dt. Conservation of angular momentum is simply the case where ΣM = 0, so dL/dt = 0, meaning **L = constant**. The logic mirrors linear momentum conservation exactly — just as a net force is required to change linear momentum, a net external torque is required to change angular momentum. If no torque acts, the rotational state of the system cannot change.

For a rigid body spinning about a fixed axis, this takes the compact form L = Iω = constant. The critical insight is that the **moment of inertia** I is not fixed — it depends on how mass is distributed relative to the spin axis. When an ice skater pulls their arms inward, they reduce their moment of inertia. Because Iω must stay constant, ω must increase proportionally. The total angular momentum (the product Iω) is conserved; the skater hasn't done any external work on angular momentum — they've merely redistributed mass to change I and ω simultaneously. This is why conservation calculations often proceed differently from torque-based ones: you don't need to know the internal forces, just the initial and final moments of inertia.

For particles and systems where the position vector matters, the vector form L = r × p becomes important. Angular momentum depends on both the speed of the particle *and* its perpendicular distance from the rotation axis (the moment arm). A planet in an elliptical orbit conserves angular momentum because gravity always points through the Sun (zero torque about the Sun), so it moves faster when close to the Sun (small r) and slower when far away (large r) — this is Kepler's second law as a direct consequence of angular momentum conservation.

Conservation of angular momentum also underlies **gyroscopic stability**: a spinning gyroscope resists changes to its orientation because any torque produces a change in the direction of L, not a change in its magnitude. A fast-spinning top doesn't fall because gravity's torque causes L to precess (rotate) rather than tip over. This counterintuitive behavior — where a torque produces motion perpendicular to itself — follows directly from the vector nature of L = r × p and the fact that torque is dL/dt. Recognizing when angular momentum is conserved (isolated system or zero net torque) and when it is not (net external torque present) is the fundamental skill this topic develops, and it is the rotational counterpart of the same judgment call you already make for linear momentum.
