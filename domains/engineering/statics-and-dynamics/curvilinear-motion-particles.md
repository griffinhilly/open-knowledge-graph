---
id: curvilinear-motion-particles
title: Curvilinear Motion of Particles
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: rectilinear-motion-particles
  type: hard
- id: kinematics-particles-curvilinear
  type: soft
builds-toward:
- particle-dynamics-accelerated-motion
tags:
- kinematics
- curvilinear
- velocity
- acceleration
- components
- projectile motion
stage: formal-systems
status: draft
---

# Curvilinear Motion of Particles

## Core Idea
Curvilinear motion occurs along a curved path in 2D or 3D. Velocity and acceleration are analyzed in rectangular components (x, y, z) or natural coordinates (tangential and normal to the path), with normal acceleration always directed toward the center of curvature. Projectile motion exemplifies constant horizontal velocity with vertical acceleration under gravity.

## Explainer

From your study of rectilinear motion, you know how to describe position, velocity, and acceleration along a straight line. Curvilinear motion extends this to paths that bend — arcs, circles, parabolas — and the central challenge is that the direction of velocity is now constantly changing even when speed is constant. That directional change is itself a form of acceleration, and understanding it requires moving beyond scalar descriptions to vector component analysis.

The most natural starting point is the **rectangular (Cartesian) coordinate system**, where you treat horizontal and vertical components independently. Projectile motion is the canonical example: horizontal acceleration is zero (constant velocity) while vertical acceleration is −g. Each axis is its own simple rectilinear problem. The trajectory is generated from parametric equations x(t) and y(t), and the curved path through space is the combination of two independent motions happening simultaneously. You need no new physics — only decomposition into directions that decouple from each other.

But Cartesian coordinates become awkward when the path geometry itself is the natural reference. **Normal-tangential (n-t) coordinates** attach directly to the moving particle: the **tangential direction** is always aligned with the velocity vector (tangent to the path), and the **normal direction** always points toward the instantaneous center of curvature (inward). Velocity has only a tangential component (v = vₜ). Acceleration splits into **tangential acceleration** aₜ = dv/dt (rate of speed change) and **normal acceleration** aₙ = v²/ρ (rate of direction change), where ρ is the local radius of curvature. The normal acceleration always points inward — this is the centripetal component. Any deviation from a perfectly straight path, no matter how slight, produces a nonzero normal acceleration.

The key insight is that acceleration plays two distinct roles in curvilinear motion: it can change the particle's speed (tangential component) or steer the particle around a curve (normal component). A car taking a constant-speed highway curve experiences only normal acceleration — not speeding up or slowing down, but still accelerating because direction changes. A car braking on a straight road experiences only tangential acceleration. In general, both components act simultaneously. Choosing between rectangular and n-t coordinates is a matter of what the problem gives you: if horizontal and vertical forces are specified, Cartesian is natural; if the path geometry and speed along the path are given, n-t coordinates are cleaner and more direct.
