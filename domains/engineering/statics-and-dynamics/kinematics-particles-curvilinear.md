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
builds-toward:
- dynamics-newtons-second-law
tags:
- dynamics
- kinematics
- curvilinear motion
- normal-tangential
- polar coordinates
stage: formal-systems
status: draft
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
