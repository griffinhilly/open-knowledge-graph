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
status: validated
---

# Curvilinear Motion of Particles

## Core Idea
Curvilinear motion occurs along a curved path in 2D or 3D. Velocity and acceleration are analyzed in rectangular components (x, y, z) or natural coordinates (tangential and normal to the path), with normal acceleration always directed toward the center of curvature. Projectile motion exemplifies constant horizontal velocity with vertical acceleration under gravity.

## Questions

```yaml
- question: "A car rounds a circular track at perfectly constant speed. What is true about its acceleration?"
  type: multiple-choice
  options:
    - "Its acceleration is zero because speed is constant"
    - "It has only tangential acceleration, directed forward along the path"
    - "It has only normal acceleration, directed toward the center of the circle"
    - "It has both tangential and normal acceleration because the car is moving"
  answer: 2
  explanation: "Acceleration in curvilinear motion has two components: tangential (aₜ = dv/dt, rate of speed change) and normal (aₙ = v²/ρ, rate of direction change). Constant speed means aₜ = 0, but the velocity direction is continuously changing as the car follows the circular track. That directional change is captured by the normal component, which is nonzero and directed toward the center of curvature. Option A is the classic misconception: zero change in speed ≠ zero acceleration."

- question: "In normal-tangential (n-t) coordinates, a particle travels along a curved path while its speed is increasing. How is the total acceleration vector oriented?"
  type: multiple-choice
  options:
    - "Purely in the normal direction, pointing toward the center of curvature"
    - "Purely in the tangential direction, along the path"
    - "With both a tangential component (along the path) and a normal component (toward the center of curvature)"
    - "Radially outward from the center of curvature"
  answer: 2
  explanation: "When both speed and direction are changing, both acceleration components are nonzero. Tangential acceleration aₜ = dv/dt handles the speed increase (points forward along the path since the particle is speeding up). Normal acceleration aₙ = v²/ρ handles the direction change (always points inward toward the center of curvature). The total acceleration is the vector sum of these two perpendicular components. Only in special cases (constant speed or straight path) does one component vanish."

- question: "A particle moving at constant speed along a curved path still has a nonzero acceleration."
  type: true-false
  answer: true
  explanation: "Velocity is a vector quantity with both magnitude (speed) and direction. A particle on a curved path continuously changes its velocity direction even if speed is constant. This change in direction constitutes acceleration — specifically, the normal (centripetal) acceleration aₙ = v²/ρ, directed toward the center of curvature. Acceleration being zero would require both zero speed change and zero direction change, which only occurs for straight-line motion at constant speed."

- question: "Normal acceleration (aₙ) represents the rate at which a particle's speed is changing along its path."
  type: true-false
  answer: false
  explanation: "Normal acceleration aₙ = v²/ρ represents the rate of direction change — it steers the particle around the curve by pointing toward the center of curvature. It is tangential acceleration aₜ = dv/dt that represents the rate of speed change (speeding up or slowing down). This distinction is fundamental: you can have normal acceleration with zero tangential acceleration (constant speed on a curve), tangential with zero normal (changing speed on a straight line), or both simultaneously."

- question: "A particle travels along a circular arc at constant speed. Explain why it is still accelerating, and identify the direction of that acceleration."
  type: short-answer
  answer: "The particle accelerates because its velocity direction continuously changes as it follows the circular arc. Even though the speed |v| is constant, the velocity vector rotates, and any rate of change of velocity — whether in magnitude or direction — is acceleration. The acceleration is purely normal (centripetal): aₙ = v²/ρ, directed toward the center of the circle. There is no tangential component because speed is constant (dv/dt = 0)."
  explanation: "This is the conceptual core of curvilinear motion: confusing 'constant speed' with 'no acceleration' is the most common error. In Newtonian mechanics, this normal acceleration requires a net centripetal force (e.g., tension in a string, friction on a road surface, gravity for orbital motion). Without that force, the particle would travel in a straight line. The circular path is maintained by continuous force redirecting the particle inward."
```

## Explainer

From your study of rectilinear motion, you know how to describe position, velocity, and acceleration along a straight line. Curvilinear motion extends this to paths that bend — arcs, circles, parabolas — and the central challenge is that the direction of velocity is now constantly changing even when speed is constant. That directional change is itself a form of acceleration, and understanding it requires moving beyond scalar descriptions to vector component analysis.

The most natural starting point is the **rectangular (Cartesian) coordinate system**, where you treat horizontal and vertical components independently. Projectile motion is the canonical example: horizontal acceleration is zero (constant velocity) while vertical acceleration is −g. Each axis is its own simple rectilinear problem. The trajectory is generated from parametric equations x(t) and y(t), and the curved path through space is the combination of two independent motions happening simultaneously. You need no new physics — only decomposition into directions that decouple from each other.

But Cartesian coordinates become awkward when the path geometry itself is the natural reference. **Normal-tangential (n-t) coordinates** attach directly to the moving particle: the **tangential direction** is always aligned with the velocity vector (tangent to the path), and the **normal direction** always points toward the instantaneous center of curvature (inward). Velocity has only a tangential component (v = vₜ). Acceleration splits into **tangential acceleration** aₜ = dv/dt (rate of speed change) and **normal acceleration** aₙ = v²/ρ (rate of direction change), where ρ is the local radius of curvature. The normal acceleration always points inward — this is the centripetal component. Any deviation from a perfectly straight path, no matter how slight, produces a nonzero normal acceleration.

The key insight is that acceleration plays two distinct roles in curvilinear motion: it can change the particle's speed (tangential component) or steer the particle around a curve (normal component). A car taking a constant-speed highway curve experiences only normal acceleration — not speeding up or slowing down, but still accelerating because direction changes. A car braking on a straight road experiences only tangential acceleration. In general, both components act simultaneously. Choosing between rectangular and n-t coordinates is a matter of what the problem gives you: if horizontal and vertical forces are specified, Cartesian is natural; if the path geometry and speed along the path are given, n-t coordinates are cleaner and more direct.
