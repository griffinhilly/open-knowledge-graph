---
id: kinematics-particles-curvilinear
title: Curvilinear Kinematics of Particles
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: kinematics-particles-rectilinear
  type: hard
- id: kinematics-2d
  type: hard
- id: polar-coordinates
  type: soft
- id: projectile-motion
  type: soft
- id: vectors-in-two-dimensions
  type: hard
- id: vectors-in-rn-operations
  type: hard
builds-toward:
- dynamics-newtons-second-law
tags:
- dynamics
- kinematics
- curvilinear motion
- normal-tangential
- polar coordinates
stage: formal-systems
status: validated
---

# Curvilinear Kinematics of Particles

## Core Idea
Curvilinear motion is analyzed in three coordinate systems: (1) Cartesian — x,y components with constant unit vectors; (2) normal-tangential (n-t) — tangential direction along velocity with aₜ = dv/dt, normal direction toward center of curvature with aₙ = v²/ρ; (3) polar (r, θ) — with aᵣ = r̈ − rθ̇² and aθ = rθ̈ + 2ṙθ̇. The optimal coordinate system depends on the geometry and given information — circular paths favor n-t, problems stated in terms of angle favor polar.

## How It's Best Learned
Identify the most natural coordinate system for the problem geometry. Practice converting between systems. For n-t coordinates, always identify the center of curvature to establish the normal direction.

## Common Misconceptions
- The normal acceleration direction points toward the center of curvature (inward), not outward.
- Forgetting the Coriolis term 2ṙθ̇ in polar coordinate acceleration.
- Assuming the tangential direction unit vector is constant — it rotates continuously with the particle's path.

## Questions

```yaml
- question: "A particle travels along a curved path at constant speed. Which component of its acceleration is zero?"
  type: multiple-choice
  options:
    - "Normal acceleration aₙ = v²/ρ"
    - "Tangential acceleration aₜ = dv/dt"
    - "Radial acceleration aᵣ"
    - "Total acceleration magnitude"
  answer: 1
  explanation: "Tangential acceleration aₜ = dv/dt measures how quickly the particle's speed is changing. At constant speed, dv/dt = 0, so aₜ = 0. Normal acceleration aₙ = v²/ρ depends only on speed and radius of curvature — both nonzero — so it remains nonzero whenever the path curves. The particle still accelerates; it just changes direction, not speed."

- question: "In normal-tangential coordinates, the unit normal vector eₙ points away from the center of curvature (toward the convex, outer side of the curve)."
  type: true-false
  answer: false
  explanation: "The unit normal eₙ always points toward the center of curvature — the concave, inner side of the curve. This convention makes normal acceleration aₙ = v²/ρ a positive quantity directed inward. Confusing this direction leads to sign errors in force equations for circular or curved motion."

- question: "In polar coordinates, what is the Coriolis acceleration term, and why does it appear even when the radial speed ṙ is constant?"
  type: short-answer
  answer: "The Coriolis term is 2ṙθ̇ in the transverse (θ) direction. It arises because the radial unit vector eᵣ rotates at rate θ̇, so any radial velocity ṙ acquires a continuously changing transverse component as the reference frame rotates."
  explanation: "When you differentiate position r = r·eᵣ twice in a rotating frame, you must account for the time-varying directions of eᵣ and eθ. The term 2ṙθ̇ in aθ comes from the product of radial velocity and frame rotation rate — it is a purely kinematic effect of using a rotating coordinate system, not an additional physical force."
```

## Explainer

Rectilinear kinematics describes motion along a straight line, where velocity and acceleration always point in the same fixed direction. Curvilinear kinematics generalizes this to arbitrary curved paths, where the direction of motion changes continuously. The key challenge is that acceleration now has two components: one that changes the particle's speed and one that changes its direction.

The choice of coordinate system is not arbitrary — it should match the geometry of the problem. In Cartesian coordinates (x, y), the unit vectors are fixed, so velocity and acceleration simply decompose into two independent scalar equations. This works perfectly for projectile motion, where the x and y components decouple. For motion along a curved path of known shape, normal-tangential (n-t) coordinates are more natural: the tangential direction eₜ aligns with the velocity vector, and the normal direction eₙ points inward toward the center of curvature. The tangential acceleration aₜ = dv/dt governs how fast the speed changes; the normal acceleration aₙ = v²/ρ governs the rate of turning, where ρ is the radius of curvature at that point. A critical detail: even at constant speed, aₙ is nonzero — the particle is still accelerating because its direction is changing.

Polar coordinates (r, θ) are the coordinate system of choice when a problem is stated in terms of the distance from a fixed point and the angle swept. The radial acceleration aᵣ = r̈ − rθ̇² includes the familiar centripetal term −rθ̇² (which pulls inward for circular motion), and the transverse acceleration aθ = rθ̈ + 2ṙθ̇ includes the Coriolis term 2ṙθ̇. The Coriolis term surprises many students because it appears even when r is constant — it arises from the rotation of the coordinate frame itself, not from any physical force. Its appearance is purely a consequence of differentiating in a rotating reference system.

The practical skill is recognizing which system to use. If the path is described geometrically and you need to relate forces to the curvature of the path, use n-t coordinates. If the problem gives r(t) and θ(t) or describes motion in terms of angles from a pivot, use polar. If components separate naturally into horizontal and vertical, Cartesian is cleanest. Translating the same motion between systems is a useful exercise that sharpens understanding of what each coordinate system is actually measuring.
