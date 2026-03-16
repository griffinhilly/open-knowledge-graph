---
id: triple-integrals-cylindrical-spherical
title: Triple Integrals in Cylindrical and Spherical Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: triple-integrals-cartesian
  type: hard
- id: cylindrical-coordinates
  type: soft
builds-toward:
- change-of-variables-jacobian
tags:
- cylindrical-coordinates
- spherical-coordinates
- triple-integrals
stage: formal-systems
status: draft
---

# Triple Integrals in Cylindrical and Spherical Coordinates

## Core Idea
Cylindrical coordinates (r, θ, z) have dV = r dr dθ dz. Spherical coordinates (ρ, φ, θ) have dV = ρ² sin φ dρ dφ dθ. Choose coordinates based on the region's symmetry: cylindrical for objects with axis symmetry, spherical for radial symmetry from a point.

## Explainer

From your work with triple integrals in Cartesian coordinates, you know the setup: divide a 3D region into small rectangular boxes of volume dV = dx dy dz, integrate a function over all of them, and sum. The challenge is that many natural 3D regions — cylinders, cones, spheres — have boundaries that are ugly in Cartesian coordinates but simple in other coordinate systems. Switching to **cylindrical** or **spherical** coordinates trades a complicated region description for a complicated volume element, usually a net win.

**Cylindrical coordinates** (r, θ, z) are just polar coordinates in the xy-plane with a vertical z-axis attached. The point (r, θ, z) lies at horizontal distance r from the z-axis, at angle θ around that axis, and height z. Regions like cylinders (r ≤ a), cones (z = r), and half-spaces have simple descriptions. The volume element is dV = r dr dθ dz — note the factor of r, which is the same factor that appeared in the polar area element dA = r dr dθ. It arises because a thin cylindrical shell at radius r has circumference 2πr; a small "wedge-box" at radius r has arc length r dθ along the θ direction, not just dθ.

**Spherical coordinates** (ρ, φ, θ) describe a point by its distance ρ from the origin, polar angle φ measured down from the positive z-axis (the "colatitude"), and azimuthal angle θ around the z-axis. Spheres (ρ = a) and cones (φ = constant) have elegant descriptions. The volume element is dV = ρ² sin φ dρ dφ dθ. The factor ρ² sin φ is the Jacobian of the coordinate change — it accounts for the fact that small "spherical boxes" are larger near the equator (where sin φ is largest) and shrink toward the poles (where sin φ → 0). Forgetting this factor is the single most common error in spherical integrals.

The practical rule: **if the region has an axis of symmetry**, use cylindrical; **if it is symmetric about a central point**, use spherical. A solid ball ρ ≤ a is trivial in spherical coordinates: ∫₀²π ∫₀π ∫₀ᵃ ρ² sin φ dρ dφ dθ. Evaluating each integral separately gives (2π)(2)(a³/3) = 4πa³/3 — the familiar volume of a sphere. In Cartesian coordinates, the same calculation requires intricate nested radical limits. The coordinate system does not change the geometry; it changes how conveniently you can describe it.
