---
id: triple-integrals-cylindrical-spherical
title: Triple Integrals in Cylindrical and Spherical Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: triple-integrals
  type: hard
- id: cylindrical-coordinates
  type: hard
- id: spherical-coordinates
  type: hard
builds-toward:
- jacobian-change-of-variables
tags:
- triple-integral
- cylindrical
- spherical
- volume
- mass
stage: formal-systems
status: draft
---

# Triple Integrals in Cylindrical and Spherical Coordinates

## Core Idea
Triple integrals become tractable over symmetric solids by using cylindrical or spherical coordinates. In cylindrical: ∭_E f dV = ∫∫∫ f(r cosθ, r sinθ, z) r dr dθ dz. In spherical: ∭_E f dV = ∫∫∫ f(ρ sinφ cosθ, ρ sinφ sinθ, ρ cosφ) ρ² sinφ dρ dφ dθ. The choice of coordinate system is driven by the shape of the region: cylindrical for cylinders and cones, spherical for spheres and hemispheres. Setting up the limits correctly requires visualizing the 3D solid and determining which surfaces bound ρ (or r) as functions of the angular variables.

## How It's Best Learned
Classify solids by their symmetry before choosing coordinates. Practice the standard examples: volume of a sphere (spherical), volume of a cone (cylindrical or spherical), center of mass of a hemisphere (spherical). Always write out the volume element explicitly before integrating.

## Common Misconceptions
- Using cylindrical coordinates for a sphere (or spherical for a cylinder) is technically possible but creates unnecessary complexity.
- Volume elements in both systems include factors (r in cylindrical, ρ² sinφ in spherical) that are easy to forget.
- Limits in spherical coordinates for a solid bounded above by a sphere and below by a cone require careful analysis of where the surfaces intersect.
